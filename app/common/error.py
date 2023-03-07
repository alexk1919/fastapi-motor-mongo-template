from fastapi.responses import JSONResponse


class BaseErrResp(Exception):
    def __init__(self, status: int, title: str, details: list) -> None:
        self.__status = status
        self.__title = title
        self.__detail = details

    def gen_err_resp(self) -> JSONResponse:
        return JSONResponse(
            status_code=self.__status,
            content={
                "type": "about:blank",
                'title': self.__title,
                'status': self.__status,
                'detail': self.__detail
            }
        )


class BadRequest(BaseErrResp):
    def __init__(self, details: list):
        super(BadRequest, self).__init__(400, 'Bad Request', details)


class InternalError(BaseErrResp):
    def __init__(self, details: list):
        super(InternalError, self).__init__(500, 'Internal Error', details)


class UnprocessableError(BaseErrResp):
    def __init__(self, details: list):
        super(UnprocessableError, self).__init__(
            422,
            'Unprocessable Entity',
            details
        )
