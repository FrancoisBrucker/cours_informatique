---
layout: layout/post.njk 
title:  "Multiplication de matrices"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment utiliser la réduction pour créer des algorithmes. Exemple de la multiplication de Matrices.

> TBD en faire un DM/exos.
>
<https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication>
> algo : <https://mathworld.wolfram.com/StrassenFormulas.html>

> Multipication matrice = inversion <https://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion>

1. Simple
2. Strassen
3. voir ça comme une réduction.
4. amélioration $\mathcal{O}(n^\omega)$ 

> TBD exposé de la méthode : <https://www.youtube.com/watch?v=HdysaWNs1g8>
> voir aussi <https://www.youtube.com/watch?v=DruwS2_cVys>

> TBD utilisation de la réduction comme outils de computation d'algorithmes
> 
> TBD review <https://www.youtube.com/watch?v=sZxjuT1kUd0>

Fonctionne aussi pour inversion de matrice. (cf strassen)

> TBD review : <https://theoryofcomputing.org/articles/gs005/gs005.pdf>
> TBD coppersmith winograde <https://www-auth.cs.wisc.edu/lists/theory-reading/2009-December/pdfmN6UVeUiJ3.pdf>
