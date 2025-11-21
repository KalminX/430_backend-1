from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.donation_request import DonationRequestCreate, DonationRequestResponse
from app.routes.auth import get_current_user
from app.models.user import User
from app.database import donation_request_collection
from bson import ObjectId

router = APIRouter()

@router.post("/donation-requests/", response_model=DonationRequestResponse)
async def create_donation_request(request: DonationRequestCreate, current_user: User = Depends(get_current_user)):
    # Only recipients can create requests (optional: check user role)
    data = request.dict()
    data["_id"] = ObjectId()
    await donation_request_collection.insert_one(data)
    return {"id": str(data["_id"]), **request.dict()}

@router.get("/donation-requests/", response_model=List[DonationRequestResponse])
async def list_donation_requests(current_user: User = Depends(get_current_user)):
    requests = []
    async for r in donation_request_collection.find():
        requests.append({
            "id": str(r["_id"]),
            "recipient_id": r["recipient_id"],
            "item": r["item"],
            "custom": r.get("custom")
        })
    return requests
