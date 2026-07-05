# RAG Engine V3 - Retrieval-Augmented Generation from Scratch

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, Sentence Transformers, and OpenRouter.

Instead of relying on high-level frameworks, this project focuses on implementing every major component of a modern RAG pipeline from first principles, including document ingestion, semantic retrieval, context engineering, prompt construction, and grounded answer generation.

---

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
- Grounded LLM answer generation using OpenRouter
- Modular service-oriented architecture
- FastAPI REST API

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
              OpenRouter LLM
                    │
                    ▼
            Grounded Response
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/ingest` | Upload and index a PDF document |
| POST | `/search` | Retrieve relevant context and generate a grounded answer |

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

## Project Structure

```text
app/
│
├── config/
│   ├── embedding_config.py
│   ├── model_config.py
│   └── threshold_config.py
│
├── models/
│
├── routers/
│
├── schemas/
│
├── services/
│   ├── pdf_service.py
│   ├── chunking_service.py
│   ├── embedding_service.py
│   ├── retrieval_service.py
│   ├── context_builder_service.py
│   ├── prompt_builder_service.py
│   ├── llm_service.py
│   └── ingestion_service.py
│
└── main.py
```

---

## Retrieval Pipeline

1. Extract text from uploaded PDF documents.
2. Split pages into overlapping chunks.
3. Generate semantic embeddings for every chunk.
4. Store embeddings and metadata inside PostgreSQL using pgvector.
5. Embed the user's query.
6. Perform native cosine similarity search inside PostgreSQL.
7. Filter low-quality matches using a similarity threshold.
8. Build structured context from retrieved chunks.
9. Construct a grounded prompt.
10. Generate the final response using an LLM.

---

## Current Limitations

- No metadata-based filtering
- No Approximate Nearest Neighbor (HNSW) indexing
- No hybrid retrieval (BM25 + Vector Search)
- No Cross-Encoder reranking
- No source citations in generated responses
- No streaming responses
- No evaluation framework
- No conversational memory integration

---

## Roadmap

- HNSW indexing
- Metadata filtering
- Hybrid Retrieval (BM25 + Vector Search)
- Cross-Encoder reranking
- Source-aware citations
- Streaming LLM responses
- Retrieval evaluation metrics
- Conversational memory integration
- Multi-document retrieval
- Tool calling

---

## Version History

### v1

- Semantic retrieval pipeline
- PDF ingestion
- Chunking
- Embedding generation
- Manual cosine similarity in Python

### v1.5

- Metadata-aware chunking
- Modular service architecture
- Improved ingestion pipeline

### v2

- Native pgvector similarity search
- Database-side retrieval
- Similarity thresholding

### v3

- Context construction
- Prompt construction
- OpenRouter integration
- Complete Retrieval-Augmented Generation pipeline

---

## Future Goals

This project is part of a broader effort to build AI systems from first principles, covering retrieval, memory, evaluation, tool use, routing, and agentic workflows without abstracting away the underlying architecture.