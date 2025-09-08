FROM eclipse-temurin:17-jdk

# ติดตั้ง Python, venv และ Docker CLI
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip docker.io && \
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
