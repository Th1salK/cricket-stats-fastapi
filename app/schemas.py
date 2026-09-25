from pydantic import BaseModel, Field


# what client is allowed to send when creating a player
class PlayerCreate(BaseModel):
    name: str
    team: str
    matches: int = Field(default=0, ge=0)
    wickets: int = Field(default=0, ge=0)
    runs: int = Field(default=0, ge=0)


# what the API sends back to the client
class PlayerResponse(BaseModel):
    id: int
    name: str
    team: str
    matches: int
    wickets: int
    runs: int


model_config = {"from_attributes": True}
