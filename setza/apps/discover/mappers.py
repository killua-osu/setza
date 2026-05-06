from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class DiscoverFilterInput(BaseModel):
    model_config = ConfigDict(extra="ignore", str_strip_whitespace=True)

    q: str = ""
    countries: str = ""
    platform: str = ""
    followers: str = ""
    format: str = ""
    engagement_rate: str = ""
    gender: str = ""

