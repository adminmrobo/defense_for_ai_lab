#!/usr/bin/env python3
"""src/ 조각을 모아 index.html을 만든다. <say> 줄임 태그를 대사 상자로 바꾼다."""
import re, os
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(H, p), encoding='utf-8').read()

NAME = {'doctor': '박사', 'haru': '하루(조수)', 'jupanbot': '주판봇', 'fruitfly': '초파리',
        'sia': '시아(인턴1)', 'moa': '모아(인턴2)', 'x1': 'X1', 'x2': 'X2', 'x3': 'X3'}
SIDE = {'pro': '찬성', 'con': '반대', 'mod': '사회'}


def say(m):
    attrs, text = m.group(1), m.group(2).strip()
    who = re.search(r'who="(\w+)"', attrs).group(1)
    e = re.search(r'e="(\d+)"', attrs).group(1)
    side = re.search(r'side="(\w+)"', attrs).group(1)
    right = ' right' if re.search(r'\bright\b', attrs) else ''
    return ('<div class="say%s" data-side="%s"><img src="assets/chars/%s/E%s.webp" alt="%s" loading="lazy">'
            '<div class="bub"><span class="nm %s">%s<span class="side %s">%s</span></span><p>%s</p></div></div>'
            % (right, side, who, e, NAME[who], who, NAME[who], side, SIDE[side], text))


body = re.sub(r'<say([^>]*)>(.*?)</say>', say, rd('src/body.html'), flags=re.S)
IG = dict(re.findall(r'<!--IG:(\w+)-->(.*?)<!--/IG-->', rd('src/infographics.html'), flags=re.S))
body = re.sub(r'<ig k="(\w+)"></ig>', lambda m: IG[m.group(1)].strip(), body)
body = re.sub(r'<scene n="(\d)" alt="([^"]*)"></scene>', lambda m: '' if not os.path.exists(os.path.join(H, 'assets/scenes/sc_%s.webp' % m.group(1))) else (
    '<figure class="scene-fig" id="scene-%s"><img src="assets/scenes/sc_%s.webp" width="1200" height="800" alt="%s" loading="lazy" '
    'onerror="this.parentNode.style.display=\'none\'"></figure>' % (m.group(1), m.group(1), m.group(2))), body)
title = 'AI의 추론을 방해하는 것은 나쁜가? — AI 추론 장벽 찬반 토론 | 초파리 연구실'
desc = '시험지 패치·숨은 지시·네트워크 관문으로 AI 추론에 장벽을 세우는 원리를 베이즈 정리와 적대적 예제로 풀고, 공격인지 방어인지 찬반 토론으로 따져 보는 인터랙티브 해설.'
head = f'''<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="안상선">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 16 16%22%3E%3Crect width=%2216%22 height=%2216%22 rx=%223%22 fill=%22%237c5cd6%22/%3E%3Cpath d=%22M4 4h8v8H4z%22 fill=%22%23fff%22/%3E%3C/svg%3E">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{rd('src/style.css')}
</style>
</head><body>
'''
out = head + body + '\n<script>\n' + rd('src/app.js') + '\n</script>\n</body></html>\n'
open(os.path.join(H, 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out.encode()) // 1024, 'KB')
