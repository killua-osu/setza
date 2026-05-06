from __future__ import annotations

from pydantic import ValidationError


def pydantic_errors(exc: ValidationError) -> tuple[dict[str, list[str]], list[str]]:
    field_errors: dict[str, list[str]] = {}
    non_field_errors: list[str] = []
    for error in exc.errors():
        location = error.get("loc", ())
        target = location[0] if location else "__all__"
        message = error.get("msg", "Invalid value.")
        if target in {"__all__", "__root__"}:
            non_field_errors.append(message)
            continue
        field_errors.setdefault(str(target), []).append(message)
    return field_errors, non_field_errors
