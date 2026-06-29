from pydantic import BaseModel


class ChunkClass(BaseModel):
    text: str
    page: int
    chunk_index: int
    source: str
    embedding: list[float] | None = None
