import os
import logging
from dotenv import load_dotenv

from app.common.error import InternalError


load_dotenv()


class Config:
    version = "0.1.0"
    title = "releads"

    app_settings = {
        'db_name': os.environ['MONGO_DB'],
        'mongodb_url': os.environ['MONGO_URL'],
        'db_username': os.environ['MONGO_USER'],
        'db_password': os.environ['MONGO_PASSWORD'],
        'max_db_conn_count': os.environ['MAX_CONNECTIONS_COUNT'],
        'min_db_conn_count': os.environ['MIN_CONNECTIONS_COUNT'],
    }

    @classmethod
    def app_settings_validate(cls):
        for k, v in cls.app_settings.items():
            if None is v:
                logging.error(f'Config variable error. {k} cannot be None')
                raise InternalError([{"message": "Server configure error"}])
            else:
                logging.info(f'Config variable {k} is {v}')

