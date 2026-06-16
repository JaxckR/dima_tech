import logging
from functools import partial
from typing import Final

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


logger = logging.getLogger(__name__)

EXCEPTIONS: Final[dict[type[Exception], int]] = {}


class ErrorResponse(BaseModel):
    detail: str


async def validate(_: Request, exception: Exception, code: int) -> JSONResponse:
    return JSONResponse(
        status_code=code, content=ErrorResponse(detail=str(exception)).model_dump()
    )


async def internal_error(_: Request, exception: Exception) -> JSONResponse:
    logger.exception("ERROR", exc_info=exception)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(detail="Internal server error").model_dump(),
    )


def setup_exceptions(app: FastAPI) -> None:
    for exc, code in EXCEPTIONS.items():
        app.add_exception_handler(exc, partial(validate, code=code))

    app.add_exception_handler(Exception, internal_error)

    logger.info("Exception handlers setup")
