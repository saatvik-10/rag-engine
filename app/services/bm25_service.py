import math

from sqlalchemy.orm import Session

from app.models.chunk import Chunk

from app.config.bm25_config import K1, B


def bm25_retrieval(query: str, top_k: int, db: Session):
    results = []

    idf = {}

    chunks = db.query(Chunk).all()

    query_tokens = set(query.lower().split())

    average_document_length = compute_average_doc_length(chunks)

    document_frequency = compute_document_frequency(chunks, query_tokens)

    for token in query_tokens:
        idf[token] = compute_idf(document_frequency[token], len(chunks))

    for chunk in chunks:
        words = chunk.text.lower().split()
        score = 0

        for token in query_tokens:
            term_frequency = compute_tf(words, token)

            score += compute_bm25(
                term_frequency,
                idf[token],
                len(words),
                average_document_length,
            )

        results.append(
            {
                "id": chunk.id,
                "text": chunk.text,
                "page_number": chunk.page,
                "chunk_index": chunk.chunk_index,
                "source": chunk.source,
                "score": score,
            }
        )

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]


def compute_average_doc_length(chunks: list[Chunk]) -> float:
    total_words = 0

    for chunk in chunks:
        total_words += len(chunk.text.lower().split())

    return total_words / len(chunks)


def compute_document_frequency(chunks, query_tokens) -> dict:
    document_frequency = {}

    for token in query_tokens:
        cnt = 0
        for chunk in chunks:
            words = set(chunk.text.lower().split())

            if token in words:
                cnt += 1

        document_frequency[token] = cnt

    return document_frequency


def compute_idf(document_frequency: int, total_documents: int) -> float:
    return math.log(
        (total_documents - document_frequency + 0.5) / (document_frequency + 0.5)
    )


def compute_tf(words: list[str], token: str) -> int:
    return words.count(token)


def compute_bm25(
    term_frequency: int,
    idf: float,
    document_length: int,
    average_document_length: float,
) -> float:
    document_norm = 1 - B + B * (document_length / average_document_length)

    N = term_frequency * (K1 + 1)
    D = term_frequency + K1 * document_norm

    return idf * (N / D)
