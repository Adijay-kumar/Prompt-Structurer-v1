from pydantic import BaseModel
from typing import List

class PromptRequest(BaseModel):
    task: str
    instruction_keys: List[str]
    output_keys: List[str]

class PromptResponse(BaseModel):
    polished_prompt: str
