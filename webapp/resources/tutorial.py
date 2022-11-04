from fastapi.responses import HTMLResponse
from fastapi import Request
from webapp import app
from webapp.resources import templates


@app.get("/", response_class=HTMLResponse)
async def website(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})