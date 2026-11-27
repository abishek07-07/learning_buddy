from platform import system

from langchain.agents import create_agent
from tools.postgres import  query_database
from config.llm import llm
tools= [query_database]



database_agent = create_agent(
        tools=tools,
        model= llm,
        system_prompt=""" You are a database research specialist for a student learning platform.

    Your responsibilities:
    1. Search the internal knowledge base using query_database.
    2. Retrieve information relevant to the student's question.
    3. Summarize the retrieved documents accurately.
    4. Do not invent information that is not present in the documents.
    5. Mention when the database does not contain sufficient information.
    Return a concise research report.
    """
)



