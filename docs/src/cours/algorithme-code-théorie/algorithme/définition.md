---
layout: layout/post.njk 
title: Définition d'un algorithme

eleventyNavigation:
  key: "Définition d'un algorithme"
  parent: Algorithme
---

<!-- début résumé -->

Définition d'un algorithme

<!-- end résumé -->

> TBD : faire les liens avec dénombrable

Pseudo-code, calcul et code sont les trois faces d'une même pièce nommée algorithme. Nous allons voir les implications de ces trois termes, mais commençons par définir un algorithme.

{% info %}
Une super introduction aux algorithmes : <https://www.arte.tv/fr/videos/094414-012-A/declics/>
{% endinfo %}

On doit le mot algorithme à [Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) (1815-1852) qui est le(a) premier(e) informaticien(ne) de l'histoire. Elle a donné ce nom en hommage à un savant persan du 9ème siècle (né vers 780 et mort en 850 à Bagdad) nommé [Al-Khwârizmî](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) qui a publié le premier manuel d'algèbre connu à ce jour.

## <span id="algorithme"></span> Algorithme ?

{% note "Définition du 'Petit Robert'  d'un **algorithme** :" %}
Ensemble des règles opératoires propres à un *calcul*
{% endnote %}

Qu'est-ce que ça veut dire ?

* **algorithme** : ensemble des règles opératoires propres à un **calcul**
* **calcul** : enchaînement des instructions nécessaires à l'accomplissement d'une **tâche**
* **tâche** : ...

On a utilisé un algorithme pour comprendre ce qu'est un algorithme :

* *Nom* : définition_petit_robert
  * *paramètres* : un *mot_à_définir*
  * *sortie* : aucune
  * *description* : comprendre la définition d'un mot dans le 'Petit Robert'
* *corps de l'algorithme* :
  1. étant donné la définition nommée *définition* de *mot_à_définir* dans le 'Petit Robert'
  2. afficher *définition* à l'écran.
  3. pour chaque *mot* non compris dans *définition* :
     1. *définition_petit_robert(mot)*

C'est un algorithme tout à fait valable. Ce n'est pas du python, mais c'est :

* compréhensible
* chaque instruction (lire une définition, afficher à l'écran, ...) peut être caractérisée par un petit texte en français
* notre algorithme s'arrête bien à un moment (au pire une fois que l'on a passé en revu tous les mots du dictionnaire)

Règles de construction de l'algorithme utilisé :

* **des** paramètres en entrée mais **une** sortie (qui peut être une structure composée comme une liste ou un dictionnaire).
* le **retour** d'un algorithme est la dernière instruction qu'il fait, en rendant la sortie (ici, il ne rend rien)
* une description de ce qu'il fait
* L'exécution d'un algorithme est signifié par son nom suivie de parenthèses contenant ses paramètres
* afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme.

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

* **finitude** : *« Un algorithme doit toujours se terminer après un nombre fini d’étapes. »*
* **définition précise** : *« Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas. »*
* **entrées** : *« […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié. »*
* **sortie** : *« […] des quantités ayant une relation spécifiée avec les entrées. »*
* **rendement** : *« […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon. »*

On peut en déduire la **définition** suivante :

{% note "**Définitions**" %}
Un ***algorithme*** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{% endnote %}

Ou, de façon équivalente :

{% note "Les **4 propriétés générales** qui définissent un algorithme :" %}

1. un algorithme est constitué d'un ensemble fini d'instructions, décrites avec un nombre fini de symboles
2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes (une étape étant l'application d'une instruction) successives.
3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
4. exécuter une instruction ne doit pas nécessiter d'intelligence (à part celle pour comprendre l'instruction)

{% endnote %}

Une recette de cuisine est donc un algorithme, un trajet google maps, etc.

## <span id="algorithmes-trois-voies"></span> Algorithmes !

La définition très générale d'un algorithme se décline usuellement sous trois formes concrètes :

1. [pseudo-code](../pseudo-code) : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'instructions générales précisément définies. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser un langage de programmation pour décrire notre code. Le but ici est de résoudre un problème donné avec un algorithme utilisant le moins d'instructions possibles.
2. [code](../../code/coder) : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.
3. [fonctions](../../théorie/fonctions) : un algorithme est vu comme une fonction qui calcule un nombre. Le but est ici de comprendre ce que peuvent faire les algorithmes, quels sont les problèmes qu'ils peuvent résoudre.

Ces trois formes ont des buts différents, mais on ne peut exceller dans l'une sans connaître les autres. Tout *théoricien* doit avoir de bonnes connaissances théoriques sur ce que peut calculer  un ordinateur et — tôt ou tard — il devra programmer ses algorithmes ; tout *développeur* doit avoir des connaissances fortes en algorithmie pour pouvoir écrire du code performant.

## Nombre d'algorithmes

La définition générale d'un algorithme stipule qu'il doit être constitué d'un nombre **fini** d'instructions, chaque instruction décrite par un nombre **fini**  de symbole. De plus, c'est implicite, mais un algorithme doit être compris par un humain.

L'idée force à retenir de cette partie est que :

{% note "**A retenir :**" %}
On ne peut pas tout calculer avec des algorithmes, même si on peut calculer beaucoup de choses.
{% endnote %}

### Une infinité d'algorithmes différents

On peut donc déjà conclure que :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes différents.
{% endnote %}
{% details "preuve" %}
Si on considère l'instruction *"Ne fait rien"*, le texte ci-dessous est un algorithme d'une instruction :

```text
Ne fait rien
```

En notant alors $R_k$ ($k >0$) l'algorithme de $k$ instructions *"Ne fait rien"* à la suite (l'algorithme précédent est $A_1$).

Les algorithmes $R_k$ sont tous différents puisque leurs suites d'instructions sont différentes : il existe donc une infinité d'algorithmes différents.
{% enddetails %}

De la preuve de la proposition précédente montre qu'il existe une infinité d’algorithmes différents mais faisant la même chose (il suffit de rajouter des instruction *"Ne fait rien"* !

{% info %}
On y reviendra, mais savoir ce que fait un algorithme n'est pas un problème simple du tout dans le cas général.
{% endinfo %}

Mais, on peut aussi démonter :

{% note "**Proposition**" %}
Il existe une infinité d'algorithmes faisant des choses deux à deux différentes.
{% endnote %}
{% details "preuve" %}
On peut par exemple considérer la familles $A_i$ d'algorithmes ($i > 0$) définis tels que $A_i$ soit constitué d'une seule instruction :

```text
Rend l'entier i
```

Les $A_i$ sont bien des algorithmes puisque chaque entier $i$ se décrit avec un nombre fini de chiffres. De plus, les $A_i$ rendent tous des entiers différents.

{% enddetails %}

Il y a donc **beaucoup** d'algorithmes possibles... mais en réalité pas tant que ça.

### Mais seulement une infinité dénombrable

D'après ce qui précède, un algorithme est un texte. On peut alors considérer que les symboles formant la description de chaque instruction sont des caractères pris dans un alphabet. POur ne pas être chiche, on peut prendre l'alphabet [Unicode](https://fr.wikipedia.org/wiki/Unicode) qui permet d'écrire, entre autres, en Français et contient un peut moins de 150000 caractères.

De là :

{% note %}

Un algorithme est une suite finie $c_1 \dots c_n$ où :

* $c_i \in \mathcal{U}$ pour tout $1 \leq i \leq n$
* $\vert \mathcal{U} \vert \leq 150000$ avec $\mathcal{U}$ l'ensemble des caractères Unicode.

On note $\mathcal{A}$ cet ensemble.

{% endnote %}

Bref, les Algorithmes correspondent à un sous-ensemble de l'ensemble des chaînes de caractères écrite en Unicode

On peut alors utiliser l'ordre entre caractères Unicode (en triant les caractères par [numéro](http://ressources.univ-lemans.fr/AccesLibre/UM/Pedago/physique/02/divers/unicode.html) croissant) pour ordonner les algorithmes selon l'ordre du dictionnaire :

{% note "**Ordre entre Algorithmes**" %}

En définissant $\leq$ tel que, pour deux algorithmes $A =c_1\dots c_{n}$ et $A'={c'}_1\dots {c'}\_{n'}$ de $\mathcal{A}$ on ait $A \leq A'$ si une des trois conditions ci-après est vérifiée :

* $A = A'$
* il existe $1 \leq i \leq \min(n, n')$ tel que $c_i < c'_i$
* $c_i = c'_i$ pour tout $1 \leq i \leq n$ et $n < n'$

La relation $<$ est un [ordre total](https://fr.wikipedia.org/wiki/Ordre_total#D%C3%A9finition) sur l'ensemble des algorithmes.
{% endnote %}
{% details "preuve" %}

Les 4 propriétés de l'ordre total (transitivité, anti-symétrie, réflexivité et totalisé) sont trivialement vérifiées.

{% enddetails %}

Comme $A \leq A'$ implique que le nombre de caractère de $A$ est plus petit ou égal à celui de $A'$, il est clair que pour tout algorithme il n'existe qu'un nombre fini d'algorithme plus petit que lui.

Cet ordre nous permet de définir une bijection entre chaînes de caractères et les nombres entier :

{% note "**Proposition**" %}
La fonction :

$$
\begin{array}{ccccl}
f & : & \mathcal{A} & \to & \mathbb{N}^\star \\\\
 & & A & \mapsto & \vert \\{ A' \mid A' \leq A \\} \vert \\\\
\end{array}
$$

Est une bijection.
{% endnote %}
{% details "preuve" %}

On commence par montrer que si $A \neq A'$ alors $f(A) \neq f(A')$.

On peut considérer sans perte de généralité que $A < A'$ et donc : $\\{ B \mid B \leq A \\} \subsetneq \\{ B \mid B \leq A' \\}$ ce qui implique que $f(A) < f(A')$.
  
On vient de montrer que tous les algorithmes vont avoir une image deux à deux différente par $f$ : **$f$ est une injection**.

Continuons sur notre lancée en montrant que si $i = f(A)$, il existe un algorithme $A'$ tel que $f(A') = i-1$.

Comme $f(A) = \vert \\{ B \mid B \leq A \\} \vert$, l'ensemble $\\{ B \mid B \leq A \\}$ est fini et il existe $A'$ qui est le plus grand élément de $\\{ B \mid B \leq A \\} \backslash \\{ A \\}$. Il est ensuite clair que $f(A') = \vert \\{ B \mid B \leq A \\} \backslash \\{ A \\} \vert = f(A) - 1$.

Il nous suffit de réitérer le processus précédent pour montrer que si $i \leq f(A)$, il existe un algorithme $A'$ tel que $f(A') =i$. Comme il existe une infinité d'algorithmes et que leurs valeurs par $f$ sont deux à deux différentes, il existe pour entier $i$ un algorithme $A$ tel que $f(A) > i$. Donc tout entier $i$ est l'image d'un algorithme : **$f$ est une surjection**.

$f$ est une injection et une surjection : **$f$ une bijection**.
{% enddetails %}

On peut donc préciser le nombre infini d'algorithmes :

<span id="nb-dénombrable-algorithmes"></span>
{% note %}
Il y a exactement autant d'algorithmes différents que de nombres entier.
{% endnote %}

### Nombre réels sans algorithme

Savoir qu'il n'y a pas plus d'algorithmes que de nombres entiers est une très information très importante. Car elle montre qu'un algorithme ne peut pas tout faire.

{% note "**Théorème**" %}
Il existe strictement plus de nombres réels dans l'intervalle $[0, 1]$ que de nombres entiers.
{% endnote %}
{% details "preuve" %}
On doit cette preuve au mathématicien [allemand Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor). Cette preuve magnifique s'appelle [diagonale de Cantor](https://fr.wikipedia.org/wiki/Argument_de_la_diagonale_de_Cantor#La_non-d%C3%A9nombrabilit%C3%A9_des_r%C3%A9els).

On commence la preuve en remarquant que l'on peut associer à tout entier $i$ formé des chiffres $c_1\dots c_k$ le réel de représentation décimal $0, c1\dots c_k$, ce qui démontre qu'il y a au moins autant de réels dans $[0, 1]$ que de nombres entiers.

On suppose qu'il existe une injection entre les réels de l'intervalle $[0, 1]$ et les entiers. On a alors le 1er réel $r_1$, le second réel $r_2$, ..., le $i$ème réel $r_i$.

Chaque réel peut s'écrire sous sa représentation décimale par exemple : $0,1034842\dots$. On construit alors le nombre réel $r$ de $[0, 1]$ tel que sont $i$ème chiffre après la virgule soit :

* $0$ si le $i$ chiffre après la virgule de $r_i$ est différent de $0$
* $1$ si le $i$ chiffre après la virgule de $r_i$ est $0$

Le nombre $r$ est bien dans $[0, 1]$ mais il ne peut pas être $r_i$ quelque soit $i$ !

Il y a une contradiction : il ne peut exister d'injection entre les réels de l'intervalle $[0, 1]$ et les entiers.

Il y a donc strictement plus de réels dans $[0, 1]$ que d'entiers.

{% enddetails %}

{% info "Le fait qu'il y ait des infinis plus ou moins gros est un résultat que l'on doit à Cantor et qui est vachement profond !" %}
Pour une introduction en douceur, consulter ce lien, très bien fait :

<https://www.arte.tv/fr/videos/097454-005-A/voyages-au-pays-des-maths/>

On note communément $\aleph_0$ le nombre d'entiers qui est strictement plus petit que le nombre de réels, noté $\aleph_1$. Une question reste encore en suspend, mais on a pour l'instant toujours pas la réponse, c'est : y a-t-il un infini entre $\aleph_0$ et $\aleph_1$ ? On ne sais pas, mais on pense que non. C'est l'[hypothèse du continu](https://fr.wikipedia.org/wiki/Hypoth%C3%A8se_du_continu).

{% endinfo %}

On déduit du théorème précédent que :

{% note %}

Il existe des réels pour lesquels il n'existe aucun algorithme $A(i)$ qui calcule la $i$ème décimale de $i$ quelque soit $i$

{% endnote %}

Trouver de tels nombre est compliqué, car pour y penser il faut le décrire et donc en proposer un algorithme mais ils existent.

## Algorithmes et démonstration mathématiques

On n'en parlera pas trop dans ce cours (à moins que vous me le demandiez très fort) mais, en gros, les mathématiques sont une partie de l'informatique (certains diraient même, et réciproquement. Des mathématiciens certainement...).

De façon plus précise on a la suite d'équivalences :

1. faire une démonstration consiste — à partir d'une série finie d'axiomes — à effectuer une suite finie de déductions pour parvenir à un résultat. ([Aristote](https://fr.wikipedia.org/wiki/Aristote#Enqu%C3%AAte,_d%C3%A9monstration_et_syllogisme), en -350 environ)
2. (1) est équivalent à démontrer à l'aide d'une suite finie de déductions qu'une proposition logique est vraie ([Hilbert](https://fr.wikipedia.org/wiki/Syst%C3%A8me_%C3%A0_la_Hilbert), début XXe siècle)
3. (en passant, [Gödel](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del), en 1931, démontre qu'il existe des propositions logiques qui sont vraies mais qu'il est impossible de démontrer)
4. [Curry puis Howard qui généralise](https://fr.wikipedia.org/wiki/Correspondance_de_Curry-Howard), en 1950 et 1980, montrent que (2) est équivalent à écrire en terme de [$\lambda$-calcul](https://fr.wikipedia.org/wiki/Lambda-calcul)
5. [Turing](https://fr.wikipedia.org/wiki/Alan_Turing) démontre en 1937, que (4) est équivalent à écrire une machine de Turing.
6. (en passant, Turing démontre qu'il existe des machines de Turing qui ne s'arrêtent jamais et que savoir si une machine de Turing va s'arrêter est [indécidable](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt), ce qui est équivalent à (3)
