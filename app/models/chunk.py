from sqlalchemy import Column, Text, Integer
from pgvector.sqlalchemy import Vector
from app.db.db import Base


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Text, primary_key=True)
    text = Column(Text, nullable=False)
    embedding = Column(Vector, nullable=False)
    page = Column(Integer, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    source = Column(Text, nullable=False)
