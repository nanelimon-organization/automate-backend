from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import chat_router, vision_router
import os
from logging.config import dictConfig

from api.config.logger.log_config import LogConfig

def create_app() -> FastAPI:
    """
    Create the FastAPI application.
    Returns
    -------
    app : FastAPI
        The FastAPI instance.
    """

    app = FastAPI(
        title="AutoMate Gen-AI Backend Service",
        description="Backend service of AutoMate Gen-AI application. Includes API endpoints for chat and video operations.",
        version="0.0.1",
    )

    init_routers(app)
    init_logger()
    configure_middleware(app)

    return app

def init_routers(app: FastAPI) -> None:
    """
    Initialize routers for the application.
    Parameters
    ----------
    app : FastAPI
        The FastAPI instance to attach the routers to.
    Returns
    -------
    None
    """
    app.include_router(chat_router)
    app.include_router(vision_router)

def init_logger():
    dictConfig(LogConfig().dict())

def configure_middleware(app: FastAPI) -> None:
    """
    Configure middleware for the application.
    Parameters
    ----------
    app : FastAPI
        The FastAPI instance to configure the middleware for.
    Returns
    -------
    None
    """
    origins = os.getenv("CORS_ORIGINS", "*").split(",")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

app = create_app()
