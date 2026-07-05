# RAG Engine V3 - Retrieval-Augmented Generation from Scratch

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, Sentence Transformers, and OpenRouter. The project focuses on understanding every stage of the RAG pipeline instead of relying on high-level frameworks, covering ingestion, semantic retrieval, context engineering, prompt construction, and grounded answer generation.

## Features

- PDF document ingestion
- Page-wise text extraction using PyMuPDF
- Fixed-size chunking with overlap
- Metadata-aware chunking (`source`, `page_number`, `chunk_index`)
- Semantic embeddings using `BAAI/bge-small-en-v1.5`
- PostgreSQL + pgvector vector storage
- Native pgvector cosine similarity search
- Similarity thresholding
- Context construction
- Prompt construction
- Grounded LLM answer generation via OpenRouter
- Modular service-oriented architecture
- FastAPI REST API

---

## Architecture

```text
                 Ingestion

PDF
 │
 ▼
Page Extraction
 │
 ▼
Chunking
 │
 ▼
Embedding Generation
 │
 ▼
PostgreSQL + pgvector


────────────────────────────────────────────


                 Retrieval

User Query
 │
 ▼
Query Embedding
 │
 ▼
Native pgvector Search
 │
 ▼
Similarity Threshold
 │
 ▼
Context Builder
 │
 ▼
Prompt Builder
 │
 ▼
LLM
 │
 ▼
Grounded Response