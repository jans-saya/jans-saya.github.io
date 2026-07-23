#!/usr/bin/env python3
"""
Adds the Korean sign-language demo video to sign-language.html,
adds one sentence to the SOFTWARE card, and appends the video CSS rule.

Run from the root of the portfolio repo:
    python3 add_sl_demo.py
"""
import sys, shutil, pathlib

HTML = pathlib.Path("sign-language.html")
CSS = pathlib.Path("assets/css/site.css")

for p in (HTML, CSS):
    if not p.exists():
        sys.exit(f"Can't find {p}. Run this from the root of your portfolio repo.")

html = HTML.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

# ---------------------------------------------------------------- 1. demo section
ANCHOR = ('<section class="section"><div class="section-label reveal">'
          '<span>01</span><p>USER RESEARCH</p></div>')

DEMO = (
    '<section class="section">'
    '<div class="section-label reveal"><span>00</span><p>LIVE DEMO</p></div>'
    '<div class="split-intro">'
    '<h2 class="reveal">The system recognizing letters in real time.</h2>'
    '<div class="reveal delay"><p>Demo of the current version recognizing Korean '
    'fingerspelling. The 2022 competition prototype used the Russian alphabet; '
    'that recording was not saved.</p></div>'
    '</div>'
    '<div class="project-hero-media reveal" style="margin-top:45px">'
    '<video src="documents/SL_Korean.mp4" '
    'poster="assets/images/projects/sl-korean-poster.jpg" '
    'controls muted loop playsinline preload="metadata"></video>'
    '<div class="media-note">KOREAN FINGERSPELLING · CURRENT BUILD</div>'
    '</div>'
    '</section>'
)

# ---------------------------------------------------------------- 2. software card
OLD_P = ("and Euclidean distances between selected points.</p>")
NEW_P = ("and Euclidean distances between selected points. The letter rules were later "
         "redefined for Korean fingerspelling, so the same geometric approach transfers "
         "to a different alphabet.</p>")

# ---------------------------------------------------------------- 3. css
CSS_RULE = "\n.project-hero-media video{width:100%;display:block}\n"

changes = []

if 'documents/SL_Korean.mp4' in html:
    changes.append("demo section: already present, skipped")
else:
    if html.count(ANCHOR) != 1:
        sys.exit(f"Expected 1 match for the USER RESEARCH anchor, found {html.count(ANCHOR)}. Nothing changed.")
    html = html.replace(ANCHOR, DEMO + ANCHOR)
    changes.append("demo section: inserted before USER RESEARCH")

if "redefined for Korean fingerspelling" in html:
    changes.append("software sentence: already present, skipped")
else:
    if html.count(OLD_P) != 1:
        sys.exit(f"Expected 1 match for the software paragraph, found {html.count(OLD_P)}. Nothing changed.")
    html = html.replace(OLD_P, NEW_P)
    changes.append("software sentence: added")

if ".project-hero-media video{" in css:
    changes.append("css rule: already present, skipped")
else:
    css = css.rstrip("\n") + CSS_RULE
    changes.append("css rule: appended at end of file")

shutil.copy(HTML, str(HTML) + ".bak")
shutil.copy(CSS, str(CSS) + ".bak")
HTML.write_text(html, encoding="utf-8")
CSS.write_text(css, encoding="utf-8")

print("Backups written: sign-language.html.bak, assets/css/site.css.bak")
for c in changes:
    print("  " + c)
print("\nVideo expected at:  documents/SL_Korean.mp4")
print("Poster expected at: assets/images/projects/sl-korean-poster.jpg")
