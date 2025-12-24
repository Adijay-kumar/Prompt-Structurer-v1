# backend/core/model_loader.py
import ollama

_MODEL_NAME = "mistral"  # or "gemma3:4b"

def load_client():
    """
    Returns a callable dictionary to access Ollama's generate function.
    """
    return {
        "model": _MODEL_NAME,
        "generate": ollama.generate  # Direct function from Ollama SDK
    }
