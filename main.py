
import os

from dotenv import load_dotenv, find_dotenv
from rich import print

from database.database import load_database
from agents.supervision_agent import supervision_agent

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGEngine

load_dotenv(find_dotenv())

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

if not CONNECTION_STRING:
    raise ValueError("CONNECTION_STRING is not configured")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

engine = PGEngine.from_connection_string(
    CONNECTION_STRING
)

# Initialize database
load_database()

# Invoke supervisor
res = supervision_agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                "Explain the database using information "
                "from both the web and the database."
            )
        }
    ]
})

print(res)
