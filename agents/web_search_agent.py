from langchain.agents import create_agent
from config.llm import llm
from tools.tavily import web_search


web_agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt="""
    You are a web research specialist for a student learning platform.

    Your responsibilities:
    1. Search the internet for information relevant to the question.
    2. Prefer reliable and authoritative sources.
    3. Compare information from relevant sources when necessary.
    4. Summarize the findings clearly.
    5. Include source URLs when available.
    6. Never fabricate sources or information.

    Return a concise research report.
    """
)