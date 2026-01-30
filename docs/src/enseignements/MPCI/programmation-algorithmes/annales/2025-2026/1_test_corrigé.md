---
layout: layout/post.njk

title: "sujet Test 1 : algorithmie et preuve"
authors:
  - François Brucker
---

## Barème

Suite à une erreur de ma part, les étudiants n'ont eu que les pages impaires du sujet (photocopies non recto verso du sujet initial) il ne restait donc que les 2 questions de la page 3.

La note du test est sur 5 points répartis comme suit :

- 2pt pour la question sur le nombre d'algorithme :
  - +1 point par réponse juste (il y en avait 2)
  - -1 point par réponse fausse
- 3 pt pour la question sur le remplacement :
  - 1 pt pour un pseudo-code syntaxiquement correct
  - 1 pt pour un pseudo-code sémantiquement correct
  - 1 pt pour la preuve (.5 pour la finitude (qui fonctionne même sur un algorithme sémantiquement faux), .5 pour l'invariant)

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $4$

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève moyen** tombe dans les deux pièges mais ne fait pas d'erreurs, ce qui garantit le 10 (1 réponse juste à la première question ; pseudo-code syntaxiquement correct et prouve la finitude pour la seconde question)
- **un bon élève** ne tombe que dans un piège ce qui garantit le 14
- **un très bon élève** ne tombe dans aucun piège

{% endnote %}

La ventilation des notes est :

|note/20  |<6  | [6, 8] | ==10  | [12, 14]  | 18  |
|---------|----|-----|----------|-----------|-----|
|nombre   | 9  | 14  |  7       |  8        |  1  |
|rang min | 38 | 21  | 10       | 8         | 1   |

- moyenne : 7.36/20 (1.84/5)
- écart-type : 4.58/20 (1.15/5)
- médiane : 6/20 (1.5/5)

Un test est brutal. On peut vite avoir une très bonne note comme une note très basse. Ceux qui ont raté ce test ne désespérez pas et révisez/apprenez bien pour les prochains. Cela se rattrape. 

Au global, je trouve que vous n'avez pas assez travaillé pour le test et êtes restés sur vos acquis du premier semestre : cela ne suffit pas. Si ce test sonne comme un signal d'alarme pour vous, c'est bien. Vous savez que je suis là pour répondre à vos questions et vous aider à progresser : il ne faut pas hésiter à me solliciter pendant un cours pour des précisions ou individuellement avant/après un cours.


## Erreurs fréquemment rencontrées

### Trop vite

Vous ne réfléchissez pas assez à ce qu'on vous demande de faire. Il y avait un piège par question est vous êtes pour beaucoup tombé dans les deux. 

### Pas assez révisé

Près de la moitié des étudiants qui n'ont pas vraiment révisé, ce qui se voit tout de suite :

- à la question 1 où vous vous trompez sur des propositions du cours
- à la question 2 où vous n'écrivez pas du pseudocode syntaxiquement correct.

### Question 1 : nombre d'algorithmes

Il y a un nombre dénombrable d'algorithmes ce qui signifie qu'il y en a autant que tout ensemble en bijection avec les entiers. En particuliers tous les multiples de $\pi$ fonctionnent puisque la fonction $f: n \mapsto n \cdot \pi$ est une bijection de $\mathbb{N}$ dans l'ensemble des multiples de $\pi$. C'était le piège.

Les autres réponses sont fausses, c'est du cours. En particulier, j'ai montré en cours qu'il y a autant de fonction de $\mathbb{N}$ dans $\mathbb{N}$ que de réels ! C'est justement un résultat fondamental : un algorithme est une fonction de $\mathbb{N}$ dans $\mathbb{N}$ mais toutes les fonctions de $\mathbb{N}$ dans $\mathbb{N}$ ne sont pas des algorithmes.


### Question 2 : algorithme de remplacement

Trois fautes courantes :

1. vous ne respectez pas la signature demandée : l'algorithme n'est pas sensé rendre quelque chose (et c'est normal puisque le tableau est modifié)
2. vous tombez dans le piège : vous écrivez un algorithme syntaxiquement correct mais faux (voir corrigé). En lisant la question vous avez foncé tête baissée sur la première solution qui vous est venue à l'esprit, solution qui était fausse (mais vous auriez du vous en rendre compte en essayant de le prouver). Certains arrivent à faire l'exploit de prouver leur algorithme faux, cela montre clairement que vous ne faites pas assez attention à ce que vous faites ! 
3. Une petite dizaine n'écrivent tout simplement pas du pseudocode correct. Pour cela, relisez les algorithmes du cours et comprenez comment ils sont écrits.

Une erreur que j'ai vue plusieurs fois et qu'il faut comprendre :

```pseudocode
pour chaque e de T:
    si T[e] == n:
        #  ...
```

Ce code est une hérésie :

- pour pouvoir écrire `T[e]`{.language-} il faut que `e`{.language-} soit un indice (un entier de `[0 .. T.longueur[`{.language-})
- la boucle `pour chaque`{.language-} itère sur les valeurs de `T`{.language-}. Écrire `pour chaque e de T:`{.language-} est équivalent à écrire `pour chaque e de [T[0] .. T[T.longueur -1]]:`{.language-} et donc écrire `T[e]`{.language-}  est une aberration dans la plupart des cas.

## Corrigé

{% lien %}
[corrigé](../1_test_corrigé.pdf){.interne}
{% endlien %}