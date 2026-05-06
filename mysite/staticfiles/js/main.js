/* ═══════════════════════════════════════════
   Danny Codes — Portfolio JS
   Stack: Alpine.js · HTMX · Vanilla JS
═══════════════════════════════════════════ */

/* ── Custom Cursor ─────────────────────────── */
const cursorDot  = document.querySelector('.cursor-dot');
const cursorRing = document.querySelector('.cursor-ring');

let mouseX = 0, mouseY = 0;
let ringX  = 0, ringY  = 0;

document.addEventListener('mousemove', e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  if (cursorDot) {
    cursorDot.style.left  = mouseX + 'px';
    cursorDot.style.top   = mouseY + 'px';
  }
});

function animateCursor() {
  ringX += (mouseX - ringX) * 0.12;
  ringY += (mouseY - ringY) * 0.12;
  if (cursorRing) {
    cursorRing.style.left = ringX + 'px';
    cursorRing.style.top  = ringY + 'px';
  }
  requestAnimationFrame(animateCursor);
}
animateCursor();

document.querySelectorAll('a, button, .glass-hover, [data-hover]').forEach(el => {
  el.addEventListener('mouseenter', () => cursorRing?.classList.add('hovering'));
  el.addEventListener('mouseleave', () => cursorRing?.classList.remove('hovering'));
});

/* ── Scroll Reveal ─────────────────────────── */
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* ── Skill Bars ────────────────────────────── */
const skillObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.skill-bar-fill').forEach(bar => {
        bar.style.width = bar.dataset.width || '0%';
      });
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.skills-section').forEach(el => skillObserver.observe(el));

/* ── Typewriter Effect ─────────────────────── */
function typewriter(element, texts, speed = 80, pause = 2200) {
  let textIndex = 0, charIndex = 0, isDeleting = false;

  function type() {
    const current = texts[textIndex];
    if (isDeleting) {
      element.textContent = current.substring(0, charIndex - 1);
      charIndex--;
    } else {
      element.textContent = current.substring(0, charIndex + 1);
      charIndex++;
    }

    let delay = isDeleting ? speed / 2 : speed;
    if (!isDeleting && charIndex === current.length) {
      delay = pause;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      textIndex  = (textIndex + 1) % texts.length;
      delay = 400;
    }
    setTimeout(type, delay);
  }
  type();
}

const typeEl = document.getElementById('typewriter');
if (typeEl) {
  typewriter(typeEl, [
    'Full-Stack Developer',
    'Django Architect',
    'HTMX Enthusiast',
    'Alpine.js Craftsman',
    'Problem Solver',
    'Code Artist',
  ]);
}

/* ── Active Nav Link on Scroll ─────────────── */
const sections  = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.nav-link[data-section]');

const navObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => link.classList.remove('!text-[var(--color-neon-cyan)]'));
      const active = document.querySelector(`.nav-link[data-section="${entry.target.id}"]`);
      active?.classList.add('!text-[var(--color-neon-cyan)]');
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => navObserver.observe(s));

/* ── Mobile Nav Toggle (Alpine handled) ────── */

/* ── Particle background ────────────────────── */
(function particles() {
  const canvas = document.getElementById('particles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;

  window.addEventListener('resize', () => {
    canvas.width  = window.innerWidth;
    canvas.height = window.innerHeight;
  });

  const dots = Array.from({ length: 60 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 1.2 + 0.3,
    dx: (Math.random() - 0.5) * 0.3,
    dy: (Math.random() - 0.5) * 0.3,
    alpha: Math.random() * 0.5 + 0.1,
  }));

  function drawParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    dots.forEach(d => {
      d.x += d.dx;
      d.y += d.dy;
      if (d.x < 0 || d.x > canvas.width)  d.dx *= -1;
      if (d.y < 0 || d.y > canvas.height) d.dy *= -1;

      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(0, 245, 255, ${d.alpha})`;
      ctx.fill();
    });

    // draw connecting lines
    dots.forEach((a, i) => {
      dots.slice(i + 1).forEach(b => {
        const dist = Math.hypot(a.x - b.x, a.y - b.y);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(0, 245, 255, ${0.06 * (1 - dist / 120)})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      });
    });
    requestAnimationFrame(drawParticles);
  }
  drawParticles();
})();

/* ── Smooth section scroll ─────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(a.getAttribute('href'));
    target?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

/* ── HTMX contact form response ─────────────── */
document.body.addEventListener('htmx:afterRequest', e => {
  if (e.detail.elt.id === 'contact-form') {
    const status = document.getElementById('form-status');
    if (status) {
      status.classList.remove('hidden');
      setTimeout(() => status.classList.add('hidden'), 4000);
    }
  }
});
