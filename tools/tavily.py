from langchain_tavily import TavilySearch
from dotenv import load_dotenv , find_dotenv
from langchain.tools import tool

load_dotenv(find_dotenv())

tv = TavilySearch(max_results=5)

@tool()
def web_search(topic):
    """Search the internet for current information on a given topic."""
    topic = topic.lower()

    results = tv.invoke({"query":topic})
    print(results)
    return results
