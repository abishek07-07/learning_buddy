from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv(find_dotenv())


text =['hello world from me ', ' this is considered as cheating', 'dgflkhdfghldihejhg']

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")


embedded_texts   = embeddings.embed_query(text);


print(len(embedded_texts))
