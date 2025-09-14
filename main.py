from fastapi import FastAPI
from routes import notes

app = FastAPI(title="Notes API with Firebase")

app.include_router(notes.router)
