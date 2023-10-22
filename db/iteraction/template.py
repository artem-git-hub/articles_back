from typing import List
from sqlalchemy import asc
from sqlalchemy.orm import Session


from ..db import request
from ..models.template import TemplateModel


@request
def select_all_templates(session: Session = None) -> List[TemplateModel]:
    templates = session.query(TemplateModel).order_by(asc(TemplateModel.created_at)).all()
    return templates

@request
def add_template(name: str, code: str, data: dict, session: Session = None) -> bool:
    """Add new process"""
    new_template = TemplateModel(name=name, code=code, data=data)
    session.add(new_template)
    session.commit()


@request
def select_process_by_code(code: str, session: Session = None) -> TemplateModel:
    """Select process by name"""
    template = session.query(TemplateModel).where(TemplateModel.code == code).first()
    return template