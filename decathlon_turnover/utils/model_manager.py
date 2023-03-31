# -*- coding: utf-8 -*-

import pickle

from loguru import logger


cat_features = [
    "but_num_business_unit",
    "dpt_num_department",
    "but_postcode",
    "but_region_idr_region",
    "zod_idr_zone_dgr",
]
# numerical features
num_features = [
    "year",
    "month",
    "week_of_year",
    "day_of_week",
    "quarter",
    "latitude",
    "longitude",
]


def load_model():
    """Loading a pretrained forecasting model"""
    model_path = "./models/turnover_prediction.joblib"
    with open(model_path, "rb") as model_file:
        logger.info("Loading forecasting model")
        dummy_regr = pickle.load(model_file)

    return dummy_regr


def _init_encoder():
    """Load the one hot encoder used during training process
    """
    with open("./models/encoder", "rb") as encoder_file:
        enc = pickle.load(encoder_file)

    return enc


dummy_model = load_model()
encoder = _init_encoder()
