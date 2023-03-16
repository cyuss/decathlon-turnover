# -*- coding: utf-8 -*-

import pytest
from starlette.testclient import TestClient

from decathlon_turnover.main import get_app


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
