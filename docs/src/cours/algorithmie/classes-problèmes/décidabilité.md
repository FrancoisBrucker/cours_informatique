---
layout: layout/post.njk
title: "Décidabilité et décision"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



## Algorithmes, décideurs et vérifieurs

Rappelons qu'un algorithme est [dans toute sa généralité](../../bases-théoriques/calculabilité/#algorithme-fonction-N){.interne} une fonction de $\mathbb{N}$ dans $\mathbb{N}$ (tous les paramètres considérés comme des chaines de caractères peuvent être concaténés en une seule chaine. On verra dans quelques lignes une autre façon de _concaténer_ des entiers) et qu'[un décideur](../../écrire-algorithmes/problème/#décideur){.interne} est un algorithme dont la sortie est soit OUI (que l'on associe à 1) soit NON (associé à 0).

On va commencer par montrer qu'un algorithme peut être vu comme un décideur, ce qui nous permettra de voir les trois formes équivalentes d'un algorithme.

Commençons par démontrer que $\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection (on pourrait utiliser l'argument de [la partie calculabilité](../../bases-théoriques/calculabilité/#algorithme-fonction) en recodant les différents paramètres mais ne boudons pas notre plaisir en utilisant, et en la démontrant, la bijection classique que l'on doit au mathématicien [Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor)) :

{% note "**Théorème**" %}
$\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection.
{% endnote %}
{% details "preuve", "open" %}
Remarquons que tout élément de $\mathbb{N}^2$ est un point du plan :

![point de n2 dans le plan](n2_dans_plan.png)

On peut les parcourir en suivant les diagonales :

![point de n2 dans le plan](n2_dans_n.png)

On chemine alors comme ça :

1. $(0, 0)$
2. $(1, 0)$
3. $(0, 1)$
4. $(2, 0)$
5. $(1, 1)$
6. $(0, 2)$
7. $(3, 0)$
8. $(2, 1)$
9. $(1, 2)$
10. $(0, 3)$
11. $(4, 0)$
12. ...

Et on associe à un entier $(x, y)$ son ordre de cheminement $O((x, y))$ (par exemple $O((2, 1)) = 8$).

Ce cheminement est clairement une bijection.

On peut donc aussi associer un unique entier à tout couple d'entiers avec $O^{-1}$ ($O^{-1}(6) = (0, 2)$ par exemple).

{% enddetails %}
{% note "**Corollaire**" %}
$\mathbb{N}^p$ et $\mathbb{N}$ sont en bijection pour tout entier $p$.
{% endnote %}
{% details "preuve", "open" %}
La démonstration précédente montre que $\mathbb{N}^p = \mathbb{N}^2 \times \mathbb{N}^{p-2} $ est en bijection avec $\mathbb{N} \times \mathbb{N}^{p-2} = \mathbb{N}^{p-1}$ pour tout $p>2$.
{% enddetails %}

{% exercice %}
Écrivez le pseudo-code de la fonction $O^{-1}$ qui associe un couple $(x, y)$ unique à un entier $i$ passé en paramètre.
{% endexercice %}
{% details "solution" %}

```text
Nom : O^{-1}
Entrée : un entier i
Programme :
    x = y = 0
    k = 0
    tant que k < i:
        si x == 0:
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour (x, y)
```

{% enddetails %}

{% exercice %}
À partir du pseudo-code de $O^{-1}$, il est facile d’écrire le pseudo code de $O$ : faites le.
{% endexercice %}
{% details "solution" %}

```text
Nom : O
Entrée :  un couple (u, v) d'entiers
Programme :
    x = y = 0
    i = 0
    tant que (u, v) ≠ (x, y):
        i = i + 1
        si x == 0:
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour i
```

{% enddetails %}
Comme un algorithme est une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$, on peut lui associer de façon équivalente la fonction $v_f$ ci-dessous :

$$
v_f(n, m) = \left\\\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

On peut voir l'algorithme $v_f$ comme un vérifieur. Il vérifie que le second paramètre est la sortie du premier paramètre. On reparlera de ces algorithmes dans la suite, pour l'instant ils nous permettent de montrer que l'espace d'arriver d'un algorithme peut être uniquement deux valeurs. Un algorithme peut être vu comme une fonction de :

$$f: \mathbb{N}^2 \rightarrow \\{0, 1 \\}$$

Et comme $\mathbb{N}^2$ est en bijection avec $\mathbb{N}$ :

{% note %}
Un **_algorithme_** est une fonction de :

$$f: \mathbb{N} \rightarrow \\{0, 1 \\}$$

{% endnote %}

Un décideur est donc une notion a priori plus générale qu'un algorithme puisque l'on peut les écrire sous la forme d'un décideur ! On ne va bien sur pas uniquement utiliser des décideurs en pratique, loin de là, mais cela montre que l'on peut se contenter de considérer les propriétés théoriques des problèmes de décisions puisqu'on pourra les appliquer sans perte de généralité aux autres problèmes.

Avant de passer à l'étude théorique des problèmes et de les classer en plusieurs catégories, analysons les 3 formes d'algorithmes (que l'on a montré équivalentes) utiles :

{% note "**À retenir**" %}
On peut représenter un algorithme sous 3 formes équivalentes utiles en théorie :

- les **_fonctions_** : $A(x) = y$, avec $x, y \in \mathbb{N}$ qui permettent le calcul effectif,
- les **_décideurs_** : $A(x) = b$, avec $x \in \mathbb{N}$ et $b \in \\{0, 1\\}$ qui permettent de séparer les entiers en 2, les entiers _vrais pour $A$_ : $\\{ x \vert A(x) = 1 \\}$, et les autres
- les **_vérifieurs_** : $A(x, y) = b$, avec $x, y \in \mathbb{N}$ et $b \in \\{0, 1\\}$ qui, associé à un problème algorithmique $P$, permettent de vérifier si le couple $(x, y)$ est tel que $y$ soit une solution de $P$ avec $x$ comme entrée.

{% endnote %}

## Problèmes utilisables en pratique

Pour qu'un [problème algorithmique](../../écrire-algorithmes/problème/){.interne}) puisse être utilisé en pratique, il faut bien sûr qu'il soit [décidable](../../écrire-algorithmes/problème/#décidable){.interne}, c'est à dire qu'il existe un algorithme permettant de le résoudre. Mais parmi ces derniers, pour être utile en pratique, encore faut-il que l'on puisse les traiter en temps raisonnable (la durée d'une vie humaine par exemple). On va donner deux définitions du terme _traiter_. Commençons par la plus évidente : la résolution.

![décidable](./NP-décidable.png)

### Problèmes NP

La notion de vérificateur efficace nécessite que l'on ait une solution à vérifier, ce qui n'est pas le cas des [problèmes de décision](../../écrire-algorithmes/problème/#problème-décision){.interne} où l'on cherche juste à savoir si c'est possible (oui ou non, existe-t-il une solution ?) plutôt que de donner une solution explicite si elle existe.

De la même manière qu'un algorithme de type _fonction_ peut s'écrire sous la forme d'un algorithme de la forme _décideur_ on peut associer à tout problème décidable un problème de décision.

Considérons par exemple le problème de trouver le maximum d'un tableau. On peut lui associer le problème de décision suivant :

{% note "**Problème**" %}

- **nom** : plus grand que
- **données** :
  - un tableau d'entiers $T$
  - un entier $K$
- **question** : $T$ possède-t-il un élément plus grand ou égal à $K$

{% endnote %}

Si ce problème admet un décideur efficace, il suffit de l'appliquer pour $K$ valant itérativement toutes les valeurs de $T$ pour trouver le maximum. Ce nouvel algorithme est également efficace et résout le problème du maximum.

De façon formelle si $P$ est un problème d'entrée $e \in E$ et cherchant une solution $s \in S$, on peut lui associer le problème de décision demandant l'entrée $(e, s)$ et répondant OUI si $s$ est une solution de $P(e)$. Si le problème de décision est décidable, alors $P$ l'est aussi puisqu'il suffit d'itérer sur tous les $s$ possibles jusqu'à trouver une solution (on suppose que toute instance de $P$ admet une solution).

La remarque ci-dessus nous montre que l'on peut uniquement considérer les problèmes de décision décidables, sans perte de généralité. Dans ce cadre, on peut définir les problèmes de décision utilisable en pratique comme étant ceux tels que :

{% note "**Définition**" %}
**_Un problème de décision est dit $NP$_** s'il existe un vérificateur efficace $v$ tel que pour toute entrée $e$ du problème il existe $t$, appelé **_certificat de $e$_** tel que $v(e, t)$ soit vrai.

{% endnote %}

La définition ci-dessus appelle plusieurs remarques. Tout d'abord le nom a été très mal choisi. Il signifie _Non déterministe Polynomial_ (et **_pas du tout_** non polynomial...) car cette classe de problème a initialement été déterminée par rapport aux [machines de Turing non déterministe](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe).

Deuxièmement ce qu'est le certificat n'est pas explicite. On sait juste qu'il existe. Voyez ça comme si le vérificateur était le schéma général de la preuve que $e$ est vrai pour le problème, et que le certificat était les paramètres qui permettent d'appliquer la preuve à $e$. Dans le cas de problèmes de $P$ seul $e$ suffit et pour des problèmes qui ne sont pas de décision c'est le couple $(e, s)$ (où $s$ est la solution) qui doit être prouvé.

Enfin, la taille du certificat est bornée par la complexité du vérificateur (cela ne sert à rien que sa taille soit supérieure, elle ne sera de toute façon pas utilisée lors de l'exécution de l'algorithme) qui est polynomiale en la taille de $e$.

{% note "**À retenir**" %}
Un problème est dans $NP$ s'il existe un vérificateur efficace de ses solutions. Ce sont exactement les problèmes algorithmiques utilisable en pratique car :

- On peut énumérer toutes les solutions possibles en temps fini, mais possiblement exponentiel (ce qui fonctionne lorsque la taille d'entrée est faible).
- On peut vérifier efficacement (en temps polynomial) si une proposition de solution est réellement une solution.

{% endnote %}

Finissons cette partie en notant qu'il existe des problèmes de décisions qui sont décidables mais pas dans $NP$, par exemple le problème de décision suivant (juste en donner une idée de la démonstration nous emmènerait trop loin, croyez moi donc sur parole) :

{% note "**Problème**" %}

- **nom** : Ackerman
- **données** :
  - deux entiers $n$ et $m$
  - un entier $K$
- **question** : la valeur de [la fonction d'Ackermann](../../bases-théoriques/calculabilité/#fonction-ackermann) en $n$ et $m$ est-elle plus grande que $K$ ?

{% endnote %}

Au final on a le schéma suivant :

![décidable](./NP-NP.png)

Finissons cette partie par une question encore sans réponse actuellement. Est-ce qu'il existe des problèmes de décision de $NP$ qui ne sont pas dans $P$ ? 

La question semble idiote dit comme ça, mais c'est une vraie question et personne n'a de réponse. Certains se demandent même si cette question est décidable (_ie._ démontrable). Ce qui est en revanche sur c'est que tout le monde espère que c'est vrai car sinon tout code informatique devient facilement déchiffrable et s'en est fini de la sécurité sur les réseaux (pour ne donner qu'une des conséquence de l'égalité de $P$ et de $NP$).


> TBD langage. Décidabilité du langage. Complexité de calcul.

