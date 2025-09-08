from fastapi import FastAPI

from db.db import get_db

import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return get_db()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
