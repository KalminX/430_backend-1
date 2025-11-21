from fastapi import APIRouter, HTTPException, status
from app.models.contact import Contact, ContactCreate, create_contact

router = APIRouter()


@router.post("/contact/", response_model=Contact, status_code=status.HTTP_201_CREATED)
async def submit_contact_form(contact: ContactCreate):
    """
    This endpoint allows users to submit contact form data
    Request Body:
        name: name of the person
        email: email of the person
        message: the message content
    """
    try:
        contact_data = await create_contact(contact)
        return contact_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save contact message: {str(e)}"
        )
