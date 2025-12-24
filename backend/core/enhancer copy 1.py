from .role_selector import select_role_semantic
from .templates import INSTRUCTION_TEMPLATES, OUTPUT_FORMAT_TEMPLATES

from .model_loader import generate_text

 # dictionary with 'model' and 'generate'

def build_prompt(task, instruction_keys, output_keys):
    role = select_role_semantic(task)

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
""" + "\n".join(f"- {i}" for i in instructions) + """\n
### Output Format
""" + "\n".join(f"- {o}" for o in output_format)



def enhance_prompt(task, instruction_keys, output_keys):
    raw_prompt = build_prompt(task, instruction_keys, output_keys)

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

    text = generate_text(meta_prompt)

    if "<<<POLISHED_PROMPT>>>" in text:
        text = text.split("<<<POLISHED_PROMPT>>>", 1)[-1]

    STOP_MARKERS = [
        "```",
        "Example Output",
        "### Code",
        "### Explanation",
        "Step 1",
        "<hr>",
    ]

    for marker in STOP_MARKERS:
        if marker in text:
            text = text.split(marker, 1)[0]

    return text.strip()
