#!/usr/bin/env python3
"""
PNG 그림의 좌우상하 흰여백 자동 제거.

원본 그림 PNG 안에 들어있는 흰 padding 때문에 marp 슬라이드에서
캡션 좌측이 그림 콘텐츠보다 안쪽에 보이는 문제 해결.
원본 자산은 손대지 않고 사본을 새 폴더에 생성.

usage:
  python3 trim_assets.py SRC_DIR DST_DIR
    → SRC_DIR 안 모든 PNG 를 trim 해서 DST_DIR 에 저장 (디렉토리 구조 보존)

  python3 trim_assets.py SRC.png DST.png
    → 단일 파일 trim
"""
import sys
from pathlib import Path

from PIL import Image
import numpy as np


def trim_white_margin(img: Image.Image, threshold: int = 235, pad: int = 2) -> Image.Image:
    """흰여백을 제거한 새 PIL Image 반환. pad 만큼 안전 margin 유지."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    arr = np.array(img)
    is_content = (np.any(arr[:, :, :3] < threshold, axis=2)) & (arr[:, :, 3] > 10)
    cols = np.any(is_content, axis=0)
    rows = np.any(is_content, axis=1)
    if not cols.any():
        return img
    l = int(np.argmax(cols))
    r = int(len(cols) - 1 - np.argmax(cols[::-1]))
    t = int(np.argmax(rows))
    b = int(len(rows) - 1 - np.argmax(rows[::-1]))
    l = max(0, l - pad)
    t = max(0, t - pad)
    r = min(arr.shape[1] - 1, r + pad)
    b = min(arr.shape[0] - 1, b + pad)
    return img.crop((l, t, r + 1, b + 1))


def trim_dir(src_dir: Path, dst_dir: Path) -> int:
    dst_dir.mkdir(parents=True, exist_ok=True)
    changed = 0
    total = 0
    for src in src_dir.rglob('*.png'):
        total += 1
        rel = src.relative_to(src_dir)
        dst = dst_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            img = Image.open(src)
            cropped = trim_white_margin(img)
            cropped.save(dst)
            if img.size != cropped.size:
                changed += 1
        except Exception as e:
            print(f"[trim] skip {rel}: {e}", file=sys.stderr)
    return total, changed


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: trim_assets.py SRC DST")
        return 1
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    if src.is_dir():
        total, changed = trim_dir(src, dst)
        print(f"[trim] {total} 개 PNG 처리, {changed} 개 trim 됨 → {dst}")
    else:
        img = Image.open(src)
        cropped = trim_white_margin(img)
        cropped.save(dst)
        print(f"[trim] {src.name}: {img.size} → {cropped.size}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
