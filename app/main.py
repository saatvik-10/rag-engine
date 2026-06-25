from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.services.ingestion_service import ingest_document

from app.schemas.ingest_schema import IngestRequest

from app.db.db import get_db

app = FastAPI()


@app.post("/ingest")
def ingest_create(req: IngestRequest, db: Session = Depends(get_db)):
    return ingest_document(req.text, db)
