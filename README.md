# GDG 인천대학교 세미나 및 발표 자료

<div align="center">
  <img src="https://github.com/user-attachments/assets/86f5c469-40b7-4f49-b87b-657c2853439d" alt="GDG Logo" width="100">
  <h3>Google Developer Group 인천대학교</h3>
</div>

## 소개

이 레포지토리는 GDG 인천대학교에서 진행된 세미나, 발표, 내부 컨퍼런스 등의 자료를 보관하고 공유하기 위한 곳입니다. 우리 커뮤니티에서 공유된 지식과 경험을 누구나 접근할 수 있도록 정리했습니다.

## 세미나 종류

GDG 인천대학교에서는 다음과 같은 두 가지 유형의 세미나를 진행합니다:

1. **정기 세미나**: 코어 멤버 주도의 한 시간 ~ 한 시간 반 정도의 심층적인 발표
2. **월간 세미나**: 백엔드, AI 파트 일반 멤버들이 참가하는 10분 ~ 15분 정도의 간결한 발표

## 세미나 및 발표 자료 목록

### 정기 세미나

| 날짜 | 제목 | 발표자 | 자료 링크 |
|------|------|--------|-----------|
| 2025.03.12 | Docker 입문: 컨테이너 기술과 활용 방법 | 장철희 | [링크](/regular/2025-03/docker/) |
| 2025.04.9 | Web-And-React | 최수환 | [링크](/regular/2025-04/Web-And-React/) |
| 예정됨 | 세미나/발표 제목 | [발표자 이름] | [링크](/regular/경로/) |

### 월간 세미나: 백엔드

| 날짜 | 제목 | 발표자 | 자료 링크 |
|------|------|--------|-----------|
| 2025.03.26 | Large-Scale System Design | 김기수 | [링크](/monthly/backend/2025-03/Large-Scale-System-Design) |
| 2025.03.26 | Database Transaction | 홍은진 | [링크](/monthly/backend/2025-03/Database_transation) |
| 2025.03.26 | 3-tier architecture | 천평근 | [링크](/monthly/backend/2025-03/3-tier-architecture) |
| 2025.03.26 | TCP/IP | 전유진 | [링크](/monthly/backend/2025-03/TCP_IP) |
| 2025.03.26 | 단위 테스트 | 이제용 | [링크](/monthly/backend/2025-03/unitTest) |
| 예정됨 | 세미나/발표 제목 | [발표자 이름] | [링크](/monthly/backend/경로/) |

### 월간 세미나: AI

| 날짜 | 제목 | 발표자 | 자료 링크 |
|------|------|--------|-----------|
| 2025.03.19 | DeepSeek-R1 | 정환길 | [링크](monthly/ai/2025-03/DeepSeek-R1) |
| 2025.03.19 | A-LLMRec | 지원근 | [링크](monthly/ai/2025-03/A-LLMRec) |
| 2025.03.19 | POMO     | 박희선 | [링크](monthly/ai/2025-03/POMO) |
| 2025.03.19 | YOLO_v10 | 옥정빈 | [링크](monthly/ai/2025-03/YOLO_v10) |
| 2025.04.02 |  Chain-of-Thought(CoT) | Team 정환길 | [링크](monthly/ai/2025-04/CoT) |
| 2025.04.02 |  RecommenderSystems | Team 지원근 | [링크](monthly/ai/2025-04/RecommenderSystems) |
| 2025.04.02 |  Transformer | Team 박희선 | [링크](monthly/ai/2025-04/Transformer) |
| 2025.04.02 |  FixMatch | 홍승혁 | [링크](monthly/ai/2025-04/FixMatch) |
| 예정됨 | 세미나/발표 제목 | [발표자 이름] | [링크](/monthly/ai/경로/) |

## 디렉토리 구조

레포지토리는 다음과 같은 구조로 정리되어 있습니다:

```
/
├── regular/                # 정기 세미나 자료
│   ├── YYYY-MM/            # 연도-월 형식의 디렉토리
│   │   ├── topic-name/     # 세미나/발표 주제명
│   │   │   ├── README.md   # 세미나/발표 요약 정보
│   │   │   ├── slides/     # 발표 슬라이드 자료
│   │   │   ├── code/       # 예제 코드
│   │   │   ├── resources/  # 추가 자료
│   │   │   └── workshop/   # 워크샵 자료 (있을 경우)
│   │   │
│   │   └── another-topic/  # 같은 달에 진행된 다른 세미나/발표
│
├── monthly/                # 월간 세미나 자료
│   ├── backend/            # 백엔드 파트 세미나
│   │   ├── YYYY-MM/        # 연도-월 형식의 디렉토리
│   │   │   ├── topic-name/ # 세미나/발표 주제명
│   │   │   │   ├── README.md     # 세미나/발표 요약 정보
│   │   │   │   ├── slides.pdf    # 발표 슬라이드 자료
│   │   │   │   └── resources/    # 추가 자료 (필요 시)
│   │   │   │
│   │   │   └── another-topic/    # 같은 달에 진행된 다른 세미나/발표
│   │
│   ├── ai/                 # AI 파트 세미나
│   │   ├── YYYY-MM/        # 연도-월 형식의 디렉토리
│   │   │   ├── topic-name/ # 세미나/발표 주제명
│   │   │   │   ├── README.md     # 세미나/발표 요약 정보
│   │   │   │   ├── slides.pdf    # 발표 슬라이드 자료
│   │   │   │   └── resources/    # 추가 자료 (필요 시)
│   │   │   │
│   │   │   └── another-topic/    # 같은 달에 진행된 다른 세미나/발표
│
├── templates/              # 발표자를 위한 템플릿
│   └── README.md           # 세미나 README 템플릿
│
└── resources/              # 공통 리소스
    ├── images/             # 이미지 파일
    └── documents/          # 공통 문서
```

## 자료 기여 방법

GDG 인천대학교에서 세미나나 발표를 진행하신 후 자료를 공유하고 싶으시다면 다음 절차를 따라주세요:

1. 이 레포지토리를 포크(Fork)합니다.
2. 세미나 유형에 맞는 적절한 폴더 구조에 자료를 추가합니다:
   - 정기 세미나: `/regular/YYYY-MM/topic-name/`
   - 월간 백엔드 세미나: `/monthly/backend/YYYY-MM/topic-name/`
   - 월간 AI 세미나: `/monthly/ai/YYYY-MM/topic-name/`
3. README.md 파일을 작성하여 세미나/발표에 대한 요약 정보를 제공합니다.
4. Pull Request를 생성하여 메인 레포지토리에 반영을 요청합니다.

### README.md 작성 가이드

각 세미나/발표 디렉토리의 README.md는 다음 정보를 포함해야 합니다:

- 세미나/발표 제목
- 발표자 정보
- 날짜 및 장소
- 세미나/발표 요약
- 주요 주제
- 사전 요구사항 (필요한 경우)
- 참고 자료 및 링크

templates/README.md를 참고하여 작성해주세요.


## 커뮤니티 가이드라인

- 모든 자료는 명확한 라이선스 정보를 포함해야 합니다.
- 민감한 정보나 개인 정보가 포함되지 않도록 주의해주세요.
- 코드 예제는 가능한 한 실행 가능한 상태로 제공해주세요.
- 질문이나 이슈가 있을 경우 GitHub Issues를 통해 문의해주세요.

---

<div align="center">
  <p>© GDG 인천대학교
</div>
