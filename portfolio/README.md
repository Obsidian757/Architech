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

## Deploying to GitHub Pages

A workflow at `.github/workflows/deploy-pages.yml` publishes the `portfolio/` directory to GitHub Pages on every push to `main` (or to the `claude/build-portfolio-website-mWGLo` branch) that touches portfolio files.

**One-time setup** (the workflow can't do this for you):

1. Go to **Settings → Pages** in the GitHub repo.
2. Under **Source**, select **GitHub Actions**.
3. Push to a covered branch (or trigger the workflow manually via the *Actions* tab). The first run will create the `github-pages` environment and publish the site.

The deployed URL appears in the workflow summary and on **Settings → Pages**; it follows the pattern `https://<owner>.github.io/<repo>/`.

## Configuring the contact form (Formspree)

The contact form posts to [Formspree](https://formspree.io) — a hosted form backend with a free tier. Two steps:

1. Create a free Formspree account and a new form. Copy the form ID (looks like `xnqekvyz`).
2. Replace the placeholder `YOUR_FORM_ID` in **two places**:
   - `js/main.js` — the `FORMSPREE_ENDPOINT` constant at the top of the file.
   - `index.html` — the `action` attribute on `<form id="contact-form">` (provides the no-JS fallback).

Until the ID is set, the form shows a clear "form backend not configured — email hello@marcuschen.dev directly" message instead of pretending to send.

To use a different provider (Web3Forms, your own API), update both spots with the new endpoint; the JS sends a standard `FormData` POST that any compatible service will accept.

## Replacing the resume

The resume at `assets/marcus-chen-resume.pdf` is a generated placeholder for the demo persona. Replace it with a real PDF using the same filename — no other edits needed.
