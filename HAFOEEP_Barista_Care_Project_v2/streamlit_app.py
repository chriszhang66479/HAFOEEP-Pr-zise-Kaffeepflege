from __future__ import annotations

import base64
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="HAFOEEP | Präzise Kaffeepflege — Barista Care Guide (DE / EN)",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "assets" / "images"


@st.cache_data(show_spinner=False)
def img_to_data_uri(filename: str) -> str:
    path = IMG_DIR / filename
    if not path.exists():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


st.markdown(
    """
    <style>
      :root { --ink:#17191c; --silver:#c5c9ce; --gold:#b89b72; --muted:#a5abb2; --paper:#f3f4f2; }
      .stApp { background: radial-gradient(circle at 88% 0%, #2a2e33 0%, #17191c 42%, #111315 100%); color:#f2f3f4; }
      .block-container { max-width: 860px; padding-top: 1.15rem; padding-bottom: 2.5rem; }
      header[data-testid="stHeader"] { background: transparent; }
      #MainMenu, footer { visibility: hidden; }
      h1, h2, h3, p, li, label { color: #f0f1f2; }
      .brand-header-left { display:flex; align-items:center; gap:0.85rem; }
      .brand-logo { width:52px; height:52px; flex-shrink:0; }
      .brand-kicker { color:#bfc4ca; letter-spacing:.22em; text-transform:uppercase; font-size:.72rem; font-weight:700; }
      .hero-title { font-size:clamp(1.95rem, 5.5vw, 3.1rem); line-height:1.05; letter-spacing:-.03em; font-weight:800; margin:.35rem 0 .55rem 0; }
      .hero-title span { color:#d2b48c; }
      .hero-copy { color:#c4c8cd; font-size:.98rem; line-height:1.58; max-width:44rem; }
      .en-sub { color:#9ab0c7; font-size:.8rem; line-height:1.45; margin-top:.28rem; padding-top:.24rem; border-top:1px dashed rgba(154,176,199,.22); }
      .silver-line { height:1px; background:linear-gradient(90deg,#d0d4d8 0%,#5f666d 48%,transparent 100%); margin:1.15rem 0; }
      .section-label { color:#d2b48c; font-size:.73rem; letter-spacing:.18em; font-weight:700; text-transform:uppercase; margin-bottom:.45rem; }
      .hero-banner-wrap { position:relative; border-radius:18px; overflow:hidden; border:1px solid rgba(206,211,216,.22); margin-top:.75rem; background:#121417; }
      .hero-banner-img { width:100%; max-height:340px; object-fit:cover; display:block; }
      .hero-banner-caption { padding:.7rem 1rem; background:rgba(17,19,21,.88); border-top:1px solid rgba(255,255,255,.08); font-size:.82rem; color:#cfd4d9; display:flex; justify-content:space-between; flex-wrap:wrap; gap:.4rem; }
      .cloth-card { background:rgba(245,246,247,.055); border:1px solid rgba(206,211,216,.18); border-radius:16px; overflow:hidden; margin-bottom:.85rem; transition:all .2s ease; }
      .cloth-card-img { width:100%; height:175px; object-fit:cover; display:block; border-bottom:1px solid rgba(255,255,255,.08); }
      .cloth-card-body { padding:.95rem 1rem 1rem 1rem; }
      .cloth-number { color:#d2b48c; font-size:.7rem; letter-spacing:.16em; font-weight:700; text-transform:uppercase; }
      .cloth-title { color:#f4f5f6; font-size:1.08rem; font-weight:750; margin:.2rem 0 .4rem; }
      .cloth-desc { color:#c4c8cc; font-size:.88rem; line-height:1.52; }
      .pill { display:inline-block; border:1px solid #70777e; color:#e1e4e7; padding:.18rem .5rem; border-radius:999px; font-size:.67rem; letter-spacing:.05em; margin:.12rem .18rem .1rem 0; }
      .pill-gold { border-color:rgba(210,180,140,.45); color:#e6d5bc; background:rgba(184,155,114,.12); }
      .zone-panel { background:rgba(245,246,247,.06); border:1px solid rgba(210,180,140,.35); border-radius:18px; padding:1.1rem; margin-top:.6rem; }
      .zone-img { width:100%; height:240px; object-fit:cover; border-radius:12px; border:1px solid rgba(255,255,255,.12); display:block; }
      .notice { background:rgba(197,201,206,.08); border:1px solid rgba(197,201,206,.24); border-radius:14px; padding:.9rem 1rem; color:#d4d8dc; font-size:.86rem; line-height:1.55; }
      .notice-warn { background:rgba(210,180,140,.1); border:1px solid rgba(210,180,140,.35); border-radius:14px; padding:.85rem 1rem; color:#ece0ce; font-size:.85rem; line-height:1.52; margin-top:.65rem; }
      .footer-brand { color:#9da4ab; text-align:center; letter-spacing:.18em; font-size:.66rem; text-transform:uppercase; margin-top:1.6rem; }
      @media (max-width: 640px) {
        .block-container { padding-left:1rem; padding-right:1rem; }
        .cloth-card-img { height:160px; }
        .zone-img { height:205px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

logo_svg = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HAFOEEP H Logo">
 <path d="M19 78V24h14v20h34V24h14v54H67V58H33v20z" fill="#c5c9ce"/>
 <path d="M37 44h26l-6 10H43z" fill="#17191c"/>
 <path d="M42 35c-6-7 4-11 0-19M51 35c-6-7 4-11 0-19M60 35c-6-7 4-11 0-19" stroke="#d2b48c" stroke-width="2.8" fill="none" stroke-linecap="round"/>
</svg>
"""

top_l, top_r = st.columns([3.1, 1.4], vertical_alignment="center")
with top_l:
    st.markdown(
        f"""
        <div class="brand-header-left">
          <div class="brand-logo">{logo_svg}</div>
          <div>
            <div class="brand-kicker">HAFOEEP · Präzise Kaffeepflege</div>
            <div style="font-size:1.22rem;font-weight:800;letter-spacing:.18em;color:#f2f3f4;">HAFOEEP</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_r:
    show_en = st.toggle("🇩🇪 DE + 🇬🇧 EN", value=True, help="Show English secondary subtitles alongside German")

st.markdown('<div class="silver-line"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-title">Drei Funktionen.<br><span>Ein sauberer Kaffeeplatz.</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="hero-copy">4-teiliges Barista-Set mit 3 spezialisierten Tuchtypen: <strong>2 × Doppelseitiges Mikrofaser-/Velourstuch (Tuch A &amp; Tuch B für Sauber)</strong> · <strong>1 × Waffeltuch (Trocken)</strong> · <strong>1 × Feines Poliertuch (Polieren)</strong>.</div>',
    unsafe_allow_html=True,
)
if show_en:
    st.caption("Three Functions. One Clean Coffee Bar: 4-piece barista towel set featuring 2 × dual-sided microfiber & suede cloths (Cloth A for steam wand/milk, Cloth B for portafilter/coffee), 1 × waffle towel (Dry), and 1 × fine polishing cloth (Polish).")

hero_uri = img_to_data_uri("hero_four_towels.jpg")
if hero_uri:
    st.markdown(
        f"""
        <div class="hero-banner-wrap">
          <img src="{hero_uri}" alt="HAFOEEP 4-teiliges Barista Reinigungstuch-Set" class="hero-banner-img" />
          <div class="hero-banner-caption">
            <span><strong>Links → Rechts (Left → Right):</strong> 2 × Doppelseitiges Reinigungstuch (1. Mikrofaser-Seite / 2. Velours-Wildlederseite) · 3. Waffeltuch · 4. Feines Poliertuch</span>
            <span>4 Tücher · 3 Funktionen</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="silver-line"></div>', unsafe_allow_html=True)

# INTERACTIVE ZONE EXPLORER
st.markdown('<div class="section-label">01 · Interaktive 4-Zonen-Reinigungsführung (Interactive 4-Zone Care Guide)</div>', unsafe_allow_html=True)
st.write("Wähle den Reinigungsbereich an deiner Espressomaschine / Select your espresso machine cleaning zone:")

ZONES = {
    "01 · Dampflanze & Milch (Tuch A)": {
        "badge": "ZONE 01 · SAUBER / CLEAN (TUCH A · 2-SIDED)",
        "towel": "Tuch A · Doppelseitiges Mikrofaser- & Velourstuch",
        "towel_en": "Cloth A (1st Dual-Sided Cloth: Plush Microfiber Front + Smooth Suede Back · Dedicated to Steam Wand & Milk)",
        "action_img": "action_01_steam_wand.jpg",
        "texture_img": "towel_01_plush.jpg",
        "texture_img_alt": "towel_02_smooth.jpg",
        "summary": "Tuch A besitzt zwei Funktionsseiten: Die weiche Hochflor-Mikrofaserseite löst frische Milchreste nach dem Purgen und schützt vor Hitze; die glatte Velours-/Wildlederseite wischt das Dampfrohr streifenfrei nach.",
        "summary_en": "Cloth A features a dual-sided weave: the plush high-pile microfiber side removes fresh milk residue after purging while insulating against heat; the smooth suede (velour) side wipes the steam wand streak-free.",
        "steps": [
            "1. Dampflanze über die Tropfschale richten und 1–2 Sekunden Dampf ablassen (Point wand at drip tray and purge for 1–2s).",
            "2. Mit der leicht feuchten Mikrofaser-Seite von Tuch A Milchreste sofort abwischen; mit der Veloursseite nachziehen (Wipe milk residue with damp microfiber side; finish with suede side).",
            "3. Heiße Metallteile niemals direkt mit der Haut berühren – Verbrennungsgefahr! (Never touch hot metal with bare skin – burn hazard!).",
            "4. Tuch A ausschließlich für Dampflanze & Milch verwenden – nicht mit Tuch B tauschen (Keep Cloth A strictly for milk – never swap with Cloth B).",
        ],
        "warning": "Verbrennungsgefahr an der heißen Dampflanze! Immer mit gefaltetem Tuch A arbeiten und Hinweise des Maschinenherstellers befolgen. / Caution: Hot steam wand! Always fold Cloth A thickly and follow your machine manufacturer's manual.",
        "video_url": "https://www.youtube.com/watch?v=V3uyk3dwiUg",
        "video_title": "Video-Referenz / Video Guide: Steam Wand Purge & Care (Sage Appliances)",
    },
    "02 · Siebträger & Kaffee (Tuch B)": {
        "badge": "ZONE 02 · SAUBER / CLEAN (TUCH B · 2-SIDED)",
        "towel": "Tuch B · Doppelseitiges Mikrofaser- & Velourstuch",
        "towel_en": "Cloth B (2nd Identical Dual-Sided Cloth: Smooth Suede Back + Plush Microfiber Front · Dedicated to Portafilter & Coffee)",
        "action_img": "action_02_portafilter.jpg",
        "texture_img": "towel_02_smooth.jpg",
        "texture_img_alt": "towel_01_plush.jpg",
        "summary": "Das zweite baugleiche 2-Seiten-Tuch (Tuch B) bleibt strikt für Kaffee reserviert: Die glatte Velours-/Wildlederseite wischt den Siebkorb trocken, ohne dass Kaffeemehl hängen bleibt; die Mikrofaser-Seite nimmt Kaffeefette am Siebträger außen auf.",
        "summary_en": "Cloth B is the second identical dual-sided cloth reserved strictly for coffee: the smooth suede side wipes the filter basket dry without trapping loose coffee grounds, while the plush microfiber side removes coffee oils from the portafilter body and spouts.",
        "steps": [
            "1. Kaffeepuck ausklopfen und lose Kaffeekrümel entfernen (Knock out spent coffee puck and brush off loose grounds).",
            "2. Siebkorb innen mit der glatten Veloursseite trockenwischen; Außenseite mit der Mikrofaser-Seite reinigen (Wipe basket dry with smooth suede side; clean exterior with microfiber side).",
            "3. Getrennt von Tuch A verwenden – niemals zwischen Milch- und Kaffeebereich tauschen! (Use separately from Cloth A – never cross-contaminate milk and coffee zones!).",
        ],
        "warning": "Vor dem Einspannen prüfen, dass keine Kaffeepartikel auf dem Siebträgerrand verbleiben, um die Brühgruppendichtung zu schonen. / Ensure the basket rim is free of grounds before locking in to protect the group head gasket.",
        "video_url": "https://www.youtube.com/watch?v=lznlThSPAIQ",
        "video_title": "Video-Referenz / Video Guide: Portafilter & Group Head Daily Care",
    },
    "03 · Tropfschale & Bar (Waffeltuch)": {
        "badge": "ZONE 03 · TROCKEN / DRY (1 × WAFFELTUCH)",
        "towel": "03 · Waffelstruktur-Tuch (Waffeltuch)",
        "towel_en": "03 · 3D Waffle-Weave Drying Towel (1 Piece · Drip Tray & Work Counter)",
        "action_img": "action_03_drip_tray.jpg",
        "texture_img": "towel_03_waffle.jpg",
        "texture_img_alt": "",
        "summary": "Die ausgeprägte 3D-Waffelstruktur nimmt Wasser an Tropfschale, Abstellgitter und feuchten Bereichen rund um die Maschine schnell und gründlich auf.",
        "summary_en": "Deep 3D waffle pockets rapidly absorb water splashes on the drip tray grate, group head flush water, and wet spots across your work counter.",
        "steps": [
            "1. Nach dem Spülstoß (Flush) Wassertröpfchen auf dem Tropfblech mit dem Waffeltuch aufnehmen (Absorb water droplets on the drip tray grate after flushing).",
            "2. Feuchte Bereiche rund um die Maschine und auf der Arbeitsfläche trockenwischen (Wipe wet areas around the espresso machine and grinder dry).",
            "3. Nach Gebrauch ausspülen, auswringen und vollständig ausgebreitet trocknen lassen (Rinse, wring out if needed, and lay flat to dry completely after use).",
        ],
        "warning": "Bei starker Durchfeuchtung zwischendurch gut auswringen und nach Gebrauch vollständig trocknen lassen. / Wring out excess water when saturated and let dry completely after service.",
        "video_url": "https://www.youtube.com/watch?v=Iun9JXjI3YQ",
        "video_title": "Video-Referenz / Video Guide: Daily & Weekly Barista Cleaning Routine",
    },
    "04 · Edelstahl & Gehäuse (Poliertuch)": {
        "badge": "ZONE 04 · POLIEREN / POLISH (1 × FEINES POLIERTUCH)",
        "towel": "04 · Feines Karo-Poliertuch (mit Eckschlaufe)",
        "towel_en": "04 · Fine Grid-Weave Polishing Cloth (1 Piece with Corner Loop · Stainless Steel & Glass)",
        "action_img": "action_04_polishing.jpg",
        "texture_img": "towel_04_polish.jpg",
        "texture_img_alt": "",
        "summary": "Nach der groben Reinigung geeignete glatte Oberflächen aus Edelstahl, Chrom oder Glas mit dem feinen Poliertuch schlierenfrei nachwischen.",
        "summary_en": "After initial cleaning and drying, buff cooled stainless steel, chrome, and glass surfaces with the fine grid polishing cloth for a lint-free, streak-free mirror finish.",
        "steps": [
            "1. Vorher prüfen, ob die Oberfläche vollständig abgekühlt und frei von Partikeln ist (Verify the surface is completely cool and free of coffee particles before polishing).",
            "2. Mit dem feinen Poliertuch in sanften Zügen ohne Druck schlierenfrei nachpolieren (Buff gently without heavy pressure for a streak-free shine).",
            "3. Empfindliche Oberflächen immer zuerst an einer unauffälligen Stelle testen (Always test sensitive or coated finishes on an inconspicuous area first).",
        ],
        "warning": "Nicht auf heißen Oberflächen polieren! Grobe Körnchen immer zuerst entfernen, um Mikrokratzer auf Edelstahl zu vermeiden. / Never polish hot surfaces! Remove loose particles first to prevent micro-scratches.",
        "video_url": "https://www.youtube.com/watch?v=shm0DWZa88I",
        "video_title": "Video-Referenz / Video Guide: Expert Espresso Machine Care (DINZLER)",
    },
}

selected_zone_key = st.radio(
    "Reinigungszone auswählen:",
    list(ZONES.keys()),
    horizontal=True,
    label_visibility="collapsed",
)

zdata = ZONES[selected_zone_key]
act_uri = img_to_data_uri(zdata["action_img"])
tex_uri = img_to_data_uri(zdata["texture_img"])
tex_alt_uri = img_to_data_uri(zdata["texture_img_alt"]) if zdata["texture_img_alt"] else ""

st.markdown('<div class="zone-panel">', unsafe_allow_html=True)
zcol1, zcol2 = st.columns([1.25, 1.45], gap="medium")
with zcol1:
    if act_uri:
        st.markdown(f'<img src="{act_uri}" alt="{selected_zone_key}" class="zone-img" />', unsafe_allow_html=True)
    if tex_uri and tex_alt_uri:
        st.markdown(
            f"""
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-top:.65rem;background:rgba(255,255,255,.04);padding:.55rem;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
              <div style="display:flex;align-items:center;gap:.45rem;">
                <img src="{tex_uri}" alt="Side 1" style="width:46px;height:38px;object-fit:cover;border-radius:6px;" />
                <div style="font-size:.72rem;line-height:1.25;color:#d6dade;"><strong style="color:#f3f4f5;">Mikrofaser</strong><br>Plush Front</div>
              </div>
              <div style="display:flex;align-items:center;gap:.45rem;">
                <img src="{tex_alt_uri}" alt="Side 2" style="width:46px;height:38px;object-fit:cover;border-radius:6px;" />
                <div style="font-size:.72rem;line-height:1.25;color:#d6dade;"><strong style="color:#f3f4f5;">Velours</strong><br>Suede Back</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif tex_uri:
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:.65rem;margin-top:.65rem;background:rgba(255,255,255,.04);padding:.5rem .65rem;border-radius:10px;border:1px solid rgba(255,255,255,.08);">
              <img src="{tex_uri}" alt="Gewebestruktur" style="width:58px;height:44px;object-fit:cover;border-radius:6px;" />
              <div style="font-size:.78rem;line-height:1.35;color:#d6dade;">
                <strong style="color:#f3f4f5;">Gewebe-Erkennung (Weave ID):</strong><br>{zdata['towel']}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
with zcol2:
    st.markdown(f'<span class="pill pill-gold">{zdata["badge"]}</span>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:1.18rem;font-weight:800;color:#f4f5f6;margin:.3rem 0;">{zdata["towel"]}</div>', unsafe_allow_html=True)
    if show_en:
        st.caption(zdata["towel_en"])
    st.markdown(f'<div style="color:#d0d4d9;font-size:.9rem;line-height:1.55;margin-bottom:.6rem;">{zdata["summary"]}</div>', unsafe_allow_html=True)
    if show_en:
        st.info(zdata["summary_en"])
    for step_txt in zdata["steps"]:
        st.markdown(f'<div style="font-size:.85rem;color:#c4c8cc;margin-bottom:.28rem;">• {step_txt}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="notice-warn"><strong>⚠️ Wichtiger Hinweis / Safety Note:</strong> {zdata["warning"]}</div>', unsafe_allow_html=True)

with st.expander(f"🎬 {zdata['video_title']}"):
    st.video(zdata["video_url"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="silver-line"></div>', unsafe_allow_html=True)

# 4 PHOTOS EXPLAINING THE 2 DUAL-SIDED CLOTHS + WAFFLE + POLISH
st.markdown('<div class="section-label">02 · Gewebe-Guide: 4 Tücher · 3 Funktionen (Fabric & Weave Guide)</div>', unsafe_allow_html=True)

cards = [
    {
        "num": "01 / SAUBER · 2 × DOPPELSEITIG (VORDERSEITE: MIKROFASER)",
        "title": "Tuch A: Dampflanze & Milch (Plush Microfiber Side)",
        "desc": "Doppelseitiges Reinigungstuch (2 Stück im Set): Die weiche Hochflor-Mikrofaserseite mit Schlaufe löst Milchreste an der Dampflanze (Tuch A) und schützt vor Hitze.",
        "en": "Dual-Sided Cleaning Cloth — Front Side (Plush High-Pile Microfiber): Images 1 & 2 show the front and back of the same dual-sided cloth (2 included in the set). Dedicate Cloth A strictly to the steam wand and milk residue.",
        "img": "towel_01_plush.jpg",
        "tags": ["Vorderseite: Mikrofaser", "Tuch A: Milch", "With Hanging Loop"],
    },
    {
        "num": "01 / SAUBER · 2 × DOPPELSEITIG (RÜCKSEITE: VELOURS / SUEDE)",
        "title": "Tuch B: Siebträger & Kaffee (Smooth Suede Side)",
        "desc": "Die Rückseite desselben 2-Seiten-Tuchs besteht aus glatter Velours-Mikrofaser: Nimmt kein loses Kaffeemehl auf und wischt Siebkorb sowie Siebträger (Tuch B) sauber ab.",
        "en": "Dual-Sided Cleaning Cloth — Back Side (Smooth Suede / Velour): Shows the reverse side of the same dual-sided cloth. Dedicate the second cloth (Cloth B) strictly to the portafilter, filter basket exterior, and coffee oils.",
        "img": "towel_02_smooth.jpg",
        "tags": ["Rückseite: Velours/Suede", "Tuch B: Kaffee", "Keep Separate"],
    },
    {
        "num": "02 / TROCKEN · 1 × WAFFELTUCH (DRY)",
        "title": "Waffelstruktur-Tuch · Tropfschale & Arbeitsfläche",
        "desc": "Nimmt Wasser an Tropfschale und Arbeitsfläche auf. Ideal für feuchte Bereiche rund um die Maschine. Nach Gebrauch ausbreiten und vollständig trocknen lassen.",
        "en": "3D Waffle-Weave Towel (1 Piece): Absorbs water on the drip tray and work surface around the espresso machine. Spread out and let dry completely after use.",
        "img": "towel_03_waffle.jpg",
        "tags": ["1 × Waffeltuch", "Tropfschale", "Drip Tray & Counter"],
    },
    {
        "num": "03 / POLIEREN · 1 × FEINES POLIERTUCH (POLISH)",
        "title": "Feines Karo-Poliertuch · Oberfläche nachpflegen",
        "desc": "Nach grober Reinigung mit dem feinen Poliertuch schlierenfrei nachwischen. Vorher prüfen, ob die Oberfläche abgekühlt und frei von Partikeln ist.",
        "en": "Fine Grid Polishing Cloth (1 Piece with Corner Strap): Wipe cooled, particle-free stainless steel, chrome, and glass surfaces for a streak-free mirror finish.",
        "img": "towel_04_polish.jpg",
        "tags": ["1 × Poliertuch", "Edelstahl & Glas", "Streak-Free Finish"],
    },
]

r1 = st.columns(2, gap="medium")
r2 = st.columns(2, gap="medium")
for col, card in zip(r1 + r2, cards):
    with col:
        c_uri = img_to_data_uri(card["img"])
        img_html = f'<img src="{c_uri}" alt="{card["title"]}" class="cloth-card-img" />' if c_uri else ""
        tag_html = "".join(f'<span class="pill">{tag}</span>' for tag in card["tags"])
        en_html = f'<div class="en-sub">{card["en"]}</div>' if show_en else ""
        st.markdown(
            f"""
            <div class="cloth-card">
              {img_html}
              <div class="cloth-card-body">
                <div class="cloth-number">{card['num']}</div>
                <div class="cloth-title">{card['title']}</div>
                <div class="cloth-desc">{card['desc']}</div>
                {en_html}
                <div style="margin-top:.65rem">{tag_html}</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="silver-line"></div>', unsafe_allow_html=True)

# INTERACTIVE ROUTINE CHECKLIST AFTER ESPRESSO
st.markdown('<div class="section-label">03 · Ihre Routine nach dem Espresso (Post-Espresso Routine Checklist)</div>', unsafe_allow_html=True)
st.write("Arbeiten Sie von der gezielten Reinigung bis zur trockenen, gepflegten Oberfläche / Work from targeted cleaning to a dry, polished surface:")

c1 = st.checkbox("01 · MIKROFASER & VELOURS (Tuch A & B): Dampflanze purgen & mit Tuch A reinigen; Siebträger getrennt mit Tuch B säubern. (Purge & wipe steam wand with Cloth A; clean portafilter separately with Cloth B.)")
c2 = st.checkbox("02 · WAFFEL (Waffeltuch): Feuchtigkeit auf Tropfschale und Arbeitsfläche aufnehmen. (Absorb moisture on drip tray and counter with the waffle towel.)")
c3 = st.checkbox("03 · OBERFLÄCHE NACHPFLEGEN (Poliertuch): Abgekühlte, partikelfreie Gehäuseflächen schlierenfrei nachwischen. (Buff cooled, particle-free machine surfaces with the fine polishing cloth.)")
c4 = st.checkbox("04 · AUSWASCHEN & TROCKNEN: Tücher nach Gebrauch gut ausspülen, auswringen und vollständig trocknen lassen. (Rinse thoroughly after use, wring out, and let dry completely.)")

done_count = sum([c1, c2, c3, c4])
st.progress(done_count / 4.0, text=f"Routine-Fortschritt / Routine Progress: {done_count} / 4")
if done_count == 4:
    st.success("☕ Perfekt! Dein Kaffeeplatz ist sauber, trocken und bereit für den nächsten Espresso. / Perfect! Your coffee bar is clean, dry, and ready for the next shot.")

with st.expander("🧺 Waschen & Wichtige Sicherheitshinweise (Washing & Care Instructions)"):
    st.markdown(
        """
        - **Vor dem ersten Gebrauch waschen (Wash before first use):** Maschinenwäsche nur gemäß Pflegeetikett am Produkt (Machine wash according to product care label only).
        - **Kein Weichspüler & kein Bleichmittel (No fabric softener or bleach):** Weichspüler legt sich um die Mikrofasern und mindert die Saugkraft (Softener coats microfiber strands and reduces absorbency).
        - **Getrennt verwenden (Use separately by zone):** Die beiden doppelseitigen Tücher (Tuch A für Milch/Dampflanze, Tuch B für Siebträger/Kaffee) nicht zwischen den Bereichen tauschen (Never swap Cloth A and Cloth B between milk and coffee zones).
        - **Verbrennungsgefahr beachten (Burn hazard):** Nicht auf heißen Oberflächen polieren; heiße Metallteile der Dampflanze nicht mit der Haut berühren (Do not polish hot surfaces; never touch hot steam wand metal with bare skin).
        - **Oberflächen schonen (Surface protection):** Lose Kaffeepartikel zuerst entfernen. Empfindliche Oberflächen immer zuerst an unauffälliger Stelle testen (Remove loose particles first; test sensitive finishes on an inconspicuous spot).
        """
    )

st.markdown(
    '<div class="notice"><strong>WICHTIG / IMPORTANT:</strong> Das Tuchset ersetzt keine vom Maschinenhersteller vorgeschriebene Reinigung oder Entkalkung. Die Pflegehinweise auf dem Produkt und die Bedienungsanleitung der Kaffeemaschine haben Vorrang.<br><span style="color:#9ab0c7;font-size:.8rem;">This towel set does not replace manufacturer-required backflushing or descaling. Product care labels and your espresso machine manual always take priority.</span></div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="footer-brand">HAFOEEP · Precision Coffee Care</div>', unsafe_allow_html=True)
