import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from os import getenv
from dotenv import load_dotenv

# Check if we are under Docker
DOCKER_MODE = False
if getenv("DOCKER_MODE") == 'true':
    DOCKER_MODE = True

# Load variables from .env
if not DOCKER_MODE:
    load_dotenv()


try:
    connection = psycopg2.connect(
        host=getenv("LCT_PG_HOST"),
        user=getenv("LCT_PG_USER"),
        password=getenv("LCT_PG_PASSWD"),
        database=getenv("LCT_PG_DB")
    )
    cur = connection.cursor()
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
except Exception as ex:
    print(ex)
