---
marp: true
theme: dami-lab
paginate: true
footer: 'DAMI Lab · Newspaper Component 목업 v3'
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;800;900&family=Old+Standard+TT:wght@400;700&family=Libre+Caslon+Text:wght@400;700&family=Merriweather:wght@400;700;900&family=EB+Garamond:wght@400;700;800&family=PT+Serif:wght@400;700&family=Nanum+Myeongjo:wght@400;700;800&family=Noto+Serif+KR:wght@400;700;900&family=Gowun+Batang:wght@400;700&family=Song+Myung&family=Hahmlet:wght@400;700;900&family=Diphylleia&display=swap');

/* =========================================================
   .font-sample — 신문 느낌 폰트 비교 카드
   ========================================================= */
section .font-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
  margin-top: 10px;
}
section .font-grid.kor { grid-template-columns: 1fr 1fr 1fr; }
section .font-sample {
  background: #f5f5f5;
  border: 1px solid #d4d4d4;
  padding: 10px 12px 12px;
  display: flex;
  flex-direction: column;
  color: #1a1a1a;
}
section .font-sample .top-bar {
  height: 3px;
  background: #1a1a1a;
  margin: -10px -12px 6px;
}
section .font-sample .label {
  font-size: 0.55em;
  color: #5a5a5a;
  font-family: Arial, sans-serif;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 4px;
}
section .font-sample .masthead {
  font-size: 1.45em;
  font-weight: 900;
  text-align: center;
  border-bottom: 1px solid #999;
  padding-bottom: 3px;
  line-height: 1.0;
}
section .font-sample .headline {
  font-size: 0.95em;
  font-weight: 800;
  line-height: 1.2;
  margin: 7px 0 4px;
  text-align: center;
}
section .font-sample .lede {
  font-size: 0.7em;
  line-height: 1.5;
  text-align: justify;
}
/* 영문 폰트 매핑 */
section .font-sample.f-times { font-family: 'Times New Roman', serif; }
section .font-sample.f-playfair { font-family: 'Playfair Display', serif; }
section .font-sample.f-oldstandard { font-family: 'Old Standard TT', serif; }
section .font-sample.f-libre { font-family: 'Libre Caslon Text', serif; }
section .font-sample.f-merriweather { font-family: 'Merriweather', serif; }
section .font-sample.f-garamond { font-family: 'EB Garamond', serif; }
section .font-sample.f-ptserif { font-family: 'PT Serif', serif; }
/* 한글 폰트 매핑 */
section .font-sample.f-nanum { font-family: 'Nanum Myeongjo', serif; }
section .font-sample.f-notoserif { font-family: 'Noto Serif KR', serif; }
section .font-sample.f-gowun { font-family: 'Gowun Batang', serif; }
section .font-sample.f-songmyung { font-family: 'Song Myung', serif; }
section .font-sample.f-hahmlet { font-family: 'Hahmlet', serif; }
section .font-sample.f-diphylleia { font-family: 'Diphylleia', serif; }

/* =========================================================
   .newspaper — 신문기사 양식 컴포넌트 (half-page v3)
   - 옅은 회색조 newsprint
   - 기본은 슬라이드의 약 절반 면적
   - 단일 컬럼, 사진은 있을 때만 (.has-photo)
   ========================================================= */
section .newspaper {
  background: #f5f5f5;
  color: #1a1a1a;
  border: 1px solid #d4d4d4;
  box-shadow: 0 2px 5px rgba(0,0,0,0.08);
  font-family: 'Noto Serif KR', 'Merriweather', serif;
  padding: 14px 18px 16px;
  display: flex;
  flex-direction: column;
}
/* 영문 기사 전용 — Merriweather */
section .newspaper.eng,
section .newspaper.eng .masthead,
section .newspaper.eng .headline,
section .newspaper.eng .body {
  font-family: 'Merriweather', 'Noto Serif KR', serif;
}
/* 헤드라인 + 제호는 Hahmlet (한글 기본) */
section .newspaper .masthead,
section .newspaper .headline {
  font-family: 'Hahmlet', 'Merriweather', serif;
}
/* 강조 하이라이트 */
section .newspaper mark {
  background: #fff3a3;
  color: #1a1a1a;
  padding: 0 3px;
  border-radius: 1px;
  font-weight: 600;
}
section .newspaper .top-bar {
  height: 4px;
  background: #1a1a1a;
  margin: -14px -18px 8px;
}
section .newspaper .masthead {
  text-align: center;
  font-family: 'Hahmlet', serif;
  font-weight: 900;
  font-size: 1.75em;
  letter-spacing: -0.015em;
  line-height: 1;
  border-bottom: 1px solid #999999;
  padding-bottom: 6px;
}
section .newspaper .meta-bar {
  display: flex;
  justify-content: space-between;
  font-size: 0.55em;
  color: #5a5a5a;
  border-bottom: 2px solid #1a1a1a;
  padding: 3px 2px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-family: Arial, sans-serif;
}
section .newspaper .headline {
  font-weight: 800;
  font-size: 1.15em;
  line-height: 1.22;
  text-align: center;
  margin: 10px 0 8px;
  letter-spacing: -0.005em;
}
section .newspaper .body {
  font-size: 0.82em;
  line-height: 1.55;
  text-align: justify;
  hyphens: auto;
}
section .newspaper .body::after {
  content: '';
  display: block;
  clear: both;
}
section .newspaper .body p { margin: 0 0 6px 0; }
/* ----- 출처 링크 (각 신문 하단 필수) ----- */
section .newspaper .source-link {
  margin-top: 8px;
  padding-top: 5px;
  border-top: 1px dashed #8c8c8c;
  font-size: 0.5em;
  color: #505050;
  font-family: 'D2Coding', 'IBM Plex Mono', monospace;
  word-break: break-all;
  line-height: 1.3;
}
section .newspaper .byline {
  font-size: 0.55em;
  color: #5a5a5a;
  margin-bottom: 5px;
  font-family: Arial, sans-serif;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

/* ----- 사진 (있을 때만) ----- */
section .newspaper .photo-frame {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
section .newspaper .photo-frame.left {
  float: left;
  width: 260px;
  margin: 1px 14px 6px 0;
}
section .newspaper .photo-frame.right {
  float: right;
  width: 260px;
  margin: 1px 0 6px 14px;
}
section .newspaper .photo {
  width: 100%;
  background: #ccc;
  overflow: hidden;
  border: 1px solid #b8b8b8;
}
section .newspaper .photo img {
  display: block;
  width: 100%;
  height: auto;
}
section .newspaper .photo-caption {
  font-size: 0.58em;
  color: #5a5a5a;
  font-style: italic;
  line-height: 1.35;
  font-family: Arial, sans-serif;
}

/* ----- 작은 클립 변형 ----- */
section .newspaper.clip {
  padding: 9px 12px 11px;
}
section .newspaper.clip .top-bar {
  margin: -9px -12px 6px;
  height: 3px;
}
section .newspaper.clip .masthead {
  font-size: 1em;
  padding-bottom: 3px;
}
section .newspaper.clip .meta-bar {
  font-size: 0.5em;
  padding: 2px 1px;
}
section .newspaper.clip .headline {
  font-size: 0.9em;
  margin: 6px 0 5px;
  text-align: left;
}
section .newspaper.clip .body {
  font-size: 0.7em;
  line-height: 1.5;
}
section .newspaper.clip .body p { margin: 0 0 4px 0; }
section .newspaper.clip .byline { font-size: 0.5em; margin-bottom: 3px; }
section .newspaper.clip .source-link { font-size: 0.45em; margin-top: 5px; padding-top: 3px; }
section .newspaper.clip .photo-frame.left,
section .newspaper.clip .photo-frame.right { width: 75px; margin: 0 8px 4px 0; }
section .newspaper.clip .photo-frame.right { margin: 0 0 4px 8px; }
section .newspaper.clip .photo-caption { font-size: 0.5em; }

/* ---------- 슬라이드 레이아웃 헬퍼 ---------- */
/* 신문이 슬라이드의 절반(좌/우) 차지 */
section .half-paper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  align-items: start;
  margin-top: 6px;
}
section .stack-clips {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
</style>

<!-- ============================================================ -->
<!-- 1. 표지 -->
<!-- ============================================================ -->

<!-- _class: title -->
<!-- _paginate: false -->

# Newspaper Component<br/>v3 — half-page 양식

<div class="author">
DAMI Lab<br/>marp-skill 실험
</div>

<div class="date">2026-05-02 · AI Security 기사</div>

---

<!-- ============================================================ -->
<!-- 2. Variant A — 한글 / 신문 좌측 절반 / 사진 없음 (기본형) -->
<!-- ============================================================ -->

# Variant A · 한글 · 좌측 절반 · 사진 없음 (기본형)

<div class="half-paper">

<div class="newspaper">
  <div class="top-bar"></div>
  <div class="masthead">지티티코리아</div>
  <div class="meta-bar">
    <span>gttkorea.com</span>
    <span>2026.04.24</span>
  </div>
  <div class="headline">프롬프트 인젝션, 기업 AI 운영의 치명적 취약점으로</div>
  <div class="body">
    <div class="byline">By 이향선 기자</div>
    <p>엣지스캔(Edgescan) 의 ‘2026 취약점 통계 보고서’ 가 프롬프트 인젝션을 <mark>내부 엔터프라이즈 시스템의 치명적·고위험 취약점 상위 10개</mark> 에 포함시켰다.</p>
    <p>보고서는 이 유형이 <mark>더 이상 이론적 위험이 아니라 실제 운영 시스템 평가에서 반복 확인되는 실전 위협</mark> 이라고 평가했다.</p>
    <p>대기업의 약 37%가 발견된 취약점을 1년 이상 방치하고 있으며, 시정 속도가 발견 속도를 따라가지 못한다고 지적했다.</p>
  </div>
  <div class="source-link">출처: gttkorea.com/news/articleView.html?idxno=25445</div>
</div>

<div>

## 본 연구의 사회적 맥락
- 프롬프트 인젝션이 **이론 → 실전** 위협으로 전환
- 보안 산업이 이미 **상위 10대 취약점** 으로 분류

## 본 연구의 기여
- 동작 환경에서 **재현 가능한 평가 프로토콜** 제안
- 기업 운영 환경에 적용 가능한 **다층 방어 평가표**

</div>
</div>

---

<!-- ============================================================ -->
<!-- 3. Variant B — English / 신문 우측 절반 / 사진 없음 -->
<!-- ============================================================ -->

# Variant B · English · 우측 절반 · 사진 없음

<div class="half-paper">

<div>

## Why this article matters
- IPI is no longer **theory**, but a real-world attack vector
- Both **Google** and **Forcepoint** have observed the same wild patterns

## Connection to our research
- Our threat model **directly maps** to the kill-chain documented here
- We extend their findings with a **reproducible evaluation harness**

</div>

<div class="newspaper eng">
  <div class="top-bar"></div>
  <div class="masthead">HELP NET SECURITY</div>
  <div class="meta-bar">
    <span>helpnetsecurity.com</span>
    <span>Apr 24, 2026</span>
  </div>
  <div class="headline">Indirect Prompt Injection Is Taking Hold in the Wild</div>
  <div class="body">
    <div class="byline">By Zeljka Zorz, Editor-in-Chief</div>
    <p>The open web is increasingly populated with hidden instructions designed to manipulate LLM-powered AI agents. <mark>Google and Forcepoint researchers documented real-world IPI embedded in web pages.</mark></p>
    <p>Common tactics: shrinking malicious text to a single pixel, draining its color to near-transparency, or simply tagging it as hidden via standard CSS — invisible to humans, executed by agents.</p>
    <p>Google reported a <mark>32% relative rise</mark> in malicious-category attempts between Nov 2025 and Feb 2026.</p>
  </div>
  <div class="source-link">Source: helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/</div>
</div>
</div>

---

<!-- ============================================================ -->
<!-- 4. Variant C — 한글 / 좌측 절반 / 사진 있음 (본문에 사진) -->
<!-- ============================================================ -->

# Variant C · 한글 · 좌측 절반 · 사진 있음

<div class="half-paper">

<div class="newspaper">
  <div class="top-bar"></div>
  <div class="masthead">지티티코리아</div>
  <div class="meta-bar">
    <span>gttkorea.com</span>
    <span>2026.04.24</span>
  </div>
  <div class="headline">프롬프트 인젝션, 기업 AI 운영의 치명적 취약점으로</div>
  <div class="body">
    <div class="byline">By 이향선 기자</div>
    <div class="photo-frame left">
      <div class="photo"><img src="articles/gtt_promptinj.jpg" alt="" /></div>
      <div class="photo-caption">엣지스캔 ‘2026 취약점 통계 보고서’ 발췌.</div>
    </div>
    <p>엣지스캔(Edgescan) 의 ‘2026 취약점 통계 보고서’ 가 프롬프트 인젝션을 내부 엔터프라이즈 시스템의 치명적·고위험 취약점 상위 10개에 포함시켰다.</p>
    <p>보고서는 이 유형이 더 이상 이론적 위험이 아니라 실제 운영 시스템 평가에서 반복 확인되는 실전 위협이라고 평가했다.</p>
    <p>대기업의 약 37%가 발견된 취약점을 1년 이상 방치하고 있다.</p>
  </div>
  <div class="source-link">출처: gttkorea.com/news/articleView.html?idxno=25445</div>
</div>

<div>

## 사진을 가져오는 경우
- 원 기사가 **시각 자료**(도식·인포그래픽) 를 핵심으로 쓸 때
- 단순 stock 이미지면 **굳이 안 가져옴**

## 이 기사의 경우
- 시각자료가 **분위기 일러스트** 라 우선순위 낮음
- 그래도 **시각적 임팩트** 가 필요한 슬라이드면 추가

</div>
</div>

---

<!-- ============================================================ -->
<!-- 5. Variant D — English / 우측 절반 / 사진 있음 (도식) -->
<!-- ============================================================ -->

# Variant D · English · 우측 절반 · 사진 있음 (도식)

<div class="half-paper">

<div>

## When to include the photo
- When the article ships a **diagram / kill-chain / data plot**
- When the slide is **explaining the figure itself**

## Here
- Help Net Security 의 IPI **5단계 kill chain** 도식
- 슬라이드 메인 메시지가 “**공격 흐름 설명**” 이라 사진 포함

</div>

<div class="newspaper eng">
  <div class="top-bar"></div>
  <div class="masthead">HELP NET SECURITY</div>
  <div class="meta-bar">
    <span>helpnetsecurity.com</span>
    <span>Apr 24, 2026</span>
  </div>
  <div class="headline">Indirect Prompt Injection Is Taking Hold in the Wild</div>
  <div class="body">
    <div class="byline">By Zeljka Zorz, Editor-in-Chief</div>
    <div class="photo-frame right">
      <div class="photo"><img src="articles/helpnet_ipi_killchain.webp" alt="" /></div>
      <div class="photo-caption">Reconstructed 5-step IPI kill chain.</div>
    </div>
    <p>Hidden instructions in web pages are quietly steering LLM-powered agents into data exfiltration. <mark>Researchers from Google and Forcepoint documented the kill chain end-to-end.</mark></p>
    <p>Tactics range from 1px hidden text to invisible CSS — invisible to humans, executed by agents. Google logged a <mark>32% rise</mark> between Nov 2025 and Feb 2026.</p>
  </div>
  <div class="source-link">Source: helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/</div>
</div>

</div>

---

<!-- ============================================================ -->
<!-- 6. Variant E — 한글 / 우측 절반 / 사진 없음 -->
<!-- ============================================================ -->

# Variant E · 한글 · 우측 절반 · 사진 없음

<div class="half-paper">

<div>

## OpenAI 자기 평가
- 단일 해법이 **없음** 을 공식 인정
- 다층 방어 + 폐쇄 루프 검증 = 현실 솔루션

## 본 연구의 위치
- 다층 방어 중 **평가/검증** 단계의 표준화
- “공격 비용 인상” 이라는 동일 프레임에 부합

</div>

<div class="newspaper">
  <div class="top-bar"></div>
  <div class="masthead">데일리시큐</div>
  <div class="meta-bar">
    <span>dailysecu.com</span>
    <span>2025.12.26</span>
  </div>
  <div class="headline">오픈AI “프롬프트 인젝션, 장기 보안 과제…단일 해법 없다”</div>
  <div class="body">
    <div class="byline">By 길민권 기자</div>
    <p>오픈AI 가 프롬프트 인젝션 공격을 <mark>“장기적인 보안 과제”</mark> 로 규정하며, <mark>완벽하게 해결됐다고 말할 수 있는 단일 해법은 없다</mark> 고 공식 입장을 밝혔다.</p>
    <p>회사는 모델 정렬만으로는 외부 콘텐츠에 숨겨진 악성 명령을 모두 막을 수 없다고 인정했다. 학습 데이터 보강 · 입력 분리 · 사용자 재확인 · 출력 후처리 등 네 단계의 방어를 결합해야 한다고 설명했다.</p>
    <p>전문가들은 “책임 있는 공급자가 한계를 솔직히 공개한 신호” 로 평가했다.</p>
  </div>
  <div class="source-link">출처: dailysecu.com/news/articleView.html?idxno=203808</div>
</div>

</div>

---

<!-- ============================================================ -->
<!-- 7. Variant F — 영문 / 좌측 절반 / 사진 있음 (사람 얼굴) -->
<!-- ============================================================ -->

# Variant F · English · 좌측 절반 · 사진 있음 (배너)

<div class="half-paper">

<div class="newspaper eng">
  <div class="top-bar"></div>
  <div class="masthead">BLEEPING COMPUTER</div>
  <div class="meta-bar">
    <span>bleepingcomputer.com</span>
    <span>Apr 27, 2026</span>
  </div>
  <div class="headline">Deepfake Voice Attacks Are Outpacing Defenses</div>
  <div class="body">
    <div class="byline">By Marshall Bennett, Adaptive Security</div>
    <div class="photo-frame right">
      <div class="photo"><img src="articles/bleeping_deepfake.jpg" alt="" /></div>
      <div class="photo-caption">“Three seconds of audio is enough.”</div>
    </div>
    <p>AI-generated voice clones are powering executive impersonation fraud at unprecedented scale. Voice deepfake incidents <mark>rose 680% year-over-year</mark> in 2025.</p>
    <p>The U.S. alone logged over 100,000 attacks, including a single <mark>$11 M fraud directly attributed to voice cloning</mark>. Out-of-band verification is becoming the practical baseline.</p>
  </div>
  <div class="source-link">Source: bleepingcomputer.com/news/security/deepfake-voice-attacks-are-outpacing-defenses</div>
</div>

<div>

## 본 연구와 인접한 위협
- 본 연구는 **텍스트 기반 IPI** 가 주제
- 음성 딥페이크는 **다른 modality** 의 같은 패턴

## 함의
- 단일 채널 방어는 **곧 무력화**
- 공통 결론: **out-of-band 검증** 의 필요성

</div>
</div>

---

<!-- ============================================================ -->
<!-- 8. Variant G — 작은 클립 두 개 비교 -->
<!-- ============================================================ -->

# Variant G · 작은 클립 두 개 비교

<div class="half-paper">

<div class="stack-clips">

<div class="newspaper clip">
  <div class="top-bar"></div>
  <div class="masthead">데일리시큐</div>
  <div class="meta-bar">
    <span>dailysecu.com</span>
    <span>2025.12.26</span>
  </div>
  <div class="headline">오픈AI “프롬프트 인젝션, 장기 보안 과제”</div>
  <div class="body">
    <p>오픈AI 가 프롬프트 인젝션을 “장기 보안 과제” 로 규정. 단일 해법 없이 다층 방어로 공격 비용을 올리는 접근이 현실적이라 강조했다.</p>
  </div>
  <div class="source-link">출처: dailysecu.com/news/articleView.html?idxno=203808</div>
</div>

<div class="newspaper clip eng">
  <div class="top-bar"></div>
  <div class="masthead">HELP NET SECURITY</div>
  <div class="meta-bar">
    <span>helpnetsecurity.com</span>
    <span>Apr 24, 2026</span>
  </div>
  <div class="headline">Indirect Prompt Injection Taking Hold in the Wild</div>
  <div class="body">
    <p>Google &amp; Forcepoint document IPI in real web pages: 1px hidden text, transparent CSS, hidden meta — invisible to humans, executed by agents. <mark>32% rise from late 2025.</mark></p>
  </div>
  <div class="source-link">Source: helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/</div>
</div>

</div>

<div>

## 비교 포인트
- **공급자 시각** (OpenAI) vs **관측 시각** (보안 리서치)
- 두 기사 모두 **다층 방어** 결론
- 본 연구가 **평가 프레임** 으로 이 흐름을 잇는다

## 작은 클립의 역할
- 개별 기사 자체는 부차적
- **공통 흐름** 을 짚는 시각자료로 기능

</div>
</div>

---

<!-- ============================================================ -->
<!-- 12. 영→한 번역 케이스 (masthead 영문 유지, 본문 한글) -->
<!-- ============================================================ -->

# Variant H · 영문 기사 → 한글 번역

<div class="half-paper">

<div class="newspaper">
  <div class="top-bar"></div>
  <div class="masthead">BLEEPING COMPUTER</div>
  <div class="meta-bar">
    <span>bleepingcomputer.com</span>
    <span>2026.04.27 · 한글 번역</span>
  </div>
  <div class="headline">딥페이크 음성 공격, 방어를 앞지르고 있다</div>
  <div class="body">
    <div class="byline">By Marshall Bennett · Adaptive Security</div>
    <p>AI 가 합성한 음성 클론이 임원을 사칭한 송금 사기를 <mark>전례 없는 규모</mark> 로 확대하고 있다. 음성 딥페이크 사고는 2025년에 <mark>전년 대비 680% 급증</mark> 했다.</p>
    <p>미국 한 곳에서만 10만 건 이상 공격이 보고됐으며, 그중 단일 사례로 <mark>1,100만 달러 사기</mark> 가 음성 클로닝에 직접적으로 귀속됐다. 음성·발신번호 만으로는 더 이상 신원을 검증할 수 없다.</p>
    <p>전문가들은 사전 약속 코드워드, 콜백 절차, 별도 채널을 통한 2차 승인 같은 <mark>out-of-band 검증</mark> 을 실무 표준으로 권고하고 있다.</p>
  </div>
  <div class="source-link">원문: bleepingcomputer.com/news/security/deepfake-voice-attacks-are-outpacing-defenses</div>
</div>

<div>

## 영→한 번역 규칙
- **신문사명 (masthead) 은 영문 유지** — 출처 식별
- **헤드라인·본문은 한글 번역** — 청중 가독성
- 메타바에 `한글 번역` 표시
- 출처 링크는 `원문:` 으로 prefix
- 폰트: 자동으로 Hahmlet (헤드) + Noto Serif KR (본문) 적용

## `<mark>` 하이라이트 사용처
- 핵심 수치 (`680% 급증`, `1,100만 달러`)
- 핵심 결론 (`out-of-band 검증`)
- 인용문 (큰따옴표 안 강조 어구)

</div>
</div>
