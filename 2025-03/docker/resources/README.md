# 도커(Docker) 명령어 치트시트

## 기본 명령어

### 이미지 관련

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `docker pull` | 이미지 다운로드 | `docker pull nginx:latest` |
| `docker images` | 이미지 목록 확인 | `docker images` |
| `docker rmi` | 이미지 삭제 | `docker rmi nginx:latest` |
| `docker build` | Dockerfile로 이미지 빌드 | `docker build -t myapp:1.0 .` |
| `docker tag` | 이미지에 태그 추가 | `docker tag myapp:1.0 username/myapp:1.0` |
| `docker push` | 이미지를 레지스트리에 업로드 | `docker push username/myapp:1.0` |

### 컨테이너 관련

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `docker run` | 컨테이너 생성 및 시작 | `docker run -d -p 8080:80 nginx` |
| `docker ps` | 실행 중인 컨테이너 목록 | `docker ps` |
| `docker ps -a` | 모든 컨테이너 목록 | `docker ps -a` |
| `docker stop` | 컨테이너 정지 | `docker stop my-container` |
| `docker start` | 정지된 컨테이너 시작 | `docker start my-container` |
| `docker restart` | 컨테이너 재시작 | `docker restart my-container` |
| `docker rm` | 컨테이너 삭제 | `docker rm my-container` |
| `docker logs` | 컨테이너 로그 확인 | `docker logs -f my-container` |
| `docker exec` | 실행 중인 컨테이너에서 명령 실행 | `docker exec -it my-container bash` |

## docker run 주요 옵션

| 옵션 | 설명 | 예시 |
|------|------|------|
| `-d, --detach` | 백그라운드 모드로 실행 | `docker run -d nginx` |
| `-p, --publish` | 포트 포워딩 (호스트:컨테이너) | `docker run -p 8080:80 nginx` |
| `-v, --volume` | 볼륨 마운트 (호스트:컨테이너) | `docker run -v /host/path:/container/path nginx` |
| `-e, --env` | 환경변수 설정 | `docker run -e MYSQL_ROOT_PASSWORD=password mysql` |
| `--name` | 컨테이너 이름 지정 | `docker run --name web nginx` |
| `--network` | 네트워크 연결 | `docker run --network my-network nginx` |
| `--rm` | 컨테이너 종료 시 자동 삭제 | `docker run --rm nginx` |
| `-it` | 대화형 터미널 연결 | `docker run -it ubuntu bash` |

## Dockerfile 주요 지시어

| 지시어 | 설명 | 예시 |
|--------|------|------|
| `FROM` | 베이스 이미지 지정 | `FROM python:3.9-slim` |
| `WORKDIR` | 작업 디렉토리 설정 | `WORKDIR /app` |
| `COPY` | 파일/디렉토리 복사 | `COPY . /app` |
| `ADD` | 파일/디렉토리/URL 복사 (tar 압축해제 기능) | `ADD app.tar.gz /app` |
| `RUN` | 명령 실행 (이미지 빌드 시) | `RUN pip install -r requirements.txt` |
| `ENV` | 환경변수 설정 | `ENV NODE_ENV=production` |
| `EXPOSE` | 컨테이너가 리스닝할 포트 지정 | `EXPOSE 8000` |
| `CMD` | 컨테이너 실행 시 기본 명령 | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | 컨테이너 실행 시 항상 실행되는 명령 | `ENTRYPOINT ["python"]` |

## Docker Compose 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `docker-compose up` | 서비스 생성 및 시작 | `docker-compose up -d` |
| `docker-compose down` | 서비스 중지 및 컨테이너 삭제 | `docker-compose down` |
| `docker-compose ps` | 서비스 상태 확인 | `docker-compose ps` |
| `docker-compose logs` | 서비스 로그 확인 | `docker-compose logs -f web` |
| `docker-compose exec` | 실행 중인 서비스 컨테이너에서 명령 실행 | `docker-compose exec web bash` |
| `docker-compose build` | 서비스 빌드 또는 재빌드 | `docker-compose build` |

## 자주 사용하는 패턴

### 개발 환경 설정
```bash
# 개발 환경 컨테이너 실행 (리소스 변경 자동 반영)
docker run -d -p 3000:3000 -v $(pwd):/app --name dev-env myapp:dev
```

### 데이터베이스 설정
```bash
# MySQL 실행 (데이터 영속성 유지)
docker run -d -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=rootpw \
  -e MYSQL_DATABASE=mydb \
  -v mysql-data:/var/lib/mysql \
  --name mysql mysql:8
```

## 문제 해결 명령어

| 명령어 | 설명 |
|--------|------|
| `docker logs <container>` | 컨테이너 로그 확인 |
| `docker inspect <container/image>` | 컨테이너/이미지 세부 정보 확인 |
| `docker stats` | 컨테이너 리소스 사용량 확인 |
| `docker system df` | 도커 디스크 사용량 확인 |
| `docker system prune` | 미사용 데이터 정리 |