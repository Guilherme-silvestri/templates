from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.config.handlers import add_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from src.api.V1.router import router
from src.api.resources import APIResources

#def create_app(lifespan) -> FastAPI:
def create_app() -> FastAPI:    
    app = FastAPI(
        title="cardsys",
        description="cardsys process manager",
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        #lifespan=lifespan,
    )

    app.include_router(router=router, prefix="/cardsys/api")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    add_exception_handler(app)
    return app

#@asynccontextmanager
#async def lifespan(app: FastAPI):    
#    app.api_resources = APIResources()
#    yield
#    app.api_resources.shutdown_resources()

app = create_app()
