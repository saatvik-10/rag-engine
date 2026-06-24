from fastapi import FastAPI
from app.db.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
