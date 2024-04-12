import os
import uuid

from fastapi import UploadFile


def render_file_extension(file: UploadFile) -> str:
    return file.filename.split(".")[-1].lower()


async def validate_photo(image: UploadFile) -> bool:
    valid_extensions: set[str] = {".jpg", ".jpeg", ".png"}
    max_file_size: int = 4 * 1024 * 1024  # 4MB in bytes
    file_extension: str = f".{render_file_extension(image)}"

    if not image or not image.filename:
        return False

    if file_extension not in valid_extensions:
        return False

    if image.size > max_file_size:
        return False

    return True


async def upload_to_server(file_to_upload: UploadFile) -> str:
    file_name: str = str(uuid.uuid4()) + "." + render_file_extension(file_to_upload)
    folder_to_save_path: str = os.path.join(os.getcwd(), "assets/uploads")
    file_path: str = os.path.join(folder_to_save_path, file_name)

    if not os.path.exists(folder_to_save_path):
        os.makedirs(folder_to_save_path)

    with open(file_path, "wb") as buffer:
        buffer.write(file_to_upload.file.read())

    return file_name
