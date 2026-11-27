
from agents.database_search_agent import database_agent
from agents.web_search_agent import web_agent
from langchain.tools import tool



from agents.database_search_agent import database_agent
from agents.web_search_agent import web_agent
from langchain.tools import tool


@tool
def database_search_supervisor(query: str) -> str:
    """
    Retrieve relevant information from the application's PostgreSQL database.

    Use this tool when the user's question requires internal database
    records, stored documents, or information indexed in the RAG system.

    Args:
        query: The natural-language question to search in the database.

    Returns:
        A string containing the database agent's response.
    """
    result = database_agent.invoke({"query": query})

    return extract_agent_output(result)


@tool
def web_search_supervisor(query: str) -> str:
    """
    Search the internet for external information relevant to the user's question.

    Use this tool when the question requires external research, current
    information, documentation, or information unavailable in the database.

    Args:
        query: The natural-language internet search query.

    Returns:
        A string containing the web research agent's response.
    """
    result = web_agent.invoke({"topic": query})

    return extract_agent_output(result)


def extract_agent_output(result) -> str:
    """
    Extract a readable response from a LangChain or LangGraph agent result.
    """
    if isinstance(result, str):
        return result

    if isinstance(result, dict):
        if result.get("output"):
            return str(result["output"])

        if result.get("answer"):
            return str(result["answer"])

        messages = result.get("messages")

        if messages:
            last_message = messages[-1]
            return str(getattr(last_message, "content", last_message))

    if isinstance(result, list):
        if not result:
            return "The agent returned no results."

        last_message = result[-1]
        return str(getattr(last_message, "content", last_message))

    return str(result)


@tool
def web_search_supervisor(query: str) -> str:
    """
    Search the internet for relevant information related to the user's query.

    Use this tool when the supervisor needs external information, recent
    developments, explanations, documentation, or information that is not
    available in the application's database.

    Args:
        query: A natural-language search query describing the information
               to find on the internet.

    Returns:
        str: The web search agent's response as a readable string.
    """
    res = web_agent.invoke({
        "topic": query,
    })

    if isinstance(res, str):
        return res

    if isinstance(res, dict):
        return res.get("output") or res.get("answer") or str(res)

    if isinstance(res, list):
        if not res:
            return "The web search agent returned no results."

        last_message = res[-1]

        if hasattr(last_message, "content"):
            return str(last_message.content)

        return str(last_message)

    return str(res)
