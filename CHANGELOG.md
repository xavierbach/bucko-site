# bucko-site changelog

## 2026-04-17
- **iOS + Android positioning**. Site now reflects that Bucko ships on both stores at the same time:
  - New "iOS · Android" platform strip under the nav
  - CTA section retitled "Bucko is coming to iPhone *and* Android"
  - "Is it on Android?" FAQ flipped from "iOS first, Android someday" to "yes, both at once"
  - "What if I lose my phone?" FAQ now mentions Google Drive sync alongside iCloud sync as upcoming
- **New legal pages** required for App Store + Play Store submission:
  - `/privacy/` — full privacy policy, written around the app's actual on-device-only data behaviour
  - `/terms/` — Terms of Use (EULA) including the Apple Licensed Application clauses
  - `/support/` — FAQs + contact, with `#data-deletion` anchor for Play Console's data-deletion-URL field
- Footer now includes Privacy / Terms / Support links on every page
- New CSS modules: `.platform-strip`, `.doc-page`, `.doc-head`, `.doc-body`, `.doc-callout`, `.doc-toc`, `.footer-links`
- Default contact address: `hello@getbucko.com`
