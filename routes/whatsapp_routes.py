from fastapi import APIRouter

router = APIRouter()


@router.post("/sync/whatsapp")
def sync_whatsapp(data: dict):
    print("New WhatsApp lead:", data)

    return {
        "status": "Lead received",
        "data": data
    }