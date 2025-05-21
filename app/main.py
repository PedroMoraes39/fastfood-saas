from fastapi import FastAPI

from app.database import Base, engine
from app.models import models  # noqa

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


Base.metadata.create_all(bind=engine)
