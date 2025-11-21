import sys
import os
import asyncio
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from app.models.user import UserCreate, create_user

async def create_admin():
    admin = UserCreate(username="admin", email="admin@example.com", password="admin1")
    user = await create_user(admin)
    print("Admin user created:", user)

if __name__ == "__main__":
    asyncio.run(create_admin())
