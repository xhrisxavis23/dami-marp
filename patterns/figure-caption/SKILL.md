---
name: marp/figure-caption
description: marp PPT 의 figure (그림) 에 메시지 중심 캡션을 달고, 자동으로 Fig. N 번호 매기기 + 그림 흰여백 자동 trim. 사용자가 "캡션 달아줘 / figure 정리 / 그림에 번호 매겨줘" 등 요청 시 가동.
type: pattern
---

# Figure Caption — DAMI Lab marp 패턴

PPT 작성은 평소대로 진행하되, **사용자가 "캡션" 명령을 내리는 순간** 이 패턴이 가동된다.
한꺼번에 모든 그림에 메시지 중심 캡션 + 자동 번호 + 정렬 fix 를 적용한다.

---

## 트리거

다음 중 하나라도 사용자가 말하면 이 패턴 가동.

- "캡션 달아줘" / "캡션 추가" / "figure 캡션"
- "figure 정리" / "그림 정리"
- "그림에 번호 매겨줘" / "Fig. N"
- "figure-caption 적용"

---

## 워크플로우 (3 단계)

### ① 인벤토리 + 메시지 추출

소스 마크다운 (`*.md`) 안의 모든 figure 를 찾아 정리.
- 마크다운 `![](...)` 또는 HTML `<img>` / `<figure>` 모두 카운트
- 각 그림의 위치 (어느 슬라이드의 무슨 페이지) 와 파일명 정리
- 그림이 보여주는 **takeaway 메시지** 1-2 줄로 추출 (디테일 < takeaway 원칙)

사용자에게 "그림 N 개 발견, 캡션 후보 N 개" 형태로 먼저 제시하고 승인 받는다.

### ② 마크업 변환

승인 받은 캡션을 fig-wrap div 마크업으로 적용.

```markdown
<div class="fig-wrap w600">
<img src="assets-trimmed/path/figure.png">
<div class="fig-cap cap-B">캡션 본문, 명사형 마무리</div>
</div>
```

- `w{N}` 클래스로 폭 명시 (인라인 style 은 marpit 이 strip 하므로 사용 X)
- `assets/` → `assets-trimmed/` 경로 변경 (③ trim 결과 사용)

### ③ 빌드 (build_figcap.py 한 번에)

```bash
# 한 번 (또는 그림 추가 시): 흰여백 trim
python3 ~/wj/.claude/skills/marp/patterns/figure-caption/trim_assets.py assets/ assets-trimmed/

# 매 빌드: prebuild + marp + cleanup 통합
python3 ~/wj/.claude/skills/marp/patterns/figure-caption/build_figcap.py slides.md
```

`build_figcap.py` 가 자동으로
1. `prebuild.py` 로 Fig. N 자동 prefix 삽입 → `slides.numbered.md` 생성
2. `~/wj/.claude/skills/marp/bin/build.py` 로 PDF 빌드
3. `slides.numbered.pdf` → `slides.pdf` rename
4. **중간 파일 (`slides.numbered.md`, `slides.numbered.built.md`) 자동 삭제**

flags:
- `--format pptx|html` (default pdf)
- `--keep` 중간 파일 보존 (디버그용)

---

## 캡션 작성 철학 (지켜야 할 룰)

이 패턴이 가동될 때 **무조건** 적용한다. 사용자가 별도 지시 안 해도.

### A. 메시지 중심
- 그림이 **무엇을 보여주는가** 보다 **이 그림으로 말하고 싶은 메시지**
- 디테일 (구체 컴포넌트, 수치, 컬러 매핑 등) 은 본문 또는 발표 멘트로 분리
- 한 캡션 = 1-2 문장, 70 자 이내 권장

### B. 어미 · 마침표 룰
- **"~다" 종결 금지** — "보존한다", "가른다", "결정한다" X
- **끝 마침표 (.) 금지** — 마지막 글자가 마침표면 무조건 제거
- 마무리는 **명사형** ("보존", "통제", "추출") 또는 **"~함" / "~됨"**
- 캡션 *중간* 의 마침표는 OK (영역 구분용)

예시
| ✗ | ✓ |
|---|---|
| OURS 는 person 을 보존한다. | OURS 는 person 보존 |
| 위험을 가른다. | 위험을 가름 |
| 자동 생성된다. | 자동 생성 |
| 보존 대상. | 보존 대상 |

### C. 좌·우·중앙 표기
- 한국어 "좌 / 가운데 / 우" → **영문 약자 "Left / Center / Right"**
- **콜론 형식**: `Left :` (콤마 X, em-dash X)
- 그림이 **진짜 좌우 분리** 일 때만 사용 (KDE plot 처럼 중첩된 분포는 사용 X)

```html
<div class="fig-cap cap-B"><span class="lbl">Left :</span> ... <span class="lbl">Center :</span> ... <span class="lbl">Right :</span> ...</div>
```

### D. 글리프 금지
- `→`, `➜`, `·` (가운데점), 이모지 모두 금지
- 화살표는 자연어로 ("X 에서 Y 로", "X, 다시 Y")
- 이미 marp 글로벌 룰 (`marp 화살표/아이콘 사용 금지`) 과 일치

### E. 약어
- "예시" 같은 한글은 그대로 두는 게 자연. 단 사용자가 명시적으로 영문 약어 (e.g.) 를 원하면 그때 사용
- "와", "그리고" 같은 conjunction 은 한국어로

---

## 마크업 패턴 (복붙용)

### 일반 단일 그림
```html
<div class="fig-wrap w600">
<img src="assets-trimmed/foo/fig1.png">
<div class="fig-cap cap-B">캡션 본문, 명사형</div>
</div>
```

### Left / Center / Right 분할 그림
```html
<div class="fig-wrap w920">
<img src="assets-trimmed/foo/fig2.png">
<div class="fig-cap cap-B"><span class="lbl">Left :</span> 좌측 메시지. <span class="lbl">Center :</span> 가운데 메시지. <span class="lbl">Right :</span> 우측 메시지. 종합 takeaway</div>
</div>
```

### 비교 (Method A vs Method B) 그림
```html
<div class="fig-wrap w700">
<img src="assets-trimmed/foo/fig3.png">
<div class="fig-cap cap-B"><span class="lbl">A :</span> A 의 결과 한 줄. <span class="lbl">B :</span> B 의 결과 한 줄</div>
</div>
```

`w{N}` 변형 가능: `w560` `w600` `w680` `w700` `w800` `w860` `w920` `w1000` (필요 시 CSS 에 추가)

---

## CSS 블록 (slides.md 의 `<style>` 안에 그대로 복붙)

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700;900&display=swap');

section div.fig-wrap {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  margin: 4px auto 0;
  max-width: 95%;
  text-align: left;
}
section div.fig-wrap.w560 { width: 560px; }
section div.fig-wrap.w600 { width: 600px; }
section div.fig-wrap.w680 { width: 680px; }
section div.fig-wrap.w700 { width: 700px; }
section div.fig-wrap.w800 { width: 800px; }
section div.fig-wrap.w860 { width: 860px; }
section div.fig-wrap.w920 { width: 920px; }
section div.fig-wrap.w1000 { width: 1000px; }
section div.fig-wrap img {
  display: block;
  width: 100% !important;
  height: auto !important;
  margin: 0 !important;
  float: none !important;
  max-width: 100% !important;
}
section div.fig-wrap div.fig-cap.cap-B {
  text-align: left;
  color: #444;
  font-size: 0.7em;
  font-family: 'Noto Serif KR', serif;
  line-height: 1.4;
  margin-top: 1px;
  padding: 0 0 0 14px;
  width: 100%;
  box-sizing: border-box;
}
section div.fig-wrap div.fig-cap.cap-B .num {
  font-weight: 700;
  color: #003478;
  margin-right: 4px;
}
section div.fig-wrap div.fig-cap.cap-B .lbl {
  font-weight: 700;
  color: #003478;
}
```

---

## 도구 (이 폴더 안에 함께 위치)

### `prebuild.py`
빌드 전에 `fig-cap` 마다 `<span class="num">Fig. N.</span>` 자동 prepend.
사용자는 캡션 본문만 작성. 슬라이드 추가/삭제/순서 변경 시 자동 갱신.

```bash
python3 ~/wj/.claude/skills/marp/patterns/figure-caption/prebuild.py slides.md
# → slides.numbered.md 생성
```

### `trim_assets.py`
원본 그림 PNG 의 좌우상하 흰여백 자동 제거. `assets/` → `assets-trimmed/` 사본 생성.
원본 자산은 손대지 않음 (다른 PPT 와 공유 시 안전).

```bash
python3 ~/wj/.claude/skills/marp/patterns/figure-caption/trim_assets.py assets/ assets-trimmed/
```

---

## 왜 이렇게 설계했나 (배경)

1. **`<figure>` 가 아닌 `<div>` 사용**: marpit 이 `<figure>` 와 `<img>` 에 자동 css 룰 6개 (margin: 0 auto, float: left, height: 1em 등) 를 강제 적용 → 우리 css 가 충돌. div 는 자동 룰 영향 X.
2. **인라인 style 대신 클래스 변형 (`.w600`)**: marp 는 빌드 시 div 의 `style="..."` 인라인 속성을 sanitize (제거). 클래스 이름은 보존됨.
3. **그림 PNG 흰여백 trim**: 원본 PNG 안의 흰 padding 때문에 캡션이 그림 콘텐츠보다 시각적으로 왼쪽에 보이는 문제. 자동 trim 으로 해결.
4. **CSS counter 대신 prebuild 자동 번호**: marp 의 section break 마다 CSS counter 가 reset 되어 누적 안 됨. 빌드 전에 직접 prefix 삽입이 가장 안정.

---

## 점검 체크리스트 (캡션 작업 완료 후)

- [ ] 캡션 어미 "~다" 없음
- [ ] 캡션 끝 마침표 없음
- [ ] 화살표 글리프 (`→` `➜` `·`) 없음
- [ ] Left / Center / Right 형식이면 콜론 (`:`)
- [ ] Fig. 1 ~ Fig. N 까지 빌드 결과에 자동 매겨짐
- [ ] 모든 그림 좌측 정렬 일치 (캡션이 그림 좌측보다 14px 안쪽)
- [ ] overflow 없음 (footer 침범 X) — `marp overflow zero tolerance` 룰
