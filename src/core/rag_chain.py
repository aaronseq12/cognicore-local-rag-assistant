from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_community.llms import LlamaCpp

CHROMA_PATH = "chroma_db"
MODEL_PATH = "models/Phi-3-mini-4k-instruct-q4.gguf"

def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    retriever = vectorstore.as_retriever(search_kwargs={'k': 3})

    template = """
    <|system|>
    You are a helpful assistant. Use the following context to answer the question.
    If you don't know the answer, just say you don't know. Answer concisely.</s>
    <|user|>
    Context: {context}
    Question: {question}</s>
    <|assistant|>
    """
    prompt = ChatPromptTemplate.from_template(template)

    llm = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.1,
        n_ctx=2048,
        verbose=False
    )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain