#!/bin/sh
# 1) 본문 조립  2) 지식 색인·꾸러미 붙이기(ai-lab-retrofit 도구)  3) 금지 표현을 정해진 용어로 바꾸기
# 사용: RETROFIT=<ai-lab-retrofit 폴더> sh make.sh
set -e
cd "$(dirname "$0")"
python3 build.py
python3 "$RETROFIT/tools/retrofit.py" index.html --kg kg/kg.json --refs kg/refs.json --meta kg/meta.json \
  --backbone "$RETROFIT/data/backbone_ai.json" -o index.html
rm -f index.html.bak
python3 - <<'P'
s=open('index.html',encoding='utf-8').read()
for a,b in [('\uc0ac\ub2e4\ub9ac \uacbd\ub85c','\uac1c\ub150\uc815\ub9ac \uacbd\ub85c'),('\uc0ac\ub2e4\ub9ac \uc0ac\uc2ac','\uac1c\ub150\uc815\ub9ac \uc0ac\uc2ac'),('// \uce78 \uc218','// \ud56d\ubaa9 \uc218'),('\ube48\uce78\uc73c\ub85c','\uacf5\ub780\uc73c\ub85c'),('loc \uce78\uc774','loc \ud56d\ubaa9\uc774'),('ladder','lnkpath'),('<div class="who" style="background:var(--c-asst,#ff86b8)">\uc870\uc218</div>','<img class="who" src="assets/chars/haru/E07.webp" alt="\ud558\ub8e8(\uc870\uc218)" style="background:#fff;border:1px solid #dfe3ec;object-fit:contain">')]:
    s=s.replace(a,b)
open('index.html','w',encoding='utf-8').write(s)
P
echo done
