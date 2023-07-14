import datetime
import json
from enum import Enum
from typing import List, Optional, Union

from src.config import RATES_PATH
from src.insurance.models import Insurance_History
from src.insurance.schemas import (
    InsuranceHistoryCreate,
    InsuranceHistoryRead,
    InsuranceHistoryUpdate,
    SchemasTypes,
)


def get_model_from_schema(schema: InsuranceHistoryCreate) -> Insurance_History:
    return Insurance_History().update_from_dict(dict(schema))


def get_schema_from_model(
    model: Insurance_History, schema_type: SchemasTypes
) -> Union[InsuranceHistoryCreate, InsuranceHistoryRead, InsuranceHistoryUpdate,]:
    if schema_type == SchemasTypes.CREATE:
        return InsuranceHistoryCreate.from_model(model=model)
    elif schema_type == SchemasTypes.READ:
        return InsuranceHistoryRead.from_model(model=model)
    elif schema_type == SchemasTypes.UPDATE:
        return InsuranceHistoryUpdate.from_model(model=model)


def get_schemas_from_models(
    models: List[Insurance_History], schemas_type: SchemasTypes
) -> List[Union[InsuranceHistoryCreate, InsuranceHistoryRead, InsuranceHistoryUpdate,]]:
    if schemas_type == SchemasTypes.CREATE:
        return [InsuranceHistoryCreate.from_model(model=model) for model in models]
    elif schemas_type == SchemasTypes.READ:
        return [InsuranceHistoryRead.from_model(model=model) for model in models]
    elif schemas_type == SchemasTypes.UPDATE:
        return [InsuranceHistoryUpdate.from_model(model=model) for model in models]


async def insurance_request_handler(
    declared_price: float, date: datetime.date, cargo_type: type
) -> Optional[InsuranceHistoryCreate]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(date) in data.keys():
        rates = data[str(date)]
        for rate_info in rates:
            if rate_info["cargo_type"] == cargo_type:
                insurance_history_schema = InsuranceHistoryCreate(
                    declared_price=declared_price,
                    rate=rate_info["rate"],
                    date=datetime.datetime(
                        year=date.year, month=date.month, day=date.day
                    ),
                    cargo_type=cargo_type,
                    insurance_price=declared_price * rate_info["rate"],
                )
                insurance_history_model = get_model_from_schema(
                    schema=insurance_history_schema
                )
                await insurance_history_model.save()
                return insurance_history_schema
    return None


async def get_insurance_history_data() -> Optional[List[InsuranceHistoryRead]]:
    models = await Insurance_History.all()
    if len(models) != 0:
        schemas = get_schemas_from_models(models=models, schemas_type=SchemasTypes.READ)
        return schemas
    else:
        return None
