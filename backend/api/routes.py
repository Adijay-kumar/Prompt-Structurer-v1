from fastapi import APIRouter
from schemas.prompt import PromptRequest, PromptResponse
from core.enhancer import enhance_prompt

router = APIRouter()

@router.post("/enhance", response_model=PromptResponse)
def enhance(request: PromptRequest):
    """
    Enhance a prompt using Ollama-powered core.enhancer
    """
    result = enhance_prompt(
        task=request.task,
        instruction_keys=request.instruction_keys,
        output_keys=request.output_keys
    )
    return {"polished_prompt": result}
