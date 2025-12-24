from datasets import load_dataset
import json
from pathlib import Path


OUTPUT_FILE = Path(__file__).parent / "roles.json"

def extract_role_text(prompt: str) -> str:
    return prompt.split(".")[0].strip()

def build_roles():
    dataset = load_dataset(
        "fka/awesome-chatgpt-prompts",
        split="train"
    )

    roles = []
    for example in dataset:
        role = extract_role_text(example["prompt"])
        if role and len(role) < 100:
            roles.append(role)

    roles = sorted(set(roles))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(roles, f, indent=2)

    print(f"Saved {len(roles)} roles to roles.json")

if __name__ == "__main__":
    build_roles()
