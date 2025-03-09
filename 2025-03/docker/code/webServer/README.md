```bash
# 이미지 빌드
docker build -t my-websitee .

# 컨테이너 실행 (80번 포트 매핑)
docker run -d -p 8080:80 my-website
```