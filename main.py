import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from openai import OpenAI

ROOT = Path(__file__).resolve().parent
app = FastAPI(title="Khanh Đan AI")
app.mount("/static", StaticFiles(directory=ROOT / "static"), name="static")

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)
    history: list[dict] = Field(default_factory=list)

@app.get("/")
def home():
    return FileResponse(ROOT / "static" / "index.html")

@app.get("/manifest.json")
def manifest():
    return FileResponse(ROOT / "static" / "manifest.json", media_type="application/manifest+json")

@app.get("/health")
def health():
    return {"ok": True, "app": "Khanh Đan AI"}

@app.post("/api/chat")
def chat(req: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="Máy chủ chưa được cấu hình OPENAI_API_KEY.")
    try:
        client = OpenAI(api_key=api_key)
        # Keep only recent, well-formed turns and cap input size.
        previous = []
        for item in req.history[-12:]:
            role = item.get("role")
            content = item.get("content")
            if role in ("user", "assistant") and isinstance(content, str):
                previous.append({"role": role, "content": content[:4000]})
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            instructions=(
                "Bạn là Khanh Đan AI, một trợ lý AI thân thiện, hữu ích. "
                "Trả lời bằng tiếng Việt tự nhiên, rõ ràng, phù hợp lứa tuổi học sinh. "
                "Nếu không chắc, hãy nói rõ thay vì bịa thông tin."
            ),
            input=previous + [{"role": "user", "content": req.message}],
            max_output_tokens=1200,
        )
        return {"reply": response.output_text}
    except Exception as exc:
        # Avoid returning credentials or internal stack traces to the browser.
        print("OpenAI request failed:", repr(exc))
        raise HTTPException(status_code=502, detail="AI đang gặp lỗi kết nối. Hãy thử lại sau.")
