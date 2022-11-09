import asyncio
import json
from asyncio import sleep
from aiokafka import AIOKafkaConsumer


class ConsumerKafka:
    def __init__(self, topic, servers):
        self.topic = topic
        self.servers = servers
        self.loop = asyncio.get_event_loop()
        self.consumer = AIOKafkaConsumer("app", bootstrap_servers=['kafka:29092'], loop=self.loop)

    async def consume(self, statistic):
        while True:
            try:
                await self.consumer.start()
                break
            except:
                await sleep(10)
        try:
            async for msg in self.consumer:
                print(
                    "consumed: ",
                    msg.topic,
                    msg.partition,
                    msg.offset,
                    msg.key,
                    msg.value,
                    msg.timestamp,
                )
                msg = json.loads(msg.value)
                print(msg)
                print(msg['phrase'])
                await statistic.create_statistic(msg["phrase"])
                print("Successfuly.")

        finally:
            await self.consumer.stop()
