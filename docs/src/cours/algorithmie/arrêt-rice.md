---
layout: layout/post.njk 
title: Arrêt d'un Algorithme et Théorème de Rice
        
eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La notion d'algorithme stipule qu'il doit, à partir d'une entrée, rendre un calcul en un temps fini.

Il y a donc deux conditions pour qu'une suite d'instruction soit un algorithme :

- elle doit faire quelque chose,
- elle doit le faire en temps fini.

Ces deux notions ne vont pas de soit. Comment savoir si un texte respectant les 3 premières propriétés de [la définition d'un algorithme](../définition/#règles-générales){.interne} respecte également la quatrième ?

Les 3 premières propriétés d'un algorithme sont en effet objectives et facilement vérifiable : est ce que je comprends (ou est-ce que l'interpréteur python) toutes les instructions et est-ce que leurs enchaînement est rationnels ? Bref est-ce que mon programme est syntaxiquement correct ?

{% note "**Définition**" %}
On dira qu'un texte respectant les trois premières propriétés de [la définition d'un algorithme](../définition/#règles-générales){.interne} est un ***algorithme syntaxiquement correct***.
{% endnote %}

Alors que la 4ème règle nécessite une analyse fine de l'algorithme, qui peut souvent être ardue et – on le verra – parfois impossible.

Nous allons examiner ici ces deux problèmes au cœur de l'informatique. Étant donné un algorithme sémantiquement correct :

- est-ce un algorithme ? C'est à dire : s'arrête-t-il pour chacune de ses entrées ?
- et si c'est un algorithme que fait-il ? C'est à dire : quel nombre calcule-t-il ou quel problème résout-il ?

On verra que ces questions sont loin d'être anecdotiques.

## Problème de l'arrêt

Savoir si un algorithme syntaxiquement correct va s'arrêter, ou pas, sur une entrée donnée est un problème compliqué. Prenez par exemple l'[algorithme suivant](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) :

```text
Nom : syracuse
Entrées : 
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 1:
        si n est pair:
            n = n divisé par 2
        sinon:
            n = trois fois n plus 1
    rendre 1
```

Le texte ci-dessus est bien un algorithme syntaxiquement correct. À partir d'un entier $n$, il le divise par 2 s'il est pair ou le multiplie par 3 et ajoute 1 s'il est impair et recommence tant que ce nombre est strictement plus grand que 1.

{% faire %}
Testez chez vous pour plusieurs nombres, c'est assez bluffant.

Affichez également la suite de nombre ou la représenter graphiquement pour voir l'évolution de votre nombre d'entrée jusqu'à 1.
{% endfaire %}

Personne ne sait (à l'heure où je tape ces caractères) si cet algorithme s'arrête pour tout $n$.

Alors que l'algorithme syntaxiquement correct suivant n'est pas un algorithme :

```text
Nom : vérité
Entrées : 
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute : "L'informatique c'est vraiment super chouette !"
```

Et que celui-ci l'est :

```text
Nom : compte à rebours
Entrées : 
    n : un entier strictement positif
Programme :
    tant que n est strictement plus grand que 0:
        dire à voix haute le nombre n
        n = n moins 1
```

Bref, savoir si un algorithme syntaxiquement correct est un algorithme ne peut se faire qu'en analysant l'algorithme proprement dit.

Supposons que l'on puisse automatiser le processus de vérification qu'un algorithme syntaxiquement correct est un algorithme. Il existe alors un algorithme permettant de le faire :

```text
Nom : vérificateur
Entrée : 
    n : un entier représentant un algorithme syntaxiquement correct
Sortie :
    1 si l'algorithme syntaxiquement correct en entrée est un algorithme
    0 sinon
```

On passe en entrée de notre algorithme `vérificateur`{.language-} [un entier encodant un algorithme syntaxiquement correct](../définition/#encodage-algorithme), comme on l'a déjà fait.

{% info %}
Une démonstration étant un algorithme (une preuve est finie et s'appuie sur un nombre fini d'axiomes), donc si une méthode formelle de vérification existe, c'est un algorithme !
{% endinfo %}

On ne donne pas le code de cet algorithme parce que ce n'est pas évident à faire a priori. On ne peut bien sûr pas exécuter l'algorithme en entrée pour savoir s'il s'arrête car s'il ne s'arrête pas, notre algorithme n'en est pas un puisque lui non plus ne s'arrêtera pas. Si `vérificateur`{.language-} existe il doit être plus malin que ça.

Mais arrêtons le suspens tout de suite, [Alan Turing](https://fr.wikipedia.org/wiki/Alan_Turing) lui-même a montré qu'un tel algorithme ne peut exister dans le cadre de ses machine ([le problème de l'arrêt de la machine de Turing](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27arr%C3%AAt)) :

{% note "**Théorème**" %}
L'algorithme `vérificateur`{.language-} n'existe pas.
{% endnote %}
{% details "preuve", "open" %}
Supposons que `vérificateur`{.language-} soit un algorithme et construisons l'algorithme syntaxiquement correct suivant :

```text
Nom : oups
Programme :
    si le retour de l'algorithme vérificateur avec comme entrée le numéro de oups vaut 1:
        faire une boucle infinie
```

L'algorithme syntaxiquement correct `oups`{.language-} est infernal :
Cette machine est infernale. En effet :

- si `oups`{.language-} est un algorithme alors le vérificateur va rendre 1 ce qui fait que `oups`{.language-} ne s'arrêtera pas
- si `oups`{.language-} n'est pas un algorithme alors le vérificateur va rendre 0 ce qui fait que `oups`{.language-} s'arrêtera.

Bref, `oups`{.language-} ne peut pas exister et donc `vérificateur`{.language-} non plus.

{% enddetails %}

Comprenez bien le théorème ci-dessus. Il signifie qu'il n'existe pas de propriété **démontrable** (en temps fini) qu'auraient tout algorithme. Si on peut montrer qu'un algorithme syntaxiquement correct s'arrête, il faut faire la preuve pour cet algorithme spécifiquement.

{% lien %}
C'est la version informatique de l'entscheidungsproblem. Voir  
[cet excellent documentaire d'Arte](https://www.youtube.com/watch?v=Zci9m08HQws)
{% endlien %}

## <span id="théorème-rice"></span>Théorème de Rice

S'il est impossible de savoir si un algorithme syntaxiquement correct s'arrête ou pas a priori, il est aussi impossible de savoir ce qu'il va faire... Il n'existe en effet pas de démonstration qu'un algorithme possède une *propriété* donnée, et ce, quelque soit celle-ci.

Commençons par définir ce qu'est une propriété :

{% note "**Définition**" %}
Une ***propriété*** est un ensemble non vide $\mathcal{A}$ d'algorithmes.

Un algorithme syntaxiquement correct $A$ ***vérifie la propriété $\mathcal{A}$*** s'il existe un algorithme $A' \in \mathcal{A}$ tel que $A$ et $A'$ coincident pour toute entrée :$A(n) = A'(n)$ pour tout $n$.

{% endnote %}

Et explicitons le théorème :

{% note "**Théorème**" %}
Quelque soit la propriété $\mathcal{A}$, l'algorithme suivant n'existe pas :

```text
Nom : propriété-P
Entrée : 
    n : un entier représentant un algorithme syntaxiquement correct
Sortie :
    1 si l'algorithme en entrée vérifie la propriété P
    0 sinon
```

{% endnote %}
{% details "preuve", "open" %}
Soit $A_0 \in \mathcal{A}$ et $A$ un algorithme syntaxiquement correct. On peut alors construire l'algorithme suivant :

```text
Nom : succession
Entrée : 
    n : un entier
Sortie :
    A(n)
    A_0(n)
```

L'algorithme `succession`{.language-} vérifie la propriété $\mathcal{A}$ si et seulement si $A$ est un algorithme (s'il s'arrête).

On en conclut qu'il ne peut exister une machine décidant si un algorithme vérifie une propriété que s'il existe une machine `vérificateur`{.language-}, ce qui est impossible.

{% enddetails %}

Ceci signifie que pour toute propriété voulu sur la sortie d'un algorithme, il existe une infinité de façon différente de faire. Si on veut démontrer qu'un algorithme a une propriété donnée, il faut le démontrer pour cet algorithme, et il n'existe pas de preuve générale.

Réciproquement, quelque soit la tâche à effectuer on ne peut pas connaître les algorithmes qui l'effectueront.

Par exemple : il est indécidable de savoir si un algorithme calcule $n!$, en revanche il est parfois possible de démonter qu'un algorithme donné calcule ou pas $n!$.

Ceci rend impossible des méthodes automatisées de preuve d'algorithmes. Il est donc nécessaire :

- de prouver individuellement tout algorithme que l'on conçoit
- de tester personnellement toute fonction que l'on code

Si on sait ce que l'on veut faire, on peut créer des algorithme (exemple des fonctions calculables), mais si on a un algorithme syntaxiquement correct savoir s'il s'arrête est compliqué et si on a un algorithme savoir ce qu'il fait l'est aussi.
