from pydantic import BaseModel


class ChunkClass(BaseModel):
    text: str
    embedding: list[float]
