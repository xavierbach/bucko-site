# Bucko Site Changelog

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
