# app/main.py

from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Jenkins & SonarQube!"}


@app.get("/average")
def get_average(numbers: List[float] = Query(..., description="List ของตัวเลข")):
    try:
        result = calculate_average(numbers)
        return {"average": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/reverse")
def get_reverse(text: str = Query(..., description="ข้อความที่ต้องการกลับ")):
    result = reverse_string(text)
    return {"reversed": result}


# 🔹 เพิ่ม code smell
@app.get("/smell")
def code_smell_example():
    unused_var = 123  # ไม่ได้ใช้ → code smell
    redundant = "This is redundant"
    print("This is unnecessary log")  # logging แบบไม่เหมาะสม
    repeated_code = redundant + redundant + redundant  # duplication
    return {"message": repeated_code}

# 🔹 function ซ้ำซ้อน (อีก code smell)
def duplicated_function(x):
    return x * 2

def duplicated_function_copy(x):
    return x * 2  # duplicated code
