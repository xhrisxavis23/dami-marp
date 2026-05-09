#!/usr/bin/env python3
"""
figure-caption 패턴 통합 빌드.

prebuild.py 로 Fig. N 자동 prefix 삽입 → marp 빌드 → 중간 파일 자동 cleanup.
사용자는 .numbered.md / .numbered.built.md 같은 중간물을 보지 않아도 됨.

usage:
  python3 build_figcap.py SOURCE.md [--format pdf|pptx|html] [--keep]

flags:
  --format    출력 포맷 (default pdf)
  --keep      중간 파일 (.numbered.md / .numbered.built.md) 보존 (디버그용)
"""
from __future__ import annotations
import sys
import subprocess
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MARP_BUILD = SCRIPT_DIR.parents[1] / 'bin' / 'build.py'


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return 1

    src = Path(sys.argv[1]).resolve()
    if not src.exists():
        print(f"error: source not found: {src}", file=sys.stderr)
        return 1

    if not MARP_BUILD.exists():
        print(
            f"error: marp build.py 를 찾을 수 없습니다: {MARP_BUILD}\n"
            f"       이 스크립트는 .claude/skills/marp/patterns/figure-caption/ 안에 있다고 가정합니다.\n"
            f"       구조가 바뀌었으면 build_figcap.py 의 MARP_BUILD 경로를 갱신하세요.",
            file=sys.stderr,
        )
        return 1

    args = sys.argv[2:]
    keep = '--keep' in args
    if keep:
        args.remove('--keep')
    if '--format' not in args:
        args = ['--format', 'pdf', *args]
    fmt = args[args.index('--format') + 1]

    base = src.with_suffix('')
    numbered_md = Path(f"{base}.numbered.md")
    numbered_built = Path(f"{base}.numbered.built.md")
    numbered_out = Path(f"{base}.numbered.{fmt}")
    final_out = Path(f"{base}.{fmt}")

    # 1. prebuild
    subprocess.run(
        ['python3', str(SCRIPT_DIR / 'prebuild.py'), str(src)],
        check=True,
    )

    # 2. marp build via skill build.py
    subprocess.run(
        ['python3', str(MARP_BUILD), str(numbered_md), *args],
        check=True,
    )

    # 3. rename to final
    if numbered_out.exists():
        if final_out.exists():
            final_out.unlink()
        shutil.move(str(numbered_out), str(final_out))

    # 4. cleanup intermediates
    if not keep:
        for p in (numbered_md, numbered_built):
            if p.exists():
                p.unlink()

    print(f"[figcap] ✅ {final_out.name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
