from pydantic import BaseModel


class LLMResponse(BaseModel):
    answer: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    cost: float
