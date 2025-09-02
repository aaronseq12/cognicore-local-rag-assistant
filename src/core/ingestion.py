import os
from langchain_community.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"
DATA_PATH = "src/data"

def ingest_data():
    print("Starting data ingestion...")
    documents = []
    for filename in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
        elif filename.endswith(".md"):
            loader = UnstructuredMarkdownLoader(path)
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunked_docs = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunked_docs)} chunks.")

    print("Creating embeddings with local model 'all-MiniLM-L6-v2'...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    print("Creating and persisting vector store...")
    vectorstore = Chroma.from_documents(
        documents=chunked_docs,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"Data ingestion complete. Vector store ready at {CHROMA_PATH}")

if __name__ == "__main__":
    ingest_data()