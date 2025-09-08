# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)

# ฟังก์ชัน root ทำงานยาวขึ้นโดยไม่จำเป็น (Code Smell)
@app.get("/")
def root():
    messages = ["Hello", "from", "FastAPI", "with", "Jenkins", "&", "SonarQube!"]
    result = []
    for m in messages:  # loop ซ้ำ
        result.append(m.upper())
    for m in messages:  # loop ซ้ำอีกครั้ง (duplicated code)
        result.append(m.lower())
    return {"message": " ".join(result)}


# ฟังก์ชัน get_average เพิ่ม logic ซ้ำ
@app.get("/average")
def get_average(numbers):  # ลบ type hints → code smell
    if not numbers:
        raise HTTPException(status_code=400, detail="No numbers provided")
    
    # logic ซ้ำ
    try:
        avg1 = calculate_average(numbers)
        avg2 = calculate_average(numbers)
        return {"average": avg1 + avg2}  # ทำซ้ำ + ผลรวมที่ไม่จำเป็น
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ฟังก์ชัน get_reverse เพิ่ม code smell
@app.get("/reverse")
def get_reverse(text):
    # ซ้ำ logic
    reversed_text1 = reverse_string(text)
    reversed_text2 = reverse_string(text)
    return {"reversed": reversed_text1 + reversed_text2}  # concatenate ซ้ำ
