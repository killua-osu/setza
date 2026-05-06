from __future__ import annotations

from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from pydantic import BaseModel, ConfigDict, Field, field_validator

from apps.common.choices import RoleType


class RoleSelectionInput(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    role: str = Field(default=RoleType.CREATOR)

    @field_validator("role")
    @classmethod
    def validate_role(cls, value: str) -> str:
        if value not in RoleType.values:
            raise ValueError("Choose either Creator or Brand.")
        return value


class BasicProfileInput(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    display_name: str = Field(min_length=2, max_length=120)
    location: str = Field(min_length=2, max_length=120)
    bio: str = Field(min_length=16, max_length=1200)
    contact_email: str = Field(default="", max_length=254)

    @field_validator("contact_email")
    @classmethod
    def validate_contact_email(cls, value: str) -> str:
        if not value:
            return value
        value = value.lower()
        try:
            validate_email(value)
        except DjangoValidationError as exc:
            raise ValueError("Enter a valid contact email address.") from exc
        return value
