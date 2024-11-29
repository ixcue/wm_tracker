from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.wm import WmModel

# Создаем роутер
router = APIRouter()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для добавления новой стиральной машинки
@router.post("/")
def create_washing_machine(name: str, db: Session = Depends(get_db)):
    new_machine = WmModel(name=name)
    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)
    return {"id": new_machine.id, "name": new_machine.name, "balance": new_machine.balance}

# Маршрут для получения списка всех машинок
@router.get("/")
def get_washing_machines(db: Session = Depends(get_db)):
    machines = db.query(WmModel).all()
    return machines