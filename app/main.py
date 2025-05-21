from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def healthcheck():
    return {"status": "ok"}

from app.database import Base, engine
from app.models import models

Base.metadata.create_all(bind=engine)