# from typing import Optional

# from fastapi import APIRouter, Request, Cookie
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates


# router = APIRouter(prefix='', tags=['article'])

# templates = Jinja2Templates(directory="templates")


# @router.get('/article', response_class=HTMLResponse)
# def main_page(request: Request, session: Optional[str] = Cookie(default=None)):

#     if (session is None or session == "") or not check_valid_signed_data(data_from_cookie=session):
#         response = RedirectResponse(str(request.base_url) + "login")
#         response.delete_cookie(key="session", path="/admin")
#         return response 


#     processes = select_all_processes()

#     sys_processes = []
#     for process in processes:
#         sysprocess = SystemdProcess(process=process, without_logs=True)
#         sys_processes.append(sysprocess)

    
#     return templates.TemplateResponse("admin.html", {"request": request, "processes": sys_processes, })