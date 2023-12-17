from fastapi import APIRouter
from .controllers.automate import chat_router, vision_router
from .controllers.automate import chat_router
from .controllers.automate import vision_router
api_router = APIRouter()

api_router.include_router(
    chat_router,
    prefix="/chat",
    tags=["API endpoints for AutoMate Gen-AI App's text questions"],
)

api_router.include_router(
    vision_router,
    prefix="/vision",
    tags=["API endpoints for AutoMate Gen-AI App's vision questions"],
)
