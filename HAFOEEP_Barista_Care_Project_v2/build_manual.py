#!/usr/bin/env python3
"""Build a 4-page German A5 booklet imposed on two A4-landscape PDF sides.

Without --qr-url, a clear QR replacement box is shown on the back cover.
After the Streamlit app is deployed, rebuild with:
  python build_manual.py --qr-url https://your-live-app.streamlit.app
"""
from __future__ import annotations
import argparse
from io import BytesIO
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import qrcode
from qrcode.constants import ERROR_CORRECT_H

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "manual" / "HAFOEEP_Barista_Care_Manual_DE_Print.pdf"
PAGE_W, PAGE_H = landscape(A4)
PANEL_W, PANEL_H = PAGE_W / 2, PAGE_H
INK = HexColor("#17191C")
INK2 = HexColor("#25292E")
SILVER = HexColor("#C5C9CE")
MID = HexColor("#717981")
TEXT = HexColor("#2A2D31")
MUTED = HexColor("#5D646C")
PAPER = HexColor("#F2F3F1")
WHITE = colors.white

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if Path(FONT_REG).exists():
    pdfmetrics.registerFont(TTFont("HAFOEEP", FONT_REG))
    pdfmetrics.registerFont(TTFont("HAFOEEP-Bold", FONT_BOLD))
    F_REG, F_BOLD = "HAFOEEP", "HAFOEEP-Bold"
else:
    F_REG, F_BOLD = "Helvetica", "Helvetica-Bold"

styles = {
    "body": ParagraphStyle("body", fontName=F_REG, fontSize=7.5, leading=10, textColor=TEXT, spaceAfter=0),
    "body_small": ParagraphStyle("body_small", fontName=F_REG, fontSize=6.8, leading=8.5, textColor=TEXT, spaceAfter=0),
    "body_light": ParagraphStyle("body_light", fontName=F_REG, fontSize=7.4, leading=10, textColor=HexColor("#D8DBDE"), spaceAfter=0),
    "tiny": ParagraphStyle("tiny", fontName=F_REG, fontSize=6, leading=7.4, textColor=MUTED, spaceAfter=0),
}

def para(c, text, x, y_top, width, style="body", max_h=100):
    p = Paragraph(text, styles[style])
    w, h = p.wrap(width, max_h)
    p.drawOn(c, x, y_top - h)
    return h

def draw_logo(c, x, y, scale=1, silver=True):
    col = SILVER if silver else INK
    c.saveState()
    c.setFillColor(col)
    # Geometric H monogram.
    c.rect(x, y, 7*scale, 27*scale, fill=1, stroke=0)
    c.rect(x+21*scale, y, 7*scale, 27*scale, fill=1, stroke=0)
    c.rect(x+6*scale, y+11*scale, 16*scale, 6*scale, fill=1, stroke=0)
    # Abstract steam lines.
    c.setStrokeColor(col)
    c.setLineWidth(1.3*scale)
    for dx in (9, 14, 19):
        p = c.beginPath(); p.moveTo(x+dx*scale, y+30*scale); p.curveTo(x+(dx-3)*scale, y+35*scale, x+(dx+3)*scale, y+38*scale, x+dx*scale, y+43*scale); c.drawPath(p, stroke=1, fill=0)
    c.setFillColor(col)
    c.setFont(F_BOLD, 11*scale)
    c.drawString(x+37*scale, y+17*scale, "HAFOEEP")
    c.setFont(F_REG, 4.7*scale)
    c.drawString(x+37*scale, y+7*scale, "PRECISION COFFEE CARE")
    c.restoreState()

def draw_texture(c, x, y, w, h, kind, bg, fg):
    c.saveState(); c.setFillColor(bg); c.roundRect(x, y, w, h, 4, fill=1, stroke=0)
    clip = c.beginPath(); clip.roundRect(x, y, w, h, 4); c.clipPath(clip, stroke=0, fill=0)
    c.setStrokeColor(fg); c.setLineWidth(0.5)
    if kind == "plush":
        for xx in range(int(x+5), int(x+w-2), 6):
            for yy in range(int(y+4), int(y+h-2), 6):
                c.circle(xx, yy, 1.05, stroke=1, fill=0)
    elif kind == "waffle":
        for xx in range(int(x+4), int(x+w), 7): c.line(xx, y+3, xx, y+h-3)
        for yy in range(int(y+4), int(y+h), 7): c.line(x+3, yy, x+w-3, yy)
    elif kind == "fine":
        for off in range(-int(h), int(w), 4): c.line(x+off, y+2, x+off+h, y+h-2)
    else:
        for off in range(4, int(w), 8): c.line(x+off, y+3, x+off, y+h-3)
    c.restoreState()

def draw_front(c, x):
    c.saveState()
    c.setFillColor(INK); c.rect(x, 0, PANEL_W, PANEL_H, fill=1, stroke=0)
    # Subtle technical grid accent, intentionally low-contrast.
    c.setStrokeColor(HexColor("#31363B")); c.setLineWidth(0.45)
    for yy in range(90, 520, 36): c.line(x+18, yy, x+PANEL_W-18, yy)
    # Brand and index.
    draw_logo(c, x+27, PANEL_H-84, scale=1.05, silver=True)
    c.setFont(F_BOLD, 7); c.setFillColor(SILVER); c.drawRightString(x+PANEL_W-24, PANEL_H-39, "4-TEILIG")
    c.setStrokeColor(MID); c.setLineWidth(0.7); c.line(x+27, PANEL_H-104, x+PANEL_W-27, PANEL_H-104)
    c.setFillColor(WHITE); c.setFont(F_BOLD, 20); c.drawString(x+27, PANEL_H-151, "BARISTA CARE")
    c.setFont(F_BOLD, 16); c.drawString(x+27, PANEL_H-174, "REINIGUNGSTUCH-SET")
    c.setFillColor(SILVER); c.setFont(F_REG, 7.1); c.drawString(x+28, PANEL_H-195, "REINIGEN  ·  TROCKNEN  ·  POLIEREN")
    # Fine line illustration of a group head / portafilter on the upper right.
    c.saveState(); c.setStrokeColor(HexColor("#7E858C")); c.setLineWidth(0.9)
    gx, gy = x+PANEL_W-110, PANEL_H-270
    c.roundRect(gx-36, gy+27, 72, 24, 4, fill=0, stroke=1)
    c.line(gx-25, gy+27, gx-25, gy+11); c.line(gx+25, gy+27, gx+25, gy+11)
    c.line(gx-25, gy+11, gx+25, gy+11); c.line(gx, gy+11, gx, gy-5)
    c.line(gx-12, gy-5, gx+12, gy-5); c.line(gx-12, gy-5, gx-17, gy-18); c.line(gx+12, gy-5, gx+17, gy-18)
    c.line(gx+12, gy-5, gx+67, gy-22); c.line(gx+67, gy-22, gx+88, gy-22)
    c.restoreState()
    # Textile swatches: two similar microfiber textures, waffle, polish.
    labels = [("CLEAN", "plush"), ("CLEAN", "loops"), ("DRY", "waffle"), ("POLISH", "fine")]
    sw_w, sw_h, gap = 72, 52, 8
    start_x = x+25; base_y = 88
    for i, (lab, kind) in enumerate(labels):
        xx = start_x + i*(sw_w+gap)
        draw_texture(c, xx, base_y+22, sw_w, sw_h, kind, HexColor("#555B61"), HexColor("#9299A0"))
        c.setFillColor(SILVER); c.setFont(F_BOLD, 6.3); c.drawCentredString(xx+sw_w/2, base_y+9, lab)
    c.setFillColor(HexColor("#A8AEB4")); c.setFont(F_REG, 6)
    c.drawString(x+26, 35, "4 TÜCHER. 3 AUFGABEN. EINE KLARE ROUTINE.")
    c.restoreState()

def draw_back_cover(c, x, qr_url=None):
    c.saveState(); c.setFillColor(PAPER); c.rect(x, 0, PANEL_W, PANEL_H, fill=1, stroke=0)
    draw_logo(c, x+25, PANEL_H-72, scale=0.8, silver=False)
    c.setFillColor(INK); c.setFont(F_BOLD, 14); c.drawString(x+25, PANEL_H-112, "PFLEGE & HINWEISE")
    c.setStrokeColor(HexColor("#B9BEC2")); c.line(x+25, PANEL_H-123, x+PANEL_W-25, PANEL_H-123)
    items = [
        ("VOR DEM ERSTEN GEBRAUCH", "Alle Tücher vor der ersten Anwendung waschen."),
        ("RICHTIG WASCHEN", "Pflegeetikett beachten. Keinen Weichspüler oder Bleichmittel verwenden."),
        ("GETRENNT VERWENDEN", "Die beiden Mikrofasertücher möglichst dauerhaft ihren Reinigungsbereichen zuordnen."),
        ("OBERFLÄCHEN SCHONEN", "Lose Partikel zuerst entfernen. Empfindliche oder beschichtete Flächen an unauffälliger Stelle testen."),
    ]
    y = PANEL_H-146
    for i, (head, body) in enumerate(items):
        c.setFillColor(INK); c.setFont(F_BOLD, 6.9); c.drawString(x+27, y, head)
        h = para(c, body, x+27, y-7, PANEL_W-54, "body_small", max_h=35)
        y -= 28 + h
    # QR callout area.
    qx, qy, qs = x+25, 51, 78
    c.setFillColor(WHITE); c.roundRect(qx, qy, qs, qs, 6, fill=1, stroke=0)
    if qr_url:
        qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data(qr_url); qr.make(fit=True)
        img = qr.make_image(fill_color="#17191c", back_color="white").convert("RGB")
        buf = BytesIO(); img.save(buf, format="PNG"); buf.seek(0)
        from reportlab.lib.utils import ImageReader
        c.drawImage(ImageReader(buf), qx+7, qy+7, width=qs-14, height=qs-14, mask="auto")
        label = "DIGITALE ANLEITUNG"
        sub = "Anwendungsbeispiele und Tuch-Zuordnung scannen."
    else:
        c.setStrokeColor(HexColor("#8A9096")); c.setDash(3, 3); c.rect(qx+8, qy+8, qs-16, qs-16, fill=0, stroke=1); c.setDash()
        c.setFillColor(MID); c.setFont(F_BOLD, 7); c.drawCentredString(qx+qs/2, qy+qs/2+2, "QR")
        c.setFont(F_REG, 5.5); c.drawCentredString(qx+qs/2, qy+qs/2-8, "HIER EINFÜGEN")
        label = "DIGITALE ANLEITUNG"
        sub = "QR-Code nach Veröffentlichung der Webseite einsetzen."
    tx = qx+qs+12
    c.setFillColor(INK); c.setFont(F_BOLD, 8); c.drawString(tx, qy+qs-17, label)
    para(c, sub, tx, qy+qs-25, PANEL_W-(tx-x)-22, "body_small", max_h=50)
    c.setFillColor(MUTED); c.setFont(F_REG, 5.5); c.drawString(x+25, 24, "HAFOEEP  ·  PRECISION COFFEE CARE")
    c.restoreState()

def draw_inside_left(c, x):
    c.saveState(); c.setFillColor(PAPER); c.rect(x, 0, PANEL_W, PANEL_H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont(F_BOLD, 15); c.drawString(x+25, PANEL_H-42, "VIER TÜCHER.")
    c.drawString(x+25, PANEL_H-61, "DREI AUFGABEN.")
    para(c, "Wähle das Tuch nach dem Einsatzbereich. So bleiben Milch-, Kaffee- und Wasserreste besser voneinander getrennt.", x+25, PANEL_H-76, PANEL_W-50, "body", max_h=36)
    cards = [
        ("01 / CLEAN", "Mikrofasertuch - Dampf & Milch", "Ein Tuch für Milchreste an der Dampflanze. Maschinenhinweise beachten und heiße Bauteile vorsichtig handhaben."),
        ("02 / CLEAN", "Mikrofasertuch - Kaffee", "Das zweite Tuch für Siebträger, Kaffeerückstände und äußere Bereiche des Siebs. Möglichst getrennt vom Tuch für Milchreste halten."),
        ("03 / DRY", "Waffelstruktur-Tuch", "Zum Aufnehmen von überschüssigem Wasser an Tropfschale und Arbeitsfläche."),
        ("04 / POLISH", "Feines Poliertuch", "Für den letzten Wisch auf geeigneten glatten Oberflächen wie Edelstahl oder Glas. Empfindliche Flächen zuerst testen."),
    ]
    y_top = PANEL_H-125
    card_h, gap = 83, 9
    for idx, (tag, head, body) in enumerate(cards):
        yy = y_top - idx*(card_h+gap) - card_h
        c.setFillColor(WHITE); c.setStrokeColor(HexColor("#D0D3D5")); c.roundRect(x+22, yy, PANEL_W-44, card_h, 7, fill=1, stroke=1)
        c.setFillColor(INK2); c.roundRect(x+31, yy+card_h-24, 66, 15, 7, fill=1, stroke=0)
        c.setFillColor(SILVER); c.setFont(F_BOLD, 6); c.drawCentredString(x+64, yy+card_h-19, tag)
        c.setFillColor(INK); c.setFont(F_BOLD, 8.4); c.drawString(x+107, yy+card_h-20, head)
        para(c, body, x+32, yy+card_h-33, PANEL_W-64, "body_small", max_h=39)
    c.setFillColor(MUTED); c.setFont(F_REG, 5.5); c.drawString(x+25, 20, "HAFOEEP  ·  CLEAN / DRY / POLISH")
    c.restoreState()

def draw_inside_right(c, x):
    c.saveState(); c.setFillColor(PAPER); c.rect(x, 0, PANEL_W, PANEL_H, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont(F_BOLD, 15); c.drawString(x+25, PANEL_H-42, "DIE BARISTA-ROUTINE")
    c.setFillColor(MUTED); c.setFont(F_REG, 7); c.drawString(x+25, PANEL_H-58, "Nach jedem Kaffee - in vier einfachen Schritten.")
    steps = [
        ("01", "REINIGEN", "Milchreste und Kaffeerückstände mit den jeweils vorgesehenen Mikrofasertüchern entfernen."),
        ("02", "TROCKNEN", "Überschüssiges Wasser mit dem Waffelstruktur-Tuch aufnehmen."),
        ("03", "POLIEREN", "Geeignete glatte Außenflächen mit dem Poliertuch nachwischen."),
        ("04", "AUFHÄNGEN", "Tücher nach Gebrauch ausspülen und gemäß Pflegeetikett waschen und trocknen lassen."),
    ]
    y = PANEL_H-91
    for number, title, body in steps:
        c.setFillColor(INK); c.circle(x+37, y-7, 12, fill=1, stroke=0)
        c.setFillColor(SILVER); c.setFont(F_BOLD, 7.2); c.drawCentredString(x+37, y-9.5, number)
        c.setFillColor(INK); c.setFont(F_BOLD, 8); c.drawString(x+57, y-3, title)
        h = para(c, body, x+57, y-10, PANEL_W-86, "body_small", max_h=40)
        y -= max(55, h+33)
    # Safety notice panel.
    box_y = 85
    c.setFillColor(HexColor("#E2E4E3")); c.roundRect(x+24, box_y, PANEL_W-48, 82, 7, fill=1, stroke=0)
    c.setFillColor(INK); c.setFont(F_BOLD, 7.4); c.drawString(x+36, box_y+63, "WICHTIG")
    para(c, "Das Tuchset ersetzt keine vorgeschriebene Maschinenreinigung oder Entkalkung. Beachte immer die Pflege- und Sicherheitshinweise des Maschinenherstellers. Keine groben Partikel über empfindliche Oberflächen reiben.", x+36, box_y+53, PANEL_W-72, "body_small", max_h=48)
    c.setFillColor(MUTED); c.setFont(F_REG, 5.5); c.drawString(x+25, 20, "PFLEGEETIKETT AM PRODUKT HAT VORRANG")
    c.restoreState()

def build(output: Path, qr_url: str | None = None):
    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=landscape(A4), pageCompression=1)
    c.setTitle("HAFOEEP Barista Care - German Instruction Booklet")
    c.setAuthor("HAFOEEP")
    # Outside spread: back cover on left, front cover on right.
    draw_back_cover(c, 0, qr_url=qr_url)
    draw_front(c, PANEL_W)
    c.showPage()
    # Inside spread: page 2 on left, page 3 on right.
    draw_inside_left(c, 0)
    draw_inside_right(c, PANEL_W)
    c.showPage()
    c.save()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(OUT), help="Output PDF path")
    parser.add_argument("--qr-url", default=None, help="Verified HTTPS URL of the deployed digital guide")
    args = parser.parse_args()
    if args.qr_url and not args.qr_url.startswith("https://"):
        parser.error("--qr-url must be the verified HTTPS URL of the live app")
    build(Path(args.output), args.qr_url)
    print(f"PDF created: {args.output}")
