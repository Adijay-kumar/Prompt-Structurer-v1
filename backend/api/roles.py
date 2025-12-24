import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

ROLES_FILE = Path(__file__).parents[1] / "roles" / "roles.json"

with open(ROLES_FILE, "r", encoding="utf-8") as f:
    ROLES = json.load(f)

@router.get("/roles")
def get_roles():
    return {
        "count": len(ROLES),
        "roles": ROLES
    }
