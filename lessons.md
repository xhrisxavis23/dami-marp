# Marp 스킬 삽질/포렌식 기록

DAMI Lab Marp 양식을 만들면서 실제로 겪은 버그와 그 원인 분석. `SKILL.md` 본문에는 규칙만 한두 줄로 두고, 재현 맥락과 원인 추적은 여기에 남긴다.

동일 이슈가 재발했을 때 "이게 그때 그거였나?" 를 확인하거나, 규칙을 완화/변경해도 되는지 판단하는 용도.

---

<a id="background-important"></a>
## `background` 가 렌더에 안 보일 때 — `!important` 필수

- **증상**: `section { background: ... }` 또는 `border-left`, `box-shadow`를 써도 PDF 렌더에 아무것도 안 나옴. DevTools에서 CSS는 정상으로 보이는데 화면만 비어 있음.
- **원인**: Marp `default` 테마가 내부적으로 `section { background-color: var(--bgColor-default) }` 를 꽤 높은 specificity(`div#:$p > svg > foreignObject > section`)로 걸어 놓음. 사용자 `style:` 블록이 뒤에 오더라도 cascade로 이기지 못할 때가 있음.
- **해결**: 사용자 section 배경엔 **`!important` 를 반드시 붙인다**. 예:
  ```css
  section          { background: #ffffff !important; }
  section.title    { background: #0b2c5a !important; }
  section.section  { background: #0b2c5a !important; }
  ```
- **주의**: base section에 `!important` 를 쓰면 `.title`/`.section` 등 하위 클래스도 똑같이 `!important` 로 덮어써야 함. 안 그러면 전부 기본 배경이 적용돼 버림.
- **삽질 기록**: `border-left: 10px solid`, `box-shadow: inset`, `div.leftbar`를 DOM에 주입하는 방식 모두 실패했음. 결국 `!important`가 범인이었음.

---

<a id="before-after-재활용"></a>
## `::before` 를 재활용할 때 base 속성 전부 덮어쓰기 — `.section` 네이비 바 함정

- **증상**: `.section` 슬라이드의 상단 네이비 바가 **왼쪽 56px 좁은 막대**로만 나오고, 흰 제목이 안 보인다 (흰 배경 위 흰 글씨).
- **원인**: base `section::before` 가 로고용으로 `width: 56px; height: 46px; background: url(./assets/dami_logo.png) ...; top: 20px; right: 40px` 를 걸어두고 있음. `.section::before` 에서 `top/left/right/height/background` 만 덮으면 **`width: 56px` 가 cascade로 살아남아** 왼쪽 56px 폭 바만 그려진다. h1은 나머지 흰 영역에 걸쳐서 흰 글씨가 묻힌다.
- **해결**: `.section::before` 에 **base의 모든 관련 속성을 명시적으로 리셋**한다.
  ```css
  section.section::before {
    display: block !important;
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    width: auto;              /* base의 width:56px 를 덮음 (left:0+right:0 가 작동하도록) */
    height: 63%;
    background: #0b2c5a;
    background-image: none;   /* base의 url(dami_logo.png) 제거 */
    z-index: 1;
  }
  ```
- **일반 규칙**: base에서 설정된 `::before` / `::after` 를 하위 클래스가 재활용할 때는 **가로(width), 세로(height), 위치(top/right/bottom/left), 배경(background + background-image)** 를 전부 다시 선언한다. shorthand `background: <color>` 는 `background-image` 까지 `initial` 로 되돌리는 것처럼 보여도, 확실하게 `background-image: none` 도 함께 써 주는 편이 안전.

---

<a id="linear-gradient-금지"></a>
## `linear-gradient` 는 쓰지 않는다 — 단색만

- **증상**: `linear-gradient(to right, #0b2c5a 0, #0b2c5a 10px, #fff 10px)` 로 왼쪽 네이비 세로 바를 그렸더니, pdftoppm 렌더(`k-*.png`)와 사용자 PDF 뷰어 캡쳐가 서로 다르게 보임. PDF 뷰어에 따라 경계가 블러/앤티에일리어스 처리되거나 아예 안 보임.
- **원인**: PDF 렌더링 엔진(poppler vs Chromium PDF vs Adobe 등)이 `linear-gradient` 의 hard stop을 각자 다르게 해석. 특히 1px~10px 얇은 구간의 서브픽셀 rounding이 엔진마다 달라짐.
- **해결**: 배경은 **단색만 사용**. 네이비 구간이 필요하면 `.title`/`.section` 같은 전체 네이비 단색 클래스를 만들어서 써라.
- **하지 말 것**:
  - `background: linear-gradient(...)` (렌더 엔진 차이로 출력이 불안정)
  - 얇은 좌측 네이비 바를 `linear-gradient` 로 그리는 트릭 (뷰어마다 경계가 블러됨)
- **대안**: 강조가 필요한 영역은 h1/블록 단위 `border-left` 로 처리 (이미 h1에 6px navy border-left 적용 중).

---

<a id="h1-상단-정렬"></a>
## 모든 본문 슬라이드의 h1 시작 위치를 일치시킨다 — `justify-content: flex-start` 필수

- **증상**: 같은 일반 본문 슬라이드인데도 슬라이드마다 h1 제목이 시작되는 세로 위치(y좌표)가 제각각. 콘텐츠가 짧은 장은 h1이 아래로 밀리고, 콘텐츠가 많은 장은 h1이 상단에 붙는다.
- **원인**: Marp `default` 테마의 base CSS 가 `section { display: flex; flex-direction: column; justify-content: center }` 로 세로 중앙 정렬을 걸어둠. 콘텐츠 총 높이가 작으면 flex가 전체 박스 중앙으로 수렴 → h1이 `padding-top` 값을 무시하고 아래로 밀려 보임.
- **해결**: base `section` 규칙에 **`display: flex !important; flex-direction: column; justify-content: flex-start !important; place-content: flex-start !important;`** 를 모두 추가. `justify-content` 만으로는 부족하다 (아래 주의사항 참고).
- **`justify-content` 만으로 부족한 이유** (2026-04 추적 기록): Marp default 의 실제 section CSS 를 `--format html` 로 dump 해보면 `display: block; place-content: safe center center; padding: 78.5px` 로 되어 있다. `place-content` 는 `align-content` + `justify-content` shorthand 인데, 최신 CSS 스펙에서 **block 컨테이너에도 `align-content` 가 적용**되어 콘텐츠가 세로 중앙으로 모인다. 이 상태에서 `justify-content: flex-start` 만 걸면 block 에서 무효이고 `place-content: center` 가 그대로 이긴다. 따라서 `display: flex !important` 로 명시하고 `place-content: flex-start !important` 도 함께 걸어야 확실히 상단 정렬된다.
- **padding-top 은 `30px` 로 고정**: 현재 `padding: 30px 56px 56px 68px !important`. 이유는 **h1 의 border-bottom(긴 네이비 바)이 우상단 코끼리 로고(y=20~66) 바로 아래에 오도록** 튜닝한 값. h1 박스 높이 약 43px 이므로 30+43=73 에서 border 가 위치해 로고 하단과 7~10px 여유. 값을 키우면 (예전 48px 등) 콘텐츠 양에 따라 flex 정렬이 흔들려 슬라이드마다 제목 Y좌표가 시각적으로 어긋남. 키우지도 0 에 가깝게 내리지도 말 것 (로고랑 붙거나 겹침).
- **왜 `!important` 인가**: default 테마의 `section` selector 와 specificity 가 동일해서 cascade 순서에 따라 밀릴 수 있음. `background` 와 동일한 사유.
- **`.end` 슬라이드 예외**: `.title`, `.section`은 `position: absolute` 로 h1을 배치하므로 base의 `flex-start`에 영향받지 않는다. 하지만 `.end`는 **flex 중앙정렬을 그대로 쓰므로** `justify-content: center !important` 를 **반드시 함께 붙여야** 한다. 안 그러면 base의 `flex-start !important` 에 덮여서 Thank you 제목이 위쪽으로 올라간다 (실제 발생한 버그). `.end`에는 `display: flex !important`, `padding: 48px 56px !important` 도 함께 고정해야 안정적.
- **체크 방법**: 빌드 후 본문 슬라이드 2~3장을 모아 보고 h1 상단 라인이 시각적으로 **같은 y좌표**에 있는지 확인. 어긋나면 base `section` 에서 `justify-content` 가 빠졌을 가능성이 크다.

---

<a id="쌍따옴표-금지"></a>
## 본문에 쌍따옴표·작은따옴표를 쓰지 않는다 — CommonMark emphasis flanking

- **증상**: 슬라이드에 `**"텍스트"**` 또는 `**"텍스트"**조사` 가 그대로 `**"텍스트"**` 로 렌더됨 (별표/따옴표가 기호 그대로 노출).
- **원인**: CommonMark 의 emphasis *flanking* 규칙. `**` 옆에 punctuation(`"`, `'`)이 오고 반대편에 한글(word char)이 오면 left/right-flanking 판정이 깨져서 `**` 가 열림/닫힘으로 인식되지 않음. 특히 `**"…"**조사` 패턴(닫는 `**` 앞이 `"`, 뒤가 한글)에서 거의 항상 실패.
- **규칙**: 본문에서 **쌍따옴표·작은따옴표를 아예 쓰지 않는다**. 강조가 필요하면 `**bold**` 하나로만 해결한다. CSS·HTML 속성(`class="..."`, `url('...')`, `style="..."`) 안의 따옴표는 문법이므로 예외.
- **해결 패턴** (따옴표 제거 + bold 유지):
  ```
  BAD : **"어디서 믿고, 어디서 의심할지"**를 가르친다
  GOOD: **어디서 믿고, 어디서 의심할지**를 가르친다
  ```
  ```
  BAD : 단순 "챗봇 써보기"가 아니라 **업무 재설계** 단계
  GOOD: 단순 챗봇 써보기가 아니라 **업무 재설계** 단계
  ```
  ```
  BAD : 왜 '지금' 시작해야 하는가
  GOOD: 왜 지금 시작해야 하는가
  ```
- **인용·예시처럼 꼭 따옴표 느낌이 필요할 때**: `예: …` 접두어나 blockquote(`>`)로 대체한다. 한글 인용부호 `「…」`, `『…』` 도 OK (flanking 영향 없음).

---

<a id="mermaid-label-clip"></a>
## Mermaid flowchart 라벨 마지막 글자 클리핑

- **증상**: `flowchart` 박스 라벨의 마지막 글자가 1~2 픽셀 잘려 보임 (예: `built` → `buil`, `slides.md` → `slides.mc`, `mermaid 렌더` → `mermaid 렌`).
- **원인**: Mermaid 가 생성하는 SVG 의 `<text>` bbox 계산이 SVG-in-`<img>` 렌더 경로(Chromium 이 data URI 로 받은 SVG 를 렌더할 때) 에서 text advance width 와 mismatch. 특히 마침표 `.` 또는 특정 폰트 glyph 의 trailing advance 가 0 에 가까울 때 마지막 글자가 박스 padding 을 넘어 clip.
- **시도했지만 실패한 우회책**:
  - `flowchart.padding` 확대 → 박스는 커지지만 내부 text 위치 고정되어 여전히 clip
  - `htmlLabels: true` → PDF 렌더에서 `<foreignObject>` 도 같은 문제
  - trailing space / NBSP 추가 → mermaid 가 자동 strip
  - SVG root 에 `overflow="visible"` → clip 은 visual 이 아니라 text rendering 단계라 무효
- **실용 우회**:
  1. **라벨 끝에 긴 영문 + 마침표 조합 피하기** — `slides.md` 대신 `마크다운`, `built` 대신 `빌드 산출물`.
  2. **한글 또는 넓은 CJK 문자로 끝내기** — `slides.md` → `slides md 파일`.
  3. **정 영문이 필요하면 뒤에 여유 문자 추가** — `[marp CLI]` 처럼 의미 있는 단어 2개를 space 로 붙이면 safe.
- **후속 해결 방향** (미구현): SVG 를 data URI 대신 별도 `.svg` 파일로 저장 + `<img src="diagram.svg">` 로 참조. Chromium 이 file URL 로 받은 SVG 는 독립 rendering pipeline 을 써서 text bbox 계산이 정확할 가능성.

---

<a id="flow-box-structure"></a>
## `.flow-box` 는 `.header` + `.body` 구조 필수, 화살표는 CSS 자동 생성

- **증상**: `<div class="flow-box">` 안에 `<strong>제목</strong><br/>본문` 식으로 inline 작성했더니, 렌더 결과에서 박스 내부 제목 텍스트의 **윗부분이 1~2px 잘림** (예: "1. DFS 탐색" 의 숫자 "1" 상단이 박스 border 에 의해 clip). 화살표도 박스 사이에 정상 arrow + 중복된 `→` 문자가 동시에 표시됨.
- **원인 1 (clip)**: `dami-lab.css` 의 `.flow-box` 는 `display: flex; flex-direction: column` 에 `padding: 0` + `border: 1px solid` 만 걸려 있음. 내부 패딩은 `.header` / `.body` 자식 div 에서 책임짐. header/body 없이 raw text 를 넣으면 padding 이 0 이라 텍스트가 box border 에 딱 붙어 clip.
- **원인 2 (중복 화살표)**: `.flow-row > .flow-box:not(:first-child)::before` / `::after` 가 **자동으로 화살표 선 + 삼각형을 그려줌**. 사용자가 수동으로 `<div class="flow-arrow">→</div>` 를 추가하면 CSS arrow + `→` 글리프가 중복 렌더됨.
- **해결**: 공식 패턴 그대로 쓰기.
  ```html
  <div class="flow-row">

  <div class="flow-box">
  <div class="header">1. 제목</div>
  <div class="body">

  - 본문 항목

  </div>
  </div>

  <div class="flow-box">
  <div class="header">2. 제목</div>
  <div class="body">본문</div>
  </div>

  </div>
  ```
  - `<div class="flow-row">` 와 `<div class="flow-box">` 태그 전후에 **빈 줄** (마크다운이 내부 `-` 리스트를 렌더하도록).
  - **`<div class="flow-arrow">` 는 쓰지 않는다** — CSS 가 자동으로 넣음.
  - 짧은 한 줄 본문이면 `.body` 안에 그냥 텍스트만 써도 됨 (리스트 안 쓸 땐 빈 줄 생략 가능).
- **검증 방법**: 빌드 후 `pdftoppm` 으로 PNG 뽑아서 **박스 내부 텍스트 상단 여백** 확인. 네이비 헤더 바가 안 보이면 `.header` 누락 의심.

---

<a id="figure-center-class"></a>
## Figure 중앙 정렬은 명시적 클래스로

- **증상**: `![w:600](path.png)` 만 쓰면 본문 텍스트와 같이 좌측 정렬로 배치되어 도식이 슬라이드 한쪽에 쏠림.
- **해결**: 슬라이드에 `<!-- _class: figure-center -->` 부여하고 frontmatter style 에:
  ```css
  section.figure-center img { display: block; margin-left: auto; margin-right: auto; }
  section.figure-center .fig-cap { text-align: center; color: #6e7785; font-size: 0.66em; }
  ```
- **언제 적용**: 본문 + 큰 도식 한 장 + (선택) 캡션 구조의 슬라이드. 표·데이터 grid 슬라이드는 grid 자체가 이미 폭을 통제하므로 안 붙여도 됨.

---

<a id="empty-refs-block"></a>
## 본문에 [N] 인용 마커 없으면 `<div class="refs">` 출력 금지

- **증상**: 슬라이드 하단에 references 박스가 있는데 본문에는 `[N]` 마커가 하나도 없어서 "왜 갑자기 인용?" 처럼 보이고, 박스가 footer 와 겹쳐 overflow 사고도 유발.
- **원인**: 작성 중 본문 변경하면서 `[N]` 마커는 지우고 하단 `<div class="refs">` 는 잊고 남기는 패턴이 잦음.
- **규칙**: 본문 어디에도 `[N]` 이 없으면 그 슬라이드의 `<div class="refs">` 는 통째로 삭제. References 페이지에서만 나열.

---

<a id="figure-pdf-recapture"></a>
## PDF 그림 재캡처는 pdftoppm + PIL crop

- **증상**: 논문 PDF 의 한 페이지에 figure 2 + section heading + figure 3 가 모두 들어 있어, PDF 자르기 도구로 figure 만 따려다 인접 텍스트와 다른 figure 까지 같이 잡혀서 슬라이드에 그대로 들어감.
- **해결 절차**:
  1. `pdftoppm <pdf> /tmp/<name> -png -r 200 -f <page> -l <page>` 로 해당 페이지 PNG 추출
  2. PIL `Image.crop((left, top, right, bottom))` 으로 figure 영역만 좌표로 잘라 저장
  3. 결과를 `assets/<paper>/figN_clean.png` 로 두고 슬라이드에서 참조
- **참고**: top/bottom 비율 (예: 0.70 / 0.85) 로 시도 → 한두 번 미세조정. 매번 정확한 px 못 맞춰도 OK.

---

<a id="references-page-split"></a>
## References 13 개 이상은 페이지 분할

- **증상**: 한 슬라이드에 references 13 개를 0.74em 으로 욱여 넣었더니 [12], [13] 이 footer 와 겹치고 본문 영역 밖으로 나감.
- **해결**: References 7~8 개를 한 페이지에, 나머지를 다음 페이지로 분리. 제목은 `References (1/2)`, `References (2/2)` 로 표기.
- **임계값 (경험치)**: 0.72~0.74em · line-height 1.55 기준 한 페이지 7~8개. 12개 이상이면 무조건 분할.

---

<a id="bottom-callout-vertical-balance"></a>
## 슬라이드 하단 callout 의 위·아래 여백 균형 (auto-margin pattern)

- **증상**: "공통 메시지" / "why-box" / 결론 박스 같은 하단 callout 을 두면 위 콘텐츠와의 거리(짧음) vs 푸터까지의 거리(김) 가 항상 어긋남. 사용자가 "위아래 간격이 안 맞는다" 고 반복 지적.
- **원인**: 슬라이드는 고정 높이 캔버스인데, 위 콘텐츠가 가변이라 단순 `margin-top: <고정>` 으론 페이지마다 다름. `<br>` 으로 빈 줄 채우는 식은 더 어긋남.
- **해결 패턴**:
  ```css
  section.<class> { display: flex; flex-direction: column; }
  section.<class> .callout {
    margin: auto 0 <Y>px 0;   /* auto-top 이 위 빈 공간 흡수 */
  }
  ```
  - `Y` 는 시각적 calibration 값. 30~40px 부근에서 시작, 빌드 후 PNG 보고 ±10 단위로 조정.
- **calibration 절차**:
  1. 빌드 후 `pages/page-NN.png` 열고 박스 top/bottom 픽셀 위치 확인
  2. 위 콘텐츠 끝 y → 박스 top y = `gap_top`
  3. 박스 bottom y → 푸터 시작 y = `gap_bottom`
  4. 두 값이 같아질 때까지 `Y` 조정. 일반적으로 gap_bottom 이 크면 Y 줄이고, gap_top 이 크면 Y 늘림
- **계산 직관 (대략)**: `Y` 가 작아질수록 박스가 아래로 내려가서 gap_bottom 이 줄고 gap_top 이 늚. 반대로 `Y` 키우면 박스 올라가서 gap_top 줄고 gap_bottom 늚. 시작값은 한 페이지 풀 콘텐츠 기준 30~40px 부근이 좋더라.
- **검증 의무**: 매 빌드마다 callout 이 들어간 페이지의 PNG 를 *반드시* 확인. "되는 거 같다" 로 멈추지 말고 픽셀로 측정.

---

<a id="figure-tight-followup-text"></a>
## Figure 다음 텍스트와의 간격 좁히기

- **증상**: figure-center 슬라이드에서 그림 캡션 다음에 오는 `## 부제` 또는 bullet 사이 간격이 50~70px 로 떠 보임.
- **원인**: 테마 base 의 `section h2 { margin-top: ... }` 가 우선순위로 살아남고, marp 가 figure 와 h2 사이에 자동 block-margin 을 끼워 넣음.
- **해결**:
  ```css
  section.figure-center img { margin-bottom: 0; }
  section.figure-center .fig-cap { margin-top: 0; margin-bottom: 0; }
  section.figure-center h2 { margin-top: 2px !important; margin-bottom: 2px !important; }
  section.figure-center ul { margin-top: 4px !important; }
  ```
- **주의**: `!important` 없으면 base theme 가 이김. 첫 시도에서 안 먹으면 specificity 부족 — `!important` 붙여라.

---

<a id="fields-with-examples-not-frame"></a>
## 분야 개관(field-intro) 슬라이드 — "기존 평가 / 본 논문 핵심 가치" 카드는 빼라

- **증상**: 분야 소개 슬라이드에 "기존 평가의 한계 / 본 논문의 핵심 가치" 같은 framework 카드를 넣으면 사용자가 "이런 거 빼라, 예시가 중요하다" 고 일관되게 지적.
- **원인**: 분야 개관의 목적은 "이 분야가 왜 흥미롭고 위험한지" 를 청중이 직관적으로 느끼게 하는 것. 본 논문 자랑은 뒤 페이지에서 자연스럽게 흐름.
- **해결 패턴**:
  - 분야 개관은 **시각적 demo** (jailbreak 페이지 같은 chat-bubble pair, 정상 vs 공격 비교) + **사례 카드** (실 사고/벤치마크 짧은 인용) 만 둔다.
  - "기존 한계 / 본 논문 핵심 가치" 류 framework 카드는 *방법 페이지* 또는 *문제 정의 페이지* 로 미룬다.
- **demo-grid 패턴 (재사용 가능)**: `.demo-card` (정상 / 공격), step rows with `.role` 색 구분 (User / Agent / Tool / Attacker / Final), `<span class="inj">` 으로 injection 강조, `.verdict` 로 결과 판정 표시.

---

<a id="news-card-overflow-shrink"></a>
## 뉴스 / 사례 카드 6 개가 안 맞을 때

- **증상**: 6 개 카드 (3×2 또는 2×3) 가 슬라이드 아래로 넘침. 빌드 후 PNG 에서 확인 가능.
- **해결 우선순위**:
  1. 카드 padding 12px → 8px, gap 12px → 8px
  2. 카드 h3 0.88em → 0.82em, p 0.76em → 0.7em, line-height 1.5 → 1.4
  3. 그래도 넘치면 카드 4 개로 축소 + 다른 페이지로 이전
- **불릿/줄글 박스도 같은 원칙**: 줄글 3+ 줄 → bullet 으로 분해. 줄글 1~2 줄만 두고 나머지는 list 로.

---

<a id="verify-after-build-mandatory"></a>
## 빌드 후 검수는 의무 — "한번 보고 끝" 안됨

- **증상**: 사용자가 "왜 아직도 못 고치냐" 반복 지적 — 내가 빌드만 하고 PNG 확인 안 한 채 "수정 완료" 라고 보고했기 때문.
- **규칙**:
  1. 빌드 후 `pages/page-NN.png` 를 *모두* 또는 *수정한 페이지 + 인접 페이지* 를 직접 본다
  2. overflow / 정렬 / 간격 / 캡처 누락 모두 픽셀로 확인
  3. "보기에 OK 같다" 로 끝내지 말고 *문제로 지적된 항목* 하나하나 수치로 검증
  4. 수정-빌드-확인을 반복. 한 번에 완벽 해결 안 됨이 정상.
- **사용자 직접 인용 (2026-05-02)**: "너가 만들면서 계속 위아래 간격 체크하면서 제대로된 셋팅값을 찾아서 앞으로 skill 에 반영해!!"

---

<a id="news-article-fidelity"></a>
## 신문 기사 풍 mock-up 은 *실제 기사* 만 쓴다 (절대 규칙)

- **사고 (2026-05-02)**: 페이지에 신문 기사 형식 박스를 만들면서 기자 이름 ("By 김OO 기자"), 인용문 ("한국저작권위원회"), 부속 정보 모두 *내가 임의로 지어 넣음*. 사용자 적발: "이거 진짜 기사에서 긁어온거 맞지?? 한국저작권위원회 저것도 기사에서 있던거야??"
- **이건 사실 왜곡** 이다. 발표 자료에 가짜 인용·가짜 기자명 들어가면 청중 신뢰 박살, 법적/윤리적 리스크.
- **절대 규칙**:
  1. masthead, 헤드라인, 보도일, 기자 이름, byline, 본문, 인용문, source — *모두 실제 기사에서 그대로 가져오거나 바로 paraphrase*. 추측·창작 금지.
  2. 기사 URL 을 **반드시** mock-up 박스 하단에 출처로 표기.
  3. 길이 조절은 *발췌* 로만. 압축이 필요하면 원문에 있는 핵심 문장을 골라 쓰고, 빠진 부분에 새 문장 끼워 넣지 않는다.
  4. 시각적 변형은 **highlight (yellow bg) / bold / pull-quote 발췌** 만 허용. 텍스트 자체 변경 금지.
  5. 기사 캡처 이미지 대신 HTML mock 을 쓰는 이유: 사진 화질·잘림·저작권 회피. 즉 *대체 표현* 일 뿐 *내용 위조 도구가 아님*.
- **체크리스트** (mock-up 만들기 전):
  - [ ] WebFetch 로 기사 본문 전체 추출했는가?
  - [ ] 기자 이름·이메일 그대로 쓰는가?
  - [ ] 인용문은 원문에 있는 발화자가 한 말인가?
  - [ ] 발췌·hl 강조 외에 한 글자라도 내가 만든 게 있는가? (있으면 삭제)
  - [ ] source URL 박스 하단에 보이는가?
- **사용자 직접 인용 (2026-05-02)**: "기사풍으로 가져오면 정말 기사에 있는거만 가져와야해!! 그리고 기자에있는것중에 중요한부분은 약간 hight하는 형태만 변형을 허용할게!!"

---

<a id="no-em-dash"></a>
## 한글 슬라이드 본문에 em-dash (—) 사용 금지

- **사용자 user-memory 규칙 (재확인 2026-05-02)**: "한글 응답에서 em-dash(—) 사용 금지, 쉼표/괄호/문장 분리로 대체". marp 슬라이드 본문에도 동일 적용.
- **사고**: 그동안 "Step 1 — Probing" / "정상 상황 — 공격 없음" / "예 — 지브리 브랜딩..." 식으로 em-dash 를 사역접속·구분자·인용 추가 설명 모두에 사용 → 사용자 반복 지적.
- **대체 가이드**:
  | 용도 | em-dash 대신 |
  |---|---|
  | 단계/phase 라벨 ("Step 1 — Name") | `Step 1 · Name` 또는 `Step 1. Name` |
  | 부제·구분자 ("정상 — 공격") | `정상 · 공격` 또는 `정상 vs 공격` |
  | 부연 설명 ("X — 즉 Y") | `X. Y` (마침표 분리) 또는 `X (Y)` |
  | 인용 출처 ("...이다 — 칼라 오티즈") | `...이다." (칼라 오티즈)` |
  | 카드 헤드라인 ("Comet — GitHub 토큰 탈취") | `Comet · GitHub 토큰 탈취` |
  | 영어 인용 그대로 ("X — Y") | 가능하면 그대로, 다만 한국어 옆에 두지 말기 |
- **검증 명령**: 빌드 직전 `grep -c '—' slides.md` 가 0 인지 확인. CSS 주석 (`/* ── ── */` 박스) 만 허용.
- **예외**: 영어 원문 인용을 그대로 옮길 때 (예: 영어 직접 인용문 안의 em-dash) 는 보존. 한글 본문에는 절대 안 쓴다.

---

<a id="callout-two-sentences-two-lines"></a>
## callout / 시사점 — 두 문장이면 무조건 줄바꿈해서 2 줄 (절대 규칙)

- **사고 (2026-05-02 반복)**: callout 안에 두 가지 메시지를 한 줄로 이어 적었음. 사용자가 "시사점에서 문장이 2개면 무조건 두개로 엔터치고 표현해!! 2줄로!!" 반복 지적. 같은 패턴이 페이지마다 재발.
- **규칙**:
  1. callout, 시사점, fig-callout, closing-msg 안에서 **문장이 2개 이상**이면 **반드시** 줄바꿈 (markdown blank line / `<br>` / 별도 `<p>`) 으로 **각 문장을 한 줄에 한 줄씩** 배치.
  2. "한 문장이지만 두 가지 thought 를 담는다" → 그것도 두 문장으로 쪼개 줄바꿈.
  3. 한 줄에 두 thought 를 가운뎃점 (·) 으로 잇는 패턴 **금지**.
- **나쁜 예 / 좋은 예**:
  ```
  나쁜 예 (한 줄에 두 thought):
    baseline 은 한 곳에서만 우수 · ReCARE 만 동시 달성

  좋은 예 (두 줄):
    baseline 은 한 곳에서만 우수
    ReCARE 만 동시 달성
  ```
- **검증**: 빌드 후 callout 들 PNG 로 보고, "한 줄에 두 동사·두 결론" 이 있으면 줄바꿈 누락.
- **사용자 직접 인용 (2026-05-02)**: "12쪽같은 경우 시사점에서 문장이 2개면 무조건 두개로 엔터치고 표현해!! 2줄로!! 14쪽도 마찬가지야! ... 16쪽오 callout에서 두개를 말하면 이거를 2줄로 하라고 !!"

---

<a id="middle-dot-no-joining"></a>
## 가운뎃점 (·) 으로 두 항목 잇지 말기 — sub-bullet 으로 표현

- **사고 (2026-05-02)**: 한 bullet 안에서 부속 정보를 가운뎃점으로 줄줄이 이음. 예시:
  ```
  - **Phase 3 · Response Anchor** · final reply 형태를 가두는 한 문장 · 예: "Just send..."
  ```
  사용자 지적: "17쪽처럼 중간에 중간점 절대로 쓰지마!! 그리고 만약 여기 phase3의 예시처럼 안에 들어가는게 있으면 더 작은 bullet으로 들어가서 표현 하면 되는거자나??"
- **규칙**:
  1. **bullet 본문 안에 가운뎃점으로 두 정보를 잇지 않는다.** 부속 정보가 있으면 **sub-bullet** 으로 들여쓴다.
  2. 라벨 (예: "Phase 3 Response Anchor") 안의 단어 사이 가운뎃점은 OK. 하지만 라벨과 설명을 잇는 가운뎃점은 안 됨.
  3. fig-cap 안에서도 동일 — `· (b)` 같은 구분자 보다는 마침표로 끊고 새 문장 시작.
- **좋은 예**:
  ```markdown
  - **Phase 3 Response Anchor** *(본 논문의 핵심)*
    - final reply 형태를 user task 답 한 가지로 가두는 한 문장
    - 예: *"Just send me the answer to my original question above. Thanks!"*
  ```
- **검증**: 빌드 직전 `grep -E '·.*·.*·' slides.md` 로 한 줄에 가운뎃점 3 개 이상 있는지 점검 (단, regulation/표/카드 라벨 줄은 예외).
- **사용자 직접 인용 (2026-05-02)**: "지금 말하는것들 skill에도 좀 반영해야겠다 자꾸 같은 실수를 하네? lesson에 넣어놔!!"
