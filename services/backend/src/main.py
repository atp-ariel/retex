from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # NEW
from .framework import BaseDocument
from .retex import Retex


app = FastAPI()
system = Retex("cran")

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Welcome to Retex API!"

@app.get("/search")
async def search(q: str) -> List[BaseDocument]:
    try: 
        docs = system.do_query(q)
        return docs
    except Exception as e:
        raise HTTPException(status_code=501, detail="Oops! Sorry. Unexpected error in execution of Retex system.")


@app.get("/collection")
async def collection(doc_id: int) -> BaseDocument:
    try:
        doc = system.framework.collection[doc_id - 1]
        return doc
    except Exception:
        raise HTTPException(status_code=404, detail="Document id not found")
