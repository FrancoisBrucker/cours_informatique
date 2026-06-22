# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Exam materials for the L1 MPCI (first-year CS) final programming exam ("Examen terminal: Programmation"), held May 28, 2026. The exam covers inversion counting and skip lists.

## Structure

- `index.md` — landing page for the course website (Eleventy/Nunjucks template)
- `sujet/main.tex` — LaTeX source for the exam paper
- `sujet/code.py` — reference Python code (KMP substring search)
- `sujet/*.png` — diagrams embedded in the exam (source: `figs.graffle`)

## Building the exam PDF

```bash
cd sujet && pdflatex main.tex
```

Run twice if cross-references change. Output: `sujet/main.pdf`.

## Editing diagrams

Diagrams (`skip-list.png`, `skip-list-régulière.png`) are exported from `sujet/figs.graffle` (OmniGraffle). Edit the `.graffle` file and re-export to PNG before recompiling LaTeX.

## Course website

`index.md` uses an Eleventy layout (`layout/post.njk`). The site is built from a parent project; this directory is a content subfolder, not a standalone site.
