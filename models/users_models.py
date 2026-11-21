from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class UserData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    userId: int = Field(ge=1)
    distanceUnits: Literal["km", "ml"]
    currency: Literal["eur", "gbp", "usd", "uah", "pln"]
    photoFilename: str


class CurrentUserResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    status: Literal["ok", "error"]
    data: UserData

