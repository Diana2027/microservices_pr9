from fastapi import FastAPI, HTTPException
from app.medcard import Medcard


medcards: list[Medcard] = [
    Medcard(0, 'Медкарта №1', 'Дементьева Маргарита Ярославовна'),
    Medcard(1, 'Медкарта №2', 'Матвеев Савва Тимофеевич'),
    Medcard(2, 'Медкарта №3', 'Суркова Ева Артёмовна'),
    Medcard(3, 'Медкарта №4', 'Соколова Полина Давидовна'),
    Medcard(4, 'Медкарта №5', 'Селезнева Ника Ильинична'),
    Medcard(5, 'Медкарта №6', 'Авдеев Максим Максимович')
]

app = FastAPI()


@app.get("/v1/cards")
async def get_cards():
    return medcards

@app.get("/v1/cards/{id}")
async def get_cards_by_id(id: int):
    result = [item for item in medcards if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code = 404, detail="Документ не найден")