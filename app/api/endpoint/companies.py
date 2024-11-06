from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_language, get_db
from app.db.schemas.company import CompanyCreate, CompanyTagCreate, CompanyResponse
from app.db.crud.company import (
    get_company_by_name,
    create_company,
    create_company_tag,
    delete_company_tag,
)

router = APIRouter()


"""
    회사 이름으로 회사 검색
"""


@router.get("/{company_name}", response_model=CompanyResponse)
def get_company(
    company_name: str,
    language: str = Depends(get_language),
    db: Session = Depends(get_db),
):
    company = get_company_by_name(db=db, company_name=company_name)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return CompanyResponse.from_company(company=company, language=language)


"""
    새로운 회사 추가
"""


@router.post("/", response_model=CompanyResponse)
def create_new_company(
    company_data: CompanyCreate,
    language: str = Depends(get_language),
    db: Session = Depends(get_db),
):
    new_company = create_company(db=db, company_data=company_data)

    return CompanyResponse.from_company(company=new_company, language=language)


"""
    회사 태그 정보 추가
"""


@router.put("/{company_name}/tags", response_model=CompanyResponse)
def create_new_company_tag(
    company_name: str,
    tag_data: List[CompanyTagCreate],
    language: str = Depends(get_language),
    db: Session = Depends(get_db),
):
    company = get_company_by_name(db=db, company_name=company_name)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    company = create_company_tag(db=db, company=company, tag_data=tag_data)

    return CompanyResponse.from_company(company=company, language=language)


"""
    회사 태그 정보 삭제
"""


@router.delete("/{company_name}/tags/{tag_name}", response_model=CompanyResponse)
def delete_exist_company_tag(
    company_name: str,
    tag_name: str,
    language: str = Depends(get_language),
    db: Session = Depends(get_db),
):
    company = get_company_by_name(db=db, company_name=company_name)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    company = delete_company_tag(db=db, company=company, tag_name=tag_name)

    return CompanyResponse.from_company(company=company, language=language)
