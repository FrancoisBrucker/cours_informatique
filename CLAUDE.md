# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Static site for computer science courses given by François Brucker, published at https://francoisbrucker.github.io/cours_informatique/. Built with [Eleventy (11ty)](https://www.11ty.dev/) v3, Nunjucks templates, and Tailwind CSS.

## Commands

All commands run from the `docs/` directory:

```bash
npm install                      # First-time setup
npm run serve                    # Dev server at http://localhost:8080
npm run build                    # Production build (local paths)
npm run build-github             # Production build for GitHub Pages (prefixed paths)
npm run clean                    # Remove dist/
npm run node-modules-front       # Install frontend deps in dist/ (needed after clean)
```

Deployment is automatic via GitHub Actions on push to `main` (`.github/workflows/github-pages.yml`).

## Architecture

```
docs/
├── .eleventy.js          # Eleventy entry point: wires plugins, markdown, assets, Typst
├── config/
│   ├── markdown/
│   │   └── shortcodes/quotes/   # Custom paired shortcodes (see below)
│   ├── assets.js         # Static asset passthrough
│   ├── filters.js        # siteUrl filter for URL resolution
│   ├── post-build.js     # Tailwind CSS compilation (runs after Eleventy)
│   └── typst.js          # Typst document compilation
├── src/                  # Input (markdown + templates)
│   ├── _includes/        # Nunjucks layouts (layout/post.njk, layout/tree.njk)
│   ├── assets/           # CSS, JS, images
│   ├── cours/            # Course content by topic
│   └── enseignements/    # School-specific course pages (ECM, MPCI)
└── dist/                 # Generated output (gitignored)
```

## Content authoring

### Frontmatter

Every page requires:

```yaml
---
layout: layout/post.njk
title: Page Title
eleventyNavigation:
eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---
```

Index/listing pages use `layout: layout/tree.njk` instead.

### Custom shortcodes

All are paired shortcodes (content between open/close tags, rendered as markdown):

| Shortcode | Purpose |
|---|---|
| `{% info %}...{% endinfo %}` | Informational callout (cyan) |
| `{% attention %}...{% endattention %}` | Warning callout |
| `{% note %}...{% endnote %}` | Note callout |
| `{% faire %}...{% endfaire %}` | Action/task callout |
| `{% exercice %}...{% endexercice %}` | Exercise block |
| `{% details "Title" %}...{% enddetails %}` | Collapsible section |
| `{% prerequis "Label" %}...{% endprerequis %}` | Prerequisites block |
| `{% lien %}...{% endlien %}` | Related links |
| `{% chemin %}...{% endchemin %}` | File path display |
| `{% aller %}...{% endaller %}` | Navigation link |

### Internal links

Use `.interne` class to mark links as internal (styled differently):

```markdown
[Some page](/cours/some-topic/){.interne}
```

### Code blocks

A custom `pseudocode` language is registered for algorithm pseudocode with French keywords (`algorithme`, `si/sinon`, `tant que`, `pour`, etc.).

### Math

MathJax is configured (plugin import commented out in `config/markdown/index.js` — enable if needed).
