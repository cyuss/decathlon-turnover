# -*- coding: utf-8 -*-

from typing import Callable

from fastapi import FastAPI
from loguru import logger

from decathlon_turnover.core import setup_logger


def start_app_handler(app: FastAPI) -> Callable[[], None]:
    def startup() -> None:
        setup_logger.setup_logging()
        logger.info("Service initialization")
        # model_manager.dummy_model = model_manager.load_model()
        # model_manager.encoder = model_manager._init_encoder()

    return startup


def stop_app_handler(app: FastAPI) -> Callable[[], None]:
    def shutdown() -> None:
        logger.info("Preparing the service shutdown.")

    return shutdown
