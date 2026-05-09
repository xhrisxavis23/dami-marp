---
marp: true
theme: dami-lab
paginate: true
footer: 'DAMI Lab · Country Flags Component'
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@400;700;900&family=Noto+Serif+KR:wght@400;700;900&family=Merriweather:wght@400;700;900&display=swap');

/* =========================================================
   .flag — 원형 국기 디스크
   ========================================================= */
section .flag {
  display: inline-block;
  vertical-align: middle;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(0,0,0,0.06);
  flex-shrink: 0;
  background: #fff;
}
section .flag img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
section .flag.flag-xs { width: 20px; height: 20px; }
section .flag.flag-sm { width: 28px; height: 28px; }
section .flag           { width: 44px; height: 44px; }
section .flag.flag-lg   { width: 72px; height: 72px; }
section .flag.flag-xl   { width: 120px; height: 120px; }

/* 라벨 + 국기 한 묶음 */
section .flag-row {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
section .flag-row .label {
  font-family: Arial, sans-serif;
  font-size: 0.85em;
  letter-spacing: 0.02em;
  color: #1a1a1a;
}

/* 카탈로그 그리드 */
section .flag-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 18px 10px;
  justify-items: center;
  margin-top: 14px;
}
section .flag-grid .cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
section .flag-grid .cell .name {
  font-family: Arial, sans-serif;
  font-size: 0.55em;
  color: #333;
  letter-spacing: 0.03em;
}

/* 카드형 (큰 국기 + 텍스트) */
section .flag-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 12px;
}
section .flag-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 12px 14px;
  background: #f7f7f7;
  border-left: 3px solid #1a1a1a;
}
section .flag-card .flag-card-body {
  flex: 1;
}
section .flag-card .flag-card-title {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.95em;
  margin-bottom: 2px;
  color: #1a1a1a;
}
section .flag-card .flag-card-desc {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.68em;
  line-height: 1.5;
  color: #333;
}

/* 타임라인 (ask2026 5쪽 스타일) */
section .reg-timeline {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 10px;
}
section .reg-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  background: #f7f7f7;
  border-left: 3px solid #003478;
}
section .reg-item .reg-date {
  font-family: Arial, sans-serif;
  font-size: 0.7em;
  font-weight: 700;
  color: #1a1a1a;
  min-width: 64px;
  text-align: center;
  line-height: 1.2;
}
section .reg-item .reg-desc {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.65em;
  line-height: 1.5;
  color: #333;
  flex: 1;
}
section .reg-item .reg-desc strong {
  font-weight: 700;
  color: #1a1a1a;
}
</style>

# Country Flags Component
## G20 + EU 원형 국기 — 슬라이드 양념

- 사용 가능 코드 (20개): AR · AU · BR · CA · CN · DE · FR · GB · ID · IN · IT · JP · KR · MX · RU · SA · TR · US · ZA · EU
- 사이즈 클래스: `.flag-xs(20)` · `.flag-sm(28)` · `.flag(44)` · `.flag-lg(72)` · `.flag-xl(120)`
- 모든 국기는 `flags/<code>.svg` 에서 `<img>` 로 로드, `border-radius: 50%` 로 원형 디스크
- 본문 인라인부터 강조 카드, 카탈로그 그리드까지 같은 마크업 재사용

---

# 패턴 1 — 인라인 라벨 (작은 사이즈)

본문 흐름 안에서 국가를 살짝 표시하고 싶을 때.

- 한국 <span class="flag flag-xs"><img src="flags/kr.svg" alt=""></span> 은 2026년 1월 AI 기본법을 시행했고, 미국 <span class="flag flag-xs"><img src="flags/us.svg" alt=""></span> · 유럽연합 <span class="flag flag-xs"><img src="flags/eu.svg" alt=""></span> · 영국 <span class="flag flag-xs"><img src="flags/gb.svg" alt=""></span> 도 같은 흐름.
- 일본 <span class="flag flag-xs"><img src="flags/jp.svg" alt=""></span> 은 2025년 5월 AI 추진법, 중국 <span class="flag flag-xs"><img src="flags/cn.svg" alt=""></span> 은 2024년 9월 TC260 표준을 발표.

<br>

플래그 + 라벨 묶음 (`.flag-row`):

<div class="flag-row"><span class="flag flag-sm"><img src="flags/kr.svg" alt=""></span><span class="label">KOREA</span></div>　
<div class="flag-row"><span class="flag flag-sm"><img src="flags/us.svg" alt=""></span><span class="label">UNITED STATES</span></div>　
<div class="flag-row"><span class="flag flag-sm"><img src="flags/eu.svg" alt=""></span><span class="label">EUROPEAN UNION</span></div>　
<div class="flag-row"><span class="flag flag-sm"><img src="flags/jp.svg" alt=""></span><span class="label">JAPAN</span></div>

---

# 패턴 2 — 카드형 (큰 국기 + 설명)

각 국가의 핵심 사실 한 덩어리씩.

<div class="flag-cards">

<div class="flag-card">
<span class="flag flag-lg"><img src="flags/kr.svg" alt=""></span>
<div class="flag-card-body">
<div class="flag-card-title">대한민국 · AI 기본법</div>
<div class="flag-card-desc">2026년 1월 시행. 고영향 AI 사업자에 안전성 시험·위험관리 체계 의무 부여.</div>
</div>
</div>

<div class="flag-card">
<span class="flag flag-lg"><img src="flags/eu.svg" alt=""></span>
<div class="flag-card-body">
<div class="flag-card-title">EU · AI Act</div>
<div class="flag-card-desc">2024년 8월 발효, 2026년 8월 전면 적용. high-risk 시스템 robustness 시험·인적 감독 의무.</div>
</div>
</div>

<div class="flag-card">
<span class="flag flag-lg"><img src="flags/us.svg" alt=""></span>
<div class="flag-card-body">
<div class="flag-card-title">미국 · NIST AI RMF GenAI</div>
<div class="flag-card-desc">2024년 10월. 생성형 AI 13가지 위험 명시 + redteam·평가 가이드 표준화.</div>
</div>
</div>

<div class="flag-card">
<span class="flag flag-lg"><img src="flags/cn.svg" alt=""></span>
<div class="flag-card-body">
<div class="flag-card-title">중국 · TC260 표준</div>
<div class="flag-card-desc">2024년 9월 생성형 AI 보안 표준. 모델 등록·콘텐츠 라벨링·jailbreak 평가 의무.</div>
</div>
</div>

</div>

---

# 패턴 3 — 카탈로그 그리드 (G20 + EU 전체)

<div class="flag-grid">

<div class="cell"><span class="flag flag-lg"><img src="flags/ar.svg" alt=""></span><span class="name">ARGENTINA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/au.svg" alt=""></span><span class="name">AUSTRALIA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/br.svg" alt=""></span><span class="name">BRAZIL</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/ca.svg" alt=""></span><span class="name">CANADA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/cn.svg" alt=""></span><span class="name">CHINA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/fr.svg" alt=""></span><span class="name">FRANCE</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/de.svg" alt=""></span><span class="name">GERMANY</span></div>

<div class="cell"><span class="flag flag-lg"><img src="flags/in.svg" alt=""></span><span class="name">INDIA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/id.svg" alt=""></span><span class="name">INDONESIA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/it.svg" alt=""></span><span class="name">ITALY</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/jp.svg" alt=""></span><span class="name">JAPAN</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/mx.svg" alt=""></span><span class="name">MEXICO</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/ru.svg" alt=""></span><span class="name">RUSSIA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/sa.svg" alt=""></span><span class="name">SAUDI ARABIA</span></div>

<div class="cell"><span class="flag flag-lg"><img src="flags/za.svg" alt=""></span><span class="name">SOUTH AFRICA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/kr.svg" alt=""></span><span class="name">SOUTH KOREA</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/tr.svg" alt=""></span><span class="name">TURKEY</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/gb.svg" alt=""></span><span class="name">UNITED KINGDOM</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/us.svg" alt=""></span><span class="name">UNITED STATES</span></div>
<div class="cell"><span class="flag flag-lg"><img src="flags/eu.svg" alt=""></span><span class="name">EUROPEAN UNION</span></div>

</div>

---

# 패턴 4 — 규제 타임라인 (ask2026 5쪽 응용)

## 글로벌 AI 규제, 2024년 이후

<div class="reg-timeline">

<div class="reg-item">
<span class="flag"><img src="flags/eu.svg" alt=""></span>
<div class="reg-date">2024.08<br>EU</div>
<div class="reg-desc"><strong>EU AI Act 발효</strong> · high-risk 시스템 robustness 시험·인적 감독 의무. 2026.08 전면 적용.</div>
</div>

<div class="reg-item">
<span class="flag"><img src="flags/us.svg" alt=""></span>
<div class="reg-date">2024.10<br>USA</div>
<div class="reg-desc"><strong>NIST AI RMF GenAI Profile</strong> · 생성형 AI 13가지 위험 명시 + redteam 가이드 표준화.</div>
</div>

<div class="reg-item">
<span class="flag"><img src="flags/kr.svg" alt=""></span>
<div class="reg-date">2025.01<br>KOR</div>
<div class="reg-desc"><strong>한국 AI 기본법 통과</strong> · 고영향 AI 사업자 안전성 시험 의무. 2026.01 시행.</div>
</div>

<div class="reg-item">
<span class="flag"><img src="flags/gb.svg" alt=""></span>
<div class="reg-date">2025.06<br>UK</div>
<div class="reg-desc"><strong>AISI 평가 의무화</strong> · frontier model 출시 전 사전 평가 권고제 도입.</div>
</div>

<div class="reg-item">
<span class="flag"><img src="flags/cn.svg" alt=""></span>
<div class="reg-date">2024.09<br>CHN</div>
<div class="reg-desc"><strong>중국 TC260 표준</strong> · 모델 등록·콘텐츠 라벨링·jailbreak 평가 의무. GB/T 45654 (2025) 통합.</div>
</div>

<div class="reg-item">
<span class="flag"><img src="flags/jp.svg" alt=""></span>
<div class="reg-date">2025.05<br>JPN</div>
<div class="reg-desc"><strong>일본 AI 추진법</strong> · 보안·이용자 보호 의무 + AI 전략 본부 설치. 일본 최초 포괄 입법.</div>
</div>

</div>
