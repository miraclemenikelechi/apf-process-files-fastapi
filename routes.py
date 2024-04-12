from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, UploadFile
from pydantic import EmailStr, Field

from controllers import register_new_user
from dependencies import SESSION_DEPENDENCY

users = APIRouter(prefix="/users", tags=["users"])


@users.post("/register")
async def register_user(
    first_name: Annotated[str, Form(min_length=1, max_length=50)],
    last_name: Annotated[str, Form(min_length=1, max_length=50)],
    mail: Annotated[EmailStr, Form()],
    profile_picture: UploadFile,
    db_access: SESSION_DEPENDENCY,
):

    data_to_be_processed: dict[str, any] = {
        "first_name": first_name,
        "last_name": last_name,
        "mail": mail,
        "pfp_url": profile_picture,
    }

    data = await register_new_user(
        user_with_profile_picture=data_to_be_processed,
        session=db_access,
    )

    if not data:
        raise HTTPException(status_code=400, detail="Could not create user")

    return data
