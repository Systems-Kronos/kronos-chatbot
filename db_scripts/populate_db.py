from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Conecta com o Mongo
connection = MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
database = connection["chatbot_kronos"]
docs_collection = database["docs"]

# Lê os docs
with open("db_scripts/docs.json", "r", encoding="utf-8") as x:
    docs = json.load(x)

# Deleta qualquer documento antigo
docs_collection.delete_many({})

# Insere os novos
docs_collection.insert_many(docs)

print(f"{len(docs)} documentos inseridos.")
