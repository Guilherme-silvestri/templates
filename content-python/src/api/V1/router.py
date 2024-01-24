from fastapi import APIRouter

from src.api.V1.endpoints import listcards

router = APIRouter(prefix="/v1")
router.include_router(listcards.router)