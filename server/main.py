from starlette.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import service
import models
from os import getenv
from dotenv import load_dotenv
from database import DB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if we are under Docker
DOCKER_MODE = False
if getenv("DOCKER_MODE") == 'true':
    DOCKER_MODE = True

 # Load variables from .env
if not DOCKER_MODE:
    load_dotenv()

db_creds = {
        'host': getenv('LCT_PG_HOST'),
        'user': getenv('LCT_PG_USER'),
        'db': getenv('LCT_PG_DB'),
        'password': getenv('LCT_PG_PASSWD')
        }

db = DB(db_creds)

@app.get('/check') # проверить подключение
async def read_index():
    return JSONResponse(content='ok')

@app.post('/authcheck', response_model=models.AuthorizationResult) #Проверка логина и пароля
async def authentication(user: models.User):
    return db.check_user(user.login, user.password)

@app.get('/admin/generate') # Генерация пар логин - пароль
async def generate_user(quantity: int, is_super: int):
    if is_super == 1:
        is_super = True
    else:
        is_super = False
    return service.generate_auth_pair(db, quantity, is_super)

@app.get('/recommendations') # Для получения рекомендаций
async def get_recommendations():
    return JSONResponse(db.get_recs())

@app.post('/analysis/filter') # Для получения данных статистики
async def get_stats(product: str, direction: str, start: str, end: str):
    return JSONResponse(db.get_stats(product, direction, start, end))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=66)
