from uuid import uuid4
from app.models.chunk import Chunk


def create(chunk_data: Chunk, db):
    stored_chunk = Chunk(
        id=str(uuid4()), text=chunk_data.text, embedding=chunk_data.embedding
    )

    db.add(stored_chunk)
    db.commit()
    db.refresh(stored_chunk)

    return stored_chunk
