from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass