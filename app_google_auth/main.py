from fastapi import Body, Depends
import xlwings as xw

from app import app, User, get_current_user


@app.post("/hello")
def hello(data: dict = Body(...), current_user: User = Depends(get_current_user)):
    # Instantiate a Book object with the deserialized request body
    book = xw.Book(json=data)

    # Write the email address of the authenticated user to a cell
    sheet = book.sheets[0]
    sheet["A1"].value = current_user.email

    # Pass the following back as the response
    return book.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
