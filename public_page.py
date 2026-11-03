"""Rahgozar public subscription page renderer.

main.py's `/p/{uuid_key}` route imports `get_public_page_html` from this
module. The page (static/sub.html) reads the subscription key from the URL
path client-side, so serving it verbatim is exactly the intended behavior.
"""
from pathlib import Path

_SUB_HTML = Path(__file__).resolve().parent / "static" / "sub.html"

_FALLBACK = (
    "<!doctype html><meta charset='utf-8'>"
    "<h2 style=\"font-family:sans-serif;padding:40px;direction:rtl\">"
    "رهگذر — صفحهٔ اشتراک در دسترس نیست</h2>"
)


def get_public_page_html(uuid_key: str = "") -> str:
    try:
        return _SUB_HTML.read_text(encoding="utf-8")
    except OSError:
        return _FALLBACK
