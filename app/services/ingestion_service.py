from sqlalchemy.orm import Session

from app.services.chunking_service import chunk_page
from app.services.embedding_service import generate_embeddings
from app.services.create_chunk_service import create
from app.services.pdf_service import extract_pdf


def ingest_document(pdf_path: str, db: Session):
    pages = extract_pdf(pdf_path)

    for page in pages:
        chunks = chunk_page(page)

        for chunk in chunks:
            chunk.embedding = generate_embeddings(chunk.text)
            create(chunk, db)

    return {"message": "Document ingested successfully", "chunks": len(chunks)}
