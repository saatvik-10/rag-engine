from sqlalchemy.orm import Session

from app.models.chunk import Chunk


def bm25_retrieval(query: str, top_k: int, db: Session):
    document_frequency = {}

    chunks = db.query(Chunk).all()

    query_tokens = set(query.lower().split())

    for token in query_tokens:
        cnt = 0
        for chunk in chunks:
            words = set(chunk.text.lower().split())

            if token in words:
                cnt += 1

        document_frequency[token] = cnt

    print(document_frequency)
