from fastapi import APIRouter
from app.api.routes.findings import router as findings_router


router = APIRouter()

router.include_router(findings_router, prefix="/findings", tags=["findings"])

