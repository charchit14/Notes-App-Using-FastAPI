# Pydantic is a Python library used for data validation and parsing.
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    desc: str
    important: bool = None