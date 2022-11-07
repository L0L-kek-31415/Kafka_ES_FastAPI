import os
import json
from enum import Enum
from time import sleep
from kafka import KafkaConsumer

from app.services import create_statistic, update_statistic

# channel
topic = 'app'

# consumer
consumer = KafkaConsumer(topic, bootstrap_servers=['kafka:29093'],
                         auto_offset_reset='latest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))


for message in consumer:
    print("Consuming.....")
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key, message.value))
    if message.key == b'create':
        create_statistic(message.value['phrase'])
        print("Successfuly.")
