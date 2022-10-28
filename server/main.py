from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
import models
import uvicorn
from starlette.responses import FileResponse
from fastapi import APIRouter, FastAPI, Request, Response
import service


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_index():
    return FileResponse('../frontend/web/index.html')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
