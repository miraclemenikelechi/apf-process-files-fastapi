import uuid

from pydantic import EmailStr, Field
from sqlmodel import VARCHAR, Column, Field, SQLModel


class CreateUser(SQLModel):
    first_name: str = Field(
        min_length=1,
        max_length=50,
    )

    last_name: str = Field(
        min_length=1,
        max_length=50,
    )

    mail: EmailStr = Field(
        sa_column=Column("email", VARCHAR, unique=True, index=True),
        description="Email of the user",
    )

    pfp_url: str


class User(CreateUser, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
