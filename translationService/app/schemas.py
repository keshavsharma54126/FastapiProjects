from pydantic import BaseModel  # type: ignore
from typing import List,Dict

class TranslationRequest(BaseModel):
    text: str
    language: List[str]

class TaskResponse(BaseModel):
    tast_id: int

class TranslationStatus(BaseModel):
    task_id: int
    status: str 
    translation: Dict[str,str]