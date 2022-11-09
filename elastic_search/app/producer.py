import json
from kafka import KafkaProducer


class ProducerKafka:
    def __init__(self, topic, servers):
        self.topic = topic
        self.servers = servers
        self.producer = KafkaProducer(bootstrap_servers=self.servers,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def publish(self, method: str, body: dict):
        self.producer.send(self.topic, key=method.encode('UTF-8'), value=body)
        self.producer.flush()
