from fastapi import FastAPI
from app.routes import donations, user, donor, recipient, reviews, volunteer, contact, donation_request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_standalone_docs import StandaloneDocs
app = FastAPI(
    title="Food Donation API",
    description="API for managing food donations, donors, recipients, community volunteers and reviews",
    version="1.0.0",
)

StandaloneDocs(app=app)

""" Enable CORS """
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow requests from any origin, change in production
    allow_credentials=True, # Allow cookies and authentication headers
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all HTTP headers
)

""" routes from other modules"""
app.include_router(user.router)
app.include_router(donor.router)
app.include_router(donations.router)
app.include_router(recipient.router)
app.include_router(volunteer.router)
app.include_router(reviews.router)
app.include_router(contact.router)
app.include_router(donation_request.router)

# --- Default admin creation logic (must be after app is defined) ---
from app.models.user import UserCreate
from app.database import user_collection
from app.utils import get_password_hash
import asyncio

@app.on_event("startup")
async def create_default_admin():
    admin_username = "admin"
    admin_email = "admin@example.com"
    admin_password = "admin1"
    admin_role = "admin"
    # Check if admin user exists
    existing = await user_collection.find_one({"username": admin_username})
    if not existing:
        user_doc = {
            "username": admin_username,
            "email": admin_email,
            "password": get_password_hash(admin_password),
            "role": admin_role
        }
        await user_collection.insert_one(user_doc)
        print("Default admin user created: username='admin', password='admin1'")
    else:
        print("Default admin user already exists.")
from fastapi import FastAPI
from app.routes import donations, user, donor, recipient, reviews, volunteer, contact, donation_request
from fastapi.middleware.cors import CORSMiddleware
from fastapi_standalone_docs import StandaloneDocs


app = FastAPI(
    title="Food Donation API",
    description="API for managing food donations, donors, recipients, community volunteers and reviews",
    version="1.0.0",
)

StandaloneDocs(app=app)

""" Enable CORS """
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow requests from any origin, change in production
    allow_credentials=True, # Allow cookies and authentication headers
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all HTTP headers
)

""" routes from other modules"""
app.include_router(user.router)
app.include_router(donor.router)
app.include_router(donations.router)
app.include_router(recipient.router)
app.include_router(volunteer.router)
app.include_router(reviews.router)
app.include_router(contact.router)
app.include_router(donation_request.router)
