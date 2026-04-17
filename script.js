// Year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Reveal-on-scroll
const io = new IntersectionObserver(
  (entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    }
  },
  { rootMargin: '0px 0px -80px 0px', threshold: 0.1 }
);
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// Animated hero button counters — tick up from 0 to data-count once in view
const countEls = document.querySelectorAll('.big-btn-count');
const countObs = new IntersectionObserver(
  (entries) => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      const el = e.target;
      const target = parseInt(el.getAttribute('data-count') || '0', 10);
      const duration = 1400;
      const start = performance.now();
      const step = (now) => {
        const t = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.round(target * eased).toString();
        if (t < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
      countObs.unobserve(el);
    }
  },
  { threshold: 0.3 }
);
countEls.forEach((el) => countObs.observe(el));

// Smooth-scroll enhancement: press-feedback haptic on supported devices
document.querySelectorAll('.btn-primary').forEach((btn) => {
  btn.addEventListener('click', () => {
    if (window.navigator.vibrate) window.navigator.vibrate(12);
  });
});
