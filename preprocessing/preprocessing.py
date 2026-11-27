""" this file is for parsing the pdf """


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import  RecursiveCharacterTextSplitter



splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000 ,
    chunk_overlap = 200,
    length_function= len
)

def parse_pdf(pdf_path : str):
    pdf_loader = PyPDFLoader(pdf_path)
    pdf_text = pdf_loader.load_and_split(splitter)
    print(len(pdf_text))




# parse_pdf("docs/AI_Engineering.pdf")





