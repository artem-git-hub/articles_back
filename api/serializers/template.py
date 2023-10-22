from pydantic import BaseModel
from typing import Dict

class Template(BaseModel):
    name: str
    code: str
    data: dict
