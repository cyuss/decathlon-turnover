# -*- coding: utf-8 -*-

import subprocess

import pytest
from starlette.testclient import TestClient

from decathlon_turnover.core import settings


@pytest.mark.api
def test_version() -> None:
    """Test the application's version defined in settings
    class compared to the version number defined by Poetry.
    """
    proc = subprocess.Popen(["poetry", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    out = out.decode("utf-8").rstrip()
    poetry_version = out.split(" ")[1]

    assert settings.get_settings().app_version == poetry_version


@pytest.mark.api
def test_info(test_client: TestClient) -> None:
    """Test info endpoint.

    Parameters
    ----------
    test_client : TestClient
        The API Client for testing
    """
    response = test_client.get("/info")
    assert response.status_code == 200


@pytest.mark.api
def test_prediction(test_client: TestClient) -> None:
    """Test turnover prediction endpoint.

    Parameters
    ----------
    test_client : TestClient
        The API Client for testing
    """
    pass


@pytest.mark.ml
def test_model_loading() -> None:
    pass
