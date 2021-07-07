from typing import List
from fastapi import APIRouter, Body, Depends  
from starlette.status import HTTP_201_CREATED  
from app.models.finding import FindingBase, FindingCreate, FindingPublic  
from app.db.repositories.findings import FindingsRepository  
from app.api.dependencies.database import get_repository  

router = APIRouter()

@router.get("/")
async def getFindings() -> List[dict]:
    findings = [
        {"id": 2, "finding_class_id": 200, "application_id": 3000, "uri": "example_uri", "signature": "example_signature", "state": 9, "create_time": 1545730073, "update_time": 1545730073},
        {"id": 3, "finding_class_id": 300, "application_id": 4000, "uri": "example_uri2", "signature": "example_signature2", "state": 2, "create_time": 1545730073, "update_time": 1545730073}
    ]

    return findings

@router.post("/", status_code=HTTP_201_CREATED)
async def create_new_finding(
    findings_repo: FindingsRepository = Depends(get_repository(FindingsRepository)),
):
    created_finding = await findings_repo.create_finding(new_finding={"finding_class_id": 700, "application_id": 8000, "uri": "example_uri4", "signature": "example_signature4", "state": 5})
    return created_finding
