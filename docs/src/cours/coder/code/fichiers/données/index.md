---
layout: layout/post.njk 
title: "Fichiers de données csv et json"

eleventyNavigation:
    order: 4

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Stocker des données au format texte.

<!-- end résumé -->

Lorsque l'on manipule des données, on essaye toujours :

* d'enregistrer ses données dans un fichier texte que l'on peut simplement consulter avec un éditeur de texte
* ou d'utiliser un format de stockage connu plutôt que d'inventer son format, cela permet d'utiliser des bibliothèques de traitement de données classiques.

{% note %}

Plutôt que d'écrire simplement un fichier texte contenant nos données, on préférera les structurer dans un format permettant de les relire simplement. On en conseille deux :

* les [fichiers csv](https://fr.wikipedia.org/wiki/Comma-separated_values) pour des données de type tableaux excel
* les [fichiers json](https://www.json.org/json-fr.html) pour des données structurées en fiches.

{% endnote %}

Nous ne l'étudierons pas ici, mais la plupart du temps, lorsque l'on utilise des données, on ne le fait pas la main, mais en utilisant une bibliothèque. En analyse des données, on utilise intensivement la bibliothèque [pandas](https://pandas.pydata.org/).

## Projets

Plutôt qu'un cours, suivez ces deux projets qui vous permettrons de manipuler les deux types de fichiers de données textes standards :

<div class="interne">
{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToHtml() | safe }}
</div>
