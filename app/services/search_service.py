from sqlalchemy.orm import Session

from app.services.retrieval_service import chunks_retrieval


def search_query(query: str, top_k: int, db: Session):
    results = chunks_retrieval(query, top_k, db)

    return results
