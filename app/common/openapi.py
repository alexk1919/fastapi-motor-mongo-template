from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Callable

from app.conf.config import Config


def get_custom_openapi(app: FastAPI) -> Callable:
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title=Config.title,
            version=Config.version,
            routes=app.routes
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return custom_openapi
