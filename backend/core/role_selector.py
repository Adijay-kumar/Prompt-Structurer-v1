import json
from pathlib import Path
from difflib import SequenceMatcher


BASE_DIR = Path(__file__).resolve().parent.parent
ROLES_PATH = BASE_DIR / "roles" / "roles.json"

with open(ROLES_PATH, "r", encoding="utf-8") as f:
    ROLE_TEXTS = json.load(f)


def similarity(a: str, b: str) -> float:
    """Simple string similarity for semantic matching."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def select_role_semantic(task: str) -> str:
    """
    Select the most relevant role from cached roles.json for a given task.
    Returns a default role if nothing matches well.
    """
    best_role = "You are an AI assistant"
    best_score = 0.0

    for role in ROLE_TEXTS:
        score = similarity(task, role)
        if score > best_score:
            best_score = score
            best_role = role

    return best_role
