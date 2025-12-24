from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.enhancer import enhance_prompt
from backend.core.role_selector import ROLE_TEXTS




app = FastAPI(title="Prompt Enhancer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/roles")
def get_roles():
    return {"roles": ROLE_TEXTS}

@app.post("/enhance")
def enhance(prompt_task: dict):
    task = prompt_task.get("task", "")
    instructions = prompt_task.get("instruction_keys", [])
    output_keys = prompt_task.get("output_keys", [])

    return {
        "polished_prompt": enhance_prompt(task)
    }
