# Fix — 검출된 문제별 수정 처방

각 처방은 detect.md 의 카테고리에 1:1 대응.

---

## P0 — Overflow / 깨진 페이지

### Fix-P0-1. bottom overflow

**원인**: 콘텐츠가 footer (bottom 16px) 또는 페이지 번호 영역까지 침범.

**처방** (시도 순서):

1. 텍스트 축약 — bullet 1~2개 줄이기, 부연 문장 삭제
2. font-size 축소 — `.cell-summary { font-size: 0.78em }` 같은 페이지별 override
3. 박스 padding 축소 — `padding: 12px 14px` → `8px 12px`
4. variant 교체 — `.newspaper` → `.newspaper.clip` → `.newspaper.clip.mini`
5. 슬라이드 분할 — 마지막 수단

### Fix-P0-2. h1 양식 깨짐

**원인**: 페이지별 `section.<class>` CSS 가 base h1 의 padding-top 을 덮어쓰면서 h1 이 너무 위로 붙음.

**처방**: 해당 클래스의 `padding` 을 base 값 `30px 56px 56px 68px` 에 맞춤. h1 위 여백 (top:30px) 이 확보되어야 border-left·border-bottom 이 정상 표시됨.

### Fix-P0-4. CommonMark flanking 위반 (`****` 가 그대로 보임)

**원인**: `**bold**` 닫는 `**` 가 한글 조사 (`을`, `를`, `이`, `가`, `의`, `에`, `으로`, `까지`, `한`, `는` 등) 에 직접 붙으면 emphasis 가 닫히지 않고 `**` 가 본문에 그대로 노출. italic `*X*조사` 도 동일.

**처방** (선호 순서):

1. **조사를 emphasis 안으로 포함** (가장 자연스러움):
   ```diff
   - **사용자도 모르는 부분**까지 학습됨
   + **사용자도 모르는 부분까지** 학습됨

   - **suffix 한 곳만 가정**한 탓에
   + **suffix 한 곳만 가정한 탓**에
   ```

2. **HTML 태그로 우회** (의미 단위가 조사 앞에서 끝나는 게 자연스러울 때):
   ```diff
   - **공격자에게는 더 정확한 평가**를 동시에 제공
   + <b>공격자에게는 더 정확한 평가를</b> 동시에 제공

   - *내 옛날 이메일이랑 다닌 회사*까지 다 나오더라구요
   + <i>내 옛날 이메일이랑 다닌 회사까지</i> 다 나오더라구요
   ```

3. **조사 앞 공백 삽입** (마지막 수단, 의미 어색해질 수 있음):
   ```diff
   - **suffix 한 곳만 가정**한 탓에
   + **suffix 한 곳만 가정** 한 탓에
   ```

검출: detect.md 1-15b 의 grep -P 패턴. 발견 즉시 P0 (overflow 와 동급).

### Fix-P0-3. 페이지 수 불일치

**원인**: 빌드 캐시 lag. `python3 build.py` 가 실제로 재실행되지 않음.

**처방**: 강제 재빌드 + 페이지 PNG 재생성.

```bash
rm -f $DECK.pdf $DECK.built.md
python3 .claude/skills/marp/bin/build.py $DECK.md
rm -rf pages && mkdir pages && pdftoppm -r 100 $DECK.pdf pages/page -png
```

---

## P1 — 양식 불일치

### Fix-P1-1. 쌍따옴표 / 작은따옴표

```diff
- **"어디서 믿고, 어디서 의심할지"**를 가르친다
+ **어디서 믿고, 어디서 의심할지**를 가르친다

- "Sure, here is..." 협조 토큰
+ 협조 토큰
```

인용 느낌이 꼭 필요하면 `「...」` `『...』` 또는 blockquote (`>`).

### Fix-P1-2. em-dash

```diff
- AI 의 신뢰성은 학술적 화두가 아니다 — 법정과 규제의 영역
+ AI 의 신뢰성은 학술적 화두가 아니라 법정과 규제의 영역
+ AI 의 신뢰성은 학술적 화두가 아니다. 법정과 규제의 영역이다
+ AI 의 신뢰성 (학술적 화두) 이 아니라 법정과 규제의 영역
```

### Fix-P1-3. + 기호

```diff
- 학습 데이터 관리 + 안전성 시험
+ 학습 데이터 관리, 안전성 시험
+ 학습 데이터 관리 및 안전성 시험
```

### Fix-P1-4. ~다 종결

cell-summary / callout-impl body 에서 명사형 종결로 전환:

```diff
- <div class="cell-summary">법적 비용으로 환산되기 시작했다</div>
+ <div class="cell-summary">법적 비용으로 환산되는 신호</div>

- 학술 주제에서 GDPR 의 법적 요구로 격상되었다
+ 학술 주제에서 GDPR 의 법적 요구로 격상

- 신종 공격면이 되고 있다
+ 신종 공격면
```

### Fix-P1-5. callout 라벨 통일

```diff
- ::before { content: "💡 시사점"; }
+ ::before { content: "✨ HIGHLIGHTS "; font-family: Merriweather; text-transform: uppercase; }
```

본문에서 `<span class="cs-label">Why it matters</span>` 같은 inline 라벨도 모두 제거.

### Fix-P1-6. 화살표 글리프

```diff
- <div class="flow-arrow">→</div>
+ (삭제, ::before/::after 자동 생성)

- 모델은 거부 → 협조 로 전환
+ 모델은 거부 대신 협조 토큰을 선택
+ 모델은 거부에서 협조로 전환
```

### Fix-P1-7. raw 인용 → refs.toml

1. refs.toml 에 항목 추가 (없으면):
   ```toml
   [zou2023gcg]
   authors = "Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M."
   title = "Universal and transferable adversarial attacks on aligned language models"
   venue = "arXiv preprint arXiv:2307.15043"
   year = 2023
   ```

2. 본문에서 raw → `[N]`:
   ```diff
   - 대표적 기법 (GCG, 2023)
   + 대표적 기법 [1]
   ```

3. 슬라이드 하단에 refs 블록:
   ```markdown
   <div class="refs">

   [1] {{cite:zou2023gcg}}

   </div>
   ```

   - 빈 줄 필수 (마크다운 렌더 규칙)
   - 인용이 많으면 마지막 슬라이드 앞에 References 통합 페이지

### Fix-P1-8. refs 번호 불일치

본문 `[N]` 와 `<div class="refs">` 의 `[N]` 가 다르면:

- 덱 전체에서 1부터 전역 번호 부여
- 동일 논문 재인용 시 같은 번호 재사용
- 작성 중에는 임시 `[1]` → 완성 직전에 일괄 리넘버링

### Fix-P1-9. bullet 안 두 문장 분리

한 bullet = 한 문장. 마침표로 두 문장을 한 bullet 에 욱여넣지 말 것.

```diff
- - 한국은 2026년 1월부터 AI 기본법 시행. 미국·EU·UK·중국·일본도 같은 흐름
+ - 한국 2026년 1월 AI 기본법 시행
+ - 미국, EU, UK, 중국, 일본도 같은 흐름

- - 모델은 거부 토큰을 생성한다. 그러나 GCG 는 협조 토큰을 강제한다
+ - 정상 모델은 거부 토큰을 생성
+ - GCG 는 협조 토큰을 강제
```

### Fix-P1-10. 가운데점 dense → 콜론/괄호

`<strong>제목</strong> · 항목 · 항목 · 항목` 패턴은 모두 `:` + 쉼표 + 괄호 보조로 재작성.

```diff
- <strong>EU AI Act 발효</strong> · 세계 최초 포괄적 AI 법 · high-risk 시험 의무 · 2026.08 적용
+ <strong>EU AI Act 발효</strong>: 세계 최초의 포괄적 AI 법, high-risk 시스템에 robustness 시험과 문서화, 인적 감독을 의무화 (2026.08 전면 적용)
```

h2/h3 제목에 들어간 `·` 도 모두 제거:

```diff
- ## AgentDojo 949 trace · 5 defenses
+ ## AgentDojo 949 trace, 5 defenses 환경 평가

- ## TOFU / CLEAR / RWKU × GA · GD · NPO · RT
+ ## TOFU, CLEAR, RWKU × GA, GD, NPO, RT

- ## RATIO = Defense · Utility · CARE 종합
+ ## RATIO 는 Defense, Utility, CARE 종합 지표
```

### Fix-P1-11. 한글 `예:` → `e.g.,`

학술 발표 톤에서는 영문 축약 우선:

```diff
- 예: 사용자가 "이 PDF 요약해줘" 라고 입력
+ e.g., 사용자가 「이 PDF 요약해줘」 라고 입력
```

### Fix-P1-12. 구어체 → 공식 어조

공식 자리에 어울리지 않는 감각/구어 표현은 정량/객관 표현으로:

```diff
- oracle 과 견주는 수준
+ oracle 과 동등한 수준

- 흔적 0
+ 공격 흔적이 사용자 측에 드러나지 않음

- 그림체·캐릭터를 통째로 베껴 그린다
+ 그림체와 캐릭터를 통째로 모방하는 현상
```

### Fix-P1-13. 논문/방법 명칭 → 인용 강제

raw 약어/방법 명칭은 첫 등장 시 무조건 `[N]` 참조 + refs.toml 항목 + 하단 `<div class="refs">`.

```diff
- (AttnGCG, I-GCG, GCG-Hij 등)
+ (AttnGCG [2], I-GCG [3], GCG-Hij [4])
```

refs.toml:
```toml
[jia2024igcg]
authors = "Jia, X., Pang, T., Du, C., Huang, Y., Gu, J., Liu, Y., Cao, X., & Lin, M."
title = "Improved techniques for optimization-based jailbreaking on large language models"
venue = "arXiv preprint arXiv:2405.21018"
year = 2024
```

`+` 기호로 항목 연결한 경우도 `,` / `와`/`과` / `및` / 새 bullet 으로 모두 전환 (Fix-P1-3 의 강화판).

---

## P2 — 가독성 / 정합성

### Fix-P2-1. plain paragraph intro

```diff
  # 슬라이드 제목

- 본 페이지에서는 5단계 파이프라인을 설명한다.
+ ## 개요
+
+ - 핵심 명제 1
+ - 핵심 명제 2
+ - 핵심 명제 3
```

h2 는 `## 정의 / ## 개요 / ## 구조 / ## 상황 / ## 역할 / ## 컨셉 / ## 매핑` 같은 short header.

### Fix-P2-2. cell-summary 누락

newspaper-clip 패턴은 항상 cell-summary 동반:

```html
<div class="clip-cell">
  <div class="newspaper clip">...</div>
  <div class="cell-summary">한 줄 요약 (명사형 종결)</div>
</div>
```

### Fix-P2-3. 좌우 카드 height 불균형

```diff
- <div class="news-clip-grid">
+ <div class="news-clip-grid eq">
```

또는 짧은 쪽 본문을 늘려 동률.

### Fix-P2-4. 3-col 신문 grid overflow

```diff
- <div class="newspaper clip">
+ <div class="newspaper clip mini">
```

`.mini` variant 는 padding/font 가 더 작음. 단 `.source-link` 는 자동 hide.

### Fix-P2-5. flag / icon 분리됨

```html
<div class="reg-item eu">
  <div class="lhead">
    <span class="flag"><img src="assets/flags/eu.svg"/></span>
    <div class="date">2024.08<br>EU</div>
  </div>
  <div class="desc"><strong>EU AI Act</strong> · ...</div>
</div>
```

flag + date 를 `.lhead` 로 묶고, desc 를 같은 border-radius wrap 안에 둠.

### Fix-P2-6. figure 가 너무 작음

w:680 이 작아 보이면 w:880, w:1020, w:1100 까지 차례로 시도. 매번 overflow 검사 동반.

### Fix-P2-7a. 신문 기사 source-link 누락

`.newspaper` / `.newspaper.clip` / `.newspaper.clip.mini` 모든 variant 에 `<div class="source-link">` 동반 필수. 출처 없이 신문 카드만 두는 것은 금지.

```html
<div class="newspaper clip mini">
  <div class="kicker">Tech</div>
  <div class="headline">EU AI Act enters into force</div>
  <div class="lede">High-risk systems must undergo robustness testing...</div>
  <div class="source-link">euronews.com/2024/08/01/eu-ai-act</div>
</div>
```

mini variant 는 별도 CSS override (font-size 0.4em) 적용:

```css
section .newspaper.clip.mini .source-link {
  font-size: 0.4em;
  margin-top: 3px;
  padding-top: 2px;
  color: #6e7785;
  border-top: 1px solid #e6e8ec;
  word-break: break-all;
}
```

### Fix-P1-14. bullet 라벨 뒤 `·` / `,` → `:`

`- **라벨** ·` 또는 `- **라벨**,` 패턴은 정의/설명 도입이므로 콜론(`:`)이 자연스러움. 콜론은 `·` 와 달리 의미가 명확 (정의 / 풀이 / e.g.) 하고, 한 슬라이드 안 `·` 총량을 줄여준다.

```diff
- - **Finding 1** · 50개 prompt 의 exhaustive scan 결과
+ - **Finding 1**: 50개 prompt 의 exhaustive scan 결과

- - **Phase 1 User Authority Framing**, directive 를 user 음성으로 감싸
+ - **Phase 1 User Authority Framing**: directive 를 user 음성으로 감싸

- - **Jailbreaking** · LLM 이 학습한 안전 규칙 우회
+ - **Jailbreaking**: LLM 이 학습한 안전 규칙 우회
```

본문 산문 안 항목 나열 `·` 도 함께 점검:

```diff
- 모델이 실제로 기억한 것은 훨씬 더 많음 · 이메일·집주소·전 직장·지인 이름·학력 등
+ 모델이 실제로 기억한 것은 훨씬 더 많음. 이메일, 집주소, 전 직장, 지인 이름, 학력 등
```

### Fix-P2-7. 중간점 과다

```diff
- 모델 등록·콘텐츠 라벨링·jailbreak 평가·redteam 의무·국가 표준 통합
+ 모델 등록 · 콘텐츠 라벨링 · jailbreak 평가 의무
+ - 국가 표준 GB/T 45654 (2025) 로 통합
+ - redteam 평가 가이드 갱신
```

---

## 일반 원칙

1. **fix 는 항상 사용자 승인 후**. 봇이 자동 적용 금지.
2. **한 번에 한 카테고리**. P0 모두 해결 → P1 → P2 순서.
3. **변경 후 재빌드 + 재검수**. 한 fix 가 다른 페이지 overflow 를 유발할 수 있음.
4. **CSS override 는 페이지 단위**. theme CSS 수정은 전체 영향 — 매우 신중하게.

---

## 빌드 후 검증 명령

```bash
# 빌드 + 페이지 렌더 + 자동 검사
python3 .claude/skills/marp/bin/build.py $DECK.md \
  && rm -rf pages && mkdir pages \
  && pdftoppm -r 100 $DECK.pdf pages/page -png \
  && python3 detect.py    # PIL overflow + grep 자동 검사
```
