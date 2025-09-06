from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    birth_date: str  # YYYY-MM-DD
    birth_time: str  # HH:MM (not used in zodiac logic yet)
    birth_place: str
    language: str = "en"  # or "hi"

class InsightResponse(BaseModel):
    zodiac: str
    insight: str
    language: str
