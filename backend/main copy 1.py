from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from backend.core.enhancer import enhance_prompt
from backend.core.role_selector import ROLE_TEXTS

app = FastAPI(title="Prompt Enhancer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    task: str
    instruction_keys: Optional[List[str]] = []
    output_keys: Optional[List[str]] = []

@app.get("/roles")
def get_roles():
    return {"roles": ROLE_TEXTS}

@app.post("/enhance")
def enhance(request: PromptRequest):
    polished = enhance_prompt(
        request.task,
        request.instruction_keys,
        request.output_keys
    )
    return {"polished_prompt": polished}

@app.get("/")
def root():
    return {"message": "Prompt Enhancer API is running"}
