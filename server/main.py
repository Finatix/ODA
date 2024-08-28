#! /bin/env python3

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# webserver api

@app.get("/", response_class=HTMLResponse)
async def index():
    return read_html_file("index.html")

# helpers

def get_html_dir() -> Path:
    return Path(__file__).parent / "resources" / "static" / "html"

def read_html_file(file: str) -> str:
    html_file = get_html_dir() / file

    return html_file.read_text()
