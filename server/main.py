from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse,  HTMLResponse
from pathlib import Path
from typing import Annotated

app = FastAPI()

# webserver api

@app.get("/", response_class=HTMLResponse)
async def index():
    return read_html_file("index.html")

@app.get("/static/{resource:path}", response_class=FileResponse)
async def resource(resource: Annotated[str, 'resource path e.g. "styles.css"']):
    file = get_resource_path() / resource

    if not file.is_file():
        raise HTTPException(status_code=404, detail=f"File not found: {resource}")

    return file


# helpers

def get_html_dir() -> Path:
    return get_resource_path() / "html"

def get_resource_path() -> Path:
    return Path(__file__).resolve().parent / "resources" / "static"

def read_html_file(file: str) -> str:
    html_file = get_html_dir() / file

    return html_file.read_text()
