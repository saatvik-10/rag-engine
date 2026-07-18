import time

from sqlalchemy.orm import Session

from app.services.retrieval_service import chunks_retrieval
from app.services.context_builder_service import context_builder
from app.services.prompt_builder import prompt_builder
from app.services.llm_service import generate_answer
from app.services.observability_service import log_query
from app.services.bm25_service import bm25_retrieval
from app.services.rrf_service import rrf_fusion
from app.services.reranker_service import rerank

from app.config.threshold_config import RETRIEVAL_THRESHOLD


def search_query(query: str, top_k: int, db: Session):
    sources = []
    seen = set()

    vector_results = chunks_retrieval(query, top_k, db)
    bm25_results = bm25_retrieval(query, top_k, db)

    rrf_results = rrf_fusion(vector_results, bm25_results)

    # results are sorted by Cross-Encoder relevance score.
    results = rerank(query, rrf_results, top_k)

    if not results:
        return {"message": "No chunks found"}

    # results already being sorted by descending similarity score
    # if results[0]["score"] < RETRIEVAL_THRESHOLD:
    #     return {"message": "No relevant context retrieved"}

    for result in results:
        key = (result["source"], result["page"])

        if key not in seen:
            seen.add(key)

            sources.append({"source": result["source"], "page": result["page"]})

    context = context_builder(results)

    prompt = prompt_builder(query, context)

    start_time = time.time()
    try:
        llm_response = generate_answer(prompt)
    except:
        return {"message": "Unable to generate response at the moment."}
    elapsed_time = time.time() - start_time

    log_query(
        query=query,
        results=results,
        context_size=len(context),
        prompt_size=len(prompt),
        model=llm_response.model,
        prompt_tokens=llm_response.prompt_tokens,
        completion_tokens=llm_response.completion_tokens,
        total_tokens=llm_response.total_tokens,
        cost=llm_response.cost,
        latency=elapsed_time,
        answer=llm_response.answer,
    )

    return {"answer": llm_response.answer, "sources": sources}
