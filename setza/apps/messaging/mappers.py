from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ThreadSelectionInput(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    thread: str = ""


class MessageReplyInput(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    body: str = Field(min_length=1, max_length=2000)

