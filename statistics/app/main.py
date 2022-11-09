from typing import List

from fastapi import FastAPI
from app.schema import Statistic

from app.consumer import ConsumerKafka

from app.services import StatisticService

app = FastAPI()
consumer = ConsumerKafka("app", ['kafka:29092'])
statistics = StatisticService()


@app.get("/stat/", response_model=List[Statistic])
async def statistics_list():
    result = await statistics.return_all()
    return result


@app.on_event("startup")
async def startup_event():
    consumer.loop.create_task(consumer.consume(statistics))


@app.on_event("shutdown")
async def shutdown_event():
    await consumer.stop()
