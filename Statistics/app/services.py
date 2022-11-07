from app.db import db
from app.schema import Statistic


async def create_statistic(phrase: str):
    x = await db["statistics"].find_one({"phrase": phrase})
    if x:
        await update_statistic(phrase)
    await db['statistics'].insert_one({"phrase": phrase, "count": 1})
    return {"message": "Successfuly"}


async def update_statistic(phrase: str, count=1):
    x = await db['statistics'].find_one({"phrase": phrase})
    count = x["count"] + count
    await db['statistics'].update_one({"phrase": phrase},
                                      {"$set": {"count": count}})
    return {"message": "Successfuly"}


async def return_all():
    result = []
    async for item in db["statistics"].find({}):
        result.append(Statistic(**item))
    return result
