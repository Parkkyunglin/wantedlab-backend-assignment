from typing import Optional
from pydantic import BaseModel


class LanguageBase(BaseModel):
    ko: Optional[str] = None
    en: Optional[str] = None
    ja: Optional[str] = None
    tw: Optional[str] = None
