from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2)
    auther: str = Field(min_length=2)
    year: int = Field(ge=1900)


class BookResponse(BaseModel):
    id: int
    title: str
    auther: str
    year: int

    model_config = ConfigDict(from_attributes=True)