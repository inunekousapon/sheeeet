from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(
    docs_url=None,
    redoc_url=None,
)
templates = Jinja2Templates(directory="templates")

app.mount("/page", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=RedirectResponse)
def read_root(request: Request):
    return RedirectResponse("/page/index.html")
