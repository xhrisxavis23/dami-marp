"""
학회 로고 SVG 생성기 (초안).

각 학회마다:
- 200x200 정사각형 SVG
- 모서리 둥근 사각형 (rx=28) 배경 (brand color)
- 흰색 acronym 텍스트, sans-serif bold
- 글자 수에 맞춘 font-size

대안 모드 (outline):
- 흰 배경 + brand color 테두리 + brand color 텍스트
"""

from pathlib import Path

OUT = Path(__file__).parent / "logos"
OUT.mkdir(exist_ok=True)

# (slug, display_acronym, brand_color, font_size_px)
CONFS = [
    ("neurips", "NeurIPS",  "#5B21B6", 38),   # 짙은 보라
    ("icml",    "ICML",     "#0F766E", 70),   # teal
    ("iclr",    "ICLR",     "#1D4ED8", 70),   # blue
    ("aaai",    "AAAI",     "#DC2626", 70),   # red
    ("ijcai",   "IJCAI",    "#EA580C", 58),   # orange
    ("cvpr",    "CVPR",     "#1E3A8A", 70),   # navy
    ("iccv",    "ICCV",     "#B91C1C", 70),   # 짙은 빨강
    ("eccv",    "ECCV",     "#059669", 70),   # 에메랄드
    ("acl",     "ACL",      "#BE123C", 90),   # cherry
    ("emnlp",   "EMNLP",    "#6B21A8", 58),   # 짙은 자주
]

SOLID_TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <rect width="200" height="200" rx="28" fill="{color}"/>
  <text x="100" y="100" text-anchor="middle" dominant-baseline="central"
        font-family="Inter, 'Helvetica Neue', Arial, sans-serif"
        font-weight="800" font-size="{size}" fill="#ffffff"
        letter-spacing="-1">{label}</text>
</svg>
"""

OUTLINE_TPL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <rect x="6" y="6" width="188" height="188" rx="24"
        fill="#ffffff" stroke="{color}" stroke-width="6"/>
  <text x="100" y="100" text-anchor="middle" dominant-baseline="central"
        font-family="Inter, 'Helvetica Neue', Arial, sans-serif"
        font-weight="800" font-size="{size}" fill="{color}"
        letter-spacing="-1">{label}</text>
</svg>
"""

for slug, label, color, size in CONFS:
    (OUT / f"{slug}.svg").write_text(
        SOLID_TPL.format(color=color, size=size, label=label),
        encoding="utf-8",
    )
    (OUT / f"{slug}-outline.svg").write_text(
        OUTLINE_TPL.format(color=color, size=size, label=label),
        encoding="utf-8",
    )

print(f"generated {len(CONFS)*2} svg files to {OUT}")
