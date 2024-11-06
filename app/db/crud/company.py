from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.core.config import supported_languages
from ..models.company import Company
from ..schemas.company import CompanyCreate, CompanyTagCreate


def get_companies_by_name(db: Session, name_query: str, language: str):
    field_name = f"company_name_{language}"

    company_name_column = getattr(Company, field_name)
    if company_name_column:
        return db.query(Company).filter(company_name_column.contains(name_query)).all()

    return []


def get_companies_by_tag(db: Session, tag_query: str):
    return (
        db.query(Company)
        .filter(
            or_(
                Company.company_tag_ko.contains(tag_query),
                Company.company_tag_en.contains(tag_query),
                Company.company_tag_ja.contains(tag_query),
                Company.company_tag_tw.contains(tag_query),
            )
        )
        .distinct()
        .all()
    )


def get_company_by_name(db: Session, company_name: str):
    return (
        db.query(Company)
        .filter(
            or_(
                Company.company_name_ko == company_name,
                Company.company_name_en == company_name,
                Company.company_name_ja == company_name,
                Company.company_name_tw == company_name,
            )
        )
        .first()
    )


def create_company(db: Session, company_data: CompanyCreate):
    company = Company()

    for language in supported_languages:
        company_name = getattr(company_data.company_name, language, None)
        if company_name:
            setattr(company, f"company_name_{language}", company_name)

        tag_list = []
        for tag in company_data.tags:
            new_tag = getattr(tag.tag_name, language, None)
            if new_tag:
                tag_list.append(new_tag)

        if tag_list:
            setattr(company, f"company_tag_{language}", "|".join(tag_list))

    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def create_company_tag(db: Session, company: Company, tag_data: List[CompanyTagCreate]):
    for language in supported_languages:
        new_tag_list = []
        for tag in tag_data:
            new_tag = getattr(tag.tag_name, language, None)
            if new_tag:
                new_tag_list.append(new_tag)

        exist_tags = getattr(company, f"company_tag_{language}", language)
        exist_tag_list = exist_tags.split("|") if exist_tags else []

        new_tag_list.extend(exist_tag_list)
        if new_tag_list:
            new_tag_list = sorted(new_tag_list)
            setattr(company, f"company_tag_{language}", "|".join(new_tag_list))

    db.commit()
    db.refresh(company)
    return company


def delete_company_tag(db: Session, company: Company, tag_name: str):
    for language in supported_languages:
        exist_tags = getattr(company, f"company_tag_{language}", language)
        exist_tag_list = exist_tags.split("|") if exist_tags else []

        new_tag_list = [tag for tag in exist_tag_list if tag != tag_name]
        new_tag_list = sorted(new_tag_list)
        setattr(company, f"company_tag_{language}", "|".join(new_tag_list))

    db.commit()
    db.refresh(company)
    return company
