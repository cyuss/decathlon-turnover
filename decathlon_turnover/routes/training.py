# -*- coding: utf-8 -*-

from typing import Dict, Union

from fastapi import APIRouter

router = APIRouter()


@router.post("/train")
def train() -> Dict[str, Union[str, None]]:
    return {"message": "Training done!"}
