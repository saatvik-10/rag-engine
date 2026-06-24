from app.db.db import engine, Base
from app.models.chunk import Chunk

Base.metadata.create_all(bind=engine)

print("Tables Created")
