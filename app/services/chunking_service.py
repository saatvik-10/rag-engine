from app.schemas.pdf_schema import PdfPage
from app.schemas.chunk_schema import ChunkClass


def chunk_page(
    page: PdfPage, chunk_size: int = 500, overlap: int = 100
) -> list[ChunkClass]:
    text = page.text
    words = text.split()

    chunks = []

    start = 0
    chunk_index = 0

    while start < len(words):
        end = start + chunk_size

        chunk_text = " ".join(words[start:end])

        chunks.append(
            ChunkClass(
                text=chunk_text,
                page=page.page,
                chunk_index=chunk_index,
                source=page.source,
            )
        )

        chunk_index += 1
        start += chunk_size - overlap

    return chunks
