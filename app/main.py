from fastapi import FastAPI

from app.database import engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def main():
    return {"status": "ok"}


if __name__ == "__main__":
    main()
