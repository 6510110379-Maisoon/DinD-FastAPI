# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)

# root เดิม ไม่เปลี่ยน → test_root() ผ่าน
@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Jenkins & SonarQube!"}

@app.get("/average")
def get_average(numbers: List[float] = Query(...)):
    try:
        result = calculate_average(numbers)
        return {"average": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/reverse")
def get_reverse(text: str = Query(...)):
    result = reverse_string(text)
    return {"reversed": result}

# endpoint สำหรับ code smell
@app.get("/code_smell")
def code_smell():
    items = ["Hello", "from", "FastAPI", "with", "Jenkins", "&", "SonarQube!"]
    result = []
    for i in items:
        result.append(i.upper())
    for i in items:  # loop ซ้ำ → code smell
        result.append(i.lower())
    return {"message": " ".join(result)}
