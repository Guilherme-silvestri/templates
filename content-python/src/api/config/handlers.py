from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.domain.exceptions.ProposalExceptions import ProposalNotFoundException

def add_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        print(f"Parâmetros inválidos: {exc}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {
                    "errors": [{"field": error["loc"], "error": error["msg"]} for error in exc.errors()],
                }
            ),
        )

    @app.exception_handler(ProposalNotFoundException)
    async def not_found_exception_handler(request: Request, exc: ProposalNotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"errors": [{"message": exc.message, "param": exc.param}]},
        )