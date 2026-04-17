# Bucko — marketing site

Static landing site for [Bucko](https://getbucko.com), the family chore-and-rewards app.

## Stack

- Plain HTML, CSS, and vanilla JS — no build step, no framework
- Hosted on GitHub Pages with a custom `getbucko.com` domain (`CNAME`)
- `.nojekyll` so Pages serves the files as-is

## Local development

```
python3 -m http.server 8090
# open http://localhost:8090/
```

## Deploy

Push to `main`. GitHub Pages is configured to serve from the root of the `main` branch.

## Files

- `index.html` — single-page layout (hero, features, how it works, CTA, FAQ, footer)
- `styles.css` — brand tokens + all component styles
- `script.js` — reveal-on-scroll, animated hero counters
- `assets/` — app icon + favicon
- `CNAME` — custom domain record read by GitHub Pages
