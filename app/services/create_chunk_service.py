from uuid import uuid4
from sqlalchemy.orm import Session
from app.models.chunk import Chunk


def create(chunk_data: Chunk, db: Session):
    stored_chunk = Chunk(
        id=str(uuid4()),
        text=chunk_data.text,
        embedding=chunk_data.embedding,
        page=chunk_data.page,
        chunk_index=chunk_data.chunk_index,
        source=chunk_data.source,
    )

    db.add(stored_chunk)
    db.commit()
    db.refresh(stored_chunk)

    return stored_chunk
