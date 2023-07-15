import datetime

from fastapi import APIRouter

from src.rate.schemas import Rate
from src.rate.text.details import DETAILS
from src.rate.text.messages import MESSAGE, get_days_word
from src.rate.utils import (
    UpdateRateMode,
    delete_rate_from_file,
    delete_rates_from_file,
    get_all_rates_data,
    get_rate_data,
    get_rates_by_date_data,
    update_rate_in_file,
)
from src.utils import STATUS, return_json

router = APIRouter(prefix="/rate", tags=["rate"])


@router.get("/get/all")
async def get_all_rates() -> dict:
    try:
        data = get_all_rates_data()
        details = None
        if data is None:
            details = DETAILS["there_is_no_rates"]
        days_count = len(data.keys())
        days = get_days_word(days_count=days_count)
        return return_json(
            status=STATUS[200],
            message=MESSAGE["get_all_rates_success"].format(
                days_count=days_count, days=days
            ),
            data=data,
            details=details,
        )
    except Exception as e:
        return return_json(
            status=STATUS[400], message=MESSAGE["get_all_rates_error"], details=str(e)
        )


@router.get("/get/{date}")
async def get_rates_by_date(date: datetime.date) -> dict:
    try:
        data = get_rates_by_date_data(date=date)
        details = None
        if data is None:
            details = DETAILS["rates_are_not_found"].format(date=date)
        return return_json(
            status=STATUS[200],
            message=MESSAGE["get_rate_by_date_success"].format(date=str(date)),
            data=data,
            details=details,
        )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_rate_by_date_error"].format(date=str(date)),
            details=str(e),
        )


@router.get("/get/{date}/{cargo_type}")
async def get_rate(date: datetime.date, cargo_type: str) -> dict:
    try:
        data = get_rate_data(date=date, cargo_type=cargo_type)
        details = None
        if data is None:
            details = DETAILS["rate_is_not_found"].format(
                cargo_type=cargo_type, date=date
            )
        return return_json(
            status=STATUS[200],
            message=MESSAGE["get_rate_success"].format(
                cargo_type=cargo_type, date=str(date)
            ),
            data=data,
            details=details,
        )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["get_rate_error"].format(
                cargo_type=cargo_type, date=str(date)
            ),
            details=str(e),
        )


@router.post("/add")
async def add_rate(rate: Rate):
    try:
        details = update_rate_in_file(rate=rate, mode=UpdateRateMode.ADD)
        if details is None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["add_rate_success"].format(
                    cargo_type=rate.cargo_type, date=str(rate.date)
                ),
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["add_rate_error"].format(
                    cargo_type=rate.cargo_type, date=str(rate.date)
                ),
                details=details,
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["add_rate_error"].format(
                cargo_type=rate.cargo_type, date=str(rate.date)
            ),
            details=str(e),
        )


@router.put("/edit")
async def edit_rate(rate: Rate):
    try:
        details = update_rate_in_file(rate=rate, mode=UpdateRateMode.EDIT)
        if details is None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["edit_rate_success"].format(
                    cargo_type=rate.cargo_type, date=str(rate.date)
                ),
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["edit_rate_error"].format(
                    cargo_type=rate.cargo_type, date=str(rate.date)
                ),
                details=details,
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["edit_rate_error"].format(
                cargo_type=rate.cargo_type, date=str(rate.date)
            ),
            details=str(e),
        )


@router.delete("/delete/{date}")
async def delete_rates(date: datetime.date):
    try:
        details = delete_rates_from_file(date=date)
        if details is None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["delete_rates_success"].format(date=str(date)),
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["delete_rates_error"].format(date=str(date)),
                details=details,
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["delete_rates_error"].format(date=str(date)),
            details=str(e),
        )


@router.delete("/delete/{date}/{cargo_type}")
async def delete_rate(date: datetime.date, cargo_type: str):
    try:
        details = delete_rate_from_file(date=date, cargo_type=cargo_type)
        if details is None:
            return return_json(
                status=STATUS[200],
                message=MESSAGE["delete_rate_success"].format(
                    cargo_type=cargo_type, date=str(date)
                ),
            )
        else:
            return return_json(
                status=STATUS[400],
                message=MESSAGE["delete_rate_error"].format(
                    cargo_type=cargo_type, date=str(date)
                ),
                details=details,
            )
    except Exception as e:
        return return_json(
            status=STATUS[400],
            message=MESSAGE["delete_rate_error"].format(
                cargo_type=cargo_type, date=str(date)
            ),
            details=str(e),
        )
