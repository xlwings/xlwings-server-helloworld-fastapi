import os
import secrets

import xlwings as xw
from fastapi import Body, FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader

# Require the API_KEY for every endpoint
app = FastAPI()


@app.post("/hello")
def hello(data: dict = Body):
    # Instantiate a Book object with the deserialized request body
    book = xw.Book(json=data)

    # Use xlwings as usual
    sheet = book.sheets[0]
    cell = sheet["A1"]
    if cell.value == "Hello xlwings!":
        cell.value = "Bye xlwings!"
    else:
        cell.value = "Hello xlwings!"

    # Pass the following back as the response
    return book.json()


# Excel on the web requires CORS
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*.officescripts.microsoftusercontent.com",
    allow_methods=["POST"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
