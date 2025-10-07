from langchain_mongodb import MongoDBChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()


def get_memory(session_id):
    return MongoDBChatMessageHistory(
        session_id=session_id,
        connection_string=os.getenv("MONGO_CONNECTION_STRING"),
        database_name="chatbot_kronos",
        collection_name="conversations",
    )
