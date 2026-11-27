from langchain_groq import ChatGroq


model = "openai/gpt-oss-120b"


llm = ChatGroq(
    model= model,
    temperature= 0.4
)