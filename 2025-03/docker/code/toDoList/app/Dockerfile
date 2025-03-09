FROM python:3.9-slim

WORKDIR /app

# 의존성 설치 레이어 분리
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트 노출
EXPOSE 5000

# 컨테이너 실행 명령
CMD ["python", "app.py"]
