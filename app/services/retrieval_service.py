from app.models.chunk import Chunk
from app.services.similarity_service import cosine_similarity
from app.services.embedding_service import generate_embeddings
from sqlalchemy.orm import Session


def chunks_retrieval(query: str, top_k: int, db: Session):
    query_embedding = generate_embeddings(query)

    chunks = db.query(Chunk).all()

    results = []

    for chunk in chunks:
        score = cosine_similarity(query_embedding, chunk.embedding)

        results.append({"id": chunk.id, "chunk": chunk.text, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]
