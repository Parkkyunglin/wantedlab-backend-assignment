from sqlalchemy import Column, Integer, String, Text
from ..base_class import Base


class Company(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name_ko = Column(String(length=256), nullable=True)
    company_name_en = Column(String(length=256), nullable=True)
    company_name_ja = Column(String(length=256), nullable=True)
    company_name_tw = Column(String(length=256), nullable=True)
    company_tag_ko = Column(Text, nullable=True)
    company_tag_en = Column(Text, nullable=True)
    company_tag_ja = Column(Text, nullable=True)
    company_tag_tw = Column(Text, nullable=True)
