import json
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from typing import List

from db.iteraction.template import add_template, select_all_templates, select_process_by_code
from api.serializers.template import Template

router = APIRouter(prefix='', tags=['template'])

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

@router.get("/api/template/{code}", response_model=Template)
async def get_template_by_code(code: str = Path(..., title="Code of the template")) -> Template:
    try:
        template = select_process_by_code(code)

        if not template:
            raise HTTPException(status_code=404, detail="Template not found")

        template_data = {
            "name": template.name,
            "code": template.code,
            "data": template.data
        }

        return JSONResponse(content=template_data)
    except Exception as e:
        return JSONResponse(content={"success": False, "error": str(e)})
    

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

