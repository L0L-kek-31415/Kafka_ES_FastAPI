from app.db import db
from app.schema import Statistic


class StatisticService:
    def __init__(self):
        self.db = db["statistics"]

    async def create_statistic(self, phrase: str):
        x = await self.db.find_one({"phrase": phrase})
        if x:
            await self.update_statistic(phrase)
        else:
            await self.db.insert_one({"phrase": phrase, "count": 1})
        return {"message": "Successfuly"}

    async def update_statistic(self, phrase: str, count=1):
        x = await self.db.find_one({"phrase": phrase})
        count = x["count"] + count
        await self.db.update_one({"phrase": phrase},
                                          {"$set": {"count": count}})
        return {"message": "Successfuly"}

    async def return_all(self):
        result = []
        async for item in self.db.find({}):
            result.append(Statistic(**item))
        return result
