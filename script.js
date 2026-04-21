// ── Scroll reveal ──────────────────────────────────────────────────────
const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(
    entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }),
    { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
  );
  revealEls.forEach(el => io.observe(el));
} else {
  revealEls.forEach(el => el.classList.add('in'));
}

// ── Counter animation (phone mockup) ──────────────────────────────────
function animateCounter(el, target, duration) {
  const start = performance.now();
  (function tick(now) {
    const p = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - p, 3);
    el.textContent = Math.round(eased * target);
    if (p < 1) requestAnimationFrame(tick);
  })(start);
}
document.querySelectorAll('[data-count]').forEach(el => {
  const target = parseInt(el.dataset.count, 10);
  const io = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) { animateCounter(el, target, 1800); io.disconnect(); }
  }, { threshold: 0.5 });
  io.observe(el);
});

// ── Currency picker ────────────────────────────────────────────────────
const CURRENCIES = {
  AUD: { monthly: 'A$1.99',  annual: 'A$17.99',  faqM: 'A$1.99/month',  faqA: 'A$17.99/year'  },
  NZD: { monthly: 'NZ$1.99', annual: 'NZ$17.99', faqM: 'NZ$1.99/month', faqA: 'NZ$17.99/year' },
  GBP: { monthly: '£0.99',   annual: '£9.99',    faqM: '£0.99/month',   faqA: '£9.99/year'    },
  USD: { monthly: '$0.99',   annual: '$9.99',     faqM: '$0.99/month',   faqA: '$9.99/year'    },
  CAD: { monthly: 'C$0.99',  annual: 'C$12.99',   faqM: 'C$0.99/month',  faqA: 'C$12.99/year'  },
  EUR: { monthly: '€0.99',   annual: '€9.99',     faqM: '€0.99/month',   faqA: '€9.99/year'    },
};

function detectCurrency() {
  const tz   = (Intl.DateTimeFormat().resolvedOptions().timeZone || '').toLowerCase();
  const lang = (navigator.language || '').toLowerCase();

  if (tz.startsWith('australia/') || lang === 'en-au') return 'AUD';
  if (tz.startsWith('pacific/auckland') || tz === 'pacific/chatham' || lang === 'en-nz') return 'NZD';
  if (tz === 'europe/london'      || lang === 'en-gb') return 'GBP';
  if (lang.startsWith('en-ca') || [
    'america/toronto','america/vancouver','america/edmonton',
    'america/winnipeg','america/halifax','america/st_johns','america/regina',
    'america/moncton','america/glace_bay','america/goose_bay'
  ].includes(tz)) return 'CAD';
  if (tz.startsWith('america/') && (lang === 'en-us' || lang.startsWith('en-us'))) return 'USD';
  if (tz.startsWith('europe/')) return 'EUR';
  return 'USD';
}

function applyCurrency(code) {
  const c = CURRENCIES[code];
  if (!c) return;

  const pm = document.getElementById('price-monthly');
  const pa = document.getElementById('price-annual');
  const fm = document.getElementById('faq-price-monthly');
  const fa = document.getElementById('faq-price-annual');

  if (pm) pm.textContent = c.monthly;
  if (pa) pa.textContent = c.annual;
  if (fm) fm.textContent = c.faqM;
  if (fa) fa.textContent = c.faqA;

  document.querySelectorAll('.currency-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.currency === code);
  });

  try { localStorage.setItem('bucko_currency', code); } catch (e) {}
}

const picker = document.getElementById('currency-picker');
if (picker) {
  let saved;
  try { saved = localStorage.getItem('bucko_currency'); } catch (e) {}
  applyCurrency((saved && CURRENCIES[saved]) ? saved : detectCurrency());

  picker.addEventListener('click', e => {
    const btn = e.target.closest('.currency-btn');
    if (btn && btn.dataset.currency) applyCurrency(btn.dataset.currency);
  });
}

// ── Footer year ────────────────────────────────────────────────────────
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();
