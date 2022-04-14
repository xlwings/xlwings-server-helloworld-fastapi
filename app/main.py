import datetime as dt

import xlwings as xw
import yfinance as yf
from fastapi import Body

from app import app


@app.post("/hello")
def hello(data: dict = Body):
    # Instantiate a Book object with the deserialized request body
    book = xw.Book(json=data)

    # Use xlwings as usual
    sheet = book.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"

    # Pass the following back as the response
    return book.json()


@app.post("/yahoo")
def yahoo_finance(data: dict = Body):
    """
    This is a sample function using the yfinance package to query
    Yahoo! Finance. It writes a pandas DataFrame to Excel/Google Sheets.
    """
    book = xw.Book(json=data)

    if "yahoo" not in [sheet.name for sheet in book.sheets]:
        # Insert and prepare the sheet for first use
        sheet = book.sheets.add("yahoo")
        sheet["A1"].value = [
            "Ticker:",
            "MSFT",
            "Start:",
            dt.date.today() - dt.timedelta(days=30),
            "End:",
            dt.date.today(),
        ]
        for address in ["B1", "D1", "F1"]:
            sheet[address].color = "#D9E1F2"
        for address in ["D1", "F1"]:
            sheet[address].columns.autofit()
        sheet[
            "A3"
        ].value = "'=> Adjust the colored parameters and run the script again!"
        sheet.activate()
    else:
        # Query Yahoo! Finance
        sheet = book.sheets["yahoo"]
        target_cell = sheet["A3"]
        target_cell.expand().clear_contents()
        try:
            df = yf.download(
                sheet["B1"].value,
                start=sheet["D1"].value,
                end=sheet["F1"].value,
                progress=False,
            )
            target_cell.value = df
            target_cell.offset(row_offset=1).columns.autofit()
        except Exception as e:
            target_cell.value = repr(e)

    return book.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
