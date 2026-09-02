#!/usr/bin/env python3
"""Builds ig/card.html from ig/card.template.html: inlines the seven brand fonts as
base64 @font-face rules and the icon manifest, so the page is fully self-contained.
Run from the repo root:  python3 ig/build.py"""
import base64, json, os, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
fonts = [("Fredoka", 500, "fredoka-500"), ("Fredoka", 600, "fredoka-600"),
         ("Nunito", 500, "nunito-500"), ("Nunito", 600, "nunito-600"), ("Nunito", 700, "nunito-700"),
         ("Nunito", 800, "nunito-800"), ("Nunito", 900, "nunito-900")]
css = []
for fam, w, f in fonts:
    b = base64.b64encode((root / "assets/fonts" / f"{f}.woff2").read_bytes()).decode()
    css.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:block;"
               f"src:url(data:font/woff2;base64,{b}) format('woff2');}}")
manifest = {}
for cat in ("animals", "rewards", "chores"):
    manifest[cat] = sorted(p.stem for p in (root / "assets/ig" / cat).glob("*.png"))
(root / "ig/icons.json").write_text(json.dumps(manifest, indent=1) + "\n")
tpl = (root / "ig/card.template.html").read_text()
out = tpl.replace("/*__FONTS__*/", "\n".join(css)).replace("/*__ANIMALS__*/[]", json.dumps(manifest["animals"]))
(root / "ig/card.html").write_text(out)
print("wrote ig/card.html", len(out), "bytes; icons:", {k: len(v) for k, v in manifest.items()})
