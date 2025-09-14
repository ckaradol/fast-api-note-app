from pydantic import BaseModel
from typing import Any, Optional, List

class NoteOut(BaseModel):
    id: str
    title: str
    content: str
    user_id: str
    created_at: str

class NotesResponse(BaseModel):
    success: bool
    status: int
    data: List[NoteOut]
class Note(BaseModel):
    id: str | None = None
    title: str
    content: str
    user_id: str | None = None
    created_at: str | None = None
