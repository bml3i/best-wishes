from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Blessing(BaseModel):
    content: str = Field(description="祝福的内容")
