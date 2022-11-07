from typing import List

from fastapi import FastAPI

from app.schema import Statistic
from app.services import create_statistic, return_all

app = FastAPI()

    # x = db["statistics"].find({})
    # print(x)
    # return x




@app.get("/hello/{name}")
async def say_hello(name: str):
    await create_statistic(name)
    return {"message": f"Hello {name}"}


@app.get("/stat/", response_model=List[Statistic])
async def statistics_list():
    result = await return_all()
    return result


