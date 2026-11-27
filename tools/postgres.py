from database.database import  store
from langchain.tools import tool


@tool
def query_database(text : str):
    "Can do the semantic analysis for the given text"
    return  store.similarity_search(text, k=4);




