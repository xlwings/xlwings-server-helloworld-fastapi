import datetime as dt

import xlwings as xw
import yfinance as yf
from fastapi import Body
import statbotics
sb = statbotics.Statbotics()

from app import app

@app.post("/getteaminfo")
def get_team_info(data: dict = Body):
    book = xw.Book(json=data)
    sheet = book.sheets[0]
    l1 = sb.get_teams(state="california", fields=['name']) # this is a list of dictionaries
    number_of_teams = sheet["D1"].value
    print(number_of_teams)
    for i in range(number_of_teams):
        sheet["A" + str(i+1)].value = l1[i]['name']
    return book.json() 



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
