import datetime

from pydantic import BaseModel


class Rate(BaseModel):
    date: datetime.date
    cargo_type: str
    rate: float

    def get_rate_info(self):
        return {"cargo_type": self.cargo_type, "rate": self.rate}
