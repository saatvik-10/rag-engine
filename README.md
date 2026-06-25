# RAG Engine V1

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, and Sentence Transformers. This version focuses on understanding the retrieval pipeline before integrating an LLM.

## Features

- Document ingestion
- Fixed-size chunking with overlap
- Semantic embeddings using `BAAI/bge-small-en-v1.5`
- PostgreSQL + pgvector storage
- Cosine similarity search
- Top-K semantic retrieval
- FastAPI REST API

## Architecture

```text
Document
    ↓
Chunking
    ↓
Embedding
    ↓
PostgreSQL (pgvector)
    ↓
-------------------------
User Query
    ↓
Query Embedding
    ↓
Cosine Similarity
    ↓
Top-K Retrieval
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/ingest` | Ingest and index a document |
| POST | `/search` | Retrieve the most relevant chunks |

## Tech Stack

- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- Sentence Transformers
- NumPy

## Current Limitations

- Text-only ingestion
- Fixed-size chunking
- Linear search over stored embeddings
- No metadata filtering
- No reranking
- No LLM-based answer generation

## Roadmap

- PDF ingestion
- Metadata support
- Similarity threshold
- Hybrid retrieval (BM25 + Vector Search)
- Cross-Encoder reranking
- LLM-based answer generation