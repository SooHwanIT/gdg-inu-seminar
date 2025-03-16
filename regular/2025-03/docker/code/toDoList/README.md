# Docker 및 Docker Compose 데모 애플리케이션

이 프로젝트는 Docker와 Docker Compose를 이용한 Flask + MySQL 애플리케이션 데모입니다.

## 프로젝트 구조

```
demo-app/
├── app/
│   ├── app.py              # Flask 애플리케이션 코드
│   ├── requirements.txt    # Python 패키지 의존성
│   └── Dockerfile          # Flask 앱 빌드를 위한 Dockerfile
├── docker-compose.yml      # 서비스 구성 정의 파일
└── README.md               # 프로젝트 설명 파일

```

## 기능

- Flask 웹 애플리케이션 (할 일 관리 앱)
- MySQL 데이터베이스 연동
- RESTful API 제공
- 도커 컨테이너를 이용한 애플리케이션 실행

## 실행 방법

### 1. Docker Compose로 실행하기

```bash
# 컨테이너 빌드 및 시작
docker-compose up -d

# 실행 중인 컨테이너 확인
docker-compose ps

# 컨테이너 로그 확인
docker-compose logs

# 컨테이너 중지 및 삭제
docker-compose down

```

### 2. 개별 Docker 명령어로 실행하기

```bash
# MySQL 컨테이너 실행
docker run -d --name mysql-db \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=flaskdb \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=password \
  -p 3306:3306 \
  mysql:8

# Flask 애플리케이션 빌드
docker build -t flask-app ./app

# Flask 애플리케이션 실행
docker run -d --name flask-app \
  -e DB_HOST=mysql-db \
  -e DB_USER=user \
  -e DB_PASSWORD=password \
  -e DB_NAME=flaskdb \
  -p 5000:5000 \
  --link mysql-db:mysql-db \
  flask-app

```

## API 엔드포인트

- `GET /api/tasks` - 모든 할 일 목록 조회
- `POST /api/tasks` - 새로운 할 일 추가
- `PUT /api/tasks/<id>` - 특정 할 일 수정
- `DELETE /api/tasks/<id>` - 특정 할 일 삭제
- `GET /health` - 서비스 헬스 체크

## 웹 인터페이스

애플리케이션이 실행된 후 브라우저에서 다음 URL에 접속하여 웹 인터페이스를 사용할 수 있습니다:
http://localhost:5000