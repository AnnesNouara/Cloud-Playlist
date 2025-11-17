from pydantic import BaseModel, Field, ConfigDict

class TrackBase(BaseModel):
    song_name: str = Field(min_length=1, max_length=50),
    artist: str = Field(min_length=1, max_length=50),
    duration: str = Field(min_length=1, max_length=50)

class TrackCreate(TrackBase):
    pass

class TrackResponse(TrackBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
