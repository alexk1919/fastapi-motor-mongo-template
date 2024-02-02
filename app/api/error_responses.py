import logging

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.common.error import UnprocessableError
from app.main import app


@app.exception_handler(RequestValidationError)
async def invalid_req_handler(
    _: Request,
    exc: RequestValidationError
) -> JSONResponse:
    logging.error(f'Request invalid. {str(exc)}')
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            'title': 'Bad Request',
            'status': 400,
            'detail': [str(exc)]
        }
    )


@app.exception_handler(UnprocessableError)
async def unprocessable_error_handler(
    _: Request,
    exc: UnprocessableError
) -> JSONResponse:
    return exc.gen_err_resp()
