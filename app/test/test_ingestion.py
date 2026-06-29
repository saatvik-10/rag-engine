from app.services.ingestion_service import ingest_document

from app.db.db import SessionLocal

db = SessionLocal()

test = ingest_document("report.pdf", db)

db.close

print(test)
