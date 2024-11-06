from fastapi import Header

from app.db.session import SessionLocal
from app.core.config import supported_languages, fallback_language


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_language(x_wanted_language: str = Header(...)):
    if x_wanted_language not in supported_languages:
        return fallback_language

    return x_wanted_language
