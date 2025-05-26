from fastapi import FastAPI
from app import auth, views

app = FastAPI()

app.include_router(auth.router)
app.include_router(views.router)
