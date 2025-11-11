from pymongo import MongoClient
from shared.core.config import settings

client = MongoClient(settings.mongo_host, settings.mongo_port)
db = client["advices_db"]
collection = db["advices"]

def save_advice(advice: dict):
    collection.insert_one(advice)
    print("[✓] Saved to MongoDB")
