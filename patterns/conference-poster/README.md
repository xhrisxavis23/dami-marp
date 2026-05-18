# Marp 학회 포스터 (Conference Poster) 패턴

> 한 장짜리 학회 발표 포스터 — A0 (841×1189mm ISO 216) 또는 1m×2.1m 같은 비표준 사이즈. DAMI Lab 슬라이드 양식을 포스터 스케일로 재해석.
>
> **기본 marp 스킬(slide theme 1280×720)로는 안 됨** — 별도 CSS 테마 + 포스터 전용 컴포넌트 + 2단계 빌드가 필요. 이 문서가 그 시드.

**설계 근거**: [references-analysis.md](references-analysis.md) — DAMI Lab 선행 포스터 4종 (산공 2023/24/25, 자료분석 2023) 의 공통 양식 분석. 헤더 띠·카드 격자·컬러 토큰·폰트 위계가 어디서 온 건지 추적할 때 참고.

---

## 언제 쓰나
- 학회 한 장짜리 (single-page) 포스터 — 산공/자료분석/KIPS 같은 국내 학회
- 사이즈 A0, B0, 1×1.2m, 1×2.1m 등 m 단위 큰 인쇄물
- DAMI Lab 시각 정체성 (네이비 헤더 + 카드 격자 + 동국대/DAMI 로고 띠) 유지

## 언제 안 쓰나
- 16:9 슬라이드 덱 (`theme: dami-lab` 그대로 쓸 것)
- 외부 기관 .pptx 템플릿 (python-pptx 스킬 쓸 것)

---

## 핵심 차이 (slide vs poster)

| | Slide deck | Poster |
|---|---|---|
| 사이즈 | 1280×720 (16:9 고정) | `@size poster <w> <h>` 커스텀 |
| 테마 | `theme: dami-lab` (built-in) | `theme: dami-poster` (이 패턴의 `poster-theme.css`) |
| 빌드 | `build.py` 한 번 | **2단계** — `build.py --keep-built` + 직접 `marp --theme-set` |
| 폰트 단위 | px (~22px 본문) | **mm** (5~15mm 본문, 사이즈에 비례) |
| 레이아웃 | h1 + h2 + bullets | 2단 카드 격자 (.poster-col × .sec) |
| 로고 | 우상단 워터마크 | 하단 풀폭 띠 (.poster-logos) |

---

## 워크플로우

1. **새 프로젝트 폴더**
   ```bash
   mkdir -p ppt_generation/projects/<YYYY-MM-DD-이름>-poster/{assets,pages}
   ```
2. **이 패턴의 CSS 와 로고 복사**
   ```bash
   cp .claude/skills/marp/patterns/conference-poster/poster-theme.css <proj>/
   cp .claude/skills/marp/assets/dami_logo_full.png <proj>/assets/
   # 동국대 로고는 별도 (assets 폴더 또는 기존 포스터 프로젝트에서 복사)
   ```
3. **마크다운 작성** — 아래 "구조 템플릿" 복붙
4. **인용 치환 (refs.toml 있다면)**
   ```bash
   python3 .claude/skills/marp/bin/build.py poster.md --keep-built
   ```
   `--keep-built` 가 **필수** — build.py 는 dami-lab.css 강제 주입해 잘못된 PDF 생성하지만 `.built.md` 가 남아 다음 단계에 쓸 수 있음
5. **포스터 테마로 직접 marp 호출**
   ```bash
   CHROME_PATH=$HOME/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome \
   PUPPETEER_TIMEOUT=300000 \
   marp poster.built.md --pdf \
     --theme-set poster-theme.css \
     --allow-local-files \
     -o poster.pdf
   ```
6. **미리보기**
   ```bash
   pdftoppm -r 30 poster.pdf pages/preview -png -f 1 -l 1
   # Read /pages/preview-1.png 로 시각 검증
   ```

`CHROME_PATH` 없으면 marp 가 Firefox 폴백으로 timeout 발생. 반드시 puppeteer Chrome 경로 지정.

---

## 프론트매터

```yaml
---
marp: true
theme: dami-poster
size: poster
paginate: false
math: katex
---
```

- `theme: dami-poster` — `poster-theme.css` 안의 `@theme dami-poster` 와 매칭
- `size: poster` — `@size poster 841mm 1189mm` 와 매칭 (CSS 에서 정의)
- `math: katex` — KaTeX 수식 활성화

---

## 구조 템플릿 (복붙용)

```markdown
<div class="poster-header">

# 메인 한글 제목 (한 줄)

<div class="subtitle">English Subtitle Here</div>

<div class="authors">저자1<sup>1</sup>, 저자2<sup>1</sup>, ... , 교신저자<sup>1,*</sup></div>

<div class="affil"><sup>1</sup>동국대학교 컴퓨터·AI학과 &nbsp;|&nbsp; {id1, id2, ...}@dgu.ac.kr</div>

</div>

<div class="poster-body">

<div class="poster-col">

<div class="sec">
<h2>1. Introduction</h2>
<div class="sec-body">

- 동기 / 배경 bullet 4–5개
- 기존 연구의 한계
- ...

<div class="keyclaim">

**본 연구의 기여** · ① ... ② ... ③ ...

</div>

<!-- 선택: 시각 자료 (다이어그램) -->
<img src="assets/overview.png" alt="overview" class="full-bleed">

</div>
</div>

<div class="sec">
<h2>2. Problem / Background</h2>
<div class="sec-body">

- 문제 정의
- ...

<div class="twoup">
<div class="col">

#### Sub-case A
설명...

</div>
<div class="col">

#### Sub-case B
설명...

</div>
</div>

</div>
</div>

<div class="sec">
<h2>3. Theory / Analysis</h2>
<div class="sec-body">

- 분석 / 수식
- $M_{eg} := \eta(\langle g^+, g^-\rangle - ...)$
- 표 (markdown 또는 raw HTML)

| Criterion | Description |
|---|---|
| (i) ... | ... |

<div class="implication">
<div class="impl-title">▎ Implications</div>

- 시사점 bullet 1
- 시사점 bullet 2

</div>

</div>
</div>

</div><!-- /poster-col left -->

<div class="poster-col">

<div class="sec">
<h2>4. Proposed Method</h2>
<div class="sec-body">

- 한 줄 요약 / 핵심 통찰

<div class="pipeline">

<div class="step">
<div class="step-head"><span class="num">1</span><span class="lbl">Stage Name</span></div>

설명 paragraph (수식 $f_i$ 포함 가능 — blank-line 으로 감싸야 KaTeX 렌더됨)

</div>

<div class="step">
<div class="step-head"><span class="num">2</span><span class="lbl">Stage Name</span></div>

...

</div>

</div>

</div>
</div>

<div class="sec">
<h2>5. Experiments & Results</h2>
<div class="sec-body">

- 벤치마크 / 비교 대상

| Method | Metric1 | Metric2 |
|---|---|---|
| Baseline | ... | ... |
| **Ours** | **...** | **...** |

![Result chart](assets/chart.png)

- 핵심 발견 bullet 들

</div>
</div>

<div class="sec">
<h2>6. Conclusion & Future Work</h2>
<div class="sec-body">

- 결론 bullet 1
- 결론 bullet 2

<div class="keyclaim">

**Future Work** · ① ... ② ... ③ ...

</div>

</div>
</div>

</div><!-- /poster-col right -->

</div><!-- /poster-body -->

<div class="poster-logos">

<div class="logo-block">
  <img src="assets/dongguk_about_logo.png" alt="Dongguk" class="logo-dongguk">
</div>

<div class="logo-block">
  <img src="assets/dami_logo_full.png" alt="DAMI Lab" class="logo-dami">
</div>

</div>
```

---

## 컴포넌트 사전

| Class | 용도 |
|---|---|
| `.poster-header` | 네이비 상단 배너 (제목 + 부제 + 저자 + 소속) |
| `.poster-body` | 2단 flex 컨테이너 |
| `.poster-col` | 컬럼 (자식 카드를 flex-grow 로 stretch) |
| `.sec` | 섹션 카드 (테두리 + 네이비 헤더 바 + 본문) |
| `.sec > h2` | 섹션 제목 (네이비 배경 + 흰 글자) |
| `.sec-body` | 본문 영역 (padding + content) |
| `.keyclaim` | **노란 callout** — 본 연구의 기여 / Future Work 처럼 한 줄 흐름 강조 |
| `.implication` + `.impl-title` | **파란 callout** — Implications / 시사점 처럼 bulleted 박스 |
| `.twoup` + `.col` | 2 grid 비교 박스 (Before/After, Sub-case A/B) |
| `.pipeline` + `.step` + `.step-head` + `.num` + `.lbl` | 단계별 박스 (1열 stack — 3~5단계 파이프라인) |
| `.poster-logos` + `.logo-block` | 하단 로고 띠 (2-grid, 본문 컬럼과 정렬) |
| `.logo-dongguk` / `.logo-dami` | 두 로고 각각 height 별도 지정 |

### 표 강조 패턴 (style consistency)
모든 표에서 **동일 패턴**으로 강조:
```html
<tr>
  <td class="row-h"><strong>WinnerRow</strong></td>   <!-- 행 라벨 bold -->
  <td class="hi">0.358</td>                           <!-- 데이터 셀 노란 bg + 주황 bold -->
  <td class="hi">0.565</td>
</tr>
```
- `.row-h` — 행 라벨 셀 (옅은 파란 배경, 네이비 텍스트, 좌측 정렬)
- `.hi` — 강조 셀 (`#fff3b8` 배경 + `--gold-d` 주황 bold)
- 강조 행에는 **반드시 `<strong>` + `.hi`** 둘 다 — 한쪽만 쓰면 다른 표와 시각 위계 어긋남

### 이미지 풀폭 (full-bleed) 패턴
카드 좌우 padding 흰 여백까지 채우는 이미지:
```html
<img src="assets/diagram.png" alt="..." class="full-bleed">
```
CSS 의 `.sec-body img.full-bleed` 가 `width: calc(100% + 18mm); margin: 0 -9mm` 로 padding 밖으로 확장.

---

## 자주 부딪히는 함정

### 1. 세로 가운데 정렬 leak
Marpit 기본 테마가 `section` 에 `place-content: safe center center` 를 걸어둠. 단순 `display: block` 으로 안 풀림.

```css
section {
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-start !important;
  place-content: flex-start stretch !important;
  align-content: flex-start !important;
}
```
**`!important` 전부 필수** — base 가 cascade 에서 이김.

### 2. `size:` 프론트매터로 임의 사이즈 안 됨
CSS 안에 `@size poster <w> <h>` 선언 + `@theme dami-poster` 선언 후, 프론트매터에서 `theme: dami-poster; size: poster` 로 호출해야 작동.

### 3. build.py 가 dami-lab.css 강제
`build.py` 는 항상 `--theme-set .claude/skills/marp/themes/dami-lab.css` 를 붙임. 포스터엔 잘못된 결과. 우회: `--keep-built` 로 `.built.md` 만 만들고 별도 marp 직접 호출.

### 4. Marp Firefox 폴백 timeout
Marp 가 Chrome 못 찾으면 Firefox 로 시도 → 30초 timeout. 해결:
```bash
export CHROME_PATH=$HOME/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome
export PUPPETEER_TIMEOUT=300000   # 5분
```

### 5. KaTeX in raw HTML 무시됨
Marpit 은 `<th>$math$</th>` 같은 raw HTML 안의 수식을 **렌더 안 함**. 두 가지 대응:

**표 헤더 — Unicode + HTML 태그**
```html
<th><i>D</i><sup>−</sup><sub>leak</sub></th>
```

**Pipeline step — blank-line markdown sandwich**
```html
<div class="step">
<div class="step-head"><span class="num">1</span><span class="lbl">Stage</span></div>

$f_i$ 같은 수식이 들어가는 본문 paragraph (앞뒤 blank line 필수, `<p>` 래퍼 금지)

</div>
```
앞뒤 blank line 이 markdown 처리를 트리거.

### 6. 본문에 따옴표 (`"..."`, `'...'`) 금지
CommonMark emphasis flanking 충돌로 `**bold**` 가 그대로 렌더됨. 강조는 따옴표 없이 `**bold**` 만, 또는 한글 인용부호 `「…」`.

### 7. 표 + 이미지 폭 정렬
- 두 표 모두 `width: 100%` (sec-body 가득) → 둘 다 통일됨
- 두 표 모두 `width: auto + margin: auto` (content-width 가운데) → 통일됨
- 표 100% + 이미지 auto 같이 섞으면 시각적 위계 깨짐

### 8. 카드 stretch 와 컨텐츠 정렬
```css
.poster-col > .sec { flex: 1 1 auto; display: flex; flex-direction: column; }
.poster-col > .sec > .sec-body { flex: 1 1 auto; display: flex; flex-direction: column; justify-content: space-between; }
.poster-col > .sec:first-child > .sec-body { justify-content: flex-start; }
```
- 모든 카드 stretch 로 column 채움
- 본문은 `space-between` 으로 위/아래 분산
- **단, intro card 만 `flex-start`** — bullet → keyclaim 사이 여백이 어색하게 벌어지는 거 방지

---

## 사이즈별 폰트 가이드

| 사이즈 | h1 | h2 | 본문 | 표 | 비고 |
|---|---|---|---|---|---|
| **A0 (841×1189mm)** | 15.5mm (한 줄 보장) | 14.5mm | 9.5mm | 9.1mm | 이 패턴 기본값 |
| 1m × 2.1m (portrait) | 37mm | 22mm | 14mm | 13mm | LLM unlearning 포스터 |
| B0 (1m × 1.4m) | ~20mm | ~17mm | ~11mm | ~10mm | 미검증 — 위 둘 사이 비례 |

**다른 사이즈 대응**: 모든 mm 값에 동일한 scale factor 곱하기. 예 — A0 → 1×2.1m 변환:
- A0 본문 9.5mm × (37/15.5) ≈ 22.7mm... 아니, h1 비율 (37/15.5 = 2.39) 로 나머지도 곱하면 큼.
- 실제로는 폰트는 1.5x, 패딩은 1.8x, 이미지 max-height 는 2x 처럼 **요소별로 조정**.
- 한 번에 다 곱하지 말고 빌드 → 시각 검증 → 미세 조정 반복.

---

## 참고 예시 (concrete reference)

| 포스터 | 사이즈 | 폴더 |
|---|---|---|
| LLM Unlearning (CONFS) | 1m × 2.1m portrait | `~/sh/ppt_generation/projects/2026-05-18-llm-unlearning-poster/` |
| FORGE Factor Mining | A0 (841×1189mm) | `~/sh/ppt_generation/projects/2026-05-18-forge-factor-mining-poster/` |

두 포스터 모두 같은 `poster-theme.css` 의 변형. 폰트만 사이즈에 맞게 조정.

---

## 디버깅 팁

- **렌더 실패** → `.built.md` 가 만들어졌는지 확인 (없으면 build.py 단계 실패)
- **Page size 가 16:9 로 나옴** → `--theme-set poster-theme.css` 누락 또는 CSS 안 `@size` 정의 누락
- **컨텐츠 세로 가운데 몰림** → section flex CSS 의 `!important` 누락
- **표 헤더 수식 안 보임** → markdown table 로 바꾸거나 unicode 로 대체
- **카드 컨텐츠 overflow** → 폰트 조금 줄이거나 (-0.5mm) sec-body padding 줄이기 (8mm → 6mm)
- **로고 위치 이상** → `.poster-logos` 가 2-col grid 인지 확인 (`display: grid; grid-template-columns: 1fr 1fr`)
