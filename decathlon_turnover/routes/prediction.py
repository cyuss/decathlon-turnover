# -*- coding: utf-8 -*-

from fastapi import APIRouter

from ..utils.model_manager import dummy_model, encoder
from ..utils.preprocessing import transform
from .schemas import BatchPredictionIn, PredictionIn

router = APIRouter()


@router.post("/predict")
async def predict(req_input: PredictionIn):
    df = transform(
        [
            req_input.dict(),
        ],
        encoder,
    )
    result = dummy_model.predict(df)
    output = {"turnover": result[0]}

    return output


@router.post("/batch_predict")
async def batch_predict(req_input: BatchPredictionIn):
    req_input = req_input.dict()["input"]
    print(type(req_input))
    df = transform(req_input, encoder)
    results = dummy_model.predict(df)
    output = {"turnover": list(results)}

    return output
