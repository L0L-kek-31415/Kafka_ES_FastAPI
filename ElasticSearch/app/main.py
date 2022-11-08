from typing import List
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, Response

from app.schemas import Item
from app.services import ElasticService

from app.producer import ProducerKafka

app = FastAPI()
es = ElasticService()
producer = ProducerKafka('app', ["localhost:29093", "kafka:29092"])


@app.post("/search/{description}/")
async def root(description, background_task: BackgroundTasks):
    background_task.add_task(producer.publish, method="create", body={"phrase": description})
    result = es.search_by_words(description, "lolkek")
    hits = result.get("hits", {}).get("hits", [])
    return {
        "results": [hit.get("_source") for hit in hits]
    }


@app.post("/create_item/", response_model=List[Item])
async def say_hello(item: Item):
    es.create_item(item, "lolkek")
    return Response(status_code=200)
