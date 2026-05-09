# Detect — 검수 봇이 자동으로 잡아내야 할 패턴

이 문서는 grep / PIL 으로 자동 검출 가능한 red flag 목록.

검수 봇은 **빌드 직전과 직후** 두 시점에 이 검사를 돌린다:

- 빌드 직전 (마크다운 grep)
- 빌드 직후 (PDF + page PNG PIL 검사)

---

## 1. 마크다운 grep 검사

### 1-1. 쌍따옴표 / 작은따옴표 (P1)

```bash
grep -nE '"|'\''' $DECK \
  | grep -vE '^\s*[0-9]+:.*(class=|style=|url\(|font-family|content:|footer:|src=|alt=|href=|@import)'
```

기각 사유: CommonMark emphasis flanking 규칙 충돌 + DAMI Lab 양식상 본문 따옴표 금지.

CSS 속성 안은 정상 (`class="..."` 등) → 두 번째 grep 으로 제외.

### 1-2. em-dash (P1)

```bash
grep -nE '—' $DECK
```

한글 응답에서 절대 금지. 대체: `,` `(` `)` 또는 문장 분리.

### 1-3. + 기호 항목 연결 (P1)

```bash
grep -nE '\s\+\s' $DECK | grep -v 'background:\|font-weight:\|font-size:\|calc('
```

본문에서 "X + Y + Z" 식으로 항목 연결한 경우. **공식 발표 자리에서는 모두 비공식.** 대체: 쉼표 `,`, "및", "와/과", 새 bullet.

```diff
- 공격 차단 + retained concepts 보존을 동시에
+ 공격 차단과 retained concepts 보존을 동시에 달성

- Subtriplet 분해 + Reconfession
+ Subtriplet 분해와 Reconfession
```

### 1-4. ~다 종결 (P1)

cell-summary, callout-impl body 등 양식상 명사형 종결이 정답인 영역에서 `~다.` 로 끝나는지 검사:

```bash
grep -nE '(다|함|음)\.</div>|(다|함)\.<' $DECK | head
```

대체: 명사형 종결 ("축 이동", "신종 공격면", "첫 사례", "공격면 확대").

### 1-5. 옛 callout 라벨 (P1)

```bash
grep -nE '시사점|Why it matters|연구 의미|implication' $DECK
```

전부 `✨ HIGHLIGHTS` 로 통일됨. 다른 라벨이 남아있으면 alert.

### 1-6. 본문 화살표 글리프 (P1)

```bash
grep -nE '→|➜' $DECK | grep -v 'class=\|::before\|::after\|content:\|---\|->'
```

`.flow-row` `.flow-box` 의 화살표는 CSS `::before`/`::after` 가 자동 생성. 본문 텍스트의 `→` 도 baseline 이슈로 사용 자제. 대체: 자연어 ("따라서", "다음으로", "→ 결과").

### 1-7. 중간점 과다 (P1)

**원칙: `·` 는 정말 최대한 쓰지 않는다.** 한 줄에 4개 이상이면 무조건 분리 후보. 산문 안 `·` 는 거의 항상 자연어 (쉼표, "와/과", "및", 새 bullet) 로 대체 가능.

```bash
grep -nE '·.*·.*·.*·' $DECK
```

추가로 산문 안 어떤 `·` 라도 다음 우선순위로 검토:

```bash
# 문장 안 항목 나열용 · (제거 후보)
grep -nE '[가-힣A-Za-z]+\s*·\s*[가-힣A-Za-z]+\s*·' $DECK
```

`·` 를 살려도 되는 곳 (제외):
- meta-bar 의 `<span>...· 날짜</span>` (출처 헤더)
- group-label / subtitle 등 짧은 디자인 라벨 (`Trustworthy AI · 7원칙` 류는 차라리 영어 sep 또는 콤마)
- enumeration 의도가 명확한 7원칙 같은 fixed list

### 1-7b. bullet 라벨 뒤 `·` (P1)

`- **라벨** ·` 또는 `- **라벨**,` 패턴은 본문 들어가는 분리자가 콜론(`:`)이어야 함:

```bash
grep -nE '^\s*-\s+\*\*[^*]+\*\*\s*[·,]' $DECK
```

대체: `: ` (콜론 + 공백). 콜론은 정의/설명 도입에 자연스러움.

```diff
- - **Finding 1** · 50개 prompt 의 exhaustive scan 결과
+ - **Finding 1**: 50개 prompt 의 exhaustive scan 결과

- - **Phase 1 User Authority Framing**, directive 를 user 음성으로 감싸
+ - **Phase 1 User Authority Framing**: directive 를 user 음성으로 감싸

- - **Jailbreaking** · LLM 이 학습한 안전 규칙 우회
+ - **Jailbreaking**: LLM 이 학습한 안전 규칙 우회
```

### 1-8. raw 인용 (P1)

본문에 `(저자, YYYY)` 패턴이 있는데 refs.toml `{{cite:키}}` 가 없는 경우:

```bash
grep -nE '\([A-Z][a-zA-Z]+( et al\.)?,\s*20[0-9]{2}\)' $DECK
```

대체: 본문 `[N]` + 하단 `<div class="refs">` + refs.toml 항목.

### 1-9. plain paragraph intro (P2)

h1 직후가 `## h2` 아닌 plain paragraph 인 경우 검출. 정규식으로는 어렵고 시각 검수에서 잡는 게 안전.

### 1-10. bullet 안 두 문장 연결 (P1)

한 bullet 안에 마침표 + 추가 문장이 들어간 경우. 한 bullet = 한 문장 원칙 위반:

```bash
grep -nE '^\s*-\s.*[가-힣A-Za-z][.]\s+[가-힣A-Z]' $DECK
```

대체: 마침표 자리에서 새 bullet 으로 분리, 또는 `:` / `,` 로 연결.

```diff
- - 한국은 2026년 1월부터 AI 기본법 시행. 미국·EU·UK·중국·일본도 같은 흐름
+ - 한국 2026년 1월 AI 기본법 시행
+ - 미국, EU, UK, 중국, 일본도 같은 흐름
```

### 1-11. desc/제목 가운데점 dense (P1)

`<strong>제목</strong> · 설명 · 추가설명` 같은 dense 가운데점 연결, h2/h3 에 `·` 포함:

```bash
grep -nE '<strong>[^<]+</strong>\s*·' $DECK
grep -nE '^##\s.*·' $DECK
grep -nE '^###\s.*·' $DECK
```

대체: `<strong>제목</strong>: 내용 (괄호 보조)` 또는 새 bullet. 제목에서는 쉼표/공백/자연어로.

```diff
- ## AgentDojo 949 trace · 5 defenses
+ ## AgentDojo 949 trace, 5 defenses 환경 평가

- <strong>EU AI Act 발효</strong> · 세계 최초 포괄적 AI 법 · high-risk 시험 의무 · 2026.08 적용
+ <strong>EU AI Act 발효</strong>: 세계 최초의 포괄적 AI 법, high-risk 시스템에 robustness 시험과 문서화, 인적 감독을 의무화 (2026.08 전면 적용)
```

### 1-12. 한글 `예:` (P1)

공식 발표 자리에서는 영어 축약 사용:

```bash
grep -nE '예:' $DECK
```

대체: `e.g.,` (한국어 본문이라도 학술 발표 톤에서는 영문 축약 우선).

### 1-13. 구어체 표현 (P1)

공식 자리에 어울리지 않는 구어/감각적 표현. lexicon 기반 검출:

```bash
grep -nE '견주는|버금가는|흔적\s*0|흔적이\s*0|티가\s*안|쪽팔|어림|껌|식은\s*죽' $DECK
```

대체:
- `oracle 과 견주는 수준` → `oracle 과 동등한 수준`
- `흔적 0` → `공격 흔적이 사용자 측에 드러나지 않음`
- `~ 식은 죽 먹기` → `~ 매우 용이`

### 1-14. 논문/방법 명칭 raw 등장 (P1)

공식 약어/방법 명칭(대문자+하이픈, 또는 대문자 알파벳 약어)이 본문에 처음 등장할 때 `[N]` 참조 없이 나오면 alert:

```bash
# 페이지별로 검사 — 약어 + 인접 [N] 없음
grep -nE '\b([A-Z]{2,}|[A-Z][a-zA-Z]*-[A-Za-z]+)\b' $DECK \
  | grep -vE '\[[0-9]+\]|class=|style=|<!--|src=|href=|EU|US|UK|AI|GPU|CPU|API|URL|PDF|PNG|JPG|HTML|CSS|JS'
```

대체: `(GCG [1], AttnGCG [2], I-GCG [3], GCG-Hij [4])` 형태 + refs.toml + 하단 `<div class="refs">`.

### 1-15b. CommonMark flanking 위반 — `**X**한글조사` (P0)

`**bold**` 닫는 `**` 가 한글 조사 (`을`, `를`, `이`, `가`, `의`, `에`, `으로`, `까지`, `한`, `는` 등) 에 직접 붙으면, CommonMark flanking 규칙상 닫히지 않고 `**` 가 본문에 그대로 렌더된다 (`****` 처럼 보임). italic `*X*` 도 동일.

```bash
# bold close 가 한글 직접 따라옴
grep -nP '\*\*[^*\s][^*]*[^*\s]\*\*[가-힣]' $DECK

# italic close 가 한글 직접 따라옴
grep -nP '(?<![*])\*[^*\s][^*]*[^*\s]\*(?!\*)[가-힣]' $DECK
```

**P0 승격 사유**: 양식이 깨지는 게 아니라 본문에 `**` 가 그대로 노출되어 슬라이드 자체가 망가진다. overflow 와 같은 등급.

대체 (3가지 중 택1):

1. 조사를 bold 안으로 포함 (선호):
   ```diff
   - **사용자도 모르는 부분**까지 학습됨
   + **사용자도 모르는 부분까지** 학습됨
   ```
2. HTML 태그로 우회:
   ```diff
   - **공격자에게는 더 정확한 평가**를 동시에 제공
   + <b>공격자에게는 더 정확한 평가를</b> 동시에 제공
   ```
3. 조사 앞 공백 삽입 (마지막 수단):
   ```diff
   - **suffix 한 곳만 가정**한 탓에
   + **suffix 한 곳만 가정** 한 탓에   ← 의미 어색
   ```

### 1-15. 신문 기사 source-link 누락 (P2)

`<div class="newspaper">` 또는 `clip` / `clip mini` variant 안에 `<div class="source-link">` 가 없으면 alert:

```python
import re
# 각 newspaper 블록 안에 source-link 가 있는지 검사
pattern = re.compile(r'<div class="newspaper[^"]*">(.*?)</div>\s*(?:<div class="cell-summary"|</div>)', re.S)
for m in pattern.finditer(content):
    if 'source-link' not in m.group(1):
        # alert: newspaper without source-link
        ...
```

기사 인용은 무조건 출처 링크 동반 (mini variant 포함, font-size 0.4em).

---

## 2. PDF / PNG PIL 검사

### 2-1. Overflow 검사 (P0)

```python
from PIL import Image
import os, glob

DARK_THRESH = 200
DARK_COUNT_THRESH = 1500   # 정상 footer+페이지번호 ~800

for png in sorted(glob.glob('pages/page-*.png')):
    im = Image.open(png).convert('L')
    w, h = im.size
    bottom = im.crop((0, h-50, w, h))
    pixels = list(bottom.getdata())
    dark = sum(1 for p in pixels if p < DARK_THRESH)
    if dark > DARK_COUNT_THRESH:
        print(f'OVERFLOW {os.path.basename(png)}: {dark}')
```

`-r 100` (1280x720 정도) 기준 임계값. DPI 변경 시 임계값도 조정.

### 2-2. 페이지 수 일치 (P0)

```bash
pdfinfo $DECK.pdf | grep '^Pages:'
ls pages/page-*.png | wc -l
```

두 값이 다르면 빌드 캐시 lag. 강제 재빌드 필요.

### 2-3. 페이지 번호 / footer 누락 (P0)

각 PNG 의 bottom-right 50x30 strip 에 dark pixel 이 거의 없으면 페이지 번호 누락 의심:

```python
br = im.crop((w-100, h-40, w, h))
dark_br = sum(1 for p in list(br.getdata()) if p < 200)
if dark_br < 30:
    print(f'PAGE NUMBER MISSING {png}')
```

### 2-4. 좌우 카드 height 불균형 (P2)

`.news-clip-grid` `.cols-2` 가 있는 페이지에서 좌우 column 의 white-space 분포가 크게 차이나면 제안.

벡터 분석 어려움 → 시각 검수에서 처리 권장.

---

## 3. 구조적 검사

### 3-1. 본문 슬라이드 첫 콘텐츠 검사 (P2)

각 슬라이드 (`---` 단위) 에서 h1 다음 첫 non-empty 라인이:

- `## ...` (h2) → OK
- `<!-- _class: ... -->` 만 → 클래스 페이지 (toc/section/title/end), 통과
- `<div class="..."> ` → 커스텀 레이아웃, 시각 검수에서 판단
- 일반 텍스트 / `- ...` / 표 → P2 alert ("plain paragraph intro" 또는 "no h2")

### 3-2. cell-summary 누락 (P2)

`<div class="newspaper">` 또는 `<div class="newspaper clip">` 다음에 같은 `<div class="clip-cell">` 안에서 `<div class="cell-summary">` 가 없으면 alert.

### 3-3. refs vs cite 번호 일치 (P1)

본문의 `[N]` 마커 개수 vs `<div class="refs">` 안의 `[N]` 항목 개수 비교.

```python
import re
markers = set(re.findall(r'(?<!\d)\[(\d+)\](?!\d)', content_body))
refs    = set(re.findall(r'^\[(\d+)\]\s+\{\{cite:', content_refs, re.M))
missing = markers - refs
extra   = refs - markers
```

---

## 4. 보고 형식

검수 봇은 결과를 다음 표로 보고:

```markdown
## 검수 결과 (자동 검사)

| Page | Severity | Category | Detail |
|------|----------|----------|--------|
| 4    | P1       | + 기호   | line 1947: "명시 + management 절차" |
| 7    | P1       | raw 인용 | line 2048: "(GCG, 2023)" → refs.toml |
| 14   | P0       | overflow | bottom 50px dark=2340 (>1500) |
| 28   | P2       | h2 누락  | h1 직후 plain paragraph |
```

승인 후 fix.md 의 처방에 따라 수정.
