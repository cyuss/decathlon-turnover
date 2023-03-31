# -*- coding: utf-8 -*-

from typing import Optional

from pydantic import BaseModel, Field

# --------------------- EXAMPLES ---------------------


# ---------------------- INPUTS ----------------------
class PredictionIn(BaseModel):
    year: int = Field(..., title="Year input")
    month: int = Field(..., title="Month input")
    week_of_year: int = Field(..., title="Week of the year")
    day_of_week: int = Field(..., title="Day of the week")
    quarter: int = Field(..., title="Quarter in the year")
    but_latitude: float = Field(..., title="Latitude - Store's coordinates")
    but_longitude: float = Field(..., title="Longitude - Store's coordinates")
    but_num_business_unit: str = Field(..., title="Store's ID")
    dpt_num_department: str = Field(..., title="Department's ID")
    but_postcode: str = Field(..., title="Store's postcode location")
    but_region_idr_region: str = Field(..., title="Region's ID")
    zod_idr_zone_dgr: str = Field(..., title="Zone's ID")


class BatchPredictionIn(BaseModel):
    input: list[PredictionIn]


# ---------------------- OUTPUTS ----------------------
class InfoOut(BaseModel):
    app_name: str
    app_version: str
    app_description: str
    author: Optional[str] = None
    host: str
    port: str


class PredictionOut(BaseModel):
    turnover: float


class BatchPredictionOut(BaseModel):
    turnover: list[float]
