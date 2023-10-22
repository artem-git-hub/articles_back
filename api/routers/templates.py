import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List

from db.iteraction.template import add_template, select_all_templates
from api.serializers.template import Template

router = APIRouter(prefix='', tags=['template'])

database_data = [
    {
        'name': 'name1',
        'code': 'code1',
        'data': {
            'title': {
                'column': '3/7',
                'row': '2/5'
            },
            'subtitle': {
                'column': '2/5',
                'row': '2/5',
            }
        }
    },
    {
        'name': 'name2',
        'code': 'code2',
        'data': {
            'title': {
                'column': '3/7',
                'row': '2/5'
            },
            'subtitle': {
                'column': '2/5',
                'row': '2/5',
            }
        }
    },
]

@router.get("/api/templates/", response_model=List[Template])
async def get_templates():
    try:
        templates_data = []
        templates = select_all_templates()

        for template in templates:
            print(template.data)
            template_data = {
                "name": template.name,
                "code": template.code,
                "data": template.data
            }
            templates_data.append(template_data)

        return JSONResponse(content=templates_data)
    except Exception as e:
        return JSONResponse(content={"success": False, "error": e})

@router.post("/api/template/")
async def create_template(template_data: Template) -> JSONResponse:
    try:
        data_json = json.dumps(template_data.data)

        add_template(
            name=template_data.name,
            code=template_data.code,
            data=data_json)
        
        return JSONResponse(content={"success": True})
    except Exception as e:
        return JSONResponse(content={"success": False, "error": e})

