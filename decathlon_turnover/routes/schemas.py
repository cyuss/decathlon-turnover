# -*- coding: utf-8 -*-


from pydantic import BaseModel

# --------------------- EXAMPLES ---------------------


# ---------------------- INPUTS ----------------------
class TrainIn(BaseModel):
    pass


class PredictIn(BaseModel):
    pass


# ---------------------- OUTPUTS ----------------------
class TrainOut(BaseModel):
    message: str


class PredictOut(BaseModel):
    message: str
