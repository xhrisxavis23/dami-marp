---
marp: true
theme: dami-lab
paginate: true
footer: 'marp skill · conference-logos pattern'
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Serif+KR:wght@400;700;900&display=swap');

/* =========================================================
   .conf — 둥근 사각형 학회 로고
   ========================================================= */
section .conf {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  line-height: 0;
}
section .conf img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 8px;
}
section .conf.conf-xs { width: 28px; height: 28px; }
section .conf.conf-sm { width: 40px; height: 40px; }
section .conf           { width: 56px; height: 56px; }
section .conf.conf-lg   { width: 88px; height: 88px; }
section .conf.conf-xl   { width: 140px; height: 140px; }

/* xs/sm 사이즈에서는 둥근 정도 줄이기 */
section .conf.conf-xs img,
section .conf.conf-sm img { border-radius: 5px; }

/* 로고 + 연도 한 묶음 (badge) */
section .conf-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}
section .conf-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px 4px 4px;
  background: #f5f5f5;
  border-radius: 24px;
}
section .conf-badge .conf {
  width: 32px;
  height: 32px;
}
section .conf-badge .conf img { border-radius: 6px; }
section .conf-badge .meta {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.75em;
  font-weight: 600;
  color: #1a1a1a;
  letter-spacing: 0.01em;
}
section .conf-badge .year {
  color: #666;
  font-weight: 500;
  margin-left: 2px;
}

/* 카탈로그 그리드 */
section .conf-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 22px 14px;
  justify-items: center;
  margin-top: 18px;
}
section .conf-grid .cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
section .conf-grid .cell .name {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.6em;
  font-weight: 600;
  color: #333;
  letter-spacing: 0.04em;
}

/* 카드형 (큰 로고 + 설명) */
section .conf-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 12px;
}
section .conf-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 12px 14px;
  background: #f7f7f7;
  border-left: 3px solid #1a1a1a;
}
section .conf-card .conf-card-body { flex: 1; }
section .conf-card .conf-card-title {
  font-family: 'Noto Serif KR', serif;
  font-weight: 700;
  font-size: 0.95em;
  margin-bottom: 2px;
  color: #1a1a1a;
}
section .conf-card .conf-card-desc {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.68em;
  line-height: 1.5;
  color: #333;
}

/* 출판 타임라인 (학회명 + 연도 + 논문 한줄) */
section .pub-timeline {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 10px;
}
section .pub-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px;
  background: #f7f7f7;
  border-left: 3px solid #003478;
}
section .pub-item .conf {
  width: 52px;
  height: 52px;
}
section .pub-item .pub-meta {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.7em;
  font-weight: 700;
  color: #1a1a1a;
  min-width: 76px;
  text-align: center;
  line-height: 1.25;
}
section .pub-item .pub-meta .pub-year { display: block; color: #666; font-weight: 500; }
section .pub-item .pub-desc {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.65em;
  line-height: 1.5;
  color: #333;
  flex: 1;
}
section .pub-item .pub-desc strong { font-weight: 700; color: #1a1a1a; }

/* =========================================================
   .conf-logo — 공식 로고 (실제 학회 brand asset)
   가로 비율이 제각각이라 height 기준 + width: auto
   ========================================================= */
section .conf-logo {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
section .conf-logo img {
  height: 56px;
  width: auto;
  max-width: 220px;
  object-fit: contain;
  display: block;
}
section .conf-logo.conf-logo-xs img { height: 22px; max-width: 100px; }
section .conf-logo.conf-logo-sm img { height: 34px; max-width: 140px; }
section .conf-logo.conf-logo-lg img { height: 80px; max-width: 280px; }
section .conf-logo.conf-logo-xl img { height: 120px; max-width: 380px; }

/* 공식 로고 카탈로그 (height 통일 + 가변 폭 셀) */
section .official-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 24px 18px;
  align-items: center;
  justify-items: center;
  margin-top: 16px;
}
section .official-grid .cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 90px;
  padding: 6px 4px;
}
section .official-grid .cell img {
  height: 52px;          /* SVG intrinsic 크기 무시하고 height 강제 통일 */
  width: auto;
  max-width: 100%;
  object-fit: contain;
}
section .official-grid .cell .name {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.55em;
  font-weight: 600;
  color: #555;
  letter-spacing: 0.04em;
}

/* =========================================================
   .hero-conf — 단일 학회 hero 표지
   ========================================================= */
section .hero-conf {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 18px;
  margin: 36px auto 0 auto;
  padding: 32px 48px;
  max-width: 760px;
  border-top: 4px solid #003478;
  border-bottom: 4px solid #003478;
}
section .hero-conf img {
  height: 140px;
  width: auto;
  max-width: 480px;
  object-fit: contain;
}
section .hero-conf .hero-tag {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.65em;
  font-weight: 600;
  letter-spacing: 0.18em;
  color: #003478;
  text-transform: uppercase;
}
section .hero-conf .hero-title {
  font-family: 'Noto Serif KR', serif;
  font-size: 1.05em;
  font-weight: 700;
  color: #1a1a1a;
  text-align: center;
  line-height: 1.4;
}
section .hero-conf .hero-authors {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.7em;
  color: #555;
}

/* =========================================================
   .paper-card-grid — 학회별 논문 카드 (큰 grid)
   ========================================================= */
section .paper-card-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 12px;
}
section .paper-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 14px 16px;
  background: #fafafa;
  border: 1px solid #e5e5e5;
  border-top: 3px solid #003478;
}
section .paper-card .paper-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
section .paper-card .paper-head img {
  height: 28px;
  width: auto;
  max-width: 110px;
  object-fit: contain;
}
section .paper-card .paper-head .paper-year {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.65em;
  font-weight: 700;
  color: #666;
  letter-spacing: 0.04em;
}
section .paper-card .paper-title {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.78em;
  font-weight: 700;
  line-height: 1.4;
  color: #1a1a1a;
}
section .paper-card .paper-authors {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.6em;
  color: #555;
  font-style: italic;
}
section .paper-card .paper-abs {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.6em;
  line-height: 1.5;
  color: #333;
}

/* =========================================================
   .vt-timeline — 수직 마일스톤 타임라인
   ========================================================= */
section .vt-timeline {
  position: relative;
  margin: 14px 0 0 24px;
  padding-left: 28px;
  border-left: 2px solid #c8d4e6;
}
section .vt-step {
  position: relative;
  padding: 6px 0 14px 8px;
}
section .vt-step::before {
  content: "";
  position: absolute;
  left: -36px;
  top: 6px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #003478;
  border: 3px solid #fff;
  box-shadow: 0 0 0 2px #003478;
}
section .vt-step.vt-pending::before {
  background: #fff;
  box-shadow: 0 0 0 2px #b0b0b0;
}
section .vt-step .vt-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 4px;
}
section .vt-step .vt-row img {
  height: 26px;
  width: auto;
  max-width: 100px;
  object-fit: contain;
}
section .vt-step .vt-row .vt-when {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.65em;
  font-weight: 700;
  color: #003478;
  letter-spacing: 0.04em;
}
section .vt-step.vt-pending .vt-when { color: #888; }
section .vt-step .vt-detail {
  font-family: 'Noto Serif KR', serif;
  font-size: 0.65em;
  line-height: 1.5;
  color: #333;
}
section .vt-step .vt-detail strong { color: #1a1a1a; font-weight: 700; }

/* =========================================================
   .pub-heatmap — 연구실 연도×학회 publication grid
   ========================================================= */
section .pub-heatmap {
  display: grid;
  grid-template-columns: 70px repeat(10, 1fr);
  gap: 4px;
  margin-top: 10px;
  font-family: Inter, Arial, sans-serif;
}
section .pub-heatmap .h-corner {
  background: transparent;
}
section .pub-heatmap .h-col {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  padding: 4px;
}
section .pub-heatmap .h-col img {
  height: 28px;
  width: auto;
  max-width: 100%;
  object-fit: contain;
}
section .pub-heatmap .h-row {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7em;
  font-weight: 700;
  color: #1a1a1a;
  background: #f3f3f3;
  border-radius: 4px;
  padding: 6px 4px;
}
section .pub-heatmap .h-cell {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75em;
  font-weight: 700;
  color: #fff;
  border-radius: 4px;
  padding: 6px 0;
  min-height: 28px;
}
section .pub-heatmap .h-cell.h-0 { background: #f3f3f3; color: #bbb; font-weight: 400; }
section .pub-heatmap .h-cell.h-1 { background: #c5d2e8; color: #1a1a1a; }
section .pub-heatmap .h-cell.h-2 { background: #6986b9; }
section .pub-heatmap .h-cell.h-3 { background: #003478; }
section .pub-heatmap .h-legend {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 8px;
  font-size: 0.6em;
  color: #666;
}
section .pub-heatmap .h-legend .swatch {
  display: inline-block;
  width: 16px;
  height: 12px;
  border-radius: 2px;
  margin-right: 4px;
  vertical-align: middle;
}

/* =========================================================
   .org-conf — 모 조직 mark + 학회명 라벨 (A안)
   조직 마크와 학회명 텍스트를 명확히 분리된 두 요소로 배치
   학회명 텍스트는 슬라이드 표준 폰트 (Inter) 사용
   ========================================================= */
section .org-conf {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 12px 20px 12px 12px;
  background: #fafafa;
  border: 1px solid #e8e8e8;
  border-radius: 12px;
}
section .org-conf .org-mark {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  flex-shrink: 0;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
}
section .org-conf .org-mark img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}
section .org-conf .org-divider {
  width: 1px;
  height: 36px;
  background: #d8d8d8;
}
section .org-conf .conf-stack {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
section .org-conf .conf-stack .conf-name {
  font-family: 'Helvetica Neue', Inter, Arial, sans-serif;
  font-weight: 800;
  font-size: 1.55em;
  letter-spacing: -0.02em;
  line-height: 1;
  color: #1a1a1a;
}
section .org-conf .conf-stack .org-caption {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.5em;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #888;
}
section .org-conf.color-cvpr .conf-name { color: #1E3A8A; }
section .org-conf.color-iccv .conf-name { color: #B91C1C; }
section .org-conf.color-eccv .conf-name { color: #059669; }
section .org-conf.color-emnlp .conf-name { color: #6B21A8; }

/* A vs B 비교 표 */
section .ab-grid {
  display: grid;
  grid-template-columns: 80px 1fr 1fr;
  gap: 12px 16px;
  align-items: center;
  margin-top: 14px;
}
section .ab-grid .ab-head {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.7em;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #003478;
  text-align: center;
  padding: 4px 0;
  border-bottom: 2px solid #003478;
}
section .ab-grid .ab-label {
  font-family: Inter, Arial, sans-serif;
  font-weight: 700;
  font-size: 0.85em;
  color: #555;
  text-align: right;
  padding-right: 4px;
}
section .ab-grid .ab-cell {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* =========================================================
   .unified-grid — 10개 학회 통일 카드
   원본 마크는 그대로, 카드 디자인으로 일관성 확보
   ========================================================= */
section .unified-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px 14px;
  margin-top: 14px;
}
section .unified-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 14px 8px 12px;
  background: #fafafa;
  border: 1px solid #e8e8e8;
  border-radius: 12px;
  min-height: 134px;
  gap: 6px;
}
section .unified-card .uc-mark {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 46px;
  width: 100%;
}
section .unified-card .uc-mark img {
  max-height: 46px;
  max-width: 90%;
  object-fit: contain;
}
section .unified-card .uc-label {
  font-family: 'Helvetica Neue', Inter, Arial, sans-serif;
  font-weight: 800;
  font-size: 1em;
  letter-spacing: -0.02em;
  line-height: 1;
  color: #1a1a1a;
  margin-top: 4px;
}
section .unified-card .uc-caption {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.42em;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #888;
  text-align: center;
  line-height: 1.35;
}
section .unified-card.uc-neurips .uc-label { color: #5B21B6; }
section .unified-card.uc-icml    .uc-label { color: #0F766E; }
section .unified-card.uc-iclr    .uc-label { color: #1D4ED8; }
section .unified-card.uc-aaai    .uc-label { color: #DC2626; }
section .unified-card.uc-ijcai   .uc-label { color: #EA580C; }
section .unified-card.uc-cvpr    .uc-label { color: #1E3A8A; }
section .unified-card.uc-iccv    .uc-label { color: #B91C1C; }
section .unified-card.uc-eccv    .uc-label { color: #059669; }
section .unified-card.uc-acl     .uc-label { color: #BE123C; }
section .unified-card.uc-emnlp   .uc-label { color: #6B21A8; }

/* 원형 crop 실험 비교 */
section .circle-exp {
  display: grid;
  grid-template-columns: 90px 1fr 1fr;
  gap: 14px 18px;
  align-items: center;
  margin-top: 14px;
}
section .circle-exp .ce-head {
  font-family: Inter, Arial, sans-serif;
  font-size: 0.7em;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #003478;
  text-align: center;
  padding: 4px 0;
  border-bottom: 2px solid #003478;
}
section .circle-exp .ce-label {
  font-family: Inter, Arial, sans-serif;
  font-weight: 700;
  font-size: 0.85em;
  color: #555;
  text-align: right;
  padding-right: 4px;
}
section .circle-exp .ce-cell {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100px;
  background: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 6px;
}
section .circle-exp .ce-cell img {
  max-height: 88px;
  max-width: 100%;
  object-fit: contain;
}
section .circle-exp-note {
  margin-top: 18px;
  padding: 10px 14px;
  background: #fff8e1;
  border-left: 3px solid #f59e0b;
  font-family: 'Noto Serif KR', serif;
  font-size: 0.65em;
  line-height: 1.55;
  color: #5d4400;
}
</style>

# Conference Logos Pattern
## AI/CS 학회 12개 자산 + 다양한 layout 패턴

- 사용 가능 슬러그 (12개): `neurips · icml · iclr · aaai · ijcai · kdd · cvpr · iccv · eccv · acl · emnlp · sigmod`
- 사이즈 클래스: `.conf-xs(28)` · `.conf-sm(40)` · `.conf(56)` · `.conf-lg(88)` · `.conf-xl(140)`
- solid 버전 (`logos/<slug>.svg`) + outline 버전 (`logos/<slug>-outline.svg`)
- typography-only SVG wordmark — 저작권 부담 0, 빌드 시 외부 통신 0

---

# 패턴 1 — 인라인 본문

본문 안에 학회명을 시각적으로 강조.

- 최근 LLM safety 연구는 <span class="conf conf-xs"><img src="logos/neurips.svg" alt=""></span> NeurIPS 2024 <span class="conf conf-xs"><img src="logos/iclr.svg" alt=""></span> ICLR 2025 에서 본격적으로 다뤄지기 시작했습니다.
- multi-agent planning 분야는 <span class="conf conf-xs"><img src="logos/aaai.svg" alt=""></span> AAAI · <span class="conf conf-xs"><img src="logos/ijcai.svg" alt=""></span> IJCAI 가 전통 강세, 최근 <span class="conf conf-xs"><img src="logos/icml.svg" alt=""></span> ICML 도 합류.

<br>

학회명 + 연도 묶음 (`.conf-badge` — `.conf-badges` 래퍼로 감싸기):

<div class="conf-badges">
<span class="conf-badge"><span class="conf"><img src="logos/neurips.svg" alt=""></span><span class="meta">NeurIPS<span class="year">2025</span></span></span>
<span class="conf-badge"><span class="conf"><img src="logos/icml.svg" alt=""></span><span class="meta">ICML<span class="year">2025</span></span></span>
<span class="conf-badge"><span class="conf"><img src="logos/iclr.svg" alt=""></span><span class="meta">ICLR<span class="year">2026</span></span></span>
<span class="conf-badge"><span class="conf"><img src="logos/cvpr.svg" alt=""></span><span class="meta">CVPR<span class="year">2025</span></span></span>
<span class="conf-badge"><span class="conf"><img src="logos/acl.svg" alt=""></span><span class="meta">ACL<span class="year">2025</span></span></span>
<span class="conf-badge"><span class="conf"><img src="logos/emnlp.svg" alt=""></span><span class="meta">EMNLP<span class="year">2025</span></span></span>
</div>

---

# 패턴 6 — 공식 로고 (실제 학회 자산)

각 학회 공식 사이트에서 받은 brand asset. 비율이 제각각이라 height 기준으로 통일.

<div class="official-grid">

<div class="cell"><img src="logos-official/neurips.svg" alt="NeurIPS"><span class="name">NEURIPS</span></div>
<div class="cell"><img src="logos-official/icml.svg" alt="ICML"><span class="name">ICML</span></div>
<div class="cell"><img src="logos-official/iclr.svg" alt="ICLR"><span class="name">ICLR</span></div>
<div class="cell"><img src="logos-official/aaai.svg" alt="AAAI"><span class="name">AAAI</span></div>
<div class="cell"><img src="logos-official/ijcai.png" alt="IJCAI"><span class="name">IJCAI</span></div>

<div class="cell"><img src="logos-official/cvpr.svg" alt="CVPR"><span class="name">CVPR</span></div>
<div class="cell"><img src="logos-official/iccv.svg" alt="ICCV"><span class="name">ICCV</span></div>
<div class="cell"><img src="logos-official/eccv.png" alt="ECCV"><span class="name">ECCV</span></div>
<div class="cell"><img src="logos-official/acl.svg" alt="ACL"><span class="name">ACL</span></div>
<div class="cell"><img src="logos-official/emnlp.png" alt="EMNLP"><span class="name">EMNLP</span></div>

</div>

---

# 패턴 7 — 공식 로고 인라인 / 카드 / 타임라인

## 인라인 사용

본문에 자연스럽게 끼워넣기. height 22px (xs) 또는 34px (sm) 추천.

- <span class="conf-logo conf-logo-xs"><img src="logos-official/neurips.svg" alt="NeurIPS"></span> 의 LLM safety track 이 2024년부터 본격 확장.
- <span class="conf-logo conf-logo-xs"><img src="logos-official/iclr.svg" alt="ICLR"></span> 의 오픈리뷰는 dLLM 분야 핵심 venue.

## 출판 타임라인 (공식 로고 버전)

<div class="pub-timeline">

<div class="pub-item">
<span class="conf-logo conf-logo-sm"><img src="logos-official/neurips.svg" alt="NeurIPS"></span>
<div class="pub-meta">2025</div>
<div class="pub-desc"><strong>KLASS: KL-aware Sampling</strong> · diffusion LM selective forget. KL projection.</div>
</div>

<div class="pub-item">
<span class="conf-logo conf-logo-sm"><img src="logos-official/iclr.svg" alt="ICLR"></span>
<div class="pub-meta">2026</div>
<div class="pub-desc"><strong>Hierarchical dLLM Unlearning</strong> · token / span / concept 3계층 forget.</div>
</div>

<div class="pub-item">
<span class="conf-logo conf-logo-sm"><img src="logos-official/icml.svg" alt="ICML"></span>
<div class="pub-meta">2025</div>
<div class="pub-desc"><strong>Negative Preference Optimization</strong> · DPO 의 negative-only 변형.</div>
</div>

<div class="pub-item">
<span class="conf-logo conf-logo-sm"><img src="logos-official/acl.svg" alt="ACL"></span>
<div class="pub-meta">2025</div>
<div class="pub-desc"><strong>TOFU benchmark v2</strong> · synthetic author 200명 + paraphrase robustness.</div>
</div>

</div>

---

# 패턴 8 — Hero 표지 (논문 발표 첫 슬라이드)

<div class="hero-conf">
<img src="logos-official/neurips.svg" alt="NeurIPS">
<div class="hero-tag">Accepted · Spotlight</div>
<div class="hero-title">KLASS — KL-aware Sampling for Selective Forgetting in Diffusion LMs</div>
<div class="hero-authors">Lee · Kim · Park · Choi · DAMI Lab, 2025</div>
</div>

---

# 패턴 9 — 논문 카드 grid (학회별 introduce)

<div class="paper-card-grid">

<div class="paper-card">
<div class="paper-head">
<img src="logos-official/neurips.svg" alt="NeurIPS">
<span class="paper-year">2025 · Spotlight</span>
</div>
<div class="paper-title">KLASS — KL-aware Sampling for Selective Forgetting</div>
<div class="paper-authors">Lee, Kim, Park, Choi (DAMI Lab)</div>
<div class="paper-abs">diffusion LM 의 forget set 만 KL projection 으로 분리. retain quality 손실 0.4% 이내.</div>
</div>

<div class="paper-card">
<div class="paper-head">
<img src="logos-official/iclr.svg" alt="ICLR">
<span class="paper-year">2026 · Poster</span>
</div>
<div class="paper-title">Hierarchical dLLM Unlearning across Token / Span / Concept</div>
<div class="paper-authors">Qi, Zhang, DAMI collab.</div>
<div class="paper-abs">3계층 forget granularity 동시 처리. TOFU 에서 SOTA, retain BLEU drop &lt; 1.</div>
</div>

<div class="paper-card">
<div class="paper-head">
<img src="logos-official/icml.svg" alt="ICML">
<span class="paper-year">2025 · Oral</span>
</div>
<div class="paper-title">Negative Preference Optimization without Anchor Pairs</div>
<div class="paper-authors">Park, Lee (DAMI Lab)</div>
<div class="paper-abs">DPO 의 negative-only 변형. anchor-free 구조로 unlearning 안정성 +14%.</div>
</div>

<div class="paper-card">
<div class="paper-head">
<img src="logos-official/acl.svg" alt="ACL">
<span class="paper-year">2025 · Findings</span>
</div>
<div class="paper-title">TOFU-2 — A Robust Benchmark for LLM Unlearning</div>
<div class="paper-authors">Choi, Park, et al.</div>
<div class="paper-abs">synthetic author 200명 + paraphrase / multi-hop QA 평가 추가. v1 대비 leakage 12% 감소.</div>
</div>

</div>

---

# 패턴 10 — 수직 마일스톤 타임라인

## LLM Unlearning 라인 — 2024년 가을 ~ 2026년 봄

<div class="vt-timeline">

<div class="vt-step">
<div class="vt-row">
<img src="logos-official/icml.svg" alt="ICML">
<span class="vt-when">2024.07 · Honolulu</span>
</div>
<div class="vt-detail"><strong>Workshop 발표</strong> · DPO-style negative loss 의 안정성 분석. peer 피드백으로 retain regularizer 도입 결정.</div>
</div>

<div class="vt-step">
<div class="vt-row">
<img src="logos-official/neurips.svg" alt="NeurIPS">
<span class="vt-when">2025.05 → 2025.12</span>
</div>
<div class="vt-detail"><strong>NeurIPS 2025 Spotlight</strong> · KLASS 본 논문 등재. KL-aware sampling 으로 forget vs retain trade-off 안정 영역 발견.</div>
</div>

<div class="vt-step">
<div class="vt-row">
<img src="logos-official/iclr.svg" alt="ICLR">
<span class="vt-when">2025.10 → 2026.05</span>
</div>
<div class="vt-detail"><strong>ICLR 2026</strong> · Hierarchical dLLM Unlearning 채택. KLASS 후속, granularity 3계층으로 확장.</div>
</div>

<div class="vt-step vt-pending">
<div class="vt-row">
<img src="logos-official/acl.svg" alt="ACL">
<span class="vt-when">2026.05 (under review)</span>
</div>
<div class="vt-detail"><strong>ACL 2026 main</strong> · TOFU-3 benchmark + Membership Inference 통합. 결과 통보 6월 말.</div>
</div>

<div class="vt-step vt-pending">
<div class="vt-row">
<img src="logos-official/emnlp.png" alt="EMNLP">
<span class="vt-when">2026.06 (submission)</span>
</div>
<div class="vt-detail"><strong>EMNLP 2026 target</strong> · safety alignment retention 후속 연구. 7월 deadline.</div>
</div>

</div>

---

# 패턴 11 — 연구실 출판 이력 heatmap

## DAMI Lab · 학회 × 연도 publication count

<div class="pub-heatmap">

<div class="h-corner"></div>
<div class="h-col"><img src="logos-official/neurips.svg" alt=""></div>
<div class="h-col"><img src="logos-official/icml.svg" alt=""></div>
<div class="h-col"><img src="logos-official/iclr.svg" alt=""></div>
<div class="h-col"><img src="logos-official/aaai.svg" alt=""></div>
<div class="h-col"><img src="logos-official/ijcai.png" alt=""></div>
<div class="h-col"><img src="logos-official/cvpr.svg" alt=""></div>
<div class="h-col"><img src="logos-official/iccv.svg" alt=""></div>
<div class="h-col"><img src="logos-official/eccv.png" alt=""></div>
<div class="h-col"><img src="logos-official/acl.svg" alt=""></div>
<div class="h-col"><img src="logos-official/emnlp.png" alt=""></div>

<div class="h-row">2022</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>

<div class="h-row">2023</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>

<div class="h-row">2024</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-1">1</div>

<div class="h-row">2025</div>
<div class="h-cell h-3">3</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-3">3</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-2">2</div>

<div class="h-row">2026</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-2">2</div>
<div class="h-cell h-3">3</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-0">·</div>
<div class="h-cell h-1">1</div>
<div class="h-cell h-0">·</div>

<div class="h-legend">
<span><span class="swatch" style="background:#f3f3f3"></span>0</span>
<span><span class="swatch" style="background:#c5d2e8"></span>1</span>
<span><span class="swatch" style="background:#6986b9"></span>2</span>
<span><span class="swatch" style="background:#003478"></span>3+</span>
</div>

</div>

---

# 패턴 12 — 10개 학회 통일 카드 그리드

generic 자산이 있는 학회는 학회 공식 로고, 없는 학회는 모 조직 로고. 모두 동일한 카드 디자인. 라벨은 우리 슬라이드 표준 폰트 (Inter).

<div class="unified-grid">

<div class="unified-card uc-neurips">
<div class="uc-mark"><img src="logos-official/neurips.svg" alt=""></div>
<div class="uc-label">NeurIPS</div>
<div class="uc-caption">Neural Information<br>Processing Systems</div>
</div>

<div class="unified-card uc-icml">
<div class="uc-mark"><img src="logos-official/icml.svg" alt=""></div>
<div class="uc-label">ICML</div>
<div class="uc-caption">Int'l Conference on<br>Machine Learning</div>
</div>

<div class="unified-card uc-iclr">
<div class="uc-mark"><img src="logos-official/iclr.svg" alt=""></div>
<div class="uc-label">ICLR</div>
<div class="uc-caption">Int'l Conference on<br>Learning Representations</div>
</div>

<div class="unified-card uc-aaai">
<div class="uc-mark"><img src="logos-official/aaai.svg" alt=""></div>
<div class="uc-label">AAAI</div>
<div class="uc-caption">Assoc. for Advancement<br>of Artificial Intelligence</div>
</div>

<div class="unified-card uc-ijcai">
<div class="uc-mark"><img src="logos-official/ijcai.png" alt=""></div>
<div class="uc-label">IJCAI</div>
<div class="uc-caption">Int'l Joint Conference<br>on Artificial Intelligence</div>
</div>

<div class="unified-card uc-cvpr">
<div class="uc-mark"><img src="logos-marks/cvf.jpg" alt=""></div>
<div class="uc-label">CVPR</div>
<div class="uc-caption">CVF · IEEE<br>Computer Society</div>
</div>

<div class="unified-card uc-iccv">
<div class="uc-mark"><img src="logos-marks/cvf.jpg" alt=""></div>
<div class="uc-label">ICCV</div>
<div class="uc-caption">CVF · IEEE<br>Computer Society</div>
</div>

<div class="unified-card uc-eccv">
<div class="uc-mark"><img src="logos-marks/ecva.png" alt=""></div>
<div class="uc-label">ECCV</div>
<div class="uc-caption">European Computer<br>Vision Association</div>
</div>

<div class="unified-card uc-acl">
<div class="uc-mark"><img src="logos-official/acl.svg" alt=""></div>
<div class="uc-label">ACL</div>
<div class="uc-caption">Assoc. for Computational<br>Linguistics</div>
</div>

<div class="unified-card uc-emnlp">
<div class="uc-mark"><img src="logos-official/acl.svg" alt=""></div>
<div class="uc-label">EMNLP</div>
<div class="uc-caption">ACL SIGDAT</div>
</div>

</div>

