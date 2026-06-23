from sqlalchemy import Column, Text
from pgvector.sqlalchemy import Vector
from app.db.database import Base


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Text, primary_key=True)
    text = Column(Text, nullable=False)
    embedding = Column(Vector, nullable=False)
