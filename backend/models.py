from pydantic import BaseModel

class GeneratePopcornRequest(BaseModel):
    name: str
    mood: str
