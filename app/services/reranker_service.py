from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, results, top_k):
    reranked_result = []

    pairs = [(query, result["text"]) for result in results]

    scores = model.predict(pairs)

    for result, score in zip(results, scores):
        reranked_result.append({**result, "score": score})

    reranked_result.sort(key=lambda x: x["score"], reverse=True)

    return reranked_result[:top_k]
