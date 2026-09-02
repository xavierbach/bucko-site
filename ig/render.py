#!/usr/bin/env python3
"""Render Bucko Instagram cards from ig/card.html with headless Chromium.

Usage:
  python3 ig/render.py spec.json outdir            # local checkout (uses ./ig/card.html)
  python3 render.py spec.json outdir --fetch        # standalone: downloads card.html + icons first

spec.json = {"name": {card params}, ...}  (see PLAYBOOK for the parameter reference)
Each card is screenshotted at exactly 1080x1350 (r=45), 1080x1920 (r=916 or overlay).
Prints one JSON line per card: {"name","file","width","height","ready","overflow"}.
Exit code 1 if any card is not ready, has overflow, or has wrong dimensions.
No dependencies beyond python3 and a Chromium binary (Playwright's bundled one is found
automatically). Falls back to `npx playwright screenshot` when no binary is found.
"""
import base64, glob, json, os, re, shutil, struct, subprocess, sys, tempfile, urllib.request

BASES = [
    "https://raw.githubusercontent.com/xavierbach/bucko-site/main/",
    "https://raw.githubusercontent.com/xavierbach/bucko-site/claude/bucko-instagram-marketing-kuhhh6/",
    "https://getbucko.com/",
]

def find_chrome():
    for c in [os.environ.get("CHROME_BIN", "")] + sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"), reverse=True) \
             + ["google-chrome", "chromium", "chromium-browser", "chrome"]:
        if c and (os.path.isfile(c) or shutil.which(c)):
            return c
    return None

def enc(o):
    return base64.urlsafe_b64encode(json.dumps(o, ensure_ascii=False).encode()).decode().rstrip("=")

def fetch(rel, dest):
    last = None
    for base in BASES:
        try:
            with urllib.request.urlopen(base + rel, timeout=30) as r:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "wb").write(r.read())
                return base
        except Exception as e:  # noqa
            last = e
    raise SystemExit(f"could not fetch {rel}: {last}")

def icons_needed(spec):
    out = set()
    for o in spec.values():
        a = o.get("a")
        if a and a != "auto":
            out.add(a if "/" in a else "animals/" + a)
        ph = o.get("ph") or {}
        for k in ("a", "b"):
            ic = (ph.get(k) or {}).get("icon")
            if ic: out.add(ic if "/" in ic else "animals/" + ic)
    return out

def prepare_root(spec, fetch_remote):
    here = os.path.dirname(os.path.abspath(__file__))
    local_root = os.path.dirname(here)
    if not fetch_remote and os.path.isfile(os.path.join(here, "card.html")):
        return local_root
    root = tempfile.mkdtemp(prefix="bucko-ig-")
    fetch("ig/card.html", os.path.join(root, "ig/card.html"))
    fetch("ig/icons.json", os.path.join(root, "ig/icons.json"))
    fetch("assets/icon-160.png", os.path.join(root, "assets/icon-160.png"))
    manifest = json.load(open(os.path.join(root, "ig/icons.json")))
    need = icons_needed(spec)
    for o in spec.values():
        if o.get("a") == "auto":  # auto picks by hash in the page; mirror the whole animal set
            need.update("animals/" + s for s in manifest["animals"])
    for rel in sorted(need):
        fetch(f"assets/ig/{rel}.png", os.path.join(root, f"assets/ig/{rel}.png"))
    return root

def png_size(path):
    with open(path, "rb") as f:
        f.seek(16); return struct.unpack(">II", f.read(8))

def render_one(chrome, root, name, o, outdir):
    r = str(o.get("r", "45")); h = 1350 if r == "45" else 1920
    url = f"file://{root}/ig/card.html?p={enc(o)}"
    out = os.path.join(outdir, f"{name}.png")
    common = ["--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
              f"--window-size=1080,{h}", "--virtual-time-budget=8000",
              "--default-background-color=" + ("00000000" if r == "overlay" else "FBF3E4")]
    if chrome:
        subprocess.run([chrome] + common + [f"--screenshot={out}", url], check=True, capture_output=True)
        dom = subprocess.run([chrome] + common + ["--dump-dom", url], capture_output=True, text=True).stdout
    else:
        env = dict(os.environ, PLAYWRIGHT_BROWSERS_PATH=os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
        subprocess.run(["npx", "-y", "playwright", "screenshot", "--browser=chromium", f"--viewport-size=1080,{h}",
                        "--wait-for-selector=html[data-ready]", url, out], check=True, env=env, capture_output=True)
        dom = 'data-ready="1"'  # overflow check unavailable in this tier; inspect the PNG visually
    w, hh = png_size(out)
    over = re.findall(r'data-overflow="([^"]*)"', dom)
    res = {"name": name, "file": out, "width": w, "height": hh, "ready": 'data-ready="1"' in dom,
           "overflow": over[0] if over else ""}
    res["ok"] = res["ready"] and not res["overflow"] and w == 1080 and hh == h
    return res

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    spec = json.load(open(sys.argv[1])); outdir = sys.argv[2]; os.makedirs(outdir, exist_ok=True)
    root = prepare_root(spec, "--fetch" in sys.argv)
    chrome = find_chrome()
    bad = 0
    for name, o in spec.items():
        res = render_one(chrome, root, name, o, outdir)
        print(json.dumps(res)); bad += 0 if res["ok"] else 1
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
