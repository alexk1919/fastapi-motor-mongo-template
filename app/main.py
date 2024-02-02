from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.db.db import connect_and_init_db, close_db_connect
from app.conf.logging import setup_logging
from app.conf.config import Config
from app.common.openapi import get_custom_openapi

from app.api import health
from app.api.v1 import sample_resource as sample_resource_v1


setup_logging()

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# DB Events
app.add_event_handler("startup", Config.check_app_settings_on_none)
app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connect)

app.openapi = get_custom_openapi(app)

app.include_router(
    health.router,
    prefix='/health',
    tags=["health"]
)
app.include_router(
    sample_resource_v1.router,
    prefix='/api/sample-resource-app/v1/sample-resource',
    tags=["sample resource v1"]
)
