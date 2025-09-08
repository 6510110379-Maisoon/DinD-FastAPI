# Dockerfile

FROM eclipse-temurin:17-jdk

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# สร้าง virtual environment
RUN python3 -m venv venv

# คัดลอกไฟล์ requirements
COPY requirements.txt .

# ติดตั้ง dependencies ใน venv
RUN ./venv/bin/pip install --upgrade pip \
    && ./venv/bin/pip install -r requirements.txt

# คัดลอก source code
COPY . .

# ใช้ venv python เป็นค่า default
ENV PATH="/app/venv/bin:$PATH"

# เปิด port ของ FastAPI
EXPOSE 8090

# สั่งให้รัน uvicorn เป็น process หลักของ container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8090"]
