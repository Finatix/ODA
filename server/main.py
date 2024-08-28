from fastapi import FastAPI
from fastapi.responses import FileResponse,  HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# settings

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "resources" / "static"
HTML_DIR = STATIC_DIR / "html"

# webserver

app = FastAPI()

## static files
app.mount("/static", StaticFiles(directory=STATIC_DIR))

## frontend
@app.head("/")
@app.get("/")
async def index():
    return FileResponse(HTML_DIR / "index.html")
