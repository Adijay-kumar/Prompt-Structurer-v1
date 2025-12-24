# backend/core/model_loader.py
import ollama

_MODEL_NAME = "mistral"

def generate_text(prompt: str) -> str:
    result = ollama.generate(
        model=_MODEL_NAME,
        prompt=prompt,
        stream=False
    )
    
    return result.get("response", "")
