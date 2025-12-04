---
layout: layout/post.njk

title: Tutoriel numpy

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à étoffer, ajouter les création de listes à intervalle fixe

Le [module `numpy`{.language-}](https://numpy.org/) possède de nombreuses fonction permettant de manipuler des tableaux. Ce ne sont pas _stricto sensu_ des listes puisque leur type est [`array`{.language-}](https://numpy.org/doc/stable/reference/generated/numpy.array.html) mais on peut souvent utiliser des `array`{.language-}s à la place des listes et réciproquement.

{% exercice %}
Utilisez la fonction [`numpy.random.randint`{.language-}](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html) pour créer un array de 10 entiers pris aléatoirement entre 3 et 9.
{% endexercice %}
{% details "solution" %}

```python
>>> import numpy as np
>>> np.random.randint(3, 10, size=10)
array([4, 6, 4, 7, 6, 5, 6, 7, 8, 5])
```

{% enddetails %}
