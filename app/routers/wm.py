from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.models.wm import WmModel
# Создаем роутер
router = APIRouter(
    tags=["Washing Machine"]
)

# Маршрут для добавления новой стиральной машинки
@router.post("/")
async def create_washing_machine(name: str, location: str, description: str, db: AsyncSession = Depends(get_session)):
    new_machine = WmModel(
        name=name, 
        location=location, 
        description=description,
    )
    db.add(new_machine)
    await db.commit()
    await db.refresh(new_machine)
    return new_machine

# Маршрут для получения списка всех машинок
@router.get("/")
async def get_washing_machines(db: AsyncSession = Depends(get_session)):
    query = select(WmModel)
    result = await db.execute(query)
    return result.scalars().all()
