from sqlalchemy.orm import Session

from app.services.chunking_service import chunk_document
from app.services.embedding_service import generate_embeddings
from app.services.create_chunk_service import create

from app.schemas.chunk_schema import ChunkClass
from app.schemas.ingest_schema import IngestRequest


def ingest_document(text: IngestRequest, db: Session):
    chunks = chunk_document(text)

    for chunk in chunks:
        embedding = generate_embeddings(chunk)

        chunk_data = ChunkClass(chunk, embedding)

        create(chunk_data, db)

    return {"message": "Document ingested successfully", "chunks": len(chunks)}
