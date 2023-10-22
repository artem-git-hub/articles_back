from dataclasses import dataclass
from environs import Env
from sqlalchemy.orm import Session


@dataclass
class DbData:
    debug: bool
    session: Session = None

@dataclass
class Config:
    db: DbData

def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    config = Config(
        db=DbData(
            debug=env.bool("DB_DEBUG")
        ),
    )
    return config

config = load_config("./.env")