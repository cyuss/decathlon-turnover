# -*- coding: utf-8 -*-

from typing import Optional

from pydantic import BaseModel

# --------------------- EXAMPLES ---------------------


# ---------------------- INPUTS ----------------------
class InfoIn(BaseModel):
    pass


class TrainIn(BaseModel):
    pass


class PredictIn(BaseModel):
    pass


# ---------------------- OUTPUTS ----------------------
class InfoOut(BaseModel):
    app_name: str
    app_version: str
    app_description: str
    author: Optional[str] = None
    host: str
    port: str


class TrainOut(BaseModel):
    message: str


class PredictOut(BaseModel):
    message: str
