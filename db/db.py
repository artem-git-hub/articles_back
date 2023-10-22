"""Основной файл взаимодействия с БД"""
import logging

import sqlite3
from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config


logger = logging.getLogger(__name__)

Base = declarative_base()

class TimedModel(Base):
    """Модель на основе которой будут строиться все остальные"""
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(
        DateTime(True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )

def request(func):
    """Декоратор для взаимодействия с БД"""
    def good_interaction(*args, **kwargs):
        try:
            # Начало явной транзакции
            config.db.session.begin()

            # Операции с базой данных
            result = func(session=config.db.session, *args, **kwargs)

            # Закрыть сессию
            config.db.session.close()


            return result

        except Exception as e:
            config.db.session.rollback()
            logger.error("Transaction error: %s".format(e))
            raise Exception from e
    return good_interaction



def on_startapp():
    """Функция запуска и подключения к базе данных"""
    try:
        engine = create_engine('sqlite:///db/database.sqlite', echo=True)

        Session = sessionmaker(bind=engine)

        config.db.session = Session()

        logger.info("Successful connection to SQLite")
    except sqlite3.OperationalError as e:
        logger.error("Failed to establish connection with SQLite.")
        logger.error(str(e))
        exit(1)


    if config.db.debug:
        Base.metadata.create_all(engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)



def on_shutdown():
    """Функция отключения от базы данных"""
    config.db.session.close()
