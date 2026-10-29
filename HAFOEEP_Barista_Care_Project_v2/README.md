# HAFOEEP Präzise Kaffeepflege — Interactive Barista Zone Cleaning Guide (v2.0)

An interactive, visual, German/Chinese bilingual mobile web app built with Streamlit for the **HAFOEEP 4-Piece Barista Cleaning Towel Set (`Barista Reinigungstuch-Set`)**.

## Key Features in v2.0

- **Real Product & Action Photography**: High-resolution embedded visuals (`assets/images/`) showing all 4 distinct towel weaves (`Tuch A` plush microfiber, `Tuch B` smooth microfiber, `03 Waffeltuch` waffle weave, `04 Feines Poliertuch` grid polishing cloth) and zone-by-zone barista cleaning actions.
- **Interactive 4-Zone Espresso Machine Guide**: Switch between `01 Dampflanze & Milch`, `02 Siebträger & Siebkorb`, `03 Tropfschale & Arbeitsfläche`, and `04 Edelstahl, Glas & Gehäuse` with step-by-step instructions, safety callouts, and embedded video tutorials.
- **Interactive Post-Espresso Routine Checklist**: Live progress tracker for daily barista care.
- **Mobile-First & Zero External Image Hosting**: All product images are cached and served locally via `assets/images/` with responsive Flexbox header layout so scanning the packaging QR code on iOS/Android loads cleanly.

## Quick Start

```bash
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on GitHub + Streamlit Community Cloud

1. Push the contents of this folder directly to the root of your GitHub repository.
2. Connect the repository on Streamlit Community Cloud (`streamlit_app.py` on `main` branch).
3. Once your `https://YOUR-APP.streamlit.app` URL is live, generate the 300 DPI print QR code and final 4-page A5 print booklet:

```bash
python -m pip install -r requirements-tools.txt
python scripts/generate_qr.py https://YOUR-APP.streamlit.app
python build_manual.py --qr-url https://YOUR-APP.streamlit.app --output manual/HAFOEEP_Barista_Care_Manual_DE_Print.pdf
```
