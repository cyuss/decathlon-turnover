# -*- coding: utf-8 -*-

from typing import Dict, Union

from fastapi import APIRouter

router = APIRouter()


@router.post("/predict")
def predict() -> Dict[str, Union[str, None]]:
    return {"message": "Prediction done!"}
