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
npm run debug                    # Eleventy build with full DEBUG output
```

`npm test` runs `jest`, but the project has no tests.

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
│   ├── pseudocode.js     # Prism language `pseudocode` (French keywords, variable highlighting)
│   └── typst.js          # Typst: .typ templates + {% typst %} / {% algorithme %} shortcodes
├── src/                  # Input (markdown + templates)
│   ├── _includes/
│   │   ├── layout/       # base.njk (HTML shell, MathJax), post.njk (content pages), index.njk
│   │   ├── toc.njk       # Floating table of contents (included by post.njk)
│   │   └── tree.njk      # Tree listing (used by tutoriels/index.njk)
│   ├── assets/           # CSS (stylesheets/main.css), JS, images
│   ├── cours/            # Course content by topic
│   ├── enseignements/    # School-specific course pages (ECM, MPCI)
│   └── tutoriels/        # Tutorials
└── dist/                 # Generated output (gitignored)
```

## Content authoring

### Frontmatter

Every page, including course index pages, uses `layout/post.njk`:

```yaml
---
layout: layout/post.njk
title: Page Title
tags: ["cours", "algorithmie"]   # optional
authors:
  - François Brucker
resume: "Short summary"          # optional
date: 2026-01-02                 # optional
eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---
```

### Custom shortcodes

All are paired shortcodes (content between open/close tags, rendered as markdown):

| Shortcode | Purpose |
|---|---|
| `{% info %}...{% endinfo %}` | Informational callout (cyan) |
| `{% attention %}...{% endattention %}` | Warning callout |
| `{% note %}...{% endnote %}` | Note callout |
| `{% definition "Title" %}...{% enddefinition %}` | Definition callout |
| `{% retenir %}...{% endretenir %}` | "À retenir" callout |
| `{% faire %}...{% endfaire %}` | Action/task callout |
| `{% exercice %}...{% endexercice %}` | Exercise block |
| `{% details "Title" %}...{% enddetails %}` | Collapsible section |
| `{% prerequis "Label" %}...{% endprerequis %}` | Prerequisites block |
| `{% lien %}...{% endlien %}` | Related links |
| `{% chemin %}...{% endchemin %}` | File path display |
| `{% aller %}...{% endaller %}` | Navigation link |

Typst shortcodes (defined in `config/typst.js`, compiled to SVG at build time):

| Shortcode | Purpose |
|---|---|
| `{% typst "#set …", … %}...{% endtypst %}` | Arbitrary Typst content rendered as SVG; arguments are prepended Typst lines |
| `{% algorithme %}...{% endalgorithme %}` | Pseudocode written with the Typst `lovelace` package, rendered as SVG |

`.typ` files in `src/` are also compiled as templates (output SVG).

### Links

External links are detected automatically: any link whose `href` starts with `http://` or `https://` is styled as external via a CSS attribute selector in `src/assets/stylesheets/main.css`. No class is needed:

```markdown
[Some site](https://example.com/)
```

Internal links must therefore be relative (not absolute `https://…` URLs to the site itself). The `.externe` class still exists to force external styling on a link (or on all links inside an element) when needed.

Other markdown-it-attrs classes:

- `{.fichier}`: file/path styling with a file icon, mostly on inline code (`` `/dev/random`{.fichier} ``)
- `{.interne}`: internal-link styling, typically on placeholder links to pages not written yet (`[ensembles](){.interne}`)

### Code blocks

A custom Prism language `pseudocode` (in `config/pseudocode.js`) is registered for algorithm pseudocode with French keywords (`algorithme`, `si/sinon`, `tant que`, `pour`, etc.). Use it with a ```` ```pseudocode ```` fenced block.

### Table of contents

`src/_includes/toc.njk` (included at the end of `post.njk`) builds a floating "Sommaire" client-side from the article's `h2`/`h3` headings, ignoring headings inside `<details>`, and adds an `id` to headings that lack one. It is fixed top-left, closed by default, and toggled by its button; the active section is highlighted on scroll. It also moves the header's scroll-to-top/bottom arrow buttons to the right of the "Sommaire" button. Pages with fewer than two headings get no TOC, and the arrows stay in the header. Styles are under `#toc` in `src/assets/stylesheets/main.css`.

### Math

MathJax is loaded client-side in `src/_includes/layout/base.njk` (served from `dist/assets/node_modules/mathjax`, hence `npm run node-modules-front`). Inline math: `$…$` or `\(…\)`; display math: `$$…$$`. The `eleventy-plugin-mathjax` import in `config/markdown/index.js` is commented out and unused.

### Bulk edits

Some course examples contain their own `node_modules/` (e.g. under `src/cours/web/projet-numérologie/`). Exclude `node_modules` when searching or doing mass replacements in `src/`.
