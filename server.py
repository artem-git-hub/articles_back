import atexit
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from api.routers.templates import router as template_router
from db.db import on_shutdown, on_startapp

app  = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    startapp()
    atexit.register(shutdown)


def startapp():

    #included diferent routers from modules
    app.include_router(template_router)
    #startapp sqlite
    on_startapp()
    print("\n\n----------------\n\nstart application\n\n----------------\n\n")


def shutdown():
    #shutdown sqlite
    on_shutdown()
    print("\n\n----------------\n\nstop application\n\n----------------\n\n")

main()
