from fastapi import APIRouter

from decathlon_turnover.routes import prediction, training, info

api_router = APIRouter()

api_router.include_router(info.router, tags=["metadata"])
api_router.include_router(training.router, tags=["training"])
api_router.include_router(prediction.router, tags=["inference"])
