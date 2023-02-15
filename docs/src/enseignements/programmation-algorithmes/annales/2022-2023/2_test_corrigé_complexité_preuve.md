---
layout: layout/post.njk

title:  "Corrigé Test 2 : complexité et preuve"
authors:
    - François Brucker
---


## Barème

Une note sur 5 répartie comme suit :

1. sur 1 point (plus un bonus de 1/4 pour ceux ayant répondu parfaitement)
2. sur 1 point (1/3 pour le code, 1/3 pour la complexité et 1/3 pour la preuve)
3. sur 1 point (1/3 pour les condition aux limites, 1/3 pour le cas général et 1/3 pour la finitude de l'algorithme)
4. sur 1 point (1/2 pour borner le nombre d'itérations du while, 1/2 pour la bonne borne)
5. sur 1 point

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $6$

{% note "**Objectif du test**" %}

En 15 minutes :

* **un élève *normal*** doit parvenir à faire parfaitement les 2 premières questions. Ce qui lui permet d'avoir 2/5, soit 12/20
* **un bon élève** doit parvenir à réussir l'équivalent de 3 questions. Ce qui lui permet d'avoir 3/5 et donc 18/20
* **un très bon élève** fait plus que 3 questions

{% endnote %}

La ventilation des notes est :

|note/5 | 0 | 0.25 | 0.58 | 0.75 | 0.83 | 1 | 1.17 | 1.25 | 1.33 | 1.42 | 1.67 | 1.92 | 2  | 2.25 | 2.67 | 2.75 | 3  |
|note/20| 0 | 1.25 | 3.5  | 4.5  | 5    | 6 | 7    | 7.5  | 8    | 8.5  | 10   | 11.5 | 12 | 13.5 | 16   | 16.5 | 18 |
|-------|---|------|------|------|------|---|------|------|------|------|------|------|----|------|------|------|----|
|nombre | 5 |  1   |  1   |  4   |  5   | 5 | 3    | 1    | 3    |   1  |   2  |  5   | 2  | 2    |  1   | 1    | 1  |
| rang  | 39| 38   | 37   | 33   | 28   |23 |  20  |   19 | 16   | 15   | 13   | 8    |  6 | 4    | 3    | 2    |  1 |
| # <   |  0|  5   |  6   | 7    |  11  |16 |  21  | 24   |  25  |  28  | 29   |  31  | 36 |  38  | 40   | 41   | 42 |

* moyenne : 7.4/20 (1.23/5)
* écart-type : 4.58/20 (0.76/5)
* médiane : 7/20 (1.17/5)

## Erreurs fréquemment rencontrées

Vous n'êtes globalement pas très à l'aise avec les preuves d'algorithmes (et c'est un euphémisme), comme le prouve vos notes. Il vous faut les travailler encore et encore jusqu'à ce que ça rentre. En effet :

* La partie algorithmique de l'informatique au concours se fera presque exclusivement au tableau ou sur feuille, on jugera donc essentiellement vos capacités à écrire et expliciter vos algorithmes (*ie* à les prouver), plutôt que vos capacités à écrire du code.
* Mais aussi, du code non prouvé n'est rien d'autre qu'un tas de bits inutile car on ne sait pas vraiment ce qu'il fait. Les autres membres de l'équipe de développement auront alors des réticences à l'utiliser. Donc même si vous préférez le code, il vous faut mieux conceptualiser ce que vous écrivez et **surtout** apprendre à l'expliciter. Faites vôtre le Nindô de Boileau : *Ce que l'on conçoit bien s'énonce [se code] clairement, et les mots [boucles] pour le dire [l'écrire] arrivent [se tapent] aisément*.  

{% note "**comment progresser**" %}
Même si vous avez actuellement du mal, ce n'est pas perdu (et une moyenne se remonte facilement avec un test réussi). Les techniques de preuve de ce que l'on vous demandera de prouver seront toujours plus ou moins les mêmes. Le cours et les annales regorgent d'exemples et vous montrent tout ce qui est à savoir.

* **Commencez** par de pas (plus) être dans le déni et évaluez clairement ce qui vous manque pour mettre en œuvre un plan d'action.
* **Ensuite**, apprenez et comprenez les techniques de preuves des algorithmes de tri. C'est très utile car il existe de nombreux algorithmes de tri différents, chacun utilisant une technique différente. Une fois ces preuves maîtrisées, vous pourrez facilement les adapter à tout autre algorithme que l'on vous demandera d'écrire et de prouver.

{% endnote %}

### Preuve

Beaucoup n'essaient même pas de prouver l'existence d'un col. C'est dommage car les algorithmes que l'on vous demande de coder ou de comprendre ensuite reposent sur cette compréhension.

D'autres se perdent dans les récurrences, mais ce n'est pas très grave, cela viendra avec la répétition de ce genre de preuve.

Enfin, certains dégoupillent les fumigènes et utilisent les célèbres :

* *"il est évident que"*
* *"donc"*
* *"une récurrence immédiate nous montre que"*

Suivi d'un CQFD péremptoire qui ne démontre rien.

Évitez ce genre d'astuces comme la peste, cela énerve le correcteur. Il sera d'autant plus suspicieux quand à vos arguments futurs et ne vous laissera plus le bénéfice du doute. Au final, vous perdez des points à la place d'en gagner. Il est **toujours plus avantageux** de dire qu'on ne sais plus continuer et donc qu'on admettra ce résultat puis de poursuivre la preuve.

Rien ne vous empêche de revenir plus tard pour prouver correctement le résultat.

### Algorithme de la question 2

#### Écrire un algorithme

Consiste **toujours** en trois parties :

1. le pseudo-code
2. la complexité
3. la preuve

Même si vous ne donnez que des éléments de preuves ou de complexité, c'est préférable à ne rien mettre.

Attention cependant. Une personne m'a écrit un calcul de complexité alors qu'elle n'avait pas écrit d'algorithme... Je n'ai pas compté de points, cela va sans dire.

#### Pseudo-code

Vous tentez parfois de faire compliqué, et du coup ça rate. PENSEZ SIMPLE ! Une action par ligne. Dans le cas de cette question, on procède par ordre :

1. cas i=0
2. cas i = n-1
3. cas général

et on sort de la fonction dèq qu'on peut.

Lisez aussi l'énoncé. On vous demande de rendre l'**indice** d'un col, pas s'il en existe un ou non (retour d'un booléen). Surtout que la question 1 montre qu'il en existe toujours un, vous auriez pu vous douter que votre algorithme ne répondait pas à la question.

#### Retour de fonction

Le pattern :

```python
def fonction():
    if condition:
        return une-chose
    elif autre-condition:
        return autre-chose
    else:
        return un-troisième truc
```

Ou pire, ce pattern là :

```python
def fonction():
    if condition:
        i = une-chose
    elif autre-condition:
        i = autre-chose
    else:
        i = un-troisième truc
    
    return i
```

N'est pas joli et il confuse. Un `return`{.language-} sort de la fonction, donc autant écrire :

```python
def fonction():
    if condition:
        return une-chose

    if autre-condition:
        return autre-chose

    return un-troisième truc
```

Qui est plus compacte et plus clair.

{% note %}
Ne mettez pas de condition s'il n'y en a pas besoin. Ca alourdit le code et le rend moins compréhensible.
{% endnote %}

### On ne modifie pas les itérateurs de boucles

{% note %}
On ne modifie jamais ce sur quoi on itère.
{% endnote %}

En particulier, j'ai vu plusieurs :

```python
# ...

for i in range(len(T)):
    if T[i] > T[i+1]:
        i += 1

# ...
```

Ca ne marche pas. Au début de la prochaine boucle, $i$ sera à nouveau égal à $i+1$.

### Question 4

Cela vaut le coup de connaître et de reconnaître une dichotomie (on coupe le tableau en 2 à chaque fois) **et** sa complexité $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$ opérations.

Cela vous sera utile :

* pour trouver immédiatement une complexité
* tenter d'améliorer vos algorithme en passant un d'une complexité linéaire à une complexité logarithmique.

Quand une question vous demande d'améliorer un algorithme linéaire, c'est quasi-tout le temps une dichotomie qui fonctionne.

### Question 5

Le cours donne une borne min d'un algorithme faisant $n$ choix ($\log_2(n)$ tests sont nécessaire). Gardez cette remarque du cours dans la poche, cela sert plus souvent qu'on ne le pense.

## Corrigé de la question 1. Existence

La première preuve est celle que j'attendais. Elle reprend la définition est la travaille pour obtenir le résultat. La seconde est bien plus simple, mais encore faut-il voir l'astuce (une personne l'a trouvée). Enfin la troisième preuve par récurrence fonctionne aussi si l'on justifie bien comment passer de $n$ à $n+1$.

### En reprenant la définition

Si la première condition ($i=0$) est vérifiée, le tableau contient un col. On la suppose donc non vérifiée : $T[0] > T[1]$. De même, si la seconde condition ($i=n-1$) est vérifiée, le tableau contient également un col. Supposons la donc également non vérifiée : $T[n-2] < T[n-1]$.

Les deux conditions précédentes montrent qu'il existe $n-1 > i^\star > 0$ le plus petit indice tel que $T[i^\star] \leq T[i^\star +1]$. On a alors : $T[i^\star -1] > T[i^\star ] \leq T[i^\star +1]$ et $i^\star$ est un col.

### Une astuce

Un tableau d'entier possède forcément un élément minimum. Il existe donc $i^\star$ tel que $T[i^\star] \leq T[i]$ pour tout $0 \leq i < n$. De là :

* soit $i^\star = 0$ et $T[i^\star] \leq T[1]$
* soit $i^\star = n-1$ et $T[i^\star] \leq T[n-2]$
* soit $0 < i^\star < n-1$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$

Simple et efficace, non ?

### Par récurrence

On montre par récurrence sur la taille $n$ du tableau qu'il existe toujours un col.

1. Initialisation. Si $n=2$ soit $T[0] \leq T[1]$ soit $T[0] \geq T[1]$ (ce qui est équivalent pour $n=2$ à $T[n-1] \leq T[n-2]$). Ces deux cas correspondent aux deux premières possibilités pour un col
2. on suppose la propriété vrai pour $n \geq 2$. Et on se donne un tableau $T$ de taille $n+1$.
3. l'hypothèse de récurrence stipule que le tableau $T'$ constitué des $n$ premières cases de $T$ ($T'= T[:-1]$) possède un col, disons à l'indice $i^\star$. 3 cas sont possibles :
   1. $i^\star = 0$ et $T'[0] \leq T'[1]$ ce qui implique $T[0] \leq T[1]$ : $i^\star$ est aussi un col pour $T$
   2. $0 < i^\star < n-1$ et $T'[i^\star] \leq \min(T'[i-1], T'[i+1])$ ce qui implique $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
   3. $i^\star = n-1$ et $T'[n-1] \leq T'[n-2]$ ce qui implique $T[n-1] \leq T[n-2]$. On conclut en remarquant que :
      1. soit $T[n] \geq T[n-1]$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
      2. soit $T[n] < T[n-1]$ et $n$ est un col pour $T$.

## Corrigé de la question 2. Découverte

{% note %}
Lorsque l'on demande de donner un algorithme, il y a plusieurs chose à donner :

* le code ou pseudo-code
* complexité (max)
* preuve

{% endnote %}

La preuve de la 1ère question montrant qu'il existe forcément un col, l'algorithme suivant qui mime directement la définition (lignes 2-3 : 1ère condition, lignes 5-6 : 2ème condition et lignes 8-10 la troisième condition) trouvera forcément un col :

```python#
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= min(T[i-1], T[i + 1]):
            return i

```

Sa complexité dans le cas le pire a lieu pour les tableaux dont le premier et seul col se trouve à l'avant dernier indice (comme pour la liste $[5, 4, 3, 2, 1, 2]$ par exemple), forçant l'algorithme à :

* faire échouer le 1er test de la ligne 2 en $\mathcal{O}(1)$ opérations
* faire échouer le 2er test de la ligne 5 en $\mathcal{O}(1)$ opérations
* faire les $\mathcal{O}(n)$ itérations de la boucle for en :
  * faisant échouer tous les tests sauf le dernier $\mathcal{O}(1)$ opérations
  * réussissant le dernier test et en faisant un retour de fonction en $\mathcal{O}(1)$ opérations

La complexité totale maximale est alors :

$$
C(n) = \mathcal{O}(1) + \mathcal{O}(1) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) = \mathcal{O}(n)
$$

On peut aussi utiliser la preuve précédente et *simplifier* la boucle `for`{.language-} en gardant la même complexité :

```python
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= T[i + 1]:
            return i

```

## Corrigé de la question 3. Rapidité

La preuve d'existence du 1 montre que pour tout $i + 1 < j$, si $T[i] > T[i+1]$ et $T[j] > T[j-1]$, alors il existe un indice $i < k < j$  tel que $k$ soit un col de la matrice.

L'invariant de boucle de la boucle `while`{.language-} est alors :

> A la fin de chaque itération de la boucle `while`{.language-}, soit :
>
> * `T[milieu]`{.language-} est un col
> * `T[milieu]`{.language-} n'est pas un col et :
>   * `début + 1 < fin`{.language-}
>   * `T[début] > T[début+1]`{.language-} et `T[fin] > T[fin-1]`{.language-}
>

A la fin de la première itération,  on a soit :

* `T[milieu] <= min(T[milieu - 1], T[milieu + 1])`{.language-} et `milieu`{.language-} est un col
* `fin' = milieu`{.language-} et `début' = début`{.language-} si `T[milieu] > T[milieu -1]`{.language-}. Comme initialement `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu - 1 > début`{.language-} puisque `T[0] > T[1]`{.language-} et l'invariant est vérifié.
* `fin' = fin`{.language-} et `début' = milieu`{.language-} si `T[milieu] <= T[milieu -1]`{.language-} et `T[milieu] > T[milieu + 1]`{.language-}. Comme `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu + 1 < fin`{.language-} puisque `T[-1] > T[-2]`{.language-} et l'invariant est vérifié.

La même démonstration fonctionne à l'identique à la fin de l'itération $i+1$ si l'invariant est vrai à la fin de l'itération $i$.

Comme `fin - début >= 0` et diminue strictement à chaque itération de la boucle `while`{.language-}, il arrivera **forcément** un moment où `milieu`{.language-} sera un col.

## Corrigé de la question 4. Complexité

La procédure de la boucle `while`{.language-} est identique à la recherche dichotomique puisque l'on se place toujours au milieu de l'espace de recherche. Le cours nous indiquant que la complexité de la recherche dichotomique est $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$, on en conclut que l'algorithme `trouve_vite(T)`{.language-} est également en $\mathcal{O}(\ln(n))$ opérations.

## Corrigé de la question 5. complexité du problème

Il existe des tableaux ayant tous un unique col en position $i$ pour tout $0 \leq i < n$ (prenez les tableaux $[0, -1, \dots, -i, -i+1, -i +2, \dots, -i + (n - i - 1)]$). Tout algorithme trouvant les col des tableaux doit donc pouvoir distinguer parmi $n$ cas : il est au moins de complexité $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$.

Comme l'algorithme `trouve_vite(T)`{.language-} est de complexité $\mathcal{O}(\ln(n))$, c'est borne min est atteinte.
