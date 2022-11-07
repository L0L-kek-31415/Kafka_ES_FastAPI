import json
from typing import List

from elasticsearch import Elasticsearch
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, Response

from app.producer import publish
from app.schemas import Item

es = Elasticsearch("http://es:9200")
app = FastAPI()


def create_item(item: Item, index):
    return es.index(index=index, body=item.dict())


def search_by_words(description, index):
    result = es.search(
        index=index, body={"query": {"match": {"description": description}}}
    )
    return result


@app.post("/search/{description}/")
async def root(description):
    BackgroundTasks.add_task(publish, method="create", body={"phrase": description})
    result = search_by_words(description, "lolkek")
    hits = result.get("hits", {}).get("hits", [])
    return {
        "results": [hit.get("_source") for hit in hits]
    }


@app.post("/hello/", response_model=List[Item])
async def say_hello(item: Item):
    result = create_item(item, "lolkek")
    return Response(status_code=200)
