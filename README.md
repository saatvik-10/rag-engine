# Production-Grade RAG Engine from Scratch

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, Sentence Transformers, and OpenRouter.

The project implements the core components of a modern retrieval pipeline, including semantic search, BM25 lexical retrieval, hybrid retrieval using Reciprocal Rank Fusion (RRF), context engineering, grounded answer generation, and retrieval observability.

---

## Features

- PDF document ingestion
- Metadata-aware chunking
- Semantic embeddings
- PostgreSQL + pgvector vector search
- BM25 lexical retrieval
- Hybrid Retrieval (RRF)
- Context construction
- Prompt construction
- Grounded LLM responses
- Source citations
- Query observability

---

## Architecture

```text
                INGESTION

               PDF Document
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



────────────────────────────────────────────────────────────



                 RETRIEVAL

                User Question
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
 Query Embedding          BM25 Retrieval
        │                        │
        ▼                        ▼
 Vector Search         Lexical Search
        └───────────┬────────────┘
                    ▼
         Reciprocal Rank Fusion
                    │
                    ▼
             Context Builder
                    │
                    ▼
             Prompt Builder
                    │
                    ▼
              OpenRouter LLM
                    │
                    ▼
            Grounded Response
                    │
                    ▼
             Source Citations
                    │
                    ▼
              Observability
```

---

## API Endpoints

| Method | Endpoint  | Description                                     |
| ------ | --------- | ----------------------------------------------- |
| POST   | `/ingest` | Upload and index PDF documents                  |
| POST   | `/search` | Hybrid retrieval and grounded answer generation |

---

## Tech Stack

- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- Sentence Transformers
- PyMuPDF
- OpenRouter

---

## Core Concepts

- Dense Retrieval
- Sparse Retrieval (BM25)
- Hybrid Retrieval
- Reciprocal Rank Fusion (RRF)
- Semantic Search
- Vector Databases
- Context Engineering
- Prompt Engineering
- Grounded Generation
- Retrieval Observability

---

## Retrieval Pipeline

1. Extract text from PDF documents.
2. Chunk documents with metadata.
3. Generate semantic embeddings.
4. Store embeddings in PostgreSQL using pgvector.
5. Generate the query embedding.
6. Retrieve semantic candidates using pgvector.
7. Retrieve lexical candidates using BM25.
8. Fuse both rankings using Reciprocal Rank Fusion (RRF).
9. Build contextual prompt.
10. Generate a grounded response with OpenRouter.
11. Return the response with source citations and observability metrics.
