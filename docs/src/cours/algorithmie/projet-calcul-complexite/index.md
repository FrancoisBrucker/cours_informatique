---
layout: layout/post.njk

title: "Projet : calcul de complexité"

eleventyNavigation:
  prerequis:
    - /cours/algorithmie/projet-itératif-récursif/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples d'algorithme pour le calcul de la complexité. Nous allons reprendre les algorithmes que nous avons crée précédemment dans la partie [calcul et preuve d'algorithmes](../projet-itératif-récursif){.interne} en utilisant ceux proposés dans la correction.

Nous allons aller de plus en plus vite, à mesure que nous gagnons en automatisme.

## Concaténation

```pseudocode/
algorithme concaténation(début: [entier], fin: [entier]) → [entier]
    t ← tableau de taille début.longueur + fin.longueur
    i ← -1

    pour chaque j de [0, début.longueur - 1]:
        i ← i + 1
        t[i] ← début[j]
  
    pour chaque j de [0, fin.longueur - 1]:
        i ← i + 1
        t[i] ← fin[j]

    rendre t
```

{% exercice %}
Quelle est la complexité de l'algorithme `concaténation`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

Les lignes 1, 5 et 9 définissent des blocs, les autres sont des instructions composées d'instructions basiques (affectations, sommes et lectures) toutes en $\mathcal{O}(1)$ : la complexité va être égale au nombre de fois où chaque ligne est exécutée. Calculons la en regroupant les lignes de l'algorithme en _paquets_ :

1. boucle 5-7
2. boucle 9-11
3. le reste

Les lignes du paquet 1 vont être exécutées autant de fois que la boucle va itérer, c'est à dire `début.longueur`{.language-} fois. La complexité du paquet 1 est donc : $\mathcal{O}(1) \cdot \mbox{début.longueur} = \mathcal{O}(\mbox{début.longueur})$

De la même manière, les lignes du paquet 2 vont être exécutées autant de fois que la boucle va itérer, c'est à dire `fin.longueur`{.language-} fois. La complexité du paquet 2 est donc : $\mathcal{O}(\mbox{fin.longueur})$.

Enfin, les lignes du paquet 3 vont toutes être exécutées 1 fois : la complexité totale de l'exécution de toutes les lignes du paquet 3 va être $\mathcal{O}(1)$.

La complexité totale est donc en $\mathcal{O}(\mbox{début.longueur} + \mbox{fin.longueur})$.

{% enddetails %}

## Suppression de valeurs

### Itératif

```pseudocode/
algorithme supprime(t: [entier], v: entier) → [entier]
    nombre ← 0
    pour chaque e de t:
        si e == v:
            nombre ← nombre + 1
    t2 ← tableau de taille t.longueur - nombre

    j ← 0
    pour tout i allant de 0 à t.longueur - 1:
        si t[i] ≠ v:
            t2[j] ← t[i]
            j ← j + 1
    
    rendre t2
```

{% exercice %}
Quelle est la complexité de l'algorithme `supprime`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

Toutes les lignes sont en $\mathcal{O}(1)$ et deux boucles de $\mathcal{O}(\mbox{t.longueur})$ itérations.

La complexité est donc en $\mathcal{O}(1) + 2\cdot\mathcal{O}(\mbox{t.longueur}) = \mathcal{O}(\mbox{t.longueur})$

{% enddetails %}

### Récursif

```pseudocode/
algorithme supprime_rec(t: [entier], v: entier) → [entier]
    si t.longueur == 0:
        rendre t

    t2 ← tableau de longueur t.longueur - 1
    pour i allant de 0 à t2.longueur - 1:
        t2[i] ← t[i + 1]
    
    si t[0] == v:
        rendre concaténation([], supprime_rec(t2, v))
    sinon:
        rendre concaténation([t[0]], supprime_rec(t2, v))
```

{% exercice %}
Quelle est la complexité de l'algorithme `supprime_rec`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

L'algorithme est récursif calculer sa complexité va dépendre d'une équation récurrente. Une analyse rapide de l'algorithme nous indique que cette équation de récursion est basée sur la taille du tableau en entrée, on note alors $C(n)$ la complexité de `supprime_rec`{.language-} pour un tableau de taille $n$ passé en entrée.

Regardons la complexité de l'algorithme ligne à ligne :

- lignes 1 à 4 : chaque ligne est en $\mathcal{O}(1)$. Complexité totale de ce paquet : $\mathcal{O}(1)$
- lignes 6 à 7 : une boucle de $n-1 = \mathcal{O}(n)$ itérations. Comme chaque ligne de la boucle est en $\mathcal{O}(1)$, la complexité totale de ce paquet est : $\mathcal{O}(n)$
- lignes 9 à 12 : selon la valeur du test soit la ligne 10 soit la ligne 12 est exécutée.

Il faut faire **très attention** pour ce genre de lignes car :

- un des paramètres de l'appel à `concaténation`{.language-}le résultat de l'appel récursif
- la complexité de la fonction `concaténation`{.language-} n'est **pas** $\mathcal{O}(1)$, on ne peut donc pas l'ignorer dans nos calculs.

Ces deux lignes sont de même complexité : $C(n-1) + \mathcal{O}(n)$. Le premier terme correspond au calcul du second paramètre de l'appel à la fonction `concaténation`{.language-} et le second à la complexité de l'exécution de `concaténation`{.language-}.

On a maintenant assez pour écrire l'équation qui régit la complexité :

<div>
$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + \\
&  & \mathcal{O}(n) + \\
&  & \mathcal{O}(n) + C(n-1)\\
&=& \mathcal{O}(n) + C(n-1)
\end{array}
$$
</div>

Cette équation se résout simplement :

<div>
$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(n) + C(n-1)\\
     & = & \mathcal{O}(n) + \mathcal{O}(n) + C(n-2)\\
     & = & \dots\\
     & = & \mathcal{O}(n) + \dots + \mathcal{O}(n) + C(1)\\
     & = & n\cdot \mathcal{O}(n) + \mathcal{O}(1)\\
     & = & \mathcal{O}(n^2)
\end{array}
$$
</div>

{% enddetails %}

### Comparaison

{% exercice %}
Quel algorithme est préférable pour résoudre le problème de la suppression ? Et pourquoi ?
{% endexercice %}
{% details "corrigé" %}
L'algorithme itératif est bien meilleur que l'algorithme récursif : $\mathcal{O}(n)$ versus $\mathcal{O}(n^2)$ si $n$ est la taille du tableau passé en paramètre.

Ceci est du à la duplication du tableau dans la version récursive qui ajoute un facteur $\mathcal{O}(n)$ à chaque récursion.

Pour que les complexités soient comparables il faudrait pouvoir ajouter petit à petit des éléments au tableau ce qui est impossible. Les algorithmes récursifs préfèrent utiliser des structures dynamiques comme les listes qui permettent d'ajouter efficacement des objets à un conteneur. Nous verrons ces structures plus tard dans le cours.

{% enddetails %}

## Retournement d'un tableau

```pseudocode/
algorithme reverse_indice(t: [entier], i: entier) → ∅
    si t.longueur - 1 - i > i:
        temp ← t[i]
        t[i] ← t[t.longueur - 1 - i]
        t[t.longueur - 1 - i] ← temp

        reverse_indice(t, i + 1)
```

{% exercice %}
Quelle est la complexité de l'algorithme `reverse_indice`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

L'algorithme est récursif et toutes les lignes à part l'appel récursif sont en $\mathcal{O}(1)$. Comme la condition d'arrêt de la récursion se passe sur le second paramètre, on peut écrire
l'équation de récurrence :

<div>
$$
\begin{array}{lcl}
C(i) & = & \mathcal{O}(1) + C(i + 1)\\
\end{array}
$$
</div>

Avec $C(n/2) = \mathcal{O}(1)$ si $n$ est la taille du tableau. La complexité maximale sera atteinte pour $i = 0$ et dans ce cas :

<div>
$$
\begin{array}{lcl}
C(0) & = & \mathcal{O}(1) + C(1)\\
     & = & \mathcal{O}(1) + \mathcal{O}(1) + C(2)\\
     & = & \dots\\
     & = & \mathcal{O}(1) + \dots + \mathcal{O}(1) + C(n/2)\\
     & = & \frac{n}{2}\cdot \mathcal{O}(1) + \mathcal{O}(1)\\
     & = & \mathcal{O}(n)
\end{array}
$$
</div>

{% enddetails %}

## Fibonacci

{% aller %}
[Suite de Fibonacci](fibonacci){.interne}
{% endaller %}

## McCarty

[La fonction 91 de McCarty](https://fr.wikipedia.org/wiki/Fonction_91_de_McCarthy) est définie telle que :

<div>
$$
M(n) = \left\{
    \begin{array}{ll}
        n-10 & \mbox{si } n > 100 \\
        M(M(n + 11))& \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% exercice %}
Montrer que le calcul de $M^k(91)$ passe par le calcul de $M^{k-1}(91)$ si $k>1$.
{% endexercice %}
{% details "corrigé" %}

$M^k(91) = M^k(M(102)) = M^k(92) = \dots = M^k(101) = M^{k-1}(91)$
{% enddetails %}

{% exercice %}
En déduire que le nombre maximum d'appels à $M$ pour calculer $M(n)$ est 201.
{% endexercice %}
{% details "corrigé" %}

- si $n > 100$ il y a 1 appel,
- si $101 > n > 90$, il y 2 appels pour passer $M(n)$ à $M(n+1)$. Donc au plus 19 appels pour aller de $M(91)$ à $M(100)$ qui se calcule en 2 appels $M(100) = M(M(111)) = M(101) = 91$.
- sinon, $n \leq 90$ et $M(n)$ sera égal à un $M^k(n')$ avec $90 < n' < 101$. Le maximum sera atteint pour $n=1$ en 11 appels, $M^{11}(111) = M^{10}(101) = M^{9}(91)$.

Le nombre d'appel maximum sera atteint pour $n=1$. Dans ce cas là
Au pire il faudra 13 appels pour arriver à $M^{9}(91)$, puis 21 appels pour arriver à $M^{8}(91)$, puis encore $7 \cdot 21$ appels pour arriver à $M(91)$ qui se calcule en 20 appels supplémentaires.

Une borne sera donc de $13 + 21 \cdot 8 + 20 = 201$ appels.

Une vérification expérimentale possible en python :

```python
compte = [0]

def M(n):
  compte[0] += 1
  # print("    ", compte[0], n)

  if n > 100:
    return n - 10
  else:
    return M(M(n+11))

max_compte = 0

for n in range(1, 102):
  compte[0] = 0
  m = M(n)
  # print("n =", n, "M = ", m, "compte =", compte[0])
  max_compte = max(max_compte, compte[0])
print("max =", max_compte)
```

{% enddetails %}

## Triangle de Pascal

{% aller %}
[Triangle de Pascal](triangle-pascal){.interne}
{% endaller %}
