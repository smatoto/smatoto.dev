# smatoto.dev

A structured, version-controlled portfolio of public talks and workshops.

**View the portfolio:** [smatoto.dev](https://smatoto.dev)

## Key Features

- **Impact Metrics** — Tracks total sessions delivered, developers reached, and speaking years
- **Responsive Design** — Mobile-friendly portfolio built with MkDocs Material theme
- **Filterable Sessions** — Browse all sessions by year, category, or type (Talk/Workshop)

## Adding a New Session

1. Copy `template.md` to `docs/{YEAR}/T{N} - Title.md` (or `W{N}` for workshops)
2. Fill in YAML front matter with metadata (title, summary, type, category, events, etc.)
3. Write content in markdown (Abstract, Outline/Agenda, Speaker Notes)
4. Add row to `docs/index.md` session table
5. Update `mkdocs.yml` navigation tree
6. Commit & push — GitHub Actions auto-deploys

## Tech Stack

- **MkDocs** — Static site generator
- **Material for MkDocs** — Modern, responsive theme
- **Python** — Stats automation script
- **GitHub Pages** — Hosting
- **GitHub Actions** — Auto-deployment pipeline

## Local Development

```bash
# Install dependencies
pip install mkdocs-material

# Serve locally
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy --force
```

## License

Content and documentation are personal work. The repo structure and automation are available for reference.

---

**Questions or feedback?** Reach out on [LinkedIn](https://linkedin.com/in/smatoto) or [GitHub](https://github.com/smatoto)
