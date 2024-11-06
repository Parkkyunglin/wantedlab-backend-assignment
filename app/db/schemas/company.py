from typing import List, Optional
from pydantic import BaseModel

from app.core.config import supported_languages
from .common import LanguageBase
from ..models.company import Company


class CompanyTagBase(BaseModel):
    tag_name: LanguageBase


class CompanyBase(BaseModel):
    company_name: LanguageBase
    tags: List[CompanyTagBase]


class CompanyCreate(CompanyBase):
    pass


class CompanyTagCreate(CompanyTagBase):
    pass


class CompanyNameResponse(BaseModel):
    company_name: Optional[str] | None

    class Config:
        from_attributes = True


class CompanyResponse(BaseModel):
    company_name: Optional[str] | None
    tags: List[Optional[str] | None]

    class Config:
        from_attributes = True

    def get_available_name_from_all_language(company: Company, default_language: str):
        language_order = supported_languages
        language_order.insert(0, default_language)

        for value in language_order:
            name = getattr(company, f"company_name_{value}")
            if name:
                return name

        return ""

    @classmethod
    def from_company(
        cls, company: Company, language: str, get_available_name: bool = False
    ):
        if get_available_name:
            company_name = cls.get_available_name_from_all_language(
                company=company, default_language=language
            )
        else:
            company_name = getattr(company, f"company_name_{language}", language)

        company_tags = getattr(company, f"company_tag_{language}", language)
        company_tag_list = company_tags.split("|") if company_tags else []

        return cls(company_name=company_name, tags=company_tag_list)
