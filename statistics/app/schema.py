from pydantic import BaseModel


class Statistic(BaseModel):
    phrase: str
    count: int