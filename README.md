# 원티드랩 파이썬 개발자 채용 과제

작업자: 박경린

이메일: kyunglin.park@kakao.com

### 주요 라이브러리

- fastapi
- sqlalchemy
- alembic

---

### 프로젝트 디렉토리 구조

```plaintext
wantedlab-backend-assignment/
├── alembic/
│   └── env.py                    # alembic 마이그레이션 설정
├── app/
│   ├── main.py                   # FastAPI 애플리케이션의 진입점
│   ├── core/
│   │   └── config.py             # 앱의 설정 및 환경 변수 로드
│   ├── db/
│   │   ├── base_class.py         # MySQL Table 매핑용 슈퍼 클래스 정의
│   │   ├── session.py            # 데이터베이스 세션 및 엔진 설정
│   │   ├── models/
│   │   │   └── company.py        # Company 모델 정의
│   │   ├── schemas/
│   │   │   ├── common.py         # 기본 Pydantic 스키마 정의 (다국어)
│   │   │   └── company.py        # Company 모델 관련 Pydantic 스키마 정의
│   │   └── crud/
│   │       └── company.py        # Company 모델 관련 CRUD 함수 정의
│   └── api/
│       ├── deps.py               # 종속성 주입 함수 정의
│       ├── main_router.py        # 프로젝트 메인 라우팅 설정
│       └── endpoint/
│           ├── companies.py      # /companies 하위 엔드포인트 정의
│           └── search.py         # 검색 관련 엔드포인트 정의
│
├── .env                          # 환경 변수 파일
├── .env.docker                   # Docker 실행용 환경 변수 파일
├── Dockerfile                    # Docker 이미지 빌드를 위한 설정 파일
├── docker-compose.yml            # Docker Compose 설정 파일
├── requirements.txt              # Python 패키지 종속성 목록
└── README.md                     # 프로젝트 설명 파일
```
