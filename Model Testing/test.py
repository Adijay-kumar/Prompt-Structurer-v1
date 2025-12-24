# test_ollama.py
from ollama import generate

# Generate from local model
response = generate(
    model="mistral",  # or "gemma3:4b"
    prompt="Explain transformers to a beginner"
)

print("Model Response:\n")
print(response)
