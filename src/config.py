import os

from dotenv import load_dotenv

load_dotenv()

RATES_PATH = "src/rates.json"

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

DATABASE_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": DB_HOST,
                "port": DB_PORT,
                "user": DB_USER,
                "password": DB_PASSWORD,
                "database": DB_NAME,
            },
        },
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "src.insurance.models"],
            "default_connection": "default",
        },
    },
}
