# -*- coding: utf-8 -*-

from fastapi import FastAPI
from loguru import logger

from decathlon_turnover.core import settings
from decathlon_turnover.core.event_handlers import start_app_handler, stop_app_handler
from decathlon_turnover.core.middlewares import RequestContextLogMiddleware
from decathlon_turnover.routes import api_router

metadata = settings.get_settings()


def get_app() -> FastAPI:
    logger.info("App Initialization")
    fast_app = FastAPI(title=metadata.app_name, version=metadata.app_version)
    fast_app.include_router(api_router, prefix=metadata.api_prefix)
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))
    fast_app.add_middleware(RequestContextLogMiddleware)

    return fast_app


app = get_app()
