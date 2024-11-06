from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_language, get_db
from app.db.schemas.company import CompanyNameResponse, CompanyResponse
from app.db.crud.company import get_companies_by_name, get_companies_by_tag

router = APIRouter()


"""
    회사명 자동완성
"""


@router.get("/search", response_model=List[CompanyNameResponse])
def get_company_name_autocomplete(
    query: str, language: str = Depends(get_language), db: Session = Depends(get_db)
):
    companies = get_companies_by_name(db=db, name_query=query, language=language)

    field_name = f"company_name_{language}"

    return [{"company_name": getattr(company, field_name, "")} for company in companies]


"""
    태그명으로 회사 검색
"""


@router.get("/tags", response_model=List[CompanyResponse])
def search_company_by_tag(
    query: str, language: str = Depends(get_language), db: Session = Depends(get_db)
):
    companies = get_companies_by_tag(db=db, tag_query=query)

    results = []
    for company in companies:
        results.append(
            CompanyResponse.from_company(
                company=company, language=language, get_available_name=True
            )
        )

    return results
