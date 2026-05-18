# DAMI Lab 학회 포스터 구성 분석

> `ask_poster/references/` 에 있는 정승현 선행 포스터 4종 (산공2023·2024·2025, 자료분석2023) 의 공통 양식을 정리. 새 포스터 제작 시 본 문서를 참고.

원본 PDF:
- `산공2023포스터_정승현.pdf` (1.0m × 1.2m)
- `산공2024포스터_정승현.pdf` (1.0m × 1.2m)
- `산공2025포스터_정승현.pdf` (1.0m × 1.2m)
- `자료분석2023포스터_정승현.pdf` (1.0m × 1.42m)

---

## 1. 전체 구조 (Single page, portrait)

```
┌────────────────────────────────────────────────┐
│  ▎  HEADER (네이비)                              │ ← 약 10–15%
│  ▎  Korean Title (옵션: 노란 강조 키워드)        │
│  ▎  English Subtitle                           │
│  ▎  Authors¹  ²  ...  *(corresponding)         │
│  ▎  ¹동국대 컴퓨터·AI학과, ²..., emails         │
├────────────────────────────────────────────────┤
│  ┌────────────┐    ┌────────────┐              │
│  │ Section 1  │    │ Section 2  │              │ ← 본문
│  │ Introduction│    │ Method     │              │   2-column
│  └────────────┘    └────────────┘              │   grid
│  ┌────────────┐    ┌────────────┐              │
│  │ Section 3  │    │ Section 4  │              │
│  └────────────┘    └────────────┘              │
│                                                │
│  (대부분 2 col × 3–4 row 카드 = 6–8개 섹션)     │
├────────────────────────────────────────────────┤
│ Acknowledgements / 본 연구는 ... 지원으로 수행됨 │ ← 약 3–5%
└────────────────────────────────────────────────┘
```

가로:세로 비율은 대체로 **1 : 1.2~1.4**. 그 이상으로 길어지면 (예: 1×2.1m) 카드 개수를 늘리거나 글씨를 크게 키워야 함.

---

## 2. 헤더 (Navy band)

- 배경: **navy `#0b2c5a` ~ `#05264e`** 단색 (그라데이션 X — PDF 렌더 안정성)
- 좌측 끝에 **세로 강조 바** (옅은 푸른색 → 네이비 그라데이션, 폭 5–8mm)
- 제목 (h1): 흰색, 굵음 weight 800, **자간 살짝 조여서** 가독성 ↑
  - **노란 강조** (`#ffd84d` 같은 골드) 는 키워드 한두 개에만. **남용 금지** (포스터 별로 들쭉날쭉 — 강조 없는 버전도 많음)
- 영문 부제 (subtitle): 한 줄 아래, 톤다운 cyan/light-blue
- 저자 라인:
  - 이름 사이 콤마 + 위첨자 소속 번호 (`이름¹`, `이름²`)
  - corresponding 은 `*` 또는 별색 강조
- 소속 라인: `¹동국대학교 컴퓨터·AI학과, ²..., ³...` 형식. 그 다음 줄에 이메일 `{id1, id2, id3}@dgu.ac.kr` 형태.

`산공2025` 처럼 헤더에 노란 강조를 쓴 예와, `산공2024` 처럼 안 쓴 예가 둘 다 있음. 본문 강조와의 시각 충돌이 적은 쪽은 **강조 없는** 흰색 단일 톤.

---

## 3. 본문 — Section 카드 패턴

각 카드 = **네이비 헤더 바 (가운데 흰 글씨 제목)** + **흰 배경 본문 박스**.

- 카드 경계는 얇은 네이비 테두리 (0.8–1.2mm)
- 헤더 바: padding 5–8mm, font 11–14mm, 가운데 정렬
- 본문 박스 padding: 8–14mm
- 불릿: 첫 단계 `■`(채움 사각), 둘째 단계 `•`, 셋째 단계 `–`, 넷째 단계 `»`
- 본문 텍스트: 일반 한글 6–8mm, 굵은 강조는 네이비
- 하이라이트 callout: 노란 배경 (`#fff8e1`) + 주황 좌측 보더 (`#ffb300`) — "본 연구의 기여" 같은 박스에 사용

### 자주 등장하는 섹션 명
- `Introduction` — 동기 / 기존 연구의 한계 / 본 연구 내용
- `Method` / `Proposed Method` / `Our Method Pipeline`
- `Data Preprocess` / `Dataset` / `Human Pose Estimation`
- `Generating Joint Information` / `Architecture`
- `Experiments & Results` (테이블 위주)
- `Conclusion` — 종종 생략 (Results 안에 흡수)

### 표 (Table) 양식
- 테이블 헤더 행: 네이비 배경 + 흰 글씨
- 본문 행: 흰색 / 옅은 푸른 (`#f3f6fb`) 줄무늬
- **하이라이트 셀**: 노란 (`#fff3b8`) 배경 + 주황 텍스트 — 본인 모델 결과 강조
- 캡션 (`표 N. ...`) 은 표 아래 작은 italic 회색

### 그림 (Figure) 양식
- 컬럼 폭에 맞춰 100% width
- 캡션 (`그림 N. ...`) 은 그림 아래 작은 italic 회색
- 다이어그램은 라벨이 잘리지 않도록 끝 글자 한글로 마감 (Mermaid 렌더 시)

---

## 4. 푸터 (Acknowledgement)

- 모든 포스터 마지막에 `이 연구는 (주)김캐디의 지원을 받아 수행된 연구임` 같은 한 줄 감사문
- 참고문헌은 본문 슬라이드 내 `<div class="refs">` 로 카드 하단에 작은 글씨로 (각 카드별 개별 인용 [n])
- 별도 References 페이지는 사용 안 함

> **이 포스터(1×2.1m) 변경 사항**: 사용자 요청으로 푸터는 본문 마지막 카드(감사의 글)에 흡수, 참고문헌은 제거, 푸터 자리에 **동국대 + DAMI Lab 로고 띠**를 배치.

---

## 5. 컬러 토큰

| 토큰 | 값 | 용도 |
|---|---|---|
| navy | `#0b2c5a` / `#05264e` | 헤더 배경, 섹션 헤더 바, h1 border |
| accent-blue | `#4ea2ff` / `#1d4ed8` | 좌측 그라데이션 강조 바 |
| gold | `#ffd84d` / `#d97706` | 제목 키워드 강조 (선택) |
| highlight-bg | `#fff8e1` | "본 연구의 기여" 등 callout 배경 |
| highlight-border | `#ffb300` | callout 좌측 보더 |
| table-highlight | `#fff3b8` / `#b45c00` | 표 내 본인 결과 강조 셀 |
| table-stripe | `#f3f6fb` | 표 짝수행 배경 |
| body-text | `#1a1a1a` / `#1f2937` | 본문 텍스트 |

---

## 6. 폰트

- 한글: **Pretendard** (없으면 Noto Sans KR)
- 라틴: Pretendard / system sans
- 수식: KaTeX 인라인 `$...$` 또는 디스플레이 `$$...$$`

크기는 포스터 크기에 비례:
- 1.0m × 1.2m: 본문 ~7mm, 섹션 헤더 ~11mm, 제목 ~18mm
- 1.0m × 1.42m: 본문 ~7–8mm, 섹션 헤더 ~12mm, 제목 ~20mm
- 1.0m × 2.1m: 본문 ~9–11mm, 섹션 헤더 ~15mm, 제목 ~26mm (8개 카드로 채우기)

---

## 7. 카드 개수 가이드

| 포스터 크기 | 가용 본문 높이 | 권장 카드 수 (2 col) |
|---|---|---|
| 1 × 1.0m | ~750mm | 4–6 카드 (2 col × 2–3 row) |
| 1 × 1.2m | ~960mm | 6–8 카드 (2 col × 3–4 row) |
| 1 × 1.42m | ~1180mm | 8–10 카드 (2 col × 4–5 row) |
| 1 × 2.1m | ~1850mm | **10–14 카드** + 본문 글씨 확대 |

2.1m 같은 비통상적 높이는 카드 수만 늘리지 말고 **각 카드의 콘텐츠 밀도도 동시에 키워야** 빈 공간이 안 남음. 단순 분할만 하면 가독성도 떨어지고 시각적 균형도 흐트러짐.

---

## 8. 실패한 패턴 (피해야 할 것)

- **flex layout 의 vertical center 가 leak** — marp 기본 테마가 section 에 `place-content: center` 를 걸고 있어, 단순 `display: block` 으론 안 풀림. `display: flex !important + flex-direction: column !important + justify-content: flex-start !important` 로 명시 강제 필요.
- **`size: <width> <height>` 프론트매터** — 마르프 cli 는 임의 사이즈를 직접 받지 않음. 테마 CSS 에 `@size <name> <w> <h>` 선언하고 `theme: <theme-name>` + `size: <name>` 로 호출해야 함.
- **section 에 `linear-gradient`** — PDF 렌더러마다 hard stop 차이로 출력 불안정. 단색 + `border-left` 로 대체.
- **본문에 따옴표 (`"..."`, `'...'`)** — CommonMark emphasis flanking 충돌로 `**` 가 그대로 렌더됨. 따옴표 빼고 굵게만, 또는 한글 인용부호 `「…」` 사용.
- **build.py 만 사용** — build.py 는 dami-lab 테마만 등록함. 포스터처럼 별도 사이즈 테마가 필요한 경우 `--keep-built` 로 치환만 하고 `marp` 를 직접 호출 (Chrome 경로 환경변수 `CHROME_PATH`, timeout 120s+ 권장).
