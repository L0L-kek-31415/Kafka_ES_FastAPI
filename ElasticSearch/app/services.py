from elasticsearch import Elasticsearch

from app.schemas import Item


class ElasticService:
    def __init__(self):
        self.es = Elasticsearch("http://es:9200")

    def create_item(self, item: Item, index):
        return self.es.index(index=index, body=item.dict())

    def search_by_words(self, description, index):
        result = self.es.search(
            index=index, body={"query": {"match": {"description": description}}}
        )
        return result
