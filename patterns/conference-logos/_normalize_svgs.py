"""
공식 SVG 로고 normalize.
- width="100%" / height="100%" 박힌 SVG 는 browser intrinsic sizing 이 0 이 될 수 있음
- viewBox 값으로 width/height 재설정해서 <img> 에서 정상 렌더되게 만든다
"""
import re
from pathlib import Path

DIR = Path(__file__).parent / "logos-official"

for svg in DIR.glob("*.svg"):
    s = svg.read_text(encoding="utf-8")
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    if not m:
        print(f"skip (no viewBox): {svg.name}")
        continue
    w, h = m.group(1), m.group(2)
    # 첫 번째 <svg ...> 내의 width/height 만 교체
    def replace_first_svg(match):
        tag = match.group(0)
        tag = re.sub(r'\swidth="[^"]*"', f' width="{w}"', tag, count=1)
        tag = re.sub(r'\sheight="[^"]*"', f' height="{h}"', tag, count=1)
        # width/height 가 없는 경우 추가
        if 'width=' not in tag:
            tag = tag.replace('<svg', f'<svg width="{w}"', 1)
        if 'height=' not in tag:
            tag = tag.replace('<svg', f'<svg height="{h}"', 1)
        return tag
    s = re.sub(r'<svg[^>]*>', replace_first_svg, s, count=1)
    svg.write_text(s, encoding="utf-8")
    print(f"normalized {svg.name}: {w} x {h}")
