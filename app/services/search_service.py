from sqlalchemy.orm import Session

from app.services.retrieval_service import chunks_retrieval
from app.services.context_builder_service import context_builder
from app.services.prompt_builder import prompt_builder
from app.services.llm_service import generate_answer

from app.config.threshold_config import RETRIEVAL_THRESHOLD


def search_query(query: str, top_k: int, db: Session):
    results = chunks_retrieval(query, top_k, db)

    if not results:
        return {"message": "No chunks found"}

    # results already being sorted by descending similarity score
    if results[0]["score"] < RETRIEVAL_THRESHOLD:
        return {"message": "No relevant context retrieved"}

    context = context_builder(results)

    prompt = prompt_builder(query, context)

    try:
        response = generate_answer(prompt)
    except:
        return {"message": "Unable to generate response at the moment."}

    return response
