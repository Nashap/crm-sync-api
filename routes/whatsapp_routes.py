from fastapi import APIRouter

router = APIRouter()


@router.post("/sync/whatsapp")
def sync_whatsapp(data: dict):
    return {
        "status": "Lead received",
        "data": data
    }