from langchain_postgres import PGEngine, PGVectorStore
import os
from langchain_core.documents import Document
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv(find_dotenv())


CONNECTION_STRING = os.getenv("CONNECTION_STRING")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")


engine = PGEngine.from_connection_string(CONNECTION_STRING)


TABLE_NAME = "documents"

VECTOR_SIZE = 3072


# engine.init_vectorstore_table(
#     table_name=TABLE_NAME,
#     vector_size=VECTOR_SIZE,
# )

store = PGVectorStore.create_sync(
    engine=engine,
    embedding_service= embeddings,
    table_name=TABLE_NAME,
)

def load_database():
    return store



def add_embeddings_database(docs : Document):
    store.add_embeddings(docs);


async def similarity_search(query :str ):
    docs =  await store.asimilarity_search(query,k=4 )
    return  docs;
