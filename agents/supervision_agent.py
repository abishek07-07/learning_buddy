from config.llm import llm
from langchain.agents import create_agent
from tools.supervisor_tools import web_search_supervisor, database_search_supervisor

tools = [database_search_supervisor, web_search_supervisor]

supervision_agent = create_agent(
    model=llm,
    tools=tools,
    name="supervision_agent",
    system_prompt="""
    You are a supervisor agent responsible for selecting the best tool to answer the user's query.

    You have access to two tools:

    1. database_search:
       Use this tool to retrieve information from the internal database.

    2. web_search:
       Use this tool to search the internet for external or up-to-date information.

    Instructions:
    - Analyze the user's query before selecting a tool.
    - Use database_search when the required information is available in the internal database.
    - Use web_search when the query requires external or current information.
    - Use both tools when the query requires information from both sources.
    - Do not call tools unnecessarily.
    - After receiving the tool results, provide a clear and relevant response.
    - Never fabricate information or tool results.
    """
)