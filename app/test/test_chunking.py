from app.services.chunking_service import chunk_document

text = " ".join([f"word{i}" for i in range(1000)])

chunks = chunk_document(text)

print(len(chunks))

for i, chunk in enumerate(chunks):
    print(
        f"Chunk {i+1}: {len(chunk.split())}"
    )