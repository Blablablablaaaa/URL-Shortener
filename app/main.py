from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse, FileResponse
from schemas import set_new_code
from database import init_db


app = FastAPI()

longLink = "https://vk.com/blablablajh"

@app.get("/")
def root():
    return FileResponse("../static/index.html")

@app.post(longLink)
def createShortUrl(longLink):
    set_new_code(longLink)

    return {"long url":"...", "short url":"http://127.0.0.1:8000/{code}"}

@app.get()
def redirectShortYrl():
    return (RedirectResponse )