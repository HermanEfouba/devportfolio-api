from pydantic import BaseModel
from typing import List

class Profile(BaseModel):
    id: int
    name: str
    bio: str
    skills: List[str]
    projects: List[str]
