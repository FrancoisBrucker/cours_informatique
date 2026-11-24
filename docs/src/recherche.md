---
layout: layout/post.njk
title: Recherche
eleventyExcludeFromCollections: true
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js"></script>

<div id="recherche" class="not-prose"></div>

<script>
  window.addEventListener("DOMContentLoaded", () => {
    const ui = new PagefindUI({
      element: "#recherche",
      showSubResults: true,
      showImages: false,
      resetStyles: false,
      autofocus: true,
    });
    // permet les liens du type /recherche/?q=graphe
    const q = new URLSearchParams(window.location.search).get("q");
    if (q) ui.triggerSearch(q);
  });
</script>
