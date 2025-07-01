---
layout: layout/post.njk

title: "{2, 3}-SUM"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

3-SUM est la base de bien d'autres problèmes. On en reparlera bien plus tard, mais ce problème est une des bases algorithmique de [la géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique). Commençons par un problème simple, 2-SUM

## <span id="2-sum"></span>2-SUM

<span id="problème-2-SUM"></span>

{% note "Problème" %}

- **nom** : 2-SUM
- **données** : Un tableau T d'entiers relatifs
- **question** : Existe-t-il deux indices $i$ et $j$ (ils peuvent être égaux) tels que $T[i] + T[j] = 0$ ?
{% endnote %}

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^2)$
- spatiale en $\mathcal{O}(1)$

{% endexercice %}

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}\ln(T.\mbox{\small longueur}))$
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}

Un nouvel algorithme :

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité $\mathcal{O}(\max(T))$.

Est-ce réaliste ?

{% endexercice %}

## <span id="3-sum"></span>3-SUM

<span id="problème-3-SUM"></span>

{% note "Problème" %}

- **nom** : 3-SUM
- **données** : Un tableau T d'entiers relatifs
- **question** : Existe-t-il trois indices $i$, $j$ et $k$ (ils peuvent être égaux) tel que $T[i] + T[j] + T[k] = 0$ ?
{% endnote %}

{% exercice %}
Donnez une solution au problème 3-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^3)$
- spatiale en $\mathcal{O}(1)$

{% endexercice %}

Enfin, l'exercice dur qui montre que l'on peu résoudre 3-SUM plus efficacement avec un coût en mémoire :

{% exercice %}
Donnez une solution au problème 3-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^2)$
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}
