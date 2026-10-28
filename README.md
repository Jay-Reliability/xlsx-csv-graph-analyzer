# 📊 엑셀/CSV 데이터 Graph Analyzer V1.0

기존 Windows PyQt5 기반 데스크톱 프로그램(`01_General_CSV_Analyzer_1.py`)의 기능과 UI/UX Tone & Manner를 그대로 유지하여 웹 브라우저 및 **Streamlit Cloud** 환경에서 동일하게 동작하도록 마이그레이션한 웹 애플리케이션입니다.

---

## ✨ 주요 기능

1. **엑셀(`.xlsx`) 및 CSV(`.csv`) 파일 로딩**
   - UTF-8, UTF-8-SIG, CP949, EUC-KR 등 한글 인코딩 자동 감지
   - 값이 모두 동일하거나 비어 있는 무의미한 상수 채널 자동 필터링 및 유효 채널 추출
   - 다양한 한국어/영문 시계열 포맷(`2026-08-24 오후 2:49:39`, `YYYY-MM-DD HH:MM:SS.fff`, `HH:MM:SS` 등) 자동 파싱
2. **다중 채널 선택 및 인터랙티브 그래프 출력**
   - **x축 데이터 선택**: `Time` 또는 수치형 채널 단일 선택
   - **y축 데이터 선택 (다중 선택 가능)**: 마우스 클릭, `Ctrl+클릭`, `Shift+클릭`, 더블 클릭, `⬇ 데이터 선택`, `✅ 유효 CH 전체 선택`, `❌ 제거` 지원
   - 마우스 호버 시 가장 가까운 데이터 포인트의 채널명 및 `x`, `y` 좌표 툴팁 표시
   - 툴바를 통한 초기화(`🏠 초기화`), 드래그 영역 확대(`🔍 영역 확대`), 화면 이동(`✋ 이동`) 지원
3. **그래프 확대 범위 설정 및 파일 저장**
   - **x축 최소값 / 최대값**: 부분 시간 포맷(예: `08-24 14:55` ~ `08-24 15:00`) 및 전체 시간/수치 범위 필터링 지원
   - **y축 최소값 / 최대값**: 원하는 Y축 스케일(예: `10` ~ `100`) 고정 출력 지원
   - **💾 CSV 파일 저장**: 현재 선택 및 필터링된 구간의 데이터를 UTF-8 BOM(`.csv`) 파일로 다운로드
   - **🖼 그래프(jpg) 저장**: 현재 출력된 그래프를 고해상도(200 DPI급) `.jpg` 이미지로 다운로드
4. **구간 통계 데이터 분석 출력**
   - 파일 요약 정보(`[File Information]`) 및 선택된 구간의 채널별 상세 통계(`[Data Analysis]`) 실시간 산출
   - 산출 항목: `Column`, `Count`, `Mean`, `Max`, `Max Time`, `Min`, `Min Time`, `Std (ddof=1)`, `RMS`, `Range`, `Peak-Peak`

---

## 📁 저장소 파일 구성

| 파일명 | 설명 |
| :--- | :--- |
| `General_Graph_Analyzer.html` | 브라우저에서 단독 실행 가능한 통합 HTML/CSS/JS 그래프 분석기 |
| `app.py` | Streamlit Cloud 배포용 메인 엔트리포인트 (`General_Graph_Analyzer.html` 렌더링) |
| `requirements.txt` | Streamlit 실행을 위한 파이썬 패키지 의존성 목록 |
| `README.md` | 프로젝트 소개 및 GitHub + Streamlit 배포 가이드 |

---

## 🚀 사용 방법 (권장 워크플로우 예시)

1. 좌측 상단의 **`📂 csv/xlsx 파일 로딩`** 버튼을 클릭하여 분석할 파일(예: `0824_TC03_02_01.csv`)을 선택합니다.
2. **`x축 데이터 선택`**에서 `Time`을 선택합니다.
3. **`y축 데이터 선택 - 다중 선택 가능`**에서 분석할 항목(예: `온수온도`, `Comp Freq`)을 선택한 후 **`⬇ 데이터 선택`** 버튼을 클릭합니다.
4. **`📈 그래프 출력`** 버튼을 클릭하면 우측 상단 패널에 다중 채널 그래프가 출력되고, 우측 하단 패널에 통계 분석 결과가 출력됩니다.
5. **`그래프 확대 범위 및 저장`** 패널에서 원하는 범위(예: x축 최소값 `08-24 14:55`, x축 최대값 `08-24 15:00`, y축 최소값 `10`, y축 최대값 `100`)를 입력하고 **`x축 선택`** 또는 **`y축 선택`** 버튼을 누르면 확대된 그래프와 해당 구간의 통계 분석 결과가 즉시 갱신됩니다.

---

## 🌐 GitHub 및 Streamlit Cloud 게시 방법

1. **GitHub 저장소 업로드**
   - 새로운 GitHub Repository를 생성한 후 아래 4개 파일을 루트 경로에 업로드(Push)합니다.
     - `General_Graph_Analyzer.html`
     - `app.py`
     - `requirements.txt`
     - `README.md`
2. **Streamlit Community Cloud 연동**
   - [Streamlit Community Cloud](https://share.streamlit.io/)에 접속하여 로그인합니다.
   - **`Create app`** 버튼을 클릭합니다.
   - 업로드한 **GitHub Repository**, **Branch**(`main`), **Main file path**(`app.py`)를 차례로 선택합니다.
   - **`Deploy!`** 버튼을 클릭하면 웹 앱 배포가 완료됩니다.

---

## 💻 로컬 PC에서 실행하기

- **방법 1 (브라우저 직접 실행)**: `General_Graph_Analyzer.html` 파일을 크롬(Chrome), 엣지(Edge) 등 웹 브라우저에서 바로 더블클릭하여 실행합니다.
- **방법 2 (Streamlit 로컬 서버 실행)**:
  ```bash
  pip install -r requirements.txt
  streamlit run app.py
  ```
