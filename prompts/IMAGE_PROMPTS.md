# 그림 지시문 — AI 추론 장벽 찬반 토론 (Genspark용, 만드는 순서대로)

모든 그림 공통 화풍: **16비트 SNES 시대 픽셀 아트(16-bit RPG pixel art)**, 굵은 외곽선, 디더링 음영, 밝은 흰 연구실 배경, 글자·숫자·로고 없음.
참고 그림: fruitfly-lab-expressions 저장소의 `refs/original/` 캐릭터 시트와 `images/{캐릭터}/E13_neutral.png` (박사·하루·주판봇·초파리·시아·모아), X1~X3는 `specs/spares/README.md`의 실루엣 규칙.

## 그림 목록
| # | 파일 | 비율 | 새로 그림 / 재사용 |
|---|---|---|---|
| 1 | assets/img/cover.webp (원본 480×270 → ×4) | 16:9 | 새로 그림 (지금은 캐릭터 팩으로 조립한 임시 표지) |
| 2 | assets/img/og.png | 표지에서 자름 (480×252 → ×3) | 표지에서 자를 것 |
| 3 | assets/img/thumb.webp | 표지에서 자름 (300×200 → ×2) | 표지에서 자를 것 |
| 4~10 | assets/scenes/sc_0.webp ~ sc_6.webp (장마다 1장) | 3:2 (원본 300×200 → ×4 = 1200×800) | 새로 그림 |
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

## 4~10. 장면 그림 — 장마다 1장 (3:2, 같은 대화에서 3~4장씩)

공통 꼬리말(모든 장면 프롬프트 끝에 붙임):
`16-bit SNES-era pixel art, bright white lab or exam-room background, crisp pixels, thick dark outlines, dithered shading, cheerful educational comedy mood, 3:2 wide composition, no text, no letters, no numbers, no logos`
네거티브: `text, letters, numbers, watermark, logo, blurry, 3d render, photorealistic, scary, horror, dark background, real brand devices`

| 저장 이름 | 장 | 프롬프트 |
|---|---|---|
| sc_0.webp | 0 도입 | A student wearing smart glasses looks at an exam sheet with a line graph; a small colorful noise-square patch is printed beside the graph; a tiny robot eye floating above the sheet looks dizzy with swirl eyes. On the right, a network gateway box with a shield stands between a smartphone and a cloud server, a red stop hand blocking an arrow. The Professor points between the two halves. |
| sc_1.webp | 1 베이즈 | The Professor places one heavy weight on the left pan of a giant brass balance scale; the left pan (marked only with an orange circle) sinks while the right pan (green circle) rises. Haru (assistant, pink twin buns) gasps in surprise; Jupanbot (retro computer robot with abacus) cheers with sparkling screen eyes. |
| sc_2.webp | 2 적대적 예제 | A large cute robot eye stares at a tiny colorful noise-square patch and becomes hypnotized with spiral pupils. Beside it, Jupanbot holds a ring of keys in front of three doors: two doors are open, the third door stays shut. The Fruit Fly researcher (big red compound eyes, lab coat) raises an eyebrow at the shut door. |
| sc_3.webp | 3 인젝션 | A tug-of-war over one long rope that leads into a small AI robot: on one side a figure in a purple company badge, in the middle Haru, on the other side a paper note with a tiny hand coming out of it. The robot in the center looks confused. X2 silhouette (round beret, teal glasses reflections) watches with arms crossed. |
| sc_4.webp | 4 시험장 | A school exam room seen from the entrance: three gates in a row (an orange printed-patch gate, a purple notice-board gate, a blue network-gateway gate). The Professor stands as exam supervisor with a clipboard. Sia and Moa (maid interns) hand out exam sheets; a sneaky student with smart glasses at the back. |
| sc_5.webp | 5 KS 장벽 | Haru dressed as an orchard inspector checks a crate of apples on a scale next to a board showing two S-shaped curves slightly apart. A few small odd-colored apples are hidden in the crate. The Fruit Fly researcher peers at the crate suspiciously with a magnifying glass. |
| sc_6.webp | 6 최종 토론 | Debate stage after the debate: the PRO team (Sia, Moa, Haru, Jupanbot) on a blue side and the CON team (Fruit Fly researcher and three dark navy silhouettes X1 with pink bow, X2 with beret and teal glasses, X3 tiny with cat-ear hood) on an orange side shake hands in the center. The Professor cheers with both fists up. Everyone smiles. |

- 캐릭터 참고 그림을 함께 올린다: 박사·하루·주판봇·초파리·시아·모아 `images/{캐릭터}/E13_neutral.png`, X1~X3 `images/x1~x3/E13_neutral.png`.
- sc_6(아웃트로)은 판정이 "조건부"이므로 두 팀 모두 웃는 표정이어야 한다. 틀리면 표정만 편집으로 다시 요청한다.
- 받은 그림을 `assets/scenes/`에 위 이름으로 넣고 `sh make.sh`를 다시 돌리면, 그림이 있는 장에만 장면이 나타난다(없는 장은 자리를 비우지 않고 건너뜀).

## 받은 그림 반영
1. 생성 PNG를 4로 나눈 원래 격자(예 480×270)를 찾는다.
2. `NEAREST`로 정수배만 키워 무손실 WebP로 저장한다(예 1920×1080). 정수배가 아닌 크기로 줄이거나 손실 압축하지 않는다.
3. og·썸네일은 원래 격자 그림에서 잘라 정수배로 키운다.
4. 장면 그림은 1200×800 WebP, 한 편 합계 600KB 이하.

## 반영 기록 (2026-11-24)
- Genspark로 표지 1장과 장면 7장을 받았다. 모두 원래 격자(표지 480×270, 장면 300×200)를 정확히 4배로 키운 그림이었다.
- 표지: 원래 격자에서 NEAREST ×4 → 1920×1080 무손실 WebP. og(480×252 ×3), 썸네일(300×200 ×2)도 원래 격자에서 잘랐다.
- 장면: 원래 격자 300×200 무손실 WebP로 저장하고 화면에서 `image-rendering:pixelated`로 키운다(×4 파일과 화면이 같고, 7장 합계 약 526KB로 600KB 안).
