# Docker 입문: 컨테이너 기술과 활용 방법

## 세미나 정보

- **제목**: Docker 입문: 컨테이너 기술과 활용 방법
- **일시**: 2025년 3월 12일
- **발표자**: 장철ㅣ
- **장소**: 인천대학교
- **소요 시간**: 약 1시간

## 세미나 개요

이 세미나는 백엔드 개발자들을 위한 Docker 입문 과정으로, 컨테이너 기술의 기본 개념부터 Dockerfile 작성, Docker Compose를 활용한 다중 컨테이너 애플리케이션 구성까지 다룹니다. 특히 실습을 통해 Docker의 핵심 개념을 이해하고 실무에 바로 적용할 수 있는 지식을 습득하는 것을 목표로 합니다.

## 주요 내용

1. **도커 소개 (10분)**
   - 컨테이너 vs 가상머신 비교
   - 도커의 기본 구조
   - 도커의 핵심 구성요소
   - 실무에서의 도커 활용 사례

2. **도커 기본 명령어 (10분)**
   - 이미지 관련 명령어: pull, images, rmi
   - 컨테이너 관련 명령어: run, ps, stop, rm
   - 자주 사용하는 옵션: 포트 포워딩, 볼륨 마운트

3. **Dockerfile 작성법 (15분)**
   - Dockerfile 기본 구조
   - 주요 지시어: FROM, WORKDIR, COPY, RUN, ENV, EXPOSE, CMD
   - 효율적인 레이어 구성과 최적화 팁

4. **웹 애플리케이션 컨테이너화 실습 (20분)**
   - Flask 애플리케이션 예제
   - Dockerfile 작성 및 이미지 빌드
   - Docker Compose를 활용한 Flask + MySQL 구성
   - 실행 및 테스트

5. **실무 팁 및 Q&A (5분)**
   - 이미지 최적화 전략
   - 보안 관련 고려사항
   - 백엔드 개발자를 위한 도커 활용 팁

## 사전 준비사항

세미나에 참여하시는 분들은 아래 사항을 미리 준비해주시면 실습을 원활하게 진행할 수 있습니다:

1. **Docker 설치**
   - Windows: [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/install/)
   - Mac: [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
   - Linux: [Docker Engine](https://docs.docker.com/engine/install/)

2. **Git 설치** (실습 코드 클론을 위해 필요)
   - [Git 다운로드](https://git-scm.com/downloads)

3. **실습 코드 클론**
   ```bash
   git clone https://github.com/GDG-INU/gdg-inu-seminar.git
   cd gdg-inu-seminar/2025-03/docker/
   ```

## 세미나 자료

- [발표 슬라이드](./slides/)
- [도커 명령어 치트시트](./resources/)
- [실습 예제 코드](./code/)

## 참고 자료

- [Docker 공식 문서](https://docs.docker.com/)
- [Docker Compose 문서](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)


## 문의

세미나와 관련된 질문이나 피드백은 GitHub 이슈를 통해 남겨주시거나, 아래 연락처로 문의 바랍니다:

- 이메일: ironhee8005@gmail.com