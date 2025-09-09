# ใช้ Python แทน JDK เพราะ FastAPI ต้อง Python
FROM python:3.11-slim

WORKDIR /app

# คัดลอกไฟล์ requirements ก่อนเพื่อใช้ cache ของ Docker
COPY requirements.txt .

# ติดตั้ง dependencies
RUN python -m venv venv \
    && ./venv/bin/pip install --upgrade pip \
    && ./venv/bin/pip install -r requirements.txt

# คัดลอก source code
COPY . .

# ใช้ venv python เป็นค่า default
ENV PATH="/app/venv/bin:$PATH"

# เปิด port ของ FastAPI
EXPOSE 8000

# รัน uvicorn เป็น process หลัก
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
