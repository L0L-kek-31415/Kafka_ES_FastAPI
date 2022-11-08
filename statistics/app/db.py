import motor.motor_asyncio

url = "mongodb://root:root@mongodb:27017/"
client = motor.motor_asyncio.AsyncIOMotorClient(url)



db = client.college