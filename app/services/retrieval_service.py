from app.models.chunk import Chunk
from app.services.similarity_service import cosine_similarity
from app.services.embedding_service import generate_embeddings
from sqlalchemy.orm import Session


def chunks_retrieval(query: str, top_k: int, db: Session):
    # query_embedding = generate_embeddings(query)

    # chunks = db.query(Chunk).all()

    # results = []

    # for chunk in chunks:
    #     score = cosine_similarity(query_embedding, chunk.embedding)

    #     results.append(
    #         {
    #             "id": chunk.id,
    #             "text": chunk.text,
    #             "page_number": chunk.page,
    #             "chunk_index": chunk.chunk_index,
    #             "source": chunk.source,
    #             "score": score,
    #         }
    #     )

    # results.sort(key=lambda x: x["score"], reverse=True)

    # return results[:top_k]

    query_embedding = generate_embeddings(query)

    distance = Chunk.embedding.cosine_distance(query_embedding)

    results = []

    chunks = (
        db.query(Chunk, distance.label("distance"))
        .order_by(distance)
        .limit(top_k)
        .all()
    )

    return results.append(
        {
            "id": chunk.id,
            "text": chunk.text,
            "page_number": chunk.page,
            "chunk_index": chunk.chunk_index,
            "source": chunk.source,
            "score": 1 - distance,
        }
        for chunk, distance in chunks
    )
