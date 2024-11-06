---
layout: layout/post.njk

title: Noob trap

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Un piège classique dans lequel tombent les débutants.

On considère le code suivant :

```python/
def f(n):
    if n < 2:
        return 1
    return f(n // 2) * f(n // 4)
```

Quelle est l'équation de récurrence de la complexité :

1. $C(n) = C(n/2) * C(n/4)$
2. $C(n) = \mathcal{O}(1) + C(n/2) * C(n/4)$
3. $C(n) = \mathcal{O}(1) + C(n/2) + C(n/4)$

Déduire de la bonne réponse que la complexité de l'exécution de la fonction est linéaire.
