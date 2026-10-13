from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie", version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str


@app.exception_handler(RuntimeError)
async def runtime_error_handler(request: Request, exc: RuntimeError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/qa")
async def qa(data: TextRequest):
    return {"result": answer_question(data.text)}


@app.post("/explain")
async def explain(data: TextRequest):
    return {"result": explain_topic(data.text)}


@app.post("/quiz")
async def quiz(data: TextRequest):
    return {"result": generate_quiz(data.text)}


@app.post("/summarize")
async def summarize(data: TextRequest):
    return {"result": summarize_text(data.text)}


@app.post("/learn/recommendations")
async def recommendations(data: TextRequest):
    return {"result": get_learning_recommendations(data.text)}


@app.get("/health")
async def health():
    return {"status": "ok", "app": "EduGenie"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
