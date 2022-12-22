from fastapi import FastAPI, HTTPException
from app.doctor import Doctor


doctors: list[Doctor] = [
    Doctor(0, 'Голубев Роман Даниилович', 'Хирург'),
    Doctor(1, 'Михайлов Андрей Матвеевич', 'Лор'),
    Doctor(2, 'Зеленин Матвей Тимофеевич', 'Ортопед'),
    Doctor(3, 'Васильева Ева Тихоновна', 'Терапевт'),
    Doctor(4, 'Бабушкина Лиана Степановна', 'Онколог')
]

app = FastAPI()


@app.get("/v1/drs")
async def get_drs():
    return doctors

@app.get("/v1/drs/{id}")
async def get_drs_by_id(id: int):
    result = [item for item in doctors if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code = 404, detail="Документ не найден")