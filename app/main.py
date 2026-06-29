import os
import shutil

from fastapi import Depends, FastAPI, UploadFile, File
from sqlalchemy.orm import Session

from app.services.ingestion_service import ingest_document
from app.services.search_service import search_query

from app.schemas.ingest_schema import IngestRequest
from app.schemas.search_schema import SearchRequest

from app.db.db import get_db

app = FastAPI()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/ingest")
def ingest_create(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    ingest_document(file_path, db)
    
    return {
    "message": "Document ingested successfully."
    }


@app.post("/search")
def search(req: SearchRequest, db: Session = Depends(get_db)):
    return search_query(req.query, req.top_k, db)
