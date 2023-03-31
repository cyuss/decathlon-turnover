# -*- coding: utf-8 -*-

from typing import Generator

import pandas as pd
import pytest
from starlette.testclient import TestClient

from decathlon_turnover.main import get_app


@pytest.fixture(scope="session")
def test_client() -> Generator[TestClient, None, None]:
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="session")
def test_df_train() -> pd.DataFrame:
    df_train = pd.read_csv("./data/processed/train.csv", sep=";", encoding="utf-8")

    return df_train


@pytest.fixture(scope="session")
def test_df_test() -> pd.DataFrame:
    df_test = pd.read_csv("./data/processed/test.csv", sep=";", encoding="utf-8")

    return df_test
