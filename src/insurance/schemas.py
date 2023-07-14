import datetime
from enum import Enum

from pydantic import BaseModel

from src.insurance.models import Insurance_History


class InsuranceHistoryCreate(BaseModel):
    declared_price: float
    date: datetime.datetime
    cargo_type: str
    rate: float
    insurance_price: float

    @classmethod
    def from_model(cls, model: Insurance_History) -> "InsuranceHistoryCreate":
        return cls(
            declared_price=model.declared_price,
            date=model.date,
            cargo_type=model.cargo_type,
            rate=model.rate,
            insurance_price=model.insurance_price,
        )


class InsuranceHistoryRead(BaseModel):
    id: int
    declared_price: float
    date: datetime.datetime
    cargo_type: str
    rate: float
    insurance_price: float

    @classmethod
    def from_model(cls, model: Insurance_History) -> "InsuranceHistoryRead":
        return cls(
            id=model.id,
            declared_price=model.declared_price,
            date=model.date,
            cargo_type=model.cargo_type,
            rate=model.rate,
            insurance_price=model.insurance_price,
        )


class InsuranceHistoryUpdate(BaseModel):
    id: int
    declared_price: float
    date: datetime.datetime
    cargo_type: str
    rate: float
    insurance_price: float

    @classmethod
    def from_model(cls, model: Insurance_History) -> "InsuranceHistoryUpdate":
        return cls(
            id=model.id,
            declared_price=model.declared_price,
            date=model.date,
            cargo_type=model.cargo_type,
            rate=model.rate,
            insurance_price=model.insurance_price,
        )


class SchemasTypes(Enum):
    CREATE = 1
    READ = 2
    UPDATE = 3
