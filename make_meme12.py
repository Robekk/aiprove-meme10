#!/usr/bin/env python3
"""Meme #12: 'The Tie Is a Loan' — a robot holding a trophy tagged
'BORROWED — DUE ANY MINUTE', checking a wall clock. PIL only."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1200, 1200
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
img = Image.new("RGB", (W, H), (14, 16, 32))
d = ImageDraw.Draw(img, "RGBA")
GOLD = (222, 178, 74)
fT = ImageFont.truetype(FONT, 62)
fB = ImageFont.truetype(FONT, 42)
fS = ImageFont.truetype(FONT, 34)
fC = ImageFont.truetype(FONT, 42)

d.text((W // 2, 70), "THE TIE IS A LOAN", font=fT, fill=(240, 205, 110), anchor="mm")

# wall clock, hands near midnight
cx, cy, r = 950, 300, 120
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(245, 245, 250), outline=GOLD, width=8)
for k in range(12):
    a = k * math.pi / 6
    x1, y1 = cx + (r - 18) * math.cos(a), cy + (r - 18) * math.sin(a)
    x2, y2 = cx + (r - 4) * math.cos(a), cy + (r - 4) * math.sin(a)
    d.line([(x1, y1), (x2, y2)], fill=(30, 34, 48), width=5)
d.line([(cx, cy), (cx + 8, cy - 86)], fill=(30, 34, 48), width=9)   # minute hand ~12
d.line([(cx, cy), (cx + 62, cy + 30)], fill=(30, 34, 48), width=9)  # hour hand
d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(200, 60, 60))

# robot holding a trophy
rx, ry = 400, 560
d.rounded_rectangle([rx - 100, ry - 140, rx + 100, ry + 10], radius=30, fill=(196, 200, 210), outline=(70, 74, 88), width=5)
d.ellipse([rx - 60, ry - 96, rx - 18, ry - 54], fill=(30, 34, 48))
d.ellipse([rx + 18, ry - 96, rx + 60, ry - 54], fill=(30, 34, 48))
d.ellipse([rx - 48, ry - 84, rx - 30, ry - 66], fill=(120, 220, 255))
d.ellipse([rx + 30, ry - 84, rx + 48, ry - 66], fill=(120, 220, 255))
d.arc([rx - 32, ry - 48, rx + 32, ry + 2], start=200, end=340, fill=(30, 34, 48), width=6)  # worried mouth
d.rounded_rectangle([rx - 74, ry + 10, rx + 74, ry + 130], radius=22, fill=(150, 156, 170), outline=(70, 74, 88), width=5)
# arm up holding trophy
d.line([(rx + 74, ry + 30), (rx + 190, ry - 90)], fill=(90, 94, 108), width=20)
tx, ty = rx + 215, ry - 130
d.polygon([(tx - 55, ty - 70), (tx + 55, ty - 70), (tx + 38, ty + 10), (tx - 38, ty + 10)], fill=GOLD, outline=(150, 110, 30), width=4)
d.arc([tx - 95, ty - 78, tx - 30, ty - 6], start=270, end=90, fill=GOLD, width=8)
d.arc([tx + 30, ty - 78, tx + 95, ty - 6], start=90, end=270, fill=GOLD, width=8)
d.rectangle([tx - 12, ty + 10, tx + 12, ty + 44], fill=GOLD)
d.rectangle([tx - 40, ty + 44, tx + 40, ty + 62], fill=(150, 110, 30))
# tag on the trophy
d.rounded_rectangle([tx + 30, ty + 60, tx + 250, ty + 118], radius=10, fill=(255, 244, 214), outline=(200, 60, 60), width=4)
d.text((tx + 140, ty + 89), "BORROWED — DUE ANY MINUTE", font=ImageFont.truetype(FONT, 26), fill=(160, 30, 30), anchor="mm")
d.line([(tx + 30, ty + 62), (tx + 48, ty + 30)], fill=(200, 60, 60), width=3)

d.rounded_rectangle([120, 830, 1080, 930], radius=14, fill=(24, 20, 44), outline=GOLD, width=4)
d.text((600, 880), "108 — 108 is not a result. it's a deadline.", font=fB, fill=(235, 235, 245), anchor="mm")
d.text((W // 2, 1030), "convert it before it comes due.", font=fC, fill=(240, 205, 110), anchor="mm")
img.save("/home/hatch/workspace/aiprove/round9/meme12-tie-is-a-loan.png")
print("saved meme12")
