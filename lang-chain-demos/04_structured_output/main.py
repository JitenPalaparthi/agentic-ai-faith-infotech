from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama

class CodeReview(BaseModel):
    summary: str = Field(description="Short review summary")
    risk: str = Field(description="low, medium, or high")
    suggestions: list[str]

llm = ChatOllama(model="qwen3:0.6b", temperature=0)
structured = llm.with_structured_output(CodeReview)
code = "func divide(a, b int) int { return a / b }"
result = structured.invoke(f"Review this Go code: {code}. Return the requested structure. /no_think")
print(result.model_dump_json(indent=2))
