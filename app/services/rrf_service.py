from app.config.rrf_config import RRF_K


def rrf_fusion(chunks_retrieval, bm25_retrieval):
    rrf_scores = {}
    chunk_map = {}

    update_rrf_scores(chunks_retrieval, rrf_scores, chunk_map)
    update_rrf_scores(bm25_retrieval, rrf_scores, chunk_map)

    sorted_rrf_scores = sorted(
        rrf_scores.items(), key=lambda item: item[1], reverse=True
    )

    final_results = []

    for chunk_id, score in sorted_rrf_scores:
        result = chunk_map[chunk_id].copy()
        result["score"] = score
        final_results.append(result)

    return final_results


def update_rrf_scores(results, rrf_scores, chunk_map):
    for rank, result in enumerate(results, start=1):
        chunk_id = result["id"]
        contribution = compute_rrf_score(rank)

        if chunk_id not in chunk_map:
            chunk_map[chunk_id] = result

        if chunk_id not in rrf_scores:
            rrf_scores[chunk_id] = 0

        rrf_scores[chunk_id] += contribution


def compute_rrf_score(rank):
    return 1 / (RRF_K + rank)
