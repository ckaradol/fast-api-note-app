from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from google.cloud.firestore_v1.base_query import FieldFilter
from models.note import Note,NotesResponse
from dependencies.auth import verify_token
from services.firebase import db, map_firebase_error
from utils.errors import error_responses
from datetime import datetime, timezone

from utils.response import response_get_note,response_delete_note,response_set_note,response_update_note
router = APIRouter(prefix="/notes", tags=["notes"], responses=error_responses)

def generate_prefix_tokens(text: str) -> list[str]:
    tokens = []
    for word in text.split():
        word = word.lower()
        tokens.extend([word[:i] for i in range(1, len(word)+1)])
    return tokens

@router.get(
    "",
    response_model=NotesResponse,
    responses=response_get_note,
)
def list_notes(
    user_id: str = Depends(verify_token),
    search: Optional[str] = Query(None, description="Search with prefix"),
    limit: int = Query(10, ge=1, description="Number of notes per page"),
    last_id: Optional[str] = Query(None, description="Last note ID from previous page")
):
    try:
        notes_query = db.collection("notes").where(
            filter=FieldFilter("user_id", "==", user_id)
        ).order_by("created_at")

        if last_id:
            last_note = db.collection("notes").document(last_id).get()
            if last_note.exists:
                notes_query = notes_query.start_after({"created_at": last_note.get("created_at")})

        if search:
            search_token = search.lower()
            notes_query = notes_query.where(filter=FieldFilter("search_tokens", "array_contains", search_token))

        notes_query = notes_query.limit(limit)
        notes_ref = notes_query.stream()

        notes = [{"id": n.id, **n.to_dict()} for n in notes_ref]
        return {"success": True, "data": notes,"status":200}

    except Exception as e:
        code, msg = map_firebase_error(e)
        return {"success": False, "detail": msg,"status":code}

@router.post("", response_model=dict,  responses=response_set_note,)
def create_note(note: Note, user_id: str = Depends(verify_token)):
    try:
        search_tokens = generate_prefix_tokens(note.title) + generate_prefix_tokens(note.content)

        note_data = {
            "title": note.title,
            "content": note.content,
            "user_id": user_id,
            "search_tokens": search_tokens,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        doc_ref = db.collection("notes").document()
        doc_ref.set(note_data)
        return {"success": True, "data": {**note_data, "id": doc_ref.id},"status":200}
    except Exception as e:
        code, msg = map_firebase_error(e)
        return {"success": False, "detail": msg,"status":code}

@router.put("/{note_id}", response_model=dict,  responses=response_update_note,)
def update_note(note_id: str, note: Note, user_id: str = Depends(verify_token)):
    try:
        doc_ref = db.collection("notes").document(note_id)
        doc = doc_ref.get()
        if not doc.exists:
            return {"success": False, "detail": "Note not found"}
        if doc.to_dict().get("user_id") != user_id:
            return {"success": False, "detail": "You are not allowed to update this note"}
        doc_ref.update({"title": note.title, "content": note.content})
        return {"success": True, "data": {"id": note_id, "title": note.title, "content": note.content},"status":200}
    except Exception as e:
        code, msg = map_firebase_error(e)
        return {"success": False, "detail": msg,"status":code}

@router.delete("/{note_id}", response_model=dict,responses=response_delete_note)
def delete_note(note_id: str, user_id: str = Depends(verify_token)):
    try:
        doc_ref = db.collection("notes").document(note_id)
        doc = doc_ref.get()
        if not doc.exists:
            return {"success": False, "detail": "Note not found","status":404}
        if doc.to_dict().get("user_id") != user_id:
            return {"success": False, "detail": "You are not allowed to delete this note","status":400}
        doc_ref.delete()
        return {"success": True, "message": "Note deleted","status":200}
    except Exception as e:
        code, msg = map_firebase_error(e)
        return {"success": False, "detail": msg,"status":code}
