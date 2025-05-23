---
layout: layout/post.njk

title: Algorithme du pgcd

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

On a déjà vu une version de l'algorithme du pgcd. Rappelons -là :

```pseudocode
algorithme pgcd(a: entier, b: entier) → entier:  # a, b ≥ 0
    tant que min(a, b) > 0:
        a' ← max(a, b) - min(a, b)
        b' ← min(a, b)
        a, b ← a', b'
    
    rendre max(a, b)
```

La version couramment utilisée est celle utilisant un modulo (opérateur `%`{.language-} en algorithmie) qui converge plus vite.

Cet algorithme est basé sur le fait que $a = qb + r$ on a `pgcd(a, b) = pgcd(b, r)`{.language-}.

{% faire %}
Donnez un algorithme récursif calculant le pgcd en utilisant le modulo.
{% endfaire %}

Knuth analyse en détails cet algorithme dans le tome 2 de [the art of computer programming](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming). Comme à chaque fois avec Knuth : les résultats sont précis, intéressants et très bien écrits, je ne peux que vous conseillez d'allez y jeter un coup d'œil nous ne faisons en effet ici qu'effleurer le sujet.

## Complexité

Avant de prouver sa complexité, commencez par :

{% faire %}
Démontrez que si $a\geq b$ alors $a \mathbin{\small\\%} b < \frac{a}{2}$.
{% endfaire %}

Ceci vous permettra de :

{% faire %}
Déduire que le nombre de récursions de l'algorithme récursif utilisant le pgcd est inférieur à $\log_2(\max(a, b))$.
{% endfaire %}
{% faire %}
Si l'opération calculant le modulo est élémentaire, en déduire la complexité de l'algorithme récursif utilisant le pgcd.
{% endfaire %}

## Pgcd et Fibonacci

On va maintenant montrer que cette complexité est atteinte. Pour cela, exhibons d'étranges propriétés des éléments de [la suite de Fibonacci](../fibonacci/){.interne}.

{% faire %}
Si $F(n)$ est le $n$ème nombre de la suite de Fibonacci, montrez que $F(n) \mathbin{\small\\%} F(n-1) = F(n-2)$.
{% endfaire %}

En déduire que :

{% faire %}
Il y a exactement $n$ récursions de l'algorithme récursif utilisant le pgcd pour calculer le pgcd de  $F(n)$ et $F(n-1)$.
{% endfaire %}

On a même mieux :

{% faire %}
> TBD : $k$ récursions alors fibo le plus petit
{% endfaire %}

Enfin, quelques propriétés rigolotes des pgcd des nombres de Fibonacci :

{% faire %}
Montez que : $F(n)$ et $F(n-1)$ sont premiers entre eux.
{% endfaire %}
{% faire %}
Montez que le pgcd de $F(n)$ et $F(m)$ est $F(p)$ avec $p$ le pgcd de $n$ et $m$.
{% endfaire %}
{% faire %}
Si $n$ divise $m$, alors $F(n)$ divise $F(m)$.
{% endfaire %}

Et [il y en a tout un tas d'autres](http://villemin.gerard.free.fr/Wwwgvmm/Iteration/FiboProp.htm#resume).

## Complexité en moyenne

> TBD pgcd max et en moyenne et aussi algo avec modulo. Voir Knuth. et problème bale pour la complexité en moyenne.
