from pymongo import MongoClient
from shared.core.config import settings

client = MongoClient(settings.mongo_host, settings.mongo_port)
db = client["advices_db"]
collection = db["advices"]

# Salva um conselho no banco de dados
def save_advice(advice: dict):
    collection.insert_one(advice)
    print("[✓] Saved to MongoDB")

# Obtém a contagem total de conselhos armazenados
def get_count_advices() -> int:
    return collection.count_documents({})
