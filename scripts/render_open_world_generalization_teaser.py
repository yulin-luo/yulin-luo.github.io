#!/usr/bin/env python3
"""Render the homepage open-world generalization roadmap as a PNG.

The figure is intentionally rendered with PIL instead of model-generated text so
that all English labels remain exact and maintainable.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images" / "open_world_generalization_teaser_en.png"

W, H = 1672, 941
BG = "#fbf7ef"
NAVY = "#142436"
TEAL = "#0f6d72"
TEAL_LIGHT = "#62b6b3"
BLUE = "#174090"
BLUE_LIGHT = "#3d82e5"
GOLD = "#9a6c25"
GOLD_LIGHT = "#c58b22"
RED = "#d94a2b"
MUTED = "#5c6b75"
CARD = "#fbfffd"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

F_TITLE = font(SERIF_BOLD, 64)
F_SUBTITLE = font(SERIF_BOLD, 34)
F_SECTION = font(SERIF_BOLD, 30)
F_CARD_TITLE = font(SERIF_BOLD, 26)
F_CARD_SUB = font(SERIF_BOLD, 21)
F_BODY = font(SANS_BOLD, 18)
F_SMALL = font(SANS, 15)
F_TINY = font(SANS, 13)
F_LEVEL = font(SERIF_BOLD, 34)
F_AXIS = font(SERIF_BOLD, 29)
F_LEGEND = font(SERIF_BOLD, 26)


def bbox(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int, int, int]:
    return draw.textbbox((0, 0), text, font=fnt)


def text_center(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    x, y = xy
    b = bbox(draw, text, fnt)
    draw.text((x - (b[2] - b[0]) / 2, y - (b[3] - b[1]) / 2), text, font=fnt, fill=fill)


def text_right(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    x, y = xy
    b = bbox(draw, text, fnt)
    draw.text((x - (b[2] - b[0]), y), text, font=fnt, fill=fill)


def wrap_center(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    width_chars: int,
    lines: list[str] | str,
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    line_gap: int = 4,
) -> int:
    if isinstance(lines, str):
        real_lines = wrap(lines, width_chars)
    else:
        real_lines = []
        for line in lines:
            real_lines.extend(wrap(line, width_chars) or [""])
    cy = y
    for line in real_lines:
        text_center(draw, (x, cy), line, fnt, fill)
        cy += fnt.size + line_gap
    return cy


def shadowed_round_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str, width: int = 2) -> None:
    x0, y0, x1, y1 = box
    for off, alpha in [(7, 25), (3, 18)]:
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.rounded_rectangle((x0, y0 + off, x1, y1 + off), radius=radius, fill=(20, 52, 76, alpha))
        canvas.alpha_composite(overlay)
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def level_badge(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, color: str) -> None:
    draw.rounded_rectangle((x, y, x + 58, y + 58), radius=8, fill=color)
    text_center(draw, (x + 29, y + 31), label, F_LEVEL, "white")


def robot_arm(draw: ImageDraw.ImageDraw, x: int, y: int, scale: float = 1.0, color: str = NAVY) -> None:
    p = lambda v: int(v * scale)
    draw.line((x, y + p(42), x, y + p(20), x + p(28), y + p(12), x + p(38), y + p(28)), fill=color, width=max(2, p(2)))
    draw.ellipse((x - p(5), y + p(38), x + p(5), y + p(48)), fill=TEAL_LIGHT)


def mini_scene(draw: ImageDraw.ImageDraw, x: int, y: int, color: str = NAVY) -> None:
    for i in range(3):
        bx = x + i * 73
        draw.rectangle((bx, y, bx + 58, y + 44), fill="#f4f0e8", outline="#aeb9bc")
        robot_arm(draw, bx + 20, y + 8, 0.78, color)


def sun_cloud_moon(draw: ImageDraw.ImageDraw, x: int, y: int) -> None:
    draw.ellipse((x, y, x + 30, y + 30), outline=NAVY, width=3)
    for dx, dy in [(15, -13), (15, 43), (-13, 15), (43, 15), (0, 0), (31, 0), (0, 31), (31, 31)]:
        if dx in (0, 31) and dy in (0, 31):
            draw.line((x + 15, y + 15, x + dx, y + dy), fill=NAVY, width=2)
    cx = x + 82
    draw.arc((cx, y + 7, cx + 50, y + 37), 180, 360, fill=NAVY, width=3)
    draw.line((cx, y + 22, cx + 50, y + 22), fill=NAVY, width=3)
    mx = x + 160
    draw.arc((mx, y, mx + 50, y + 42), 70, 280, fill=NAVY, width=3)
    draw.arc((mx + 20, y - 2, mx + 70, y + 45), 105, 250, fill=BG, width=8)


def cube(draw: ImageDraw.ImageDraw, x: int, y: int) -> None:
    pts = [(x, y + 22), (x + 28, y + 8), (x + 56, y + 22), (x + 56, y + 58), (x + 28, y + 72), (x, y + 58)]
    draw.line(pts + [pts[0]], fill=NAVY, width=3)
    draw.line((x + 28, y + 8, x + 28, y + 42, x, y + 22), fill=NAVY, width=3)
    draw.line((x + 28, y + 42, x + 56, y + 22), fill=NAVY, width=3)


def person(draw: ImageDraw.ImageDraw, x: int, y: int) -> None:
    draw.ellipse((x + 20, y, x + 46, y + 26), outline=NAVY, width=3)
    draw.line((x + 33, y + 26, x + 33, y + 70), fill=NAVY, width=3)
    draw.line((x + 33, y + 38, x + 12, y + 62), fill=NAVY, width=3)
    draw.line((x + 33, y + 38, x + 56, y + 62), fill=NAVY, width=3)


def warning(draw: ImageDraw.ImageDraw, x: int, y: int, size: int = 48) -> None:
    draw.polygon([(x + size // 2, y), (x + size, y + size), (x, y + size)], outline=RED, fill=None)
    draw.line((x + size // 2, y + 17, x + size // 2, y + 34), fill=RED, width=3)
    draw.ellipse((x + size // 2 - 2, y + 40, x + size // 2 + 2, y + 44), fill=RED)


def draw_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    level: str,
    title_lines: list[str],
    sub: str,
    color: str,
    accent: str,
    body: callable,
) -> None:
    x0, y0, x1, y1 = box
    shadowed_round_rect(draw, box, 18, CARD if color != GOLD else "#fffaf0", accent, 2)
    draw.polygon([(x0, y1 - 28), (x1, y1 - 28), (x1 - 25, y1), (x0, y1)], fill=accent + "55")
    level_badge(draw, x0 + 16, y0 - 20, level, color)
    cy = y0 + 33
    for line in title_lines:
        text_center(draw, ((x0 + x1) // 2 + 16, cy), line, F_CARD_TITLE, color)
        cy += 31
    text_center(draw, ((x0 + x1) // 2 + 16, cy + 6), sub, F_CARD_SUB, color)
    body(draw, box)


def l1_body(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    y = y0 + 102
    pts = [(x0 + 75, y + 4), (x0 + 115, y - 4), (x0 + 165, y + 6), (x0 + 220, y - 12), (x0 + 260, y)]
    draw.line(pts, fill=NAVY, width=3, joint="curve")
    for px, py in [pts[0], pts[2]]:
        draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=BG, outline=TEAL, width=3)
    draw.line((x0 + 260, y, x0 + 248, y - 7), fill=NAVY, width=3)
    draw.line((x0 + 260, y, x0 + 248, y + 8), fill=NAVY, width=3)
    mini_scene(draw, x0 + 55, y0 + 140)
    wrap_center(draw, (x0 + x1) // 2, y1 - 60, 24, ["same task | same robot", "new initial states"], F_BODY, NAVY)


def l2_body(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    sun_cloud_moon(draw, x0 + 55, y0 + 118)
    draw.line((x0 + 48, y0 + 185, x1 - 45, y0 + 185), fill="#b3c5c7", width=1)
    mini_scene(draw, x0 + 35, y0 + 212)
    wrap_center(draw, (x0 + x1) // 2, y1 - 64, 23, ["lighting | viewpoint", "environment shift"], F_BODY, NAVY)


def l3_body(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    y = y0 + 130
    cube(draw, x0 + 60, y)
    draw.text((x0 + 135, y + 27), "+", font=F_CARD_TITLE, fill=NAVY)
    draw.rounded_rectangle((x0 + 173, y + 20, x0 + 214, y + 74), radius=9, outline=NAVY, width=3)
    draw.text((x0 + 232, y + 27), "+", font=F_CARD_TITLE, fill=NAVY)
    person(draw, x0 + 262, y + 12)
    draw.line((x0 + 35, y0 + 230, x1 - 35, y0 + 230), fill="#b3c5c7", width=1)
    robot_arm(draw, x0 + 55, y0 + 270, 1.15)
    draw.rectangle((x0 + 145, y0 + 258, x0 + 222, y0 + 325), outline=NAVY, width=3)
    text_center(draw, (x0 + 183, y0 + 293), "instruction", F_TINY, NAVY)
    wrap_center(draw, (x0 + x1) // 2, y1 - 72, 24, ["objects | attributes", "instruction recombination"], F_BODY, NAVY)


def l4_body(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    cell_y = y0 + 120
    labels = ["mechanism", "do(.)", "prediction error"]
    for i, lab in enumerate(labels):
        cx = x0 + 22 + i * 91
        draw.rounded_rectangle((cx, cell_y, cx + 82, cell_y + 98), radius=8, fill="#ffffff", outline="#ced9e4")
        text_center(draw, (cx + 41, cell_y + 22), lab, F_TINY, NAVY)
    robot_arm(draw, x0 + 52, cell_y + 42, 0.75)
    draw.line((x0 + 128, cell_y + 48, x0 + 180, cell_y + 48), fill=NAVY, width=3)
    draw.line((x0 + 128, cell_y + 70, x0 + 180, cell_y + 70), fill=NAVY, width=3)
    draw.ellipse((x0 + 133, cell_y + 44, x0 + 139, cell_y + 50), fill=NAVY)
    draw.ellipse((x0 + 166, cell_y + 66, x0 + 172, cell_y + 72), fill=NAVY)
    draw.line((x0 + 215, cell_y + 72, x0 + 230, cell_y + 52, x0 + 248, cell_y + 63, x0 + 270, cell_y + 29), fill=NAVY, width=3)
    warning(draw, x0 + 265, cell_y + 50, 42)
    cy = y0 + 278
    circles = [
        ((x0 + 82, cy + 95), "perception"),
        ((x0 + 180, cy + 40), "model\npredict"),
        ((x0 + 274, cy + 95), "error\neval"),
        ((x0 + 180, cy + 178), "reflect\nreplan"),
    ]
    for (cx, ccy), lab in circles:
        draw.ellipse((cx - 36, ccy - 36, cx + 36, ccy + 36), fill="#ffffff", outline="#9db4c9", width=2)
        split_lab = lab.split("\n")
        base_y = ccy - 7 if len(split_lab) > 1 else ccy
        for j, line in enumerate(split_lab):
            text_center(draw, (cx, base_y + j * 15), line, F_TINY, NAVY)
    draw.arc((x0 + 82, cy + 25, x0 + 278, cy + 182), 205, 335, fill=NAVY, width=3)
    draw.arc((x0 + 82, cy + 25, x0 + 278, cy + 182), 25, 155, fill=NAVY, width=3)


def l5_body(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    text_center(draw, ((x0 + x1) // 2, y0 + 128), "task stream (ongoing)", F_BODY, NAVY)
    for i, t in enumerate(["t1", "tk", "tn"]):
        bx = x0 + 34 + i * 95
        draw.rounded_rectangle((bx, y0 + 155, bx + 60, y0 + 222), radius=9, fill="#fffdf7", outline=GOLD_LIGHT, width=2)
        text_center(draw, (bx + 30, y0 + 178), "task", F_TINY, NAVY)
        text_center(draw, (bx + 30, y0 + 205), t, F_CARD_TITLE, GOLD)
    text_center(draw, (x0 + 124, y0 + 187), "...", F_CARD_TITLE, GOLD)
    text_center(draw, (x0 + 219, y0 + 187), "...", F_CARD_TITLE, GOLD)
    draw.line((x0 + 35, y0 + 252, x1 - 35, y0 + 252), fill="#d2af72", width=1)
    labels = [("memory", x0 + 36), ("tools", x0 + 126), ("knowledge graph", x0 + 210)]
    for lab, lx in labels:
        text_center(draw, (lx + 28, y0 + 282), lab, F_TINY, NAVY)
    draw.ellipse((x0 + 38, y0 + 310, x0 + 88, y0 + 330), outline=GOLD, width=3)
    draw.rectangle((x0 + 38, y0 + 320, x0 + 88, y0 + 365), outline=GOLD, width=3)
    draw.ellipse((x0 + 38, y0 + 354, x0 + 88, y0 + 374), outline=GOLD, width=3)
    gx = x0 + 130
    for i in range(3):
        draw.line((gx, y0 + 310 + i * 18, gx + 54, y0 + 310 + i * 18), fill=GOLD, width=2)
        draw.line((gx + i * 18, y0 + 310, gx + i * 18, y0 + 364), fill=GOLD, width=2)
    draw.rectangle((gx + 19, y0 + 329, gx + 35, y0 + 345), fill="#d8a335")
    nodes = [(x0 + 228, y0 + 340), (x0 + 260, y0 + 314), (x0 + 294, y0 + 350), (x0 + 264, y0 + 375)]
    for a, b in zip(nodes, nodes[1:] + nodes[:1]):
        draw.line((*a, *b), fill=GOLD, width=3)
    for px, py in nodes:
        draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=GOLD_LIGHT)
    draw.line((x0 + 35, y0 + 405, x1 - 35, y0 + 405), fill="#d2af72", width=1)
    text_center(draw, (x0 + 83, y0 + 437), "safety", F_TINY, NAVY)
    shield = [(x0 + 62, y0 + 460), (x0 + 92, y0 + 474), (x0 + 92, y0 + 512), (x0 + 62, y0 + 540), (x0 + 32, y0 + 512), (x0 + 32, y0 + 474)]
    draw.line(shield + [shield[0]], fill=GOLD, width=3)
    draw.line((x0 + 50, y0 + 501, x0 + 60, y0 + 512, x0 + 80, y0 + 486), fill=GOLD, width=3)
    text_center(draw, (x0 + 220, y0 + 437), "long-term growth", F_TINY, NAVY)
    base_x, base_y = x0 + 158, y0 + 522
    draw.line((base_x, base_y, base_x + 145, base_y), fill="#d6c097", width=1)
    draw.line((base_x, base_y, base_x, base_y - 82), fill="#d6c097", width=1)
    pts = [(base_x + 22, base_y - 18), (base_x + 58, base_y - 30), (base_x + 92, base_y - 42), (base_x + 130, base_y - 75)]
    draw.line(pts, fill=GOLD, width=3)
    for px, py in pts:
        draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=GOLD_LIGHT)


canvas = Image.new("RGBA", (W, H), BG)
draw = ImageDraw.Draw(canvas)

# Background curves
for i, y in enumerate([38, 98, 158]):
    draw.arc((1020 - i * 20, y, 1690, y + 120), 190, 345, fill="#d5bd94", width=2)

draw.text((55, 42), "Open-World Generalization", font=F_TITLE, fill=NAVY)
draw.text((58, 108), "for Embodied Intelligence", font=F_SUBTITLE, fill=GOLD)
draw.text((58, 151), "from interpolation to open-world accumulation", font=font(SERIF_BOLD, 26), fill=GOLD)

# Vertical OOD axis
draw.line((66, 745, 66, 206), fill=TEAL, width=7)
draw.polygon([(66, 198), (51, 227), (81, 227)], fill=TEAL)
axis_label = "Structured OOD progressively strengthens"
rot = Image.new("RGBA", (420, 42), (0, 0, 0, 0))
rd = ImageDraw.Draw(rot)
rd.text((0, 0), axis_label, font=F_BODY, fill=TEAL)
canvas.alpha_composite(rot.rotate(90, expand=True), (18, 340))

# Guide lines and brackets
for y in [315, 390, 465, 540]:
    draw.line((110, y, 880, y), fill="#bbc6ca", width=1)
    for x in range(110, 880, 18):
        draw.line((x, y, x + 8, y), fill="#bbc6ca", width=1)
draw.line((108, 270, 108, 260, 862, 260, 862, 270), fill=TEAL, width=3)
text_center(draw, (485, 235), "Foundation Model Coverage + Evaluation Gates", F_SECTION, TEAL)
draw.line((883, 132, 883, 122, 1505, 122, 1505, 132), fill=BLUE, width=3)
text_center(draw, (1194, 99), "Core Research Frontier", F_SECTION, BLUE)

# Cards
draw_card(draw, (82, 496, 366, 758), "L1", ["In-Domain"], "Interpolation", TEAL, TEAL_LIGHT, l1_body)
draw_card(draw, (368, 430, 623, 758), "L2", ["Shift", "Robustness"], "Invariance", TEAL, TEAL_LIGHT, l2_body)
draw_card(draw, (636, 360, 884, 758), "L3", ["Compositional", "Systematic"], "Recomposition", TEAL, "#5a98b0", l3_body)
draw_card(draw, (904, 244, 1206, 758), "L4", ["Causal", "Mechanistic"], "Intervention", BLUE, BLUE_LIGHT, l4_body)
draw_card(draw, (1216, 164, 1518, 758), "L5", ["Open-World", "Continual"], "Accumulation", GOLD, GOLD_LIGHT, l5_body)

# Side note
shadowed_round_rect(draw, (1554, 380, 1658, 696), 20, "#fffdf8", "#d7d0c1", 1)
draw.ellipse((1576, 414, 1636, 474), fill="#f9fbfd", outline="#cfd9e5")
draw.line((1590, 448, 1628, 420), fill=NAVY, width=3)
draw.line((1628, 420, 1624, 440), fill=NAVY, width=3)
draw.line((1628, 420, 1608, 425), fill=NAVY, width=3)
for i, line in enumerate(["OOD is", "a train/test", "relation,", "not a", "single level"]):
    text_center(draw, (1606, 510 + i * 42), line, font(SERIF_BOLD, 24), NAVY)

# Bottom arrow
draw.polygon([(78, 758), (1510, 758), (1534, 779), (1510, 800), (78, 800)], fill="#80aba6")
for x, label in [(240, "Interpolation"), (500, "Invariance"), (780, "Recomposition"), (1080, "Intervention"), (1390, "Accumulation")]:
    text_center(draw, (x, 783), label, F_AXIS, "white")
for x in [355, 620, 920, 1205]:
    draw.line((x, 780, x + 38, 780), fill="white", width=5)
    draw.polygon([(x + 38, 780), (x + 28, 773), (x + 28, 787)], fill="white")

# Legend
shadowed_round_rect(draw, (48, 826, 1568, 912), 12, "#fffdf8", "#cdbf9f", 1)
for x in [373, 690, 1024, 1272]:
    draw.line((x, 838, x, 900), fill="#c7b99a", width=1)
draw.ellipse((130, 852, 184, 906), outline=NAVY, width=3)
draw.ellipse((151, 873, 163, 885), outline=NAVY, width=2)
draw.line((157, 846, 157, 912), fill=NAVY, width=2)
draw.line((124, 879, 190, 879), fill=NAVY, width=2)
draw.text((218, 868), "Target Level", font=F_LEGEND, fill=NAVY)
warning(draw, 470, 848, 60)
draw.text((562, 868), "Failure Mode", font=F_LEGEND, fill=NAVY)
draw.line((776, 892, 826, 842), fill=TEAL, width=6)
draw.arc((764, 838, 826, 900), 35, 285, fill=TEAL, width=5)
draw.text((856, 868), "Method Shift", font=F_LEGEND, fill=NAVY)
for i, h in enumerate([30, 48, 66]):
    draw.rectangle((1046 + i * 24, 912 - h, 1061 + i * 24, 912), fill=TEAL)
draw.line((1038, 912, 1122, 912), fill=TEAL, width=4)
draw.text((1142, 868), "Evidence", font=F_LEGEND, fill=NAVY)
shield = [(1320, 852), (1352, 838), (1384, 852), (1384, 892), (1352, 920), (1320, 892)]
draw.line(shield + [shield[0]], fill=RED, width=4)
draw.line((1338, 879, 1350, 893, 1370, 866), fill=RED, width=4)
draw.text((1408, 868), "Counterclaim", font=F_LEGEND, fill=NAVY)

OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(OUT, quality=95)
print(OUT)
