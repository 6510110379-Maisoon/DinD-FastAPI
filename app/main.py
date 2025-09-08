# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Demo FastAPI app for Jenkins + Docker + SonarQube pipeline",
    version="1.0.0",
)

# Root endpoint เดิม (test_root() ผ่าน)
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

# Endpoint สำหรับ Code Smell
@app.get("/code_smell")
def code_smell():
    items = ["Hello", "from", "FastAPI", "with", "Jenkins", "&", "SonarQube!"]
    result = []
    # Loop ซ้ำ → duplicated code → Code Smell
    for i in items:
        result.append(i.upper())
    for i in items:
        result.append(i.lower())
    # ฟังก์ชันยาวขึ้นโดยไม่จำเป็น → Code Smell
    return {"message": " ".join(result)}
