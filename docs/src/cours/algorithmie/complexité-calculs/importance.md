---
layout: layout/post.njk

title: Importance de la complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons illustrer l'importance pratique de la complexité en considérant 5 allures de complexité : :

{% note2 "**Définition**" %}
On note $C(n)$ la complexité d'un algorithme. On dira de cette complexité que c'est une (avec $K$ et $k$ deux constantes et $\sim$ l'[équivalent mathématique](https://fr.wikipedia.org/wiki/%C3%89quivalent)) :

- **_complexité constante_** si $C(n) \sim_{+\infty} K$
- **_complexité logarithmique_** si $C(n) \sim_{+\infty} K\cdot \ln(n)$
- **_complexité linéaire_** si $C(n) \sim_{+\infty} K\cdot n$
- **_complexité polynomiale_** $C(n) \sim_{+\infty} K\cdot n^k$
- **_complexité exponentielle_** $C(n) \sim_{+\infty} K\cdot k^n$

{% endnote2 %}

Les types de complexités ci-dessus sont rangés par ordre, de la moins grande à la plus grande.

Remarquez que si $n$ représente la taille des données, un algorithme de complexité linaire nécessite de lire toutes les données au plus un nombre constant de fois pour s'exécuter, alors qu'un algorithme de complexité logarithmique n'a même pas besoin de lire une fois toutes les données pour s'exécuter ! Ceci n'est souvent possible que si les données en entrées ont une structure très particulière. Par exemple pour le problème de la recherche d'une valeur particulière dans un tableau :

- trouver cette valeur nécessite un temps linéaire si on utilise notre algorithme `recherche`{.language-},
- trouver cette valeur nécessite un temps logarithmique si le tableau est un tableau trié et qu'on utilise l'algorithme de [recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique)

{% info %}
Notez bien que la complexité logarithmique est la même quelque soit la base utilisée puisque $\log_k(n) = \frac{\ln (n)}{\ln (k)}$ et donc $\log_k(n) = K\cdot \ln(n)$ avec $K = \frac{1}{\ln (k)}$ constant.
{% endinfo %}

Il est crucial de chercher la meilleure complexité pour un algorithme car ses performances seront drastiquement différentes selon le type de complexité qu'il possède, comme le montre les deux tableaux ci-dessous, repris du livre [Computer and intractability](https://en.wikipedia.org/wiki/Computers_and_Intractability). Ce qu'il faut retenir :

{% note %}

- il y a une **gigantesque différence** entre complexité logarithmique et complexité linéaire
- il y a une **énorme différence** entre complexité linéaire et complexité polynomiale, mais moins grande qu'entre logarithmique et linéaire
- il y a une **gigantesque différence** entre complexité polynomiale et complexité exponentielle (qu'il ne faut donc jamais avoir si possible)

{% endnote %}

## Temps pour résoudre un problème de taille $n$

Exemple d'évolution du temps de calcul par rapport à la complexité. En supposant, que l'on ait un ordinateur qui résout des problèmes de complexité $n$ en 0.01 ms pour des données de taille 10, on peut remplir le tableau ci-après.

En colonnes le nombre $n$ de données, en lignes les complexités des algorithmes.

| complexité | 10        | 20        | 30        | 40         | 50                       | 60                         |
| ---------- | --------- | --------- | --------- | ---------- | ------------------------ | -------------------------- |
| $\ln(n)$   | 2 $\mu s$ | 3 $\mu s$ | 3 $\mu s$ | 4 $\mu s$  | 4 $\mu s$                | 4 $\mu s$                  |
| $n$        | 0.01 ms   | 0.02 ms   | 0.03 ms   | 0.04 ms    | 0.05 ms                  | 0.06 ms                    |
| $n^2$      | 0.1 ms    | 0.4 ms    | 0.9 ms    | 1.6 ms     | 2.5 ms                   | 3.6 ms                     |
| $n^3$      | 1 ms      | 8 ms      | 27 ms     | 64 ms      | 125 ms                   | 216 ms                     |
| $n^5$      | 1s        | 3.2 s     | 24.3 s    | 1.7 min    | 5.2 min                  | 13 min                     |
| $2^n$      | 1 ms      | 1s        | 17.9 min  | 12.7 jours | 35.7 ans                 | 36600 ans                  |
| $3^n$      | 59 ms     | 58 min    | 6.5 ans   | 385500 ans | $2.27\cdot 10^8$ siècles | $1.3\cdot 10^{13}$ siècles |

L'évolution est dramatique plus la complexité augmente. Pour une complexité logarithmique, le temps _semble_ constant et pour une complexité polynomiale, la croissance reste maîtrisée même s'il vaut mieux avoir une petite complexité pour traiter plus de données. Pour une complexité exponentielle ($2^n$ et $3^n$) en revanche, la durée est tout simplement rédhibitoire.

{% info %}
Pour générer le tableau, on voit que le temps $t$ pour exécuter 1 opération est de .001ms (on regarde la ligne de complexité linéaire : pour $n=10$ on prend 0.01 opérations, donc 1 opération nécessite $0.01/10ms$). Le temps pris pour exécuter $f(n)$ opérations avec une entrée de taille de $n$ est alors : $t \cdot f(n)$
{% endinfo %}

## Nombre de problèmes résolus par heure

En colonne la rapidité de la machine, en ligne la taille maximale d'un problème que l'on peut résoudre en 1heure.

| complexité | machine actuelle | 100x plus rapide   | 1000x plus rapide   |
| ---------- | ---------------- | ------------------ | ------------------- |
| $\ln(n)$   | $N0$             | $e^{100} \cdot N0$ | $e^{1000} \cdot N0$ |
| $n$        | $N1$             | $100 \cdot N1$     | $1000 \cdot N1$     |
| $n^2$      | $N2$             | $10 \cdot N2$      | $31.6 \cdot N2$     |
| $n^3$      | $N3$             | $4.64 \cdot N3$    | $10 \cdot N3$       |
| $n^5$      | $N4$             | $2.5 \cdot N4$     | $3.98 \cdot N4$     |
| $2^n$      | $N5$             | $N5 + 6.64$        | $N5 + 9.97$         |
| $3^n$      | $N6$             | $N6 + 4.19$        | $N6 + 6.29$         |

La encore, l'évolution est dramatique plus la complexité augmente. Pour des complexités logarithmiques et polynomiales le nombre de problèmes augmente d'un facteur multiplicatif lorsque la vitesse augmente, mais ce n'est pas le cas pour des complexités exponentielles. Pour ces problèmes, augmenter la vitesse de la machine ne change pas fondamentalement le nombre de problèmes que l'on peut résoudre.

{% info %}
Pour générer le tableau, on suppose que l'on peut résoudre $K$ opérations en 1 heure. On cherche alors $n$ tel que $f(n)$ soit égal à $K$ et donc $n = f^{-1}(K)$. En remarquant que $K$ est égal à la taille maximale d'un problème de complexité linéaire résoluble en 1heure, on la taille maximale $n$ d'un problème de complexité $f(n)$ résoluble en 1 heure pour une machine allant $k$ fois pus vite qu'une machine actuelle vaut $f^{-1}(k \cdot N1)$.
{% endinfo %}

## Le cas particulier de $n!$

Souvent les étudiants veulent que leurs algorithmes soient de complexité $C(n) = n!$. Ce n'est **presque jamais exact** ! En effet, la [formule de Stirling](https://fr.wikipedia.org/wiki/Formule_de_Stirling) donne l'équivalent suivant pour $n!$ :

$$
n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n
$$

{% info %}
[une preuve de la formule](https://www.youtube.com/watch?v=Dgh8673ymdo)
{% endinfo %}

On a donc que $n!$ est de l'ordre de $n^{n+1/2}$, qui est vachement plus grand que $2^{n}$ qui est déjà gigantesque.

Par exemple :

- $10! = 3628800$
- $2^{10} = 1024$

Et la différence s’accroît exponentiellement avec le nombre :

- $74! = 330788544151938641225953028221253782145683251820934971170611926835411235700971565459250872320000000000000000$
- $2^{74} = 18889465931478580854784$

{% attention "**À retenir**" %}
Si vous pensez que votre algorithme tout bête est de complexité $C(n) = n!$ Réfléchissez-y à deux fois. C'est presque sûrement une erreur... Et si ce n'est est pas une, votre algorithme est inefficace et devrait sûrement être oublié plutôt que montré à votre enseignant.
{% endattention %}
