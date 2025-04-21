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

## Maximum d'un tableau

{% aller %}
[Création et preuve de l'algorithme maximum récursif](../projet-itératif-récursif/#algorithme-max-tableau-rec){.interne}
{% endaller %}

{% exercice %}
 Donnez sa complexité de l'algorithme `maximum_rec`{.language-}.

{% endexercice %}
{% details "corrigé" %}

Toutes les lignes de l'algorithme sont en $\mathcal{O}(1)$ à part la récursion. Comme la récursion est faite sur la taille du tableau, on va noter $C(n)$ sa complexité où $n$ est la taille du tableau passé en paramètre. Elle satisfait alors l'équation :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a vu en cours que cette équation se résout en : $C(n) = \mathcal{O}(n)$.

{% enddetails %}

## Concaténation

{% aller %}
[Création et preuve de l'algorithme concaténation](../projet-itératif-récursif/#algorithme-concaténation){.interne}
{% endaller %}

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

## <span id="égalité-tableaux"></span>Égalité de tableaux

### Intersection non vide

{% aller %}
[Création et preuve de l'algorithme d'intersection non vide](../projet-itératif-récursif/#algorithme-intersection-non-vide){.interne}
{% endaller %}
{% exercice %}
Quelle est la complexité min et max de l'algorithme `intersection_non_vide`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

- Dans le meilleur des cas, si $T1 = T2$ par exemple, le premier test d'égalité est vérifié et on rend directement `Vrai` : la complexité min est $\mathcal{O}(1)$
- Dans le cas le pire, si les deux tableaux ne contiennent aucune valeur commune, on rend `Faux` et on a effectué toutes les itérations des deux boucles `pour chaque` imbriquées : on a effectué $\mathcal{O}(T1.\mbox{\small longueur} \cdot T2.\mbox{\small longueur})$ opérations.

{% enddetails %}

### Mêmes valeurs

{% aller %}
[Création et preuve de l'égalités des valeurs](../projet-itératif-récursif/#algorithme-intersection-non-vide){.interne}
{% endaller %}
{% exercice %}
Quelle est la complexité min et max de l'algorithme `égalité_valeurs`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

- Dans le meilleur des cas, si les deux tableaux ne contiennent aucune valeur commune, on rend `Faux` le plus vite possible. L'algorithme fait une seule itération de la première boucle `tant que`{.language-} et toutes les itérations de la seconde : la complexité min est $\mathcal{O}(T2.\mbox{\small longueur})$

- Dans le cas le pire, si $T1 = T2$ par exemple, on rend `Vrai` et on a effectué toutes les itérations des deux boucles `pour chaque` imbriquées : on a effectué $\mathcal{O}(T1.\mbox{\small longueur} \cdot T2.\mbox{\small longueur})$ opérations.

{% enddetails %}

### Permutations

{% aller %}
[Création et preuve de l'égalités des éléments](../projet-itératif-récursif/#algorithme-intersection-non-vide){.interne}
{% endaller %}
{% exercice %}
Quelle est la complexité min et max de l'algorithme `permutation`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

- Dans le meilleur des cas, si les deux tableaux ne contiennent aucune valeur commune, on rend `Faux` le plus vite possible. L'algorithme fait une seule itération de la première boucle et une vérification de `nombre`{.language-} : la complexité min est $\mathcal{O}(T1.\mbox{\small longueur} + T2.\mbox{\small longueur})$

- dans le cas le pire, si $T1 = T2$, il faut exécuter l'algorithme `nombre`{.language-}, de complexité min et max égale a la taille du tableau en entrée, autant de fois qu'il y a d'éléments dans t1 et pour les tableaux t et t2. La complexité totale est donc de : $\mathcal{O}(T1.\mbox{\small longueur}) \cdot (t1.\mbox{\small longueur} + T2.\mbox{\small longueur})$

{% enddetails %}

## <span id="suppression-valeur"></span>Suppression de valeurs

### Itératif

{% aller %}
[Création et preuve de l'algorithme suppression valeurs itératif](../projet-itératif-récursif/#suppression-valeur-itératif){.interne}
{% endaller %}

{% exercice %}
Quelle est la complexité de l'algorithme `supprime`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

L'algorithme `nombre`{.language-} est en $\mathcal{O}(\mbox{T.longueur})$,
toutes les autres lignes sont en $\mathcal{O}(1)$ et une boucle de $\mathcal{O}(\mbox{T.longueur})$ itérations.

La complexité est donc en $\mathcal{O}(\mbox{T.longueur})$

{% enddetails %}

### Récursif

{% aller %}
[Création et preuve de l'algorithme suppression valeurs récursif](../projet-itératif-récursif/#algorithme-suppression-valeur-récursif){.interne}
{% endaller %}
{% exercice %}
Quelle est la complexité de l'algorithme `supprime_rec`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

L'algorithme est récursif, calculer sa complexité va dépendre d'une équation récurrente. Une analyse rapide de l'algorithme nous indique que cette équation de récursion est basée sur la taille du tableau en entrée, on note alors $C(n)$ la complexité de `supprime_rec`{.language-} pour un tableau de taille $n$ passé en entrée.

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

## <span id="encapsulation-récursion"></span>Encapsulation de la récursion

{% aller %}
[Création et preuve de l'algorithme palindrome](../projet-itératif-récursif/#algorithme-palindrome){.interne}
{% endaller %}

{% exercice %}
Quelle est la complexité de l'algorithme `palindrome`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

Une boucle de $\mathcal{O}(T.\mbox{\small longueur})$ itérations et que des instructions en $\mathcal{O}(1)$ donnent une complexité totale de : $\mathcal{O}(T.\mbox{\small longueur})$

{% enddetails %}

{% aller %}
[Création et preuve de l'algorithme palindrome récursif](../projet-itératif-récursif/#algorithme-palindrome-récursif){.interne}
{% endaller %}

{% exercice %}
Quelle est la complexité de l'algorithme `palindrome_rec`{.language-} ?
{% endexercice %}
{% details "corrigé" %}

La relation de récurrence sur les paramètres d'entrée est :

<div>
$$
\begin{cases}
C(T, i) = \mathcal{O}(1) + C(T, i+1)\\
C(T, T.\mbox{\small longueur}) = \mathcal{O}(1)\\
\end{cases}
$$
</div>

Cette équation se résout comme celle du cours:

<div>
$$
\begin{array}{lcl}
C(T, i) & = & \mathcal{O}(1) + C(T, i+1)\\
     & = & \mathcal{O}(1) + \mathcal{O}(1) + C(T, i+2)\\
     & = & \dots\\
     & = & \underbracket{\mathcal{O}(1) + \dots + \mathcal{O}(1)}_{T.\mbox{\small longueur}-i} + C(T, T.\mbox{\small longueur})\\
     & = & (T.\mbox{\small longueur}-i)\cdot \mathcal{O}(1) + \mathcal{O}(1)\\
     & = & \mathcal{O}(T.\mbox{\small longueur}-i)\\
     & = & \mathcal{O}(T.\mbox{\small longueur})\\
\end{array}
$$
</div>

{% enddetails %}

## Retournement d'un tableau

{% aller %}
[Création et preuve de l'algorithme retournement](../projet-itératif-récursif/#algorithme-retournement){.interne}
{% endaller %}

{% exercice %}
Quelle est la complexité de l'algorithme `retournement_indice`{.language-} ?
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

Avec $C(n/2) = \mathcal{O}(1)$ si $n$ est la taille du tableau. Comme pour le calcul de la complexité du palindrome, on a : $C(i) = \mathcal{O}(n/2 - i) = \mathcal{O}(n)$.

{% enddetails %}

## McCarty

{% aller %}
[Définitions et propriétés de la fonction de McCarty](../projet-itératif-récursif/#fonction-McCarty){.interne}
{% endaller %}

En utilisant uniquement la relation de récurrence, résolvez les exercices suivants (vous pourrez utiliser ce que l'on a démontré précédemment) :

{% exercice %}
Montrer que le calcul de $M(n)$ passe par le calcul de $M^{k}(91)$ pour tout $n\leq 100$.
{% endexercice %}
{% details "corrigé" %}
Dérive directement de la définition et du fait que on a démontré que :

- pour tout $90 \leq n < 101$, on a $M(n) = M(n+1) = \dots = M(101) = 91$
- pour tout $n < 101$, il existe $k\geq 1$ et $90 \leq n' < 101$ tels que $M(n) = M^k(n')$

{% enddetails %}
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
