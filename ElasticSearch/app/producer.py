import os
import json

from kafka import KafkaProducer

# channel
topic = 'app'

# producer
producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    print("\nERROR\n", excp, "\nERROR\n")
    pass


def publish(method: str, body: dict):
    producer.send(topic, key=method.encode('UTF-8'), value=body).add_callback(
        on_send_success).add_errback(on_send_error)
    print(f'Topic :{topic}  Key :{method}   published.')

    # block until all async messages are sent
    producer.flush()
