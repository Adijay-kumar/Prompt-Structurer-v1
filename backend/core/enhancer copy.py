from .role_selector import select_role_semantic
from .templates import INSTRUCTION_TEMPLATES, OUTPUT_FORMAT_TEMPLATES
from .model_loader import load_client

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

client = load_client()


def auto_select_keys(task, templates_dict, top_n=2):
    keys = list(templates_dict.keys())
    corpus = keys + [task]

    vectorizer = TfidfVectorizer().fit_transform(corpus)
    similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])[0]

    top_indices = similarity.argsort()[-top_n:][::-1]
    return [keys[i] for i in top_indices]


def build_prompt(task):
    role = select_role_semantic(task)

    instruction_keys = auto_select_keys(task, INSTRUCTION_TEMPLATES)
    output_keys = auto_select_keys(task, OUTPUT_FORMAT_TEMPLATES)

    instructions = []
    for key in instruction_keys:
        instructions.extend(INSTRUCTION_TEMPLATES.get(key, []))

    output_format = []
    for key in output_keys:
        output_format.extend(OUTPUT_FORMAT_TEMPLATES.get(key, []))

    return f"""
### Role
{role}

### Task
{task}

### Instructions
""" + "\n".join(f"- {i}" for i in instructions) + f"""

### Output Format
""" + "\n".join(f"- {o}" for o in output_format)


def extract_polished_prompt(text: str) -> str:
    if not text:
        return ""

    if "<<<POLISHED_PROMPT>>>" in text:
        text = text.split("<<<POLISHED_PROMPT>>>", 1)[1]

    # Remove any accidental echo of system markers
    if "<<<" in text:
        text = text.split("<<<", 1)[0]

    return text.strip()


def enhance_prompt(task):
    raw_prompt = build_prompt(task)

    meta_prompt = f"""
You are a prompt engineering expert.

TASK:
Rewrite and polish the prompt below without changing its intent.

STRICT RULES:
- Output ONLY the polished prompt
- Do NOT execute the prompt
- Do NOT include explanations or examples
- Preserve Markdown structure exactly
- Do NOT add code fences
- End immediately when the prompt definition is complete

OUTPUT:
Begin ONLY after <<<POLISHED_PROMPT>>>

PROMPT TO POLISH:
{raw_prompt}

<<<POLISHED_PROMPT>>>
"""

    response = client["generate"](
        model=client["model"],
        prompt=meta_prompt
    )

    text = response.get("response", "")
    return extract_polished_prompt(text)
