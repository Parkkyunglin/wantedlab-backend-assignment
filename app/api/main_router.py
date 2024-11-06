from fastapi import APIRouter

from app.api.endpoint import search, companies

api_router = APIRouter()
api_router.include_router(search.router)
api_router.include_router(companies.router, prefix="/companies")
