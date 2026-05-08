// =========================================================
// Marcus Chen — Portfolio: data + interactions
// =========================================================

const projects = [
    {
        title: "Helix Realtime DB",
        year: "2025",
        glyph: "⌬ helix",
        description: "Embedded, ACID-compliant realtime database with row-level subscriptions. Powers a handful of small SaaS products in production.",
        tags: ["Rust", "tokio", "WAL", "WebSocket"],
        demo: "https://helix.dev",
        repo: "https://github.com/marcuschen/helix"
    },
    {
        title: "Tideflow",
        year: "2025",
        glyph: "≋ tideflow",
        description: "A typed workflow orchestrator for distributed jobs. Built around durable execution with replayable, content-addressed steps.",
        tags: ["Go", "PostgreSQL", "gRPC", "OpenTelemetry"],
        demo: "https://tideflow.io",
        repo: "https://github.com/marcuschen/tideflow"
    },
    {
        title: "Lumen UI",
        year: "2024",
        glyph: "✦ lumen-ui",
        description: "Headless React component library focused on accessibility primitives. Used by ~120 teams; 1.4k weekly downloads.",
        tags: ["TypeScript", "React", "ARIA", "Vitest"],
        demo: "https://lumen-ui.dev",
        repo: "https://github.com/marcuschen/lumen-ui"
    },
    {
        title: "Quill CMS",
        year: "2024",
        glyph: "✎ quill",
        description: "A flat-file, git-backed CMS with a structured content schema and live preview. Optimised for static-first publishing.",
        tags: ["Node.js", "Astro", "Yjs", "Zod"],
        demo: "https://quillcms.com",
        repo: "https://github.com/marcuschen/quill"
    },
    {
        title: "Sparrow Edge",
        year: "2023",
        glyph: "↯ sparrow",
        description: "Edge-deployed analytics pipeline that streams batched events from 40+ POPs into a columnar warehouse with sub-second freshness.",
        tags: ["Rust", "ClickHouse", "Cloudflare", "Kafka"],
        demo: "https://sparrow.observer",
        repo: "https://github.com/marcuschen/sparrow"
    },
    {
        title: "Drift Migrate",
        year: "2023",
        glyph: "⤳ drift",
        description: "Zero-downtime PostgreSQL schema migrator with online-safe rewrite plans. Inspired by years of broken Saturday deploys.",
        tags: ["Go", "PostgreSQL", "DDL"],
        demo: null,
        repo: "https://github.com/marcuschen/drift"
    }
];

const skillGroups = [
    {
        title: "languages",
        items: [
            { name: "TypeScript / JavaScript", years: "8 yrs", level: 95 },
            { name: "Rust", years: "4 yrs", level: 80 },
            { name: "Go", years: "5 yrs", level: 85 },
            { name: "Python", years: "6 yrs", level: 75 },
            { name: "SQL", years: "8 yrs", level: 90 }
        ]
    },
    {
        title: "frontend",
        items: [
            { name: "React / Next.js", years: "7 yrs", level: 95 },
            { name: "CSS / Tailwind", years: "8 yrs", level: 88 },
            { name: "Web Performance", years: "5 yrs", level: 82 },
            { name: "Accessibility (WCAG)", years: "4 yrs", level: 78 }
        ]
    },
    {
        title: "backend & data",
        items: [
            { name: "Node.js / Deno", years: "8 yrs", level: 92 },
            { name: "PostgreSQL", years: "8 yrs", level: 90 },
            { name: "Redis / Streams", years: "5 yrs", level: 80 },
            { name: "gRPC / Protobuf", years: "4 yrs", level: 75 },
            { name: "GraphQL", years: "5 yrs", level: 78 }
        ]
    },
    {
        title: "infra & ops",
        items: [
            { name: "Docker / Kubernetes", years: "6 yrs", level: 85 },
            { name: "Terraform", years: "4 yrs", level: 72 },
            { name: "AWS / GCP", years: "7 yrs", level: 82 },
            { name: "Observability (OTel)", years: "3 yrs", level: 70 }
        ]
    }
];

const posts = [
    {
        date: "2026.04.18",
        title: "We rewrote our hot path in Rust — here's what we got, and what we didn't",
        tags: ["rust", "performance", "postmortem"],
        readTime: "12 min"
    },
    {
        date: "2026.02.03",
        title: "A pragmatic guide to durable workflows without the framework",
        tags: ["distributed-systems", "go"],
        readTime: "9 min"
    },
    {
        date: "2025.11.27",
        title: "PostgreSQL row-level locking: when SELECT FOR UPDATE bites back",
        tags: ["postgres", "concurrency"],
        readTime: "14 min"
    },
    {
        date: "2025.09.10",
        title: "The cost of zero — measuring the carbon overhead of edge functions",
        tags: ["edge", "sustainability"],
        readTime: "7 min"
    },
    {
        date: "2025.06.22",
        title: "Designing typed contracts between web workers without losing your mind",
        tags: ["typescript", "browser"],
        readTime: "8 min"
    }
];

// =========================================================
// Renderers
// =========================================================

const escapeHtml = (str) => String(str).replace(/[&<>"']/g, (c) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
));

function renderProjects() {
    const grid = document.getElementById('projects-grid');
    if (!grid) return;
    grid.innerHTML = projects.map((p, i) => `
        <article class="project reveal" style="transition-delay:${i * 60}ms">
            <div class="project__visual" aria-hidden="true">
                <div class="project__visual-inner">${escapeHtml(p.glyph)}</div>
                <span class="project__visual-glyph">// project ${String(i + 1).padStart(2, '0')}</span>
            </div>
            <div class="project__body">
                <div class="project__top">
                    <h3 class="project__title">${escapeHtml(p.title)}</h3>
                    <span class="project__year">${escapeHtml(p.year)}</span>
                </div>
                <p class="project__desc">${escapeHtml(p.description)}</p>
                <ul class="project__tags">
                    ${p.tags.map(t => `<li class="tag">${escapeHtml(t)}</li>`).join('')}
                </ul>
                <div class="project__links">
                    ${p.demo ? `
                        <a class="project__link project__link--demo" href="${escapeHtml(p.demo)}" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24"><path d="M14 3v2h3.6l-9.8 9.8 1.4 1.4L19 6.4V10h2V3h-7zM5 5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7h-2v7H5V5z"/></svg>
                            live demo
                        </a>` : ''
                    }
                    <a class="project__link" href="${escapeHtml(p.repo)}" target="_blank" rel="noopener">
                        <svg viewBox="0 0 24 24"><path d="M12 2C6.5 2 2 6.5 2 12c0 4.4 2.9 8.2 6.8 9.5.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.4-3.4-1.4-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.3 1.1 2.9.8.1-.6.4-1.1.6-1.3-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1 .8-.2 1.7-.3 2.5-.3s1.7.1 2.5.3c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.8v2.6c0 .3.2.6.7.5C19.1 20.2 22 16.4 22 12c0-5.5-4.5-10-10-10z"/></svg>
                        source
                    </a>
                </div>
            </div>
        </article>
    `).join('');
}

function renderSkills() {
    const wrap = document.getElementById('skills-grid');
    if (!wrap) return;
    wrap.innerHTML = skillGroups.map((g, gi) => `
        <div class="skill-group reveal" style="transition-delay:${gi * 80}ms">
            <h3 class="skill-group__title">${escapeHtml(g.title)}</h3>
            <ul class="skill-list">
                ${g.items.map(s => `
                    <li class="skill">
                        <span class="skill__name">${escapeHtml(s.name)}</span>
                        <span class="skill__years">${escapeHtml(s.years)}</span>
                        <div class="skill__bar" role="progressbar" aria-valuenow="${s.level}" aria-valuemin="0" aria-valuemax="100" aria-label="${escapeHtml(s.name)} proficiency">
                            <div class="skill__bar-fill" data-level="${s.level}"></div>
                        </div>
                    </li>
                `).join('')}
            </ul>
        </div>
    `).join('');
}

function renderPosts() {
    const list = document.getElementById('posts-list');
    if (!list) return;
    list.innerHTML = posts.map((p, i) => `
        <li class="reveal" style="transition-delay:${i * 50}ms">
            <a class="post" href="#">
                <span class="post__date">${escapeHtml(p.date)}</span>
                <div class="post__main">
                    <span class="post__title">${escapeHtml(p.title)}</span>
                    <ul class="post__tags">
                        ${p.tags.map(t => `<li class="tag">#${escapeHtml(t)}</li>`).join('')}
                    </ul>
                </div>
                <span class="post__read">${escapeHtml(p.readTime)}</span>
            </a>
        </li>
    `).join('');
}

// =========================================================
// Reveal observer
// =========================================================

function setupRevealObserver() {
    const items = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {
        items.forEach(el => el.classList.add('is-visible'));
        return;
    }
    const io = new IntersectionObserver((entries) => {
        for (const entry of entries) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                if (entry.target.classList.contains('skill-group')) {
                    const fills = entry.target.querySelectorAll('.skill__bar-fill');
                    fills.forEach((bar) => {
                        const lvl = bar.getAttribute('data-level');
                        requestAnimationFrame(() => { bar.style.width = lvl + '%'; });
                    });
                }
                io.unobserve(entry.target);
            }
        }
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(el => io.observe(el));
}

// Apply reveal class to top-level elements that aren't built dynamically
function tagBaseRevealTargets() {
    const selectors = [
        '.hero__meta', '.hero__title', '.hero__lede',
        '.hero__stack', '.hero__cta', '.hero__stats',
        '.section__header'
    ];
    selectors.forEach(sel => {
        document.querySelectorAll(sel).forEach((el, i) => {
            el.classList.add('reveal');
            el.style.transitionDelay = `${i * 60}ms`;
        });
    });
}

// =========================================================
// Nav behavior
// =========================================================

function setupNav() {
    const nav = document.getElementById('nav');
    const toggle = document.querySelector('.nav__toggle');
    const links = document.querySelector('.nav__links');

    const onScroll = () => {
        if (window.scrollY > 8) nav.classList.add('is-scrolled');
        else nav.classList.remove('is-scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    if (toggle && links) {
        toggle.addEventListener('click', () => {
            const open = links.classList.toggle('is-open');
            toggle.classList.toggle('is-open', open);
            toggle.setAttribute('aria-expanded', String(open));
        });
        links.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => {
                links.classList.remove('is-open');
                toggle.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }
}

// =========================================================
// Back to top
// =========================================================

function setupBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;
    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// =========================================================
// Contact form
// =========================================================

function setupContactForm() {
    const form = document.getElementById('contact-form');
    const status = document.getElementById('contact-status');
    if (!form) return;

    const setError = (name, msg) => {
        const field = form.querySelector(`[name="${name}"]`);
        const errEl = form.querySelector(`[data-error-for="${name}"]`);
        if (!field || !errEl) return;
        field.parentElement.classList.toggle('has-error', !!msg);
        errEl.textContent = msg || '';
    };

    const validate = (fd) => {
        let ok = true;
        const name = (fd.get('name') || '').toString().trim();
        const email = (fd.get('email') || '').toString().trim();
        const message = (fd.get('message') || '').toString().trim();

        setError('name', '');
        setError('email', '');
        setError('message', '');

        if (name.length < 2) { setError('name', 'name is required'); ok = false; }
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { setError('email', 'enter a valid email'); ok = false; }
        if (message.length < 10) { setError('message', 'tell me a bit more (10+ chars)'); ok = false; }
        return ok;
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const fd = new FormData(form);
        status.dataset.state = '';
        status.textContent = '';

        if (!validate(fd)) {
            status.dataset.state = 'error';
            status.textContent = '✗ please fix the errors above.';
            return;
        }

        const submit = form.querySelector('.contact__submit');
        const submitText = form.querySelector('.contact__submit-text');
        const original = submitText.textContent;
        submit.setAttribute('disabled', 'true');
        submitText.textContent = 'sending…';
        status.textContent = '> dispatching message…';

        // Simulated send — wire to a real endpoint when deploying
        setTimeout(() => {
            submit.removeAttribute('disabled');
            submitText.textContent = original;
            status.textContent = '✓ message queued. I\'ll get back to you within 24h.';
            form.reset();
        }, 1100);
    });

    // Clear errors on input
    form.querySelectorAll('input, textarea').forEach(el => {
        el.addEventListener('input', () => setError(el.name, ''));
    });
}

// =========================================================
// Init
// =========================================================

document.addEventListener('DOMContentLoaded', () => {
    renderProjects();
    renderSkills();
    renderPosts();
    tagBaseRevealTargets();
    setupRevealObserver();
    setupNav();
    setupBackToTop();
    setupContactForm();
});
