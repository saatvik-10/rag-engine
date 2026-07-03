# RAG Engine V1.5 - Semantic Retrieval from Scratch

A Retrieval-Augmented Generation (RAG) engine built from scratch using FastAPI, PostgreSQL, pgvector, and Sentence Transformers. This version introduces PDF ingestion, metadata-aware indexing, and a modular ingestion pipeline while focusing on building a robust retrieval system before integrating an LLM.

## Features

* PDF document ingestion
* Page-wise text extraction using PyMuPDF
* Fixed-size chunking with overlap
* Metadata-aware chunking (`source`, `page_number`, `chunk_index`)
* Semantic embeddings using `BAAI/bge-small-en-v1.5`
* PostgreSQL + pgvector storage
* Cosine similarity search
* Top-K semantic retrieval
* Modular ingestion pipeline
* FastAPI REST API

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
------------------------------------
User Query
    ↓
Query Embedding
    ↓
Cosine Similarity
    ↓
Top-K Retrieval
```

## API Endpoints

| Method | Endpoint  | Description                       |
| ------ | --------- | --------------------------------- |
| POST   | `/ingest` | Upload and index a PDF document   |
| POST   | `/search` | Retrieve the most relevant chunks |

## Tech Stack

* FastAPI
* PostgreSQL
* pgvector
* SQLAlchemy
* PyMuPDF
* Sentence Transformers
<!-- * NumPy -->

## Project Structure

* PDF extraction service
* Chunking service
* Embedding service
* Retrieval service
* Ingestion orchestration service
* PostgreSQL storage layer

## Current Limitations

* Linear similarity search over stored embeddings
* No similarity threshold
* No metadata filtering during retrieval
* No hybrid search (BM25 + Vector)
* No reranking
* No LLM-based answer generation

## Roadmap

* Native pgvector similarity search
* Similarity thresholding
* Hybrid retrieval (BM25 + Vector Search)
* Cross-Encoder reranking
* Context construction
* LLM-powered answer generation
* Grounded responses with citations
