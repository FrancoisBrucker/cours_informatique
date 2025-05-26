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

Cet algorithme est basé sur le fait que si la division euclidienne de $a$ par $b$ vaut $a = qb + r$ (avec $q$ et $r$ entiers et $r < b$) on a `pgcd(a, b) = pgcd(b, r)`{.language-}.

{% faire %}
Donnez un algorithme récursif calculant le pgcd en utilisant le modulo.
{% endfaire %}

Knuth analyse en détails cet algorithme dans le tome 2 (partie 3.5.2) de [the art of computer programming](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming). Comme à chaque fois avec Knuth : les résultats sont précis, intéressants et très bien écrits. Je ne peux que vous conseiller d'allez y jeter un coup d'œil nous ne ferons en effet ici qu'effleurer le sujet.

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
Si l'opération calculant le modulo est élémentaire, en déduire que la complexité de l'algorithme récursif utilisant le pgcd est en $\mathcal{O}(\ln(\max(a, b)))$.
{% endfaire %}

## Pgcd et Fibonacci

On va maintenant montrer que cette complexité est atteinte. Pour cela, exhibons d'étranges propriétés des éléments de [la suite de Fibonacci](../fibonacci/){.interne}.

{% faire %}
Si $F(n)$ est le $n$ème nombre de la suite de Fibonacci, montrez que $F(n) \mathbin{\small\\%} F(n-1) = F(n-2)$.
{% endfaire %}

En déduire que :

{% faire %}
Il y a exactement $n$ récursions de l'algorithme récursif utilisant le pgcd pour calculer le pgcd de  $F(n+1)$ et $F(n)$.
{% endfaire %}

On a même mieux :

{% faire %}
Si pour $a> b$ il y a au moins $n$ récursions de l'algorithme récursif, alors $a\geq F(n+1)$ et $b\geq F(n)$.
{% endfaire %}

{% faire %}
Si l'opération calculant le modulo est élémentaire, en conclure que la complexité de l'algorithme récursif utilisant le pgcd est en $\mathcal{O}(\ln(\min(a, b)))$.

{% endfaire %}

Si cela vous intéresse, vous pouvez jeter un petit coup d'œil au lien suivant qui liste quelques propriétés liées au pgcd des nombres de la suite de Fibonacci :

{% lien %}
<https://proofwiki.org/wiki/GCD_of_Fibonacci_Numbers>
{% endlien %}

## pgcd binaire

Cet algorithme, répertorié dès le 1er siècle (Knuth cite le [九章算术](https://fr.wikipedia.org/wiki/Les_Neuf_Chapitres_sur_l%27art_math%C3%A9matique) chapitre 1 section 6) puis publié dans sa forme actuelle en 1967 par Stein.

<span id="algorithme-pgcd-binaire"></span>

```pseudocode
algorithme pgcd_binaire(a: entier, b: entier) → entier:  # a, b ≥ 0

    si b == 0:
        rendre a
    si a et b sont pairs:
        rendre 2 * pgcd_binaire(a // 2, b // 2)
    si a est impair et b pair:
        rendre 2 * pgcd_binaire(a, b // 2)
    si a et b sont impairs:
        si a < b:
            a, b ← b, a
        rendre pgcd_binaire(a - b, b)
```

{% faire %}
Montrez que l'algorithme `pgcd_binaire(a, b)`{.language-} calcule bien le pgcd des deux entiers positifs a et b.
{% endfaire %}
{% faire %}
Quelle est la complexité de cet algorithme ?
{% endfaire %}
