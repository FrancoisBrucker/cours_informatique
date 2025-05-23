---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



## Valeurs

La suite de Fibonacci est clairement croissante (vous pouvez le prouver par récurrence), ce qui permet d'écrire :

<div>
$$
\begin{array}{ccccc}
&&F(n) = F(n-1) + F(n-2)&&\\
2\cdot F(n-2)&\leq&F(n)&\leq& 2\cdot F(n-1)\\
4\cdot F(n-4)&\leq&F(n)&\leq& 4\cdot F(n-2)\\
&&\dots&&\\
2^p\cdot F(n-2p)&\leq&F(n)&\leq& 2^p\cdot F(n-p)\\
2^{n/2}\cdot F(1)&\leq&F(n)&\leq& 2^n\cdot F(1)\\
2^{n/2}&\leq&F(n)&\leq& 2^n\\
(\sqrt{2})^{n}&\leq&F(n)&\leq& 2^n
\end{array}
$$
</div>

Pour démontrer la valeur exacte de $F(n)$, on utilise les deux égalités  clairement vraies (par récurrence) pour tout $n>1$ :

<div>
$$
\begin{cases}
\phi_+^n = F(n)\phi_+ + F(n-1)\\
\phi_-^n = F(n)\phi_- + F(n-1)\\
\end{cases}
$$
</div>

En les soustrayant et en utilisant le fait que $\phi_+ - \phi_- = \sqrt{5}$ permet de conclure.

## Récursif

### Finitude et correction de l'algorithme

Il faut démontrer que ce programme est bien un algorithme car il y a plusieurs récursions !

Ceci se fait facilement par une récurrence sur $n$ car chaque appel se rapproche strictement de la condition d'arrêt.

1. initialisation : `fibonacci_rec(n)`{.language-} admet un nombre fini de récursion pour $n\leq 2$.
2. hypothèse de récurrence : `fibonacci_rec(m)`{.language-} admet un nombre fini de récursion pour $m < n$.
3. Pour $n$, `fibonacci_rec(n - 1)`{.language-} et `fibonacci_rec(n-2)`{.language-} se terminent en un nombre fini de récursion donc la ligne 4 de l'algorithme aura aussi un nombre fini de récursion.

Une fois la finitude démontrée la correction est évidente, comme souvent avec les algorithmes récursif, puisque l'algorithme ne fait que transcrire l'équation de récursion.

### Calcul de complexité

En notant $C(n)$ la complexité de `fibonacci_rec(n)`{.language-}, on a clairement l'équation suivante :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1) + C(n-2)
$$
</div>

On prouve ensuite par récurrence que si $C(m) = \Omega(F(m))$ pour tout $m < n$ alors :

<div>
$$
C(n) = \mathcal{O}(1) + \Omega(F(n-1)) + \Omega(F(n-2)) = \mathcal{O}(1) + \Omega(F(n-1) + F(n-2)) = \mathcal{O}(1) + \Omega(F(n)) = \Omega(F(n))
$$
</div>

## Récursif terminal

La récursion terminale consiste à stocker les variables nécessaire au calcul récursif dans des paramètres. Ici, comme $F(n) = F(n - 1) + F(n-2)$ il faut deux accumulateurs, l'un pour $F(n - 1)$, l'autre pour $F(n - 2)$ :

<span id="algorithme-fibonacci-rec-terminale"></span>

```pseudocode
fonction fibonacci_rec_terminale(n: entier, acc_n_1, acc_n_2) → entier:
     si n == 2:
          rendre acc_n_1
     sinon si n ≤ 1:
          rendre acc_n_2
     
     rendre fibonacci_rec_terminale(n-1, acc_n_1 + acc_n_2, acc_n_1)


algorithme fibonacci_rec(n: entier) → entier:
    rendre fibonacci_rec_terminale(n, 1, 1)

```

L'algorithme se termine  puisque le paramètre d'arrêt de la récursion, `n`{.language-}, décroît strictement à chaque appel.

Par une récurrence triviale sur `n`{.language-}, les paramètres `acc_n_1`{.language-} et `acc_n_2`{.language-} de l'appel de `fibonacci_rec_terminale(n - i, acc_n_1, acc_n_2)`{.language-} valent :

- `acc_n_1`{.language-} vaut $F(i + 2)$
- `acc_n_2`{.language-} vaut $F(i + 1)$

Lors du dernier appel on a `fibonacci_rec_terminale(2, acc_n_1, acc_n_2)`{.language-} et donc `acc_n_1`{.language-} vaut $F(n-2 + 2) = F(n)$

La complexité $C(n)$ de l'algorithme satisfait l'équation de récurrence :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a déjà vu cette récurrence, elle vaut : $C(n) = \mathcal{O}(n)$.

## Itératif

On adapte l'algorithme en récursion terminale :

<span id="algorithme-fibonacci-itératif"></span>

```pseudocode
algorithme fibonacci(n: entier) → entier:
    acc_n_1 ← 1
    acc_n_2 ← 1

    tant que n > 1:
        temp ← acc_n_1 
        acc_n_1 ← acc_n_1 + acc_n_2
        acc_n_2 ← acc_n_1
        n ← n - 1
    
    rendre acc_n_1
```

Sa correction est claire puisque c'est la transcription de l'algorithme récursif terminal et sa complexité est évidemment $\mathcal{O}(n)$.
