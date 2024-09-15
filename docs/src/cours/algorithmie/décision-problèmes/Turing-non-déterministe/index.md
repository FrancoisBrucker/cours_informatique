---
layout: layout/post.njk
title: "Machine de Turing non déterministe"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une machine de Turing non déterministe est un modèle abstrait  de machine ou il y a plusieurs possibilité par transition. On montre cependant ce que modèles est équivalent à une machine de Turing.

{% lien %}
<https://www.youtube.com/watch?v=5VRjCk7R-Xg>
{% endlien %}

## Définition

{% note "**Définition**" %}
Une **_machine de Turing non déterministe_** $M$ est une machine de Turing  telle que :

- à chaque transition $\delta(q, r)$ on a plusieurs choix possibles : la fonction de transition est définie sur $2^{Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}}$.
- pour une entrée $E$, s'il existe une succession de choix de transitions pouvant amener la machine à [accepter $E$](../#accepte-rejette) (elle s'arrête pour $E$ et la case sous le ruban vaut 1), elle choisira une de ces successions de choix.
{% endnote %}

Cette machine se distingue de la machine de Turing normale parce que la fonction de transition rend un sous ensemble fini de $Q \times \\{0, 1\\} \times \\{\leftarrow, \rightarrow\\}$ et non juste un nouvel état, un nouveau caractère et une direction : elle donne plusieurs possibilités. Une machine de Turing normale est un cas particulier de machine de Turing non déterministe. C'est la machine elle même qui fait les choix pour arriver, si c'est possible à un choix de 1. Si aucun choix ne fait arriver à 1, il est possible que parfois elle s'arrête sur 0 et parfois ne s'arrête pas.

Prenons par exemple la machine de Turing non déterministe suivante :

- $\delta(\text{START}, 0) = \\{(\text{START}, 1, \leftarrow), (\text{START}, 0, \rightarrow)\\}$
- $\delta(\text{START}, 1) = \\{(\text{STOP}, 1, \rightarrow) \\}$

Avec l'entrée $E=01$ Il y a plein de choix possible :

1. On peut par exemple s'arrêter sur un 0 :
   1. de $\delta(\text{START}, 0)$ on choisit $(\text{START}, 0, \rightarrow)$
   2. puis de $(\text{START}, 1)$ choisir la seule possibilité $(\text{STOP}, 1, \rightarrow)$
2. On peut aussi s'arrêter sur un 1 :
   1. de $\delta(\text{START}, 0)$ on choisit $(\text{START}, 1, \leftarrow)$
   2. puis de de $\delta(\text{START}, 0)$ on choisit $(\text{START}, 0, \rightarrow)$
   3. enfin de $(\text{START}, 1)$ choisir la seule possibilité $(\text{STOP}, 1, \rightarrow)$

Donc la sortie de $M(01) = 1$

Avec une entrée vide en revanche, tous les choix mènent à une sortie en 0 ou une boucle infinie (faites le test) et donc $M()$ n'est pas déterminé.

{% note "**Définition**" %}
Une **_machine de Turing non déterministe polynomiale_** $M$ est une machine de Turing non déterministe qui s'arrête sur toutes les entrées $E$ quelques soient les transitions effectuées en $\mathcal{O}(\vert E \vert^k)$ opérations.
{% endnote %}

Pour rendre notre machine de Turing déterministe précédente polynomiale, il faut lui interdire d'avoir des transitions infinies. Par exemple ne pas refaire boucler sur $\text{START}$. :

- $\delta(\text{START}, 0) = \\{(\text{UN}, 1, \leftarrow), (\text{UN}, 0, \rightarrow)\\}$
- $\delta(\text{START}, 1) = \\{(\text{STOP}, 1, \rightarrow) \\}$
- $\delta(\text{UN}, 1) = \\{(\text{STOP}, 1, \rightarrow) \\}$
- $\delta(\text{UN}, 0) = \\{(\text{STOP}, 0, \rightarrow) \\}$

De là toutes les entrées vont forcément s'arrêter. On a toujours $M(01) = 1$, mais maintenant $M() = 0$.

## Usage

Ce qui nous intéresse ici ce n'est plus l'exécution effective d'une telle machine mais **s'il existe pour une entrée donnée, une suite de transitions emmenant à l'état final**. C'est à dire qu'il existe une suite de nombres $(t_1, \dots, t_k)$ telle que à chaque instruction $i$ on ait pu choisir le $t_i$ème choix pour que la $k$ instruction mène à un état final.

En représentant les choix sous la forme d'un arbre, on peut représenter $\delta$ comme ça :

![Turing non déterministe arbre](turing-nd-arbre.png)

Une exécution de la machine revient à suivre un chemin dans cet arbre, donc qu'à partir de l'état initial $e$ et du caractère $a$ sous le curseur, on a :

- $(e_{t_1}, a_{t_1}, f_{t_1}) \in \delta(e, a)$
- $(e_{t_1\dots t_i}, a_{t_1\dots t_i}, f_{t_1\dots t_i}) \in \delta(e_{t_1t_2\dots t_{i-1}}, a_{t_1t_2\dots t_1i-1})$

{% note %}
Les choix effectués pour accepter une entrée constituent un **_certificat_** de réussite.

Connaître la machine et le certificat pour une entrée permet de vérifier qu'elle fait bien partie du langage : le certificat rendant l'exécution de la machine déterministe.
{% endnote %}

## <span id="exemple"></span>Exemple

Prenons la machine non déterministe suivante :

état  | case | nouvel état | écriture | déplacement
------|------|-------------|----------|------------
START |   0  |  STOP       |     0    |  gauche
START |   1  |  START      |     0    |  droite
START |   1  |  STEP       |     0    |  droite
STEP  |   0  |  STOP       |     0    |  droite
STEP  |   1  |  STOP       |     0    |  gauche

{% exercice %}
Montrez que la machine précédente s'arrête sur toute entrée en temps linéaire
{% endexercice %}
{% details "corrigé" %}
La machine est non déterministe si l'état est `START` et il y a un `1` comme il ne peut y avoir qu'un nombre fini de `1` sur le ruban (on écrit que des 0), la machine s'arrêtera d'elle même une fois le premier 0 rencontré.
{% enddetails %}

{% exercice %}
Montrez que la machine précédente reconnaît les entrées commençant par une suite de `1` puis suivie par la chaîne `01`.
{% endexercice %}
{% details "corrigé" %}

On ne peut s'arrêter sur un 1 que si l'on choisit la transition `(UN, 0)`. On ne fait en effet qu'écrire des 0 et la seule transition qui va en `STOP` à droite. Ceci ne peut arriver que dans le cas ou l'entrée est de type `1....101?....`.

{% enddetails %}

## Équivalence avec une machine de Turing

La machine de Turing non déterministe est un outil théorique très puissant car il permet de démontrer simplement beaucoup de théorèmes d'informatique théorique. Cependant, **elle ne permet pas de faire plus de chose qu'une machine normale**.

{% note "**Proposition**" %}
Pour toute machine de Turing non déterministe, on peut créer une machine de Turing _normale_ qui reconnaîtra les même entrées.

De plus, si la machine de Turing non déterministe décide son langage. la machine de Turing associée également.
{% endnote %}
{% details "preuve", "open" %}
Soit $M$ une machine de Turing non déterministe à $Q$ états. On va construire une machine de Turing déterministe sous la forme d'un pseudo-code, qui simule $M$.

```
k = 1

Tant que Vrai:
  on construit un tableau T contenant tous les mots de $Q$ de longueur $k$ (il y en a $2^k$)
  pour chaque élément e de T:
    exécuter M en suivant, si possible les éléments de e dans l'ordre lorsqu'il y a un choix.
    Si l'exécution de M est possible et se termine sur un 1:
      rendre 1
  Si toutes les executions de T se sont terminées:
    rendre 0
  k = k+1
```

Si la machine $M$ s'arrête, c'est qu'il existe une suite de choix qui lui permette de s'arrêter. Cette suite étant de longueur finie, notre algorithme finira forcément par la considérer et il s'arrêtera.
{% enddetails %}

Notez que dans la preuve précédente on a bien besoin que la machine s'arrête sur toute entrée, sinon notre machine déterministe ne s’arrêterait jamais s'il existait une suite de choix pouvant mener à une exécution infinie.

Comme la machine de Turing non déterministe est polynomiale on a de plus :

{% note "**Proposition**" %}
Une machine de Turing non déterministe polynomiale est équivalente à une machine de Turing de complexité exponentielle.
{% endnote %}

La machine de Turing non déterministe n'est qu'une façon plus simple de décrire les mêmes choses. Dans notre cas, cela va unifier la définition des classes $P$ et $NP$. En effet :

{% note "**Proposition**" %}
Soit $M$ une machine de Turing non déterministe polynomiale. Le vérifieur $v(E, C)$ avec $v$ une entrée et $C$ une suite de transition possible qui consiste à exécuter $M$ en choisissant itérativement les les élément de $C$ est un vérifieur efficace du langage de $M$.
{% endnote %}

Si on rend déterministe la machine non déterministe exemple, on voit qu ele non déterministe permet de simuler une boucle tant que non `101` avancer de 1 case vers la droite : le non-déterminisme est une façon de condenser une énumération de choix.
