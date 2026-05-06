from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from apps.common.choices import RoleType


AUTH_FORM_FIELDS = {
    "sign_in": [
        {
            "name": "email",
            "label": "Email address",
            "type": "email",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        },
        {
            "name": "password",
            "label": "Password",
            "type": "password",
            "autocomplete": "current-password",
            "placeholder": "Password",
        },
    ],
    "sign_up": [
        {
            "name": "email",
            "label": "Email address",
            "type": "email",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        },
        {
            "name": "role",
            "label": "Role",
            "type": "select",
            "options": [
                {"value": RoleType.CREATOR, "label": "Creator"},
                {"value": RoleType.BRAND, "label": "Brand"},
            ],
        },
        {
            "name": "password",
            "label": "Password",
            "type": "password",
            "autocomplete": "new-password",
            "placeholder": "Create a password",
        },
        {
            "name": "confirm_password",
            "label": "Confirm password",
            "type": "password",
            "autocomplete": "new-password",
            "placeholder": "Repeat your password",
        },
    ],
    "forgot_password": [
        {
            "name": "email",
            "label": "Email address",
            "type": "email",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        }
    ],
}


class BaseInputMapper(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)


class SignInInput(BaseInputMapper):
    email: str = Field(min_length=3, max_length=254)
    password: str = Field(min_length=8, max_length=128)

    @field_validator("email")
    @classmethod
    def validate_email_address(cls, value: str) -> str:
        value = value.lower()
        try:
            validate_email(value)
        except DjangoValidationError as exc:
            raise ValueError("Enter a valid email address.") from exc
        return value


class SignUpInput(SignInInput):
    role: str = Field(default=RoleType.CREATOR)
    confirm_password: str = Field(min_length=8, max_length=128)

    @field_validator("role")
    @classmethod
    def validate_role(cls, value: str) -> str:
        if value not in RoleType.values:
            raise ValueError("Choose either Creator or Brand.")
        return value

    @model_validator(mode="after")
    def validate_passwords_match(self) -> "SignUpInput":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match.")
        return self


class ForgotPasswordInput(BaseInputMapper):
    email: str = Field(min_length=3, max_length=254)

    @field_validator("email")
    @classmethod
    def validate_email_address(cls, value: str) -> str:
        value = value.lower()
        try:
            validate_email(value)
        except DjangoValidationError as exc:
            raise ValueError("Enter a valid email address.") from exc
        return value


def form_values(payload: dict[str, Any] | None, form_name: str) -> dict[str, Any]:
    payload = payload or {}
    values: dict[str, Any] = {}
    for field in AUTH_FORM_FIELDS[form_name]:
        if field["type"] == "password":
            values[field["name"]] = ""
            continue
        values[field["name"]] = payload.get(field["name"], "")
    return values
