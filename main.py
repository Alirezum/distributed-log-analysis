from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    print("Hello from log-analysis!")


if __name__ == "__main__":
    main()
