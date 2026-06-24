from app.schemas.chunk_schema import ChunkClass
from app.services.chunking_service import chunk_documents
from app.services.embedding_service import generate_embeddings
from app.services.create_chunk_service import create
from app.db.db import SessionLocal

text = """
Saatvik is currently learning AI systems.
He build a memory engine from scratch.
He is now working on a RAG engine
""" * 200

db = SessionLocal()

chunks = chunk_documents(text)

for chunk in chunks:
    embeddings = generate_embeddings(chunk)

    chunk_data = ChunkClass(text=chunk, embedding=embeddings)

    create(chunk_data, db)

print(f"Stored {len(chunks)} chunks")
