from pydantic import BaseModel, Field
from typing import Optional

class DonationRequestCreate(BaseModel):
    recipient_id: str
    item: str
    custom: Optional[str] = None

class DonationRequestInDB(DonationRequestCreate):
    id: str

class DonationRequestResponse(DonationRequestInDB):
    pass
