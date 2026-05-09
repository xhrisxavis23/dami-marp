#!/usr/bin/env bash
# 공식 학회 자산 (logos-official/, logos-marks/) 을 각 학회 / 모 조직 공식 사이트에서 새로 받는다.
# - Skill 자산을 bundle 로 두지 않고 사용 시점에 fetch 하는 흐름이 깔끔.
# - 일부 conference-year specific 자산 (CVPR/ICCV/ECCV/EMNLP) 은 매년 URL 바뀔 수 있으므로 발표 시점에 재실행 권장.
#
# 사용:
#   bash download_official.sh
#   (현재 폴더 기준 logos-official/ logos-marks/ 채워줌)

set -e
cd "$(dirname "$0")"
mkdir -p logos-official logos-marks

echo "== logos-official/ =="
curl -fsSL -o logos-official/neurips.svg  "https://neurips.cc/media/Press/NeurIPS_logo.svg"
curl -fsSL -o logos-official/icml.svg     "https://icml.cc/static/core/img/ICML-logo.svg"
curl -fsSL -o logos-official/iclr.svg     "https://iclr.cc/static/core/img/iclr-navbar-logo.svg"
curl -fsSL -o logos-official/aaai.svg     "https://aaai.org/wp-content/uploads/2024/03/AAAI-Logo-Title-FullColor.svg"
curl -fsSL -o logos-official/ijcai.png    "https://www.ijcai.org/sites/all/themes/creative-responsive-theme/logo.png"
curl -fsSL -o logos-official/kdd.png      "https://kdd.org/images/kdd.png"
curl -fsSL -o logos-official/cvpr.svg     "https://cvpr.thecvf.com/static/core/img/cvpr-navbar-logo.svg"
curl -fsSL -o logos-official/iccv.svg     "https://iccv.thecvf.com/static/core/img/iccv-navbar-logo.svg"
curl -fsSL -o logos-official/eccv.png     "https://eccv2022.ecva.net/files/2022/03/ECCV-logo3.png"
curl -fsSL -o logos-official/acl.svg      "https://upload.wikimedia.org/wikipedia/commons/7/72/Association_for_Computational_Linguistics_logo.svg"
curl -fsSL -o logos-official/acl.png      "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Association_for_Computational_Linguistics_logo.svg/500px-Association_for_Computational_Linguistics_logo.svg.png"
curl -fsSL -o logos-official/emnlp.png    "https://2024.emnlp.org/assets/images/logos/emnlp-2024-logo.png"
curl -fsSL -o logos-official/sigmod.png   "https://sigmod.org/wp-content/uploads/2016/09/image_preview5.png"

echo "== logos-marks/ (모 조직: CVF, ECVA, ACL) =="
curl -fsSL -o logos-marks/cvf.jpg   "https://www.thecvf.com/wp-content/uploads/2016/04/cropped-cropped-cvf-s2-1.jpg"
curl -fsSL -o logos-marks/ecva.png  "https://www.ecva.net/src/img/ECVAlogo.png"
cp logos-official/acl.svg logos-marks/acl.svg

echo "== 후처리 =="
# (1) IJCAI: 가로형 (232x60) → 좌측 icon 81x60 만 추출 + 90x70 padding 캔버스
python3 - <<'PYEOF'
from PIL import Image
img = Image.open('logos-official/ijcai.png').convert('RGBA')
icon = img.crop((0, 0, 81, 60))
canvas = Image.new('RGBA', (90, 70), (0, 0, 0, 0))
canvas.paste(icon, (4, 5), icon)
canvas.save('logos-official/ijcai-icon.png')
print('ijcai-icon.png 생성 (90x70)')
PYEOF

# (2) SVG 의 width="100%"/height="100%" 박힌 경우 viewBox 값으로 정상화
python3 _normalize_svgs.py

# (3) CVPR navbar svg 는 fill:white (어두운 navbar 용) → 흰 슬라이드에서 안 보임. 검정으로 치환
sed -i 's/fill:white/fill:#1a1a1a/g; s/fill="white"/fill="#1a1a1a"/g; s/fill="#fff"/fill="#1a1a1a"/g; s/fill="#FFFFFF"/fill="#1a1a1a"/g' logos-official/cvpr.svg

echo "== 완료. logos-official/ logos-marks/ 확인 =="
ls -la logos-official/ logos-marks/
