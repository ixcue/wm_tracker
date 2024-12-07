from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncIterable
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Проверяем, что DATABASE_URL загружен корректно
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL не задан в .env файле")

engine = create_async_engine(
    url=DATABASE_URL,
)
sessionmaker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

async def get_session() -> AsyncIterable[AsyncSession]:
    async with sessionmaker() as session:
        yield session