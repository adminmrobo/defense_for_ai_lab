# 그림 지시문 — AI 추론 장벽 찬반 토론 (Genspark용, 만드는 순서대로)

모든 그림 공통 화풍: **16비트 SNES 시대 픽셀 아트(16-bit RPG pixel art)**, 굵은 외곽선, 디더링 음영, 밝은 흰 연구실 배경, 글자·숫자·로고 없음.
참고 그림: fruitfly-lab-expressions 저장소의 `refs/original/` 캐릭터 시트와 `images/{캐릭터}/E13_neutral.png` (박사·하루·주판봇·초파리·시아·모아), X1~X3는 `specs/spares/README.md`의 실루엣 규칙.

## 그림 목록
| # | 파일 | 비율 | 새로 그림 / 재사용 |
|---|---|---|---|
| 1 | assets/img/cover.webp (원본 480×270 → ×4) | 16:9 | 새로 그림 (지금은 캐릭터 팩으로 조립한 임시 표지) |
| 2 | assets/img/og.png | 표지에서 자름 (480×252 → ×3) | 표지에서 자를 것 |
| 3 | assets/img/thumb.webp | 표지에서 자름 (300×200 → ×2) | 표지에서 자를 것 |
| 4 | 장면: 도입 두 사례 | 3:2 | 새로 그림 |
| 5 | 장면: 아웃트로 | 3:2 | 새로 그림 |
| - | 대사 얼굴 | 1:1 | 캐릭터 팩 재사용 (assets/chars) |

## 1. 표지 (먼저 받아 그림체 확인)
```
16-bit SNES-era pixel art, a bright white university lab turned into a debate stage, wide 16:9 shot.
Center: a purple podium; the Professor (spiky black-and-white hair, teal glasses, white lab coat) stands as moderator, one hand raised, explaining.
Left: a long blue debate table (PRO team): Sia (maid intern, long straight black hair, charcoal maid dress, grey ribbon), Moa (maid intern, light brown long hair, white frill headband, red ribbon), Haru (assistant, pink twin-bun hair with navy streaks, lavender hoodie under lab coat), and Jupanbot (small retro computer robot with a green-screen smiling face holding an abacus).
Right: a long orange debate table (CON team): the Fruit Fly researcher (big red compound eyes, blue helmet, white lab coat, holding a mug) and three cute solid dark-navy silhouettes X1 (side ponytail with pink bow), X2 (round beret, round glasses with teal reflections), X3 (tiny, cat-ear hood with yellow pompoms), only white dot eyes and pink blush.
Back wall: a whiteboard showing a simple bar chart and a green shield icon with a crack, a small colorful noise-square patch pinned next to a printed exam sheet with a line graph.
Cheerful comedy mood, crisp pixels, thick dark outlines, dithered shading, no text, no letters, no numbers, no logos.
```
네거티브: `text, letters, numbers, watermark, logo, blurry, 3d render, photorealistic, scary, horror, dark background`

## 4. 장면 — 도입 두 사례 (3:2)
```
16-bit SNES-era pixel art, white lab. Left half: an exam sheet on a desk with a line graph and a small colorful noise-square patch printed beside it; a smartphone camera points at it and a speech bubble from the phone shows a confused swirl symbol. Right half: a network gateway box with a shield, standing between the phone and a cloud server, a red stop hand icon blocking an arrow. The Professor points between the two halves. No text, no letters, no numbers.
```

## 5. 장면 — 아웃트로 (3:2, 대결 결과와 표정 맞추기)
```
16-bit SNES-era pixel art, white lab debate stage after the debate. The Professor in the center smiling and cheering (both fists up). PRO team on the left looking proud (Sia, Moa, Haru proud smiles, Jupanbot with sparkling eyes). CON team on the right also satisfied (Fruit Fly researcher proud, X1~X3 silhouettes with happy dot eyes). Both teams shake hands over the center. Warm, friendly mood, no text, no letters.
```
- 판정 결과는 "조건부(목적·범위·공개·책임)"이므로 두 팀 모두 웃는 표정이어야 한다. 틀리면 기존 그림 + 캐릭터 저장소 표정 그림(E16 뿌듯함, E12 응원)을 첨부해 "표정만 편집"으로 다시 요청한다.

## 받은 그림 반영
1. 생성 PNG를 4로 나눈 원래 격자(예 480×270)를 찾는다.
2. `NEAREST`로 정수배만 키워 무손실 WebP로 저장한다(예 1920×1080). 정수배가 아닌 크기로 줄이거나 손실 압축하지 않는다.
3. og·썸네일은 원래 격자 그림에서 잘라 정수배로 키운다.
4. 장면 그림은 1200×800 WebP, 한 편 합계 600KB 이하.
