#!/usr/bin/env python3
"""Generate a high-contrast print QR for the deployed HAFOEEP guide.

Usage:
  python scripts/generate_qr.py https://your-app-name.streamlit.app
"""
from __future__ import annotations
import argparse
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_H

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code for the live HAFOEEP guide.")
    parser.add_argument("url", help="The verified, live public URL of the deployed guide")
    parser.add_argument("--output", default=str(ROOT / "manual" / "hafoeep_guide_qr.png"), help="Output PNG path")
    args = parser.parse_args()
    if not args.url.startswith("https://"):
        parser.error("Use the verified HTTPS URL of the live app.")
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=12, border=4)
    qr.add_data(args.url)
    qr.make(fit=True)
    image = qr.make_image(fill_color="#17191c", back_color="white").convert("RGB")
    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, dpi=(300, 300))
    print(f"QR saved to: {output}")
    print(f"Target URL: {args.url}")

if __name__ == "__main__":
    main()
