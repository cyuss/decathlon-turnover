from fastapi import APIRouter

from decathlon_turnover.routes import info


api_router = APIRouter()

api_router.include_router(info.router, tags=["metadata"])
