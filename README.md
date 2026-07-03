# RAG Engine V2 - Semantic Retrieval from Scratch

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, and Sentence Transformers. This version replaces manual Python-based similarity computation with native PostgreSQL vector search, resulting in a cleaner and more scalable retrieval pipeline.

## Features

- PDF document ingestion
- Page-wise text extraction using PyMuPDF
- Fixed-size chunking with overlap
- Metadata-aware chunking (`source`, `page_number`, `chunk_index`)
- Semantic embeddings using `BAAI/bge-small-en-v1.5`
- PostgreSQL + pgvector vector storage
- Native pgvector cosine similarity search
- Top-K semantic retrieval
- Modular ingestion pipeline
- FastAPI REST API

---

## Architecture

```text
PDF
    ↓
Page Extraction
    ↓
Page-wise Chunking
    ↓
Embedding Generation
    ↓
PostgreSQL (pgvector)
    ↓
────────────────────────────────────
User Query
    ↓
Query Embedding
    ↓
Native pgvector Search
    ↓
Top-K Retrieval
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/ingest` | Upload and index a PDF document |
| POST | `/search` | Retrieve the most relevant chunks |

---

## Tech Stack

- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- PyMuPDF
- Sentence Transformers

---

## Project Structure

- PDF extraction service
- Chunking service
- Embedding service
- Retrieval service
- Ingestion orchestration service
- PostgreSQL storage layer

---

## Current Limitations

- No similarity thresholding
- No metadata/document filtering during retrieval
- No Approximate Nearest Neighbor (HNSW) indexing
- No hybrid retrieval (BM25 + Vector Search)
- No reranking
- No context construction
- No LLM-based answer generation
- No retrieval evaluation metrics
