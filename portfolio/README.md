# marcus.chen — portfolio

Static portfolio site for Marcus Chen, full-stack developer. Pure HTML/CSS/JS — no build step required.

## Structure

```
portfolio/
├── index.html          # All markup
├── css/styles.css      # Theme, layout, components
├── js/main.js          # Data + interactions (projects, skills, posts, form, reveal)
└── assets/
    └── marcus-chen-resume.pdf
```

## Running locally

Any static server works. From the repo root:

```bash
cd portfolio
python3 -m http.server 8000
# then open http://localhost:8000
```

## Editing content

All projects, skills, and writing entries are defined as data arrays at the top of `js/main.js` (`projects`, `skillGroups`, `posts`). Update those to refresh the site — no template edits needed.

## Theme

Three-color palette defined as CSS custom properties in `:root`:

- `--bg` — black (`#0a0a0b`)
- `--neon` — neon green (`#39ff7a`)
- slate grays (`--text-muted`, `--slate-*`)

## Form wiring

`setupContactForm()` in `main.js` simulates submission. To wire to a real backend (Formspree, Resend, your own API), replace the `setTimeout` block with a `fetch()` POST.
