import datetime

from fastapi import APIRouter

from src.insurance.text.details import DETAILS
from src.insurance.text.messages import MESSAGE, get_rows_word
from src.insurance.utils import get_insurance_history_data, insurance_request_handler
from src.utils import STATUS, return_json

router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/")
async def insurance_request(
    declared_price: float, date: datetime.date, cargo_type: str
) -> dict:
    try:
        insurance_history = await insurance_request_handler(
            declared_price=declared_price, date=date, cargo_type=cargo_type
        )
        if insurance_history is not None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["insurance_request_success"],
                data={
                    "result": insurance_history.insurance_price,
                    "insurance_history": insurance_history,
                },
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["insurance_request_error"],
                details=DETAILS["rate_is_not_found"].format(
                    cargo_type=cargo_type, date=date
                ),
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["insurance_request_error"],
            details=str(e),
        )


@router.get("/")
async def get_insurance_history() -> dict:
    try:
        insurance_history = await get_insurance_history_data()
        if insurance_history is not None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["get_insurance_history_success"].format(
                    count=len(insurance_history),
                    rows=get_rows_word(rows_count=len(insurance_history)),
                ),
                data=insurance_history,
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["get_insurance_history_error"],
                details=DETAILS["history_is_empty"],
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_insurance_history_error"],
            details=str(e),
        )
