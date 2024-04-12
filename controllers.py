from fastapi import HTTPException

from models import User
from utils import upload_to_server, validate_photo


async def register_new_user(user_with_profile_picture: dict[str, any], session):

    if not await validate_photo(user_with_profile_picture["pfp_url"]):
        raise HTTPException(
            status_code=422,
            detail="The file must be a .jpg, .jpeg or .png file",
        )

    new_pfp_url = await upload_to_server(user_with_profile_picture["pfp_url"])
    print(new_pfp_url)

    created_user: User = {
        "first_name": user_with_profile_picture["first_name"],
        "last_name": user_with_profile_picture["last_name"],
        "mail": user_with_profile_picture["mail"],
        "pfp_url": new_pfp_url,
    }

    created_user_in_db = User(**created_user)
    session.add(created_user_in_db)
    session.commit()
    session.refresh(created_user_in_db)

    return created_user
