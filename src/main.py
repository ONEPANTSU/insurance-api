from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src import config
from src.insurance.router import router as insurance_router
from src.rate.router import router as rate_router

# from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title="Insurance API")

# origins = ["*"]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(insurance_router)
app.include_router(rate_router)

register_tortoise(
    app,
    config=config.DATABASE_CONFIG,
)
