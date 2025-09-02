from fastapi import FastAPI
from pydantic import BaseModel
from src.core.rag_chain import get_rag_chain

app = FastAPI(title="CogniCore Local API")
rag_chain = get_rag_chain()

class Query(BaseModel):
    text: str

@app.post("/query")
async def process_query(query: Query):
    result = rag_chain.invoke(query.text)
    return {"answer": result}

@app.get("/")
async def health_check():
    return {"status": "ok"}