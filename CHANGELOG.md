# Bucko Site Changelog

## [Build 18] — 2026-04-27
- **Privacy policy** — removed stale "Export your data / Settings → Export Data" bullet since that feature no longer exists (`privacy/index.html`)
- **Features section** — replaced "Pocket money that actually works" card with "Streaks kids actually chase" — highlights the smart streaks feature with a "No AI, just a number" angle (`index.html`)

## [Build 17] — 2026-04-25
- **App Store launch** — App Store badge on hero is now a live link (`https://bit.ly/4es2STp`); removed COMING SOON overlay and grayscale filter. Google Play badge retains COMING SOON. All App Store links in `/join/` updated to the same bit.ly URL (`index.html`, `join/index.html`, `styles.css`)

## [Build 16] — 2026-04-23
- **Instagram link** — added @bucko.app Instagram link to footer nav (`index.html`)

## [Build 15] — 2026-04-23
- **Pricing card copy updated** — Pro Monthly and Pro Annual now show the full feature list: Unlimited kids, Unlimited chores per child, 40+ extra animal & character avatars, Family Sharing, iCloud Backup (iOS). Removed "Backup and sync (coming soon)" and "Unlock more icons and themes" placeholders (`index.html`)
- **Pricing section header** — h2 updated to "Free for one kid, 6 chores. Pro unlocks the rest."; lede updated to mention chores as an upgrade reason alongside kids (`index.html`)

## [Build 11] — 2026-04-20
- **Family join page** — new `/join/` page extracts the family code from `?code=` query param, displays it prominently, attempts to open `bucko://join/CODE` automatically, and falls back to App Store + Play Store download links after 1.8 s (`join/index.html`)
- **Apple Universal Links** — `/.well-known/apple-app-site-association` declares that `/join/` paths are handled by `5W4VXC6XPN.com.thorleypark.bucko`, so iOS routes `https://getbucko.com/join/?code=CODE` straight into the app when it's installed
- **Android App Links** — `/.well-known/assetlinks.json` scaffolded; SHA-256 fingerprint placeholder must be replaced with the EAS Build signing cert value before Android verified App Links work

## [Build 10] — 2026-04-20
- **Free tier chore limit** — pricing cards updated: Free tier "One kid, unlimited chores" → "up to 6 chores"; Pro Monthly and Pro Annual cards gain "Unlimited chores per child"; FAQ subscription answer updated to mention the 6-chore limit (`index.html`)

## [Build 9] — 2026-04-20
- **Features section overhaul** — replaced "Pocket money that works" + "Nothing to sign up for" with "Streak chores for real habits" (new mechanic) and "Both parents, one app" (Family Sharing, Pro); updated Kids View card to mention Face ID/PIN lock; updated icons card to call out 50+ icons.
- **Pricing cards updated** — Free tier now accurately lists streak chores, Kids View with Face ID/PIN, and 50+ icons; Pro tiers replace "coming soon" sync and generic icons with specific features: Unlimited kids, 40+ extra animal avatars, Family Sharing, iCloud Backup.
- **New FAQ: "Can both parents use the app?"** — explains Family Sharing with the 6-character code flow; inserted between lost-phone and kids-use FAQs.
- **Lost-phone FAQ updated** — iCloud Backup now live for Pro iOS users; updated answer accordingly.
- **Privacy Policy updated** (20 Apr 2026) — added Family Sharing section covering Supabase as data processor, what data is stored, access control via family code, data retention/deletion, and cross-border transfer disclosure; updated "how data leaves device" list to include Family Sharing as item 4; updated permissions section (push notifications now active); updated GDPR and Australian Privacy Act notes to reference Supabase; updated callout and intro to reflect two narrow exceptions.
- **Terms of Use updated** (20 Apr 2026) — Section 3 updated to acknowledge Supabase backend for Family Sharing; Pro features list updated to include Family Sharing and iCloud Backup (removing "future version" language); new Section 3b covering Family Sharing terms (shared access, code security, data on Supabase, leaving/deletion); cancellation clause updated to list all gated Pro features.
- **Support page updated** (20 Apr 2026) — "Does Bucko sync?" answer updated to "Yes" with both iCloud Backup and Family Sharing explained; new "How do I set up Family Sharing?" step-by-step FAQ added; data deletion answer updated to mention Supabase row and deletion request process.

## [Build 8] — 2026-04-19
- **Copy overhaul** across hero, features, steps, pricing intro, and pricing cards. Shorter, punchier, more parent-voice. Removed "Priority support" from Pro tiers; replaced with "Unlock more icons and themes" + "Backup and sync (coming soon)" / "Best value for families".
- **Two new FAQs**: "What age is this for?" (4–10) and "Do rewards have to be money?" (no — points can be screen time, treats, etc.).
- **Trust line** "Built by a dad of two. Used every day in our house." added under the features header.
- **Visual polish**: feature cards and how-it-works steps are now centre-aligned inside the card (icon, title, body) with `text-wrap: balance` on headings to kill ugly 1-word wraps. Feature grid fixed to a clean 3-col (2-col ≤960px, 1-col ≤640px) with more breathing room.
- **Pricing cards** centre-aligned card headers (title + price + sub-note + lede); bullet lists stay left-aligned for readability.
- **Hero store badges** now sit equidistant between the phone mock and the "WHY BUCKO" chip — `.hero` padding-bottom and `#features` padding-top zeroed, badges carry the vertical space on margins.

## [Build 7] — 2026-04-18
- Pro Annual price corrected from $9.99 → **$17.99/year**. Savings line recalculated: **Save 25% vs monthly** (monthly × 12 = $23.88; $23.88 − $17.99 = $5.89 ≈ 25%). Per-month breakdown updated to "$1.50/month, billed yearly". Applied to the pricing card, the FAQ "Is there a subscription?" answer, the `/support/` help page, and the `/terms/` §3a auto-renewing-subscription clause.

## [Build 6] — 2026-04-18
- Dropped the tagline "Built for both stores at the same time. iPhone, iPad, Android phones and tablets." from the iOS/Android platform strip. The pill alone carries the message; the sentence was redundant noise.

## [Build 5] — 2026-04-18
- **Removed the email-waitlist CTA section entirely.** No more "coming to iPhone and Android" form — the messaging now sits with the store badges themselves.
- **Store badges in the hero.** App Store + Google Play badges live directly below the phone mockup, greyed out, each with an amber "COMING SOON" ribbon overlaid at the bottom — same treatment as the Sorted app marketing site. Added `appstore-badge.svg` to assets; Google Play badge is the Wikimedia SVG.
- **Pricing split into three tiers.** Bucko Pro is now two cards: **Pro Monthly** ($1.99/mo, "Most popular", green glow) and **Pro Annual** ($9.99/yr, "Best value", amber glow, "Save 58% vs monthly"). Free stays. Grid goes 3-wide on desktop, stacks on mobile.
- Removed `.cta-and` and `.cta-*` CSS, dead after the CTA section was dropped.
- New CSS: `.hero-badges`, `.badge-wrap`, `.badge-img`, `.coming-banner`, `.price-grid-3`, `.price-card-value`, `.price-badge-value`.

## [Build 4] — 2026-04-18
- **New Pricing section** with two side-by-side cards (Free + Bucko Pro), between How-it-works and the CTA. Pro card gets a "Most families" badge, the subtle green glow treatment, and the $9.99/year alt price with 7-day-trial line. Added `#pricing` to the nav.
- **Copy neatened across the board**. Hero lede, feature paragraphs, steps, CTA body, and all five FAQ answers trimmed — same message, fewer words. No content removed, just less filler.
- **Removed the red half-circle minus buttons** from the phone mockup in the hero (the `.big-btn-minus` overlays that peeked out of the bottom-left of each big button). Mockup now shows clean circular buttons only.
- New CSS: `.price-grid`, `.price-card`, `.price-card-featured`, `.price-badge`, `.price`, `.price-amount`, `.price-period`, `.price-alt`, `.price-lede`, `.price-list`.

## [Build 3] — 2026-04-18
- **iOS + Android positioning**. Site now reflects that Bucko ships on both stores at the same time:
  - New "iOS · Android" platform strip under the nav
  - CTA section retitled "Bucko is coming to iPhone *and* Android"
  - "Is it on Android?" FAQ flipped from "iPhone first, Android on the way" to "yes, both at once"
  - "What if I lose my phone?" FAQ now mentions Google Drive sync alongside iCloud sync as upcoming
- **Bucko Pro** ($1.99/mo or $9.99/yr, 7-day free trial) now reflected throughout:
  - "Is there a subscription?" FAQ updated from "No, pay once" to the actual model — free plan is one kid, Pro unlocks unlimited
  - "How many kids can I add?" FAQ now states the one-kid free-tier limit and the Pro upgrade
- **New legal pages** required for App Store + Play Store submission:
  - `/privacy/` — full privacy policy with a dedicated Bucko Pro subscriptions section (RevenueCat + Apple/Google data flows)
  - `/terms/` — Terms of Use (EULA) including the Apple Licensed Application clauses and a §3a auto-renewing-subscription disclosure
  - `/support/` — FAQs + contact, with a `#data-deletion` anchor for Play Console's data-deletion-URL field, plus a Subscriptions section
- Footer now includes Privacy / Terms / Support links on every page
- New CSS modules: `.platform-strip`, `.cta-and`, `.footer-links`, `.doc-page` family (`.doc-head`, `.doc-body`, `.doc-callout`, `.doc-toc`)
- Default contact address: `hello@getbucko.com`

## [Build 2] — 2026-04-17
- Replaced emoji in hero mockup and feature cards with Freepik lineal-color icons (dog, fox, trophy, calendar, coin, home, happy, art)
- Scaled phone-mockup button icons (54px) and feature-card icons (80px) to match the mobile app's icon-to-button proportions
- Rewrote copy end-to-end for parents instead of developers: removed Raspberry Pi / Node origin story, "tap-spam / cool-down" jargon, founder first-person asides, and the "3,400+ bundled icons" line
- New framing centres on the actual parent pain — kids pushing back, chore charts falling off the fridge, Sunday payout arguments

## [Build 1] — 2026-04-17
- Initial marketing site deployed to GitHub Pages at getbucko.com
- DNS configured on GoDaddy (apex A records + www CNAME), HTTPS enforced, domain verification TXT added
