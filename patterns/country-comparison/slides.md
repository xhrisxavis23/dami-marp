---
marp: true
theme: dami-lab
paginate: true
footer: 'DAMI Lab · AI 보안 정책 5개국 비교 (2024-2026)'
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700;900&display=swap');

section .flag {
  display: inline-block;
  vertical-align: middle;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(0,0,0,0.06);
  flex-shrink: 0;
  background: #fff;
  width: 44px;
  height: 44px;
}
section .flag img { width: 100%; height: 100%; object-fit: cover; display: block; }
section .flag.flag-lg { width: 72px; height: 72px; }
section .flag.flag-xl { width: 100px; height: 100px; }

/* Slide 1 — 5개국 한 줄 그리드 */
section .country-bar {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  margin-top: 18px;
}
section .country-bar .col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
  padding: 14px 10px;
  background: #f7f7f7;
  border-top: 3px solid #003478;
}
section .country-bar .col .name {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.78em;
  color: #1a1a1a;
}
section .country-bar .col .law {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.62em;
  color: #003478;
  line-height: 1.3;
}
section .country-bar .col .date {
  font-family: Arial, sans-serif;
  font-size: 0.55em;
  color: #666;
  letter-spacing: 0.04em;
}
section .country-bar .col .key {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.6em;
  color: #333;
  line-height: 1.45;
  margin-top: 4px;
}

/* Slide 2 — 카드 그리드 */
section .policy-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 10px;
}
section .policy-cards .card-wide { grid-column: 1 / span 2; }
section .policy-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 12px 16px;
  background: #f7f7f7;
  border-left: 3px solid #003478;
}
section .policy-card .body { flex: 1; }
section .policy-card .title {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.85em;
  color: #1a1a1a;
  margin-bottom: 3px;
}
section .policy-card .title .stamp {
  font-family: Arial, sans-serif;
  font-size: 0.7em;
  font-weight: 400;
  color: #666;
  margin-left: 8px;
  letter-spacing: 0.03em;
}
section .policy-card .desc {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.62em;
  line-height: 1.55;
  color: #333;
}
section .policy-card .desc strong { font-weight: 700; color: #003478; }

/* Slide 3 — 타임라인 */
section .timeline {
  position: relative;
  margin-top: 24px;
  padding-left: 0;
}
section .timeline .axis {
  position: absolute;
  top: 50px;
  left: 0;
  right: 0;
  height: 2px;
  background: #1a1a1a;
}
section .timeline .events {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0;
  position: relative;
}
section .timeline .event {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  padding-top: 0;
}
section .timeline .event .date {
  font-family: Arial, sans-serif;
  font-weight: 700;
  font-size: 0.7em;
  color: #1a1a1a;
  margin-bottom: 6px;
}
section .timeline .event .flag {
  margin-bottom: 4px;
  z-index: 2;
  border: 3px solid #fff;
}
section .timeline .event .label {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.7em;
  color: #003478;
  margin-top: 8px;
  text-align: center;
  line-height: 1.3;
}
section .timeline .event .note {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.55em;
  color: #444;
  text-align: center;
  margin-top: 4px;
  line-height: 1.45;
  max-width: 200px;
}

/* Slide 4 — 비교표 */
section table.compare {
  width: 100%;
  border-collapse: collapse;
  margin-top: 14px;
  font-family: 'Noto Serif KR', serif;
  font-size: 0.62em;
}
section table.compare th,
section table.compare td {
  border: 1px solid #d4d4d4;
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
  line-height: 1.5;
}
section table.compare th {
  background: #003478;
  color: #fff;
  font-weight: 700;
  text-align: center;
}
section table.compare td.country {
  text-align: center;
  background: #f7f7f7;
  font-weight: 700;
  white-space: nowrap;
}
section table.compare td.country .flag {
  width: 32px;
  height: 32px;
  margin-bottom: 4px;
}
section table.compare td .tag {
  display: inline-block;
  padding: 1px 6px;
  background: #fff3a3;
  font-size: 0.9em;
  font-weight: 700;
  margin-right: 3px;
}
section table.compare td .tag.law { background: #fee; color: #a00; }
section table.compare td .tag.vol { background: #e8f0fe; color: #0050b3; }
</style>

# AI 보안 정책, 주요 5개국 비교
## 2024–2026 흐름 한눈에

<div class="country-bar">

<div class="col">
<span class="flag flag-lg"><img src="flags/eu.svg" alt=""></span>
<div class="name">EU</div>
<div class="law">AI Act</div>
<div class="date">2026.08 적용</div>
<div class="key">세계 최초 포괄 입법<br>high-risk 강제</div>
</div>

<div class="col">
<span class="flag flag-lg"><img src="flags/us.svg" alt=""></span>
<div class="name">USA</div>
<div class="law">NIST AI 600-1</div>
<div class="date">2024.07 발표</div>
<div class="key">12개 위험 분류<br>자발적 가이드</div>
</div>

<div class="col">
<span class="flag flag-lg"><img src="flags/cn.svg" alt=""></span>
<div class="name">CHINA</div>
<div class="law">GB/T 45654</div>
<div class="date">2025.11 시행</div>
<div class="key">생성형 AI 보안<br>국가 표준 의무</div>
</div>

<div class="col">
<span class="flag flag-lg"><img src="flags/gb.svg" alt=""></span>
<div class="name">UK</div>
<div class="law">AISI 평가 체계</div>
<div class="date">2023.11–</div>
<div class="key">정부 평가 기관<br>자발적 약속</div>
</div>

<div class="col">
<span class="flag flag-lg"><img src="flags/kr.svg" alt=""></span>
<div class="name">KOREA</div>
<div class="law">AI 기본법</div>
<div class="date">2026.01 시행</div>
<div class="key">고영향 AI 의무<br>안전성 시험</div>
</div>

</div>

- **법적 강제 (EU·중국·한국)** 와 **자발적 가이드 (미국·영국)** 로 두 갈래
- 모두 **2024년 이후 1년 반 사이에 집중 발효**, 글로벌 동시 흐름

---

# 국가별 핵심 정책 요약

<div class="policy-cards">

<div class="policy-card">
<span class="flag flag-lg"><img src="flags/eu.svg" alt=""></span>
<div class="body">
<div class="title">EU AI Act <span class="stamp">2024.08 발효 / 2026.08.02 high-risk 적용</span></div>
<div class="desc"><strong>세계 최초의 포괄적 AI 법.</strong> 위험 기반 4단계 분류. high-risk 시스템(채용·신용·교육·법집행 등 Annex III)에 risk management, data governance, 기술 문서, 자동 로깅, 인적 감독, accuracy·robustness·cybersecurity 보장 의무. 위반 시 1500만 유로 또는 글로벌 매출 3% 과징금.</div>
</div>
</div>

<div class="policy-card">
<span class="flag flag-lg"><img src="flags/us.svg" alt=""></span>
<div class="body">
<div class="title">미국 NIST AI 600-1 (GenAI Profile) <span class="stamp">2024.07.26 발표</span></div>
<div class="desc"><strong>생성형 AI 12개 고유 위험 카테고리 표준화.</strong> CBRN 정보, confabulation, 데이터 프라이버시, 정보 보안, value chain 등. AI RMF 4 함수(Govern·Map·Measure·Manage)에 매핑. EO 14110 후속. <strong>자발적 채택</strong>이지만 연방 조달·redteam 가이드 사실상 표준.</div>
</div>
</div>

<div class="policy-card">
<span class="flag flag-lg"><img src="flags/cn.svg" alt=""></span>
<div class="body">
<div class="title">중국 GB/T 45654-2025 <span class="stamp">2025.11.01 시행</span></div>
<div class="desc"><strong>TC260 발행 생성형 AI 서비스 보안 국가 표준.</strong> training data security + model security + 운영 보안 조치를 통합. 모델 등록·콘텐츠 라벨링·jailbreak 평가 의무 + 유해 입력 반복 시 서비스 중단 요건. 강제 표준에 가까운 국가 인증 체계.</div>
</div>
</div>

<div class="policy-card">
<span class="flag flag-lg"><img src="flags/gb.svg" alt=""></span>
<div class="body">
<div class="title">영국 AI Security Institute (AISI) <span class="stamp">2023.11 설립, 2025 본격 운영</span></div>
<div class="desc"><strong>정부 직속 frontier 모델 평가 기관.</strong> 30개 이상 첨단 모델 사전 평가 (사이버·CBRN·자율 능력). Seoul Summit (2024.05)에서 20개사 Frontier AI Safety Commitments 서명. <strong>법적 강제 X</strong>, 평가·공개를 통한 산업 규율.</div>
</div>
</div>

<div class="policy-card card-wide">
<span class="flag flag-lg"><img src="flags/kr.svg" alt=""></span>
<div class="body">
<div class="title">한국 AI 기본법 <span class="stamp">2026.01.22 시행 (세계 최초 전면 적용)</span></div>
<div class="desc">정식 명칭 "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법". <strong>고영향 AI</strong> (생명·신체·기본권에 중대한 영향) 사업자에 위험식별·분석·평가·처리 정책 + 조직 체계 + 결정 기록 5년 보관 의무. <strong>대규모 AI</strong> (10²⁶ FLOPs 이상) 별도 안전성 의무. 과태료 부과는 2027년 이후 예상, 시행령 정비 중.</div>
</div>
</div>

</div>

---

# 발효 타임라인 — 2023 ~ 2026

<div class="timeline">
<div class="axis"></div>
<div class="events">

<div class="event">
<div class="date">2023.11</div>
<span class="flag"><img src="flags/gb.svg" alt=""></span>
<div class="label">UK<br>AISI 설립</div>
<div class="note">Bletchley Summit, frontier 모델 평가 개시</div>
</div>

<div class="event">
<div class="date">2024.07</div>
<span class="flag"><img src="flags/us.svg" alt=""></span>
<div class="label">USA<br>NIST 600-1</div>
<div class="note">GenAI 12개 위험 표준</div>
</div>

<div class="event">
<div class="date">2024.08</div>
<span class="flag"><img src="flags/eu.svg" alt=""></span>
<div class="label">EU<br>AI Act 발효</div>
<div class="note">Annex III 적용은 2026.08</div>
</div>

<div class="event">
<div class="date">2025.11</div>
<span class="flag"><img src="flags/cn.svg" alt=""></span>
<div class="label">CHINA<br>GB/T 45654</div>
<div class="note">생성형 AI 국가 표준 시행</div>
</div>

<div class="event">
<div class="date">2026.01</div>
<span class="flag"><img src="flags/kr.svg" alt=""></span>
<div class="label">KOREA<br>AI 기본법</div>
<div class="note">고영향 AI 의무 발효</div>
</div>

</div>
</div>

- **법적 강제 (EU · 중국 · 한국)** vs **자발적 가이드 (미국 · 영국)** 의 두 트랙이 동시 진행
- 18개월 사이에 5대국 모두 AI 보안 골격 구축 완료, **2026.08 EU 전면 적용**이 다음 분수령

---

# 강제력 · 적용 범위 · 핵심 의무 비교

<table class="compare">
<thead>
<tr>
<th style="width: 11%">국가</th>
<th style="width: 13%">법·표준</th>
<th style="width: 11%">강제력</th>
<th style="width: 18%">적용 대상</th>
<th>핵심 의무</th>
</tr>
</thead>
<tbody>
<tr>
<td class="country"><span class="flag"><img src="flags/eu.svg" alt=""></span><br>EU</td>
<td>AI Act</td>
<td><span class="tag law">법적 강제</span></td>
<td>high-risk 시스템 (채용·신용·교육·법집행 등)</td>
<td>위험관리, 데이터 거버넌스, 기술 문서, 자동 로깅, 인적 감독, robustness·cybersecurity. 위반 시 €15M 또는 매출 3%</td>
</tr>
<tr>
<td class="country"><span class="flag"><img src="flags/us.svg" alt=""></span><br>USA</td>
<td>NIST AI 600-1</td>
<td><span class="tag vol">자발적</span></td>
<td>생성형 AI 개발·배포 조직</td>
<td>12개 위험 카테고리 mapping + Govern·Map·Measure·Manage 4 함수 적용. 연방 조달 사실상 표준</td>
</tr>
<tr>
<td class="country"><span class="flag"><img src="flags/cn.svg" alt=""></span><br>중국</td>
<td>GB/T 45654-2025</td>
<td><span class="tag law">국가 표준</span></td>
<td>대중에게 제공되는 생성형 AI 서비스</td>
<td>학습 데이터 보안, 모델 보안, 콘텐츠 라벨링, 모델 등록, jailbreak 평가, 유해 입력 반복 시 서비스 중단</td>
</tr>
<tr>
<td class="country"><span class="flag"><img src="flags/gb.svg" alt=""></span><br>영국</td>
<td>AISI 평가</td>
<td><span class="tag vol">자발적</span></td>
<td>frontier 모델 (대형 LLM 등)</td>
<td>출시 전 사전 평가 권고, Frontier AI Safety Commitments (20개사 서명), 사이버·CBRN·자율 능력 정량 측정</td>
</tr>
<tr>
<td class="country"><span class="flag"><img src="flags/kr.svg" alt=""></span><br>한국</td>
<td>AI 기본법</td>
<td><span class="tag law">법적 강제</span></td>
<td>고영향 AI + 대규모 AI (10²⁶ FLOPs↑)</td>
<td>위험식별·분석·평가·처리 정책, 결과 설명 방안, 결정 기록 5년 보관, 안전성 확보 조치 이행</td>
</tr>
</tbody>
</table>

- **공통점**: 모두 **risk-based** 접근 (모든 AI가 아닌 **위험 큰 시스템에 집중**)
- **차이점**: EU·중국은 **사전 의무**, 한국은 **사후 기록·설명**, 미국·영국은 **공개와 자율**에 의존
