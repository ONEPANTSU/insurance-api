import datetime
import json
from enum import Enum
from typing import List, Optional

from loguru import logger

from src.config import RATES_PATH
from src.rate.schemas import Rate
from src.rate.text.details import DETAILS


def get_all_rates_data() -> dict:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    return data


def get_rates_by_date_data(date: datetime.date) -> List[dict]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(date) in data.keys():
        return data[str(date)]
    else:
        return None


def get_rate_data(date: str, cargo_type: str) -> Optional[float]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(date) in data.keys():
        rates = data[str(date)]
        for rate_info in rates:
            if rate_info["cargo_type"] == cargo_type:
                return rate_info["rate"]
    return None


class UpdateRateMode(Enum):
    UPDATE = 0
    ADD = 1
    EDIT = 2


@logger.catch
def update_rate_in_file(
    rate: Rate, mode: UpdateRateMode = UpdateRateMode.UPDATE
) -> Optional[str]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(rate.date) in data:
        is_existing = False
        for index in range(len(data[str(rate.date)])):
            if data[str(rate.date)][index]["cargo_type"] == rate.cargo_type:
                data[str(rate.date)][index]["rate"] = rate.rate
                is_existing = True
                if mode == UpdateRateMode.ADD:
                    return DETAILS["rate_already_exists"].format(
                        cargo_type=rate.cargo_type, date=str(rate.date)
                    )
                break
        if not is_existing:
            if mode == UpdateRateMode.EDIT:
                return DETAILS["rate_do_not_exists"].format(
                    cargo_type=rate.cargo_type, date=str(rate.date)
                )
            data[str(rate.date)].append(rate.get_rate_info())
    else:
        if mode == UpdateRateMode.EDIT:
            return DETAILS["rate_do_not_exists"].format(
                cargo_type=rate.cargo_type, date=str(rate.date)
            )
        data[str(rate.date)] = [rate.get_rate_info()]

    with open(RATES_PATH, "w") as rates_json:
        json.dump(data, rates_json)


@logger.catch
def delete_rates_from_file(date: datetime.date) -> Optional[str]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(date) in data.keys():
        data.pop(str(date))
        with open(RATES_PATH, "w") as rates_json:
            json.dump(data, rates_json)
    else:
        return DETAILS["rates_are_not_found"].format(date=str(date))


@logger.catch
def delete_rate_from_file(date: datetime.date, cargo_type: str) -> Optional[str]:
    with open(RATES_PATH, "r") as rates_json:
        data = json.load(rates_json)
    if str(date) in data.keys():
        for index in range(len(data[str(date)])):
            if data[str(date)][index]["cargo_type"] == cargo_type:
                data[str(date)].pop(index)
                if len(data[str(date)]) == 0:
                    data.pop(str(date))
                break
        with open(RATES_PATH, "w") as rates_json:
            json.dump(data, rates_json)
    else:
        return DETAILS["rate_is_not_found"].format(
            cargo_type=cargo_type, date=str(date)
        )
