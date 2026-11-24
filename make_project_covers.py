# -*- coding: utf-8 -*-
"""Minimalist black-and-white project cover cards for the AI governance portfolio.
Drawn at 2x then downscaled for crisp edges. Output: project1-cover.png, project2-cover.png
"""
from PIL import Image, ImageDraw, ImageFont

FDIR = "C:/Users/Femi Fayinminu/OneDrive/Documents/Algolog/Algolog_Projects/fonts/lexend-main/fonts/deca/ttf"
S = 2  # supersample
W, H = 1200 * S, 630 * S
BLACK = (17, 17, 17)
GREY = (90, 90, 90)
LGREY = (150, 150, 150)
RULE = (220, 220, 220)


def F(name, size):
    return ImageFont.truetype(f"{FDIR}/{name}.ttf", size * S)


def tracked(draw, xy, text, font, fill, spacing):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + spacing * S


def motif_scale(d, cx, cy):
    """A simple balance scale, thin line art."""
    lw = 3 * S
    r = 70 * S
    d.line([(cx, cy - r), (cx, cy + r)], fill=BLACK, width=lw)          # post
    d.line([(cx - r, cy - r), (cx + r, cy - r)], fill=BLACK, width=lw)  # beam
    d.polygon([(cx - 14 * S, cy + r), (cx + 14 * S, cy + r), (cx, cy + r - 20 * S)], outline=BLACK)  # base
    for ex in (cx - r, cx + r):                                         # pans
        d.line([(ex, cy - r), (ex - 22 * S, cy - r + 34 * S)], fill=BLACK, width=lw)
        d.line([(ex, cy - r), (ex + 22 * S, cy - r + 34 * S)], fill=BLACK, width=lw)
        d.arc([ex - 26 * S, cy - r + 20 * S, ex + 26 * S, cy - r + 54 * S], 0, 180, fill=BLACK, width=lw)


def motif_shield(d, cx, cy):
    """A simple shield with a plus, thin line art."""
    lw = 3 * S
    w, h = 60 * S, 44 * S
    pts = [(cx - w, cy - h), (cx + w, cy - h), (cx + w, cy + h // 2),
           (cx, cy + h + 40 * S), (cx - w, cy + h // 2)]
    d.line(pts + [pts[0]], fill=BLACK, width=lw, joint="curve")
    d.line([(cx, cy - 18 * S), (cx, cy + 34 * S)], fill=BLACK, width=lw)   # plus v
    d.line([(cx - 26 * S, cy + 8 * S), (cx + 26 * S, cy + 8 * S)], fill=BLACK, width=lw)  # plus h


def card(fname, label, title_lines, sub_lines, tag, motif):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    # border
    m = 26 * S
    d.rectangle([m, m, W - m, H - m], outline=BLACK, width=2 * S)
    lab_f = F("LexendDeca-Medium", 17)
    title_f = F("LexendDeca-SemiBold", 52)
    sub_f = F("LexendDeca-Light", 23)
    tag_f = F("LexendDeca-Regular", 19)

    pad = 72 * S
    tracked(d, (pad, 70 * S), label.upper(), lab_f, GREY, 3)

    y = 180 * S
    for ln in title_lines:
        d.text((pad, y), ln, font=title_f, fill=BLACK)
        y += 66 * S
    y += 18 * S
    for ln in sub_lines:
        d.text((pad, y), ln, font=sub_f, fill=(70, 70, 70))
        y += 34 * S

    # bottom rule + tag
    ry = H - 118 * S
    d.line([(pad, ry), (W - pad, ry)], fill=RULE, width=2 * S)
    tracked(d, (pad, ry + 26 * S), tag, tag_f, GREY, 1)

    # motif top-right
    motif(d, W - 150 * S, 150 * S)

    img = img.resize((W // S, H // S), Image.LANCZOS)
    img.save(fname)
    print("wrote", fname)


card("project1-cover.png",
     "AI Governance  /  Project 01",
     ["Credit Decision:", "Bias & Data-Drift Audit"],
     ["Fairness and data-drift checks on an automated",
      "credit-approval model, framed to the NIST AI RMF."],
     "Python   \u00b7   scikit-learn   \u00b7   NIST AI RMF",
     motif_scale)

card("project2-cover.png",
     "AI Governance  /  Project 02",
     ["Healthcare AI Triage:", "NIST AI RMF Risk Assessment"],
     ["A full risk register and build-ready controls",
      "for a clinical-intake AI assistant."],
     "NIST AI RMF   \u00b7   EU AI Act   \u00b7   NDPA",
     motif_shield)
