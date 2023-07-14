from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "insurance_history" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "declared_price" DOUBLE PRECISION NOT NULL,
    "date" DATE NOT NULL,
    "cargo_type" TEXT NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "insurance_price" DOUBLE PRECISION NOT NULL
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "insurance_history";"""
