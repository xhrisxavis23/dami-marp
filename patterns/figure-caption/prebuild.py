#!/usr/bin/env python3
"""
fig-cap 캡션마다 'Fig. N.' 자동 prefix 삽입.

usage:
  python3 prebuild.py caption-prototype-v8.md
  → caption-prototype-v8.numbered.md 생성

작동:
- <div class="fig-cap cap-B">본문</div> 형태를 찾아
- <div class="fig-cap cap-B"><span class="num">Fig. N.</span> 본문</div> 로 변환
- N 은 PPT 안에서 등장 순서대로 1, 2, 3, ...
- 슬라이드 추가/삭제/순서 변경 시 자동 갱신

향후 figure-handling 스킬에 흡수 예정.
"""
import re
import sys
from pathlib import Path


def add_fig_numbers(src_text: str) -> tuple[str, int]:
    counter = [0]

    def repl(m: re.Match) -> str:
        counter[0] += 1
        return f'<div class="fig-cap cap-B"><span class="num">Fig. {counter[0]}.</span> '

    # 'cap-B' 단독, 또는 cap-B 뒤에 다른 modifier (예: tri) 가 붙은 경우 모두 카운트
    pattern = r'<div class="fig-cap cap-B[^"]*">'
    new = re.sub(pattern, repl, src_text)
    return new, counter[0]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prebuild.py <input.md> [output.md]")
        return 1
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix('.numbered.md')
    text = src.read_text(encoding='utf-8')
    new_text, count = add_fig_numbers(text)
    dst.write_text(new_text, encoding='utf-8')
    print(f"[prebuild] {count} 개 figure 캡션에 자동 번호 삽입 → {dst.name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
