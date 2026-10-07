from pydantic import BaseModel, Field, EmailStr


class Candidate(BaseModel):
    name: str
    email: EmailStr
    experience: int = Field(ge=0)
    skills: list[str] = []
