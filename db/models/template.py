from sqlalchemy import Column, Integer, String, JSON

from ..db import TimedModel

class TemplateModel(TimedModel):
    __tablename__ = 'templates'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    code = Column(String)
    data = Column(JSON)
