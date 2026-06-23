from app.services.embedding_service import generate_embeddings

embedding = generate_embeddings("Saatvik liked Solana Blockchain")

print(len(embedding))
