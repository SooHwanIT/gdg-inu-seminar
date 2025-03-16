# Nginx 공식 이미지를 베이스로 사용
FROM nginx:alpine

# 작업 디렉토리 설정
WORKDIR /usr/share/nginx/html

# 기존 기본 파일 삭제
RUN rm -rf ./*

# 로컬 html 파일들을 컨테이너의 웹 루트 디렉토리로 복사
COPY ./html/ .

# 포트 80 노출
EXPOSE 80

# Nginx 실행
CMD ["nginx", "-g", "daemon off;"]