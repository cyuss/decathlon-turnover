# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
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
    "but_latitude",
    "but_longitude",
]


def transform(req_input, encoder):
    """Apply features engineering pipeline to the input

    Endpoint's input

    Parameters
    ----------
    req_input : list[dict[str, str]]
        Endpoint's input
    encoder :
        One Hot Encoder used during the training process
    """
    logger.info("Transforming input")
    df = pd.DataFrame.from_records(req_input)
    logger.debug(df.head())
    df_cat = df[cat_features]
    encoded_num = df[num_features].to_numpy()
    encoded_cat = encoder.transform(df_cat).toarray()
    X = np.concatenate((encoded_cat, encoded_num), axis=1)
    logger.debug(X)

    return X
