---
layout: layout/post.njk

title: Nombres aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## <span id="entier-aléatoire"></span>Entier aléatoire

- Toutes les fonctions sont à écrire dans le programme principal, en dehors de la fonctions main.
- Le programme main doit permettre de tester chaque fonction demandée

{% faire %}
Créez une fonction de signature :

```c
int aleatoire_int(int min, int max);
```

permettant de rendre un entier aléatoire entre `min`{.language-} et `max`{.language-} inclus (les deux paramètres de la fonction).

Pour cela, vous pourrez utiliser les fonctions (de la `libc`) suivantes définis dans `<stdlib.h>`{.fichier} :

- [`srand`{.language-}](https://koor.fr/C/cstdlib/srand.wp) dont le but est d'initialiser l'algorithme de nombres aléatoire avec ue seed. Attention cette fonction n'est à n'utiliser qu'une fois par programme, au tout début.
- [`rand`{.language-}](https://koor.fr/C/cstdlib/rand.wp) qui rend un entier aléatoire entre 0 et et RAND_MAX
- le  modulo  (`%`{.language-}) qui permet de conserver l'équiprobabilité.
{% endfaire %}
{% faire %}
Testez la fonction précédente en faisant la moyenne de 100000 tirage de nombres entre -50 et +50 et en vérifiant pour chaque tirage que l'on est bien entre -50 et 50.
{% endfaire %}

## Liste d'entiers aléatoires

{% faire %}
Créez une fonction de signature :

```c
int *aleatoire_tab(int max, size_t nombre);
```

Qui tire `nombre`{.language-} nombres aléatoires entre 0 et max (exclu) et les rend dans un tableau de taille nombre. Vous créerez un tableau de `nombre`{.language-} entiers `int`{.language-} avec une [allocation dans le tas](../langage/gestion-tas/){.interner}.

{% endfaire %}
{% faire %}
Testez la fonction précédente avec `int *t = aleatoire_tab(10, 1000)`{.language-} et en remplissant le tableau `int n[10]`{.language-} tel que `n[i]`{.language-} contienne le nombre de fois où le nombre `i`{.language-} est présent dans `t`{.language-}.
{% endfaire %}

## Intervalle aléatoire

{% faire %}
Créez une fonction de signature :

```c
double aleatoire_01();
```

permettant de rendre un réel aléatoire entre 0 et 1.
{% endfaire %}

## <span id="proba-aléatoire"></span>Probabilité

{% faire %}
Utilisez la fonction précédente pour créer une fonction de signature :

```c
int aleatoire_01(double proba);
```

Qui rend 1 avec une probabilité `proba`{.language-} et 0 sinon.
{% endfaire %}

{% faire %}
Utilisez la fonction précédente pour créer une fonction de signature :

```c
int *aleatoire_01_liste(double proba, size_t nombre);
```

Qui rend une liste de taille `nombre`{.language-} contenant des 0 ou des 1 tirés selon une probabilité `proba`{.language-}.
{% endfaire %}

{% faire %}
Testez la fonction précédente en tirant une liste de taille 100 avec une probabilité de .1, .5. et .75. Vérifier que les proportions sont bien vérifiées.
{% endfaire %}

## <span id="mélange"></span>Mélange d'un tableau

{% faire %}

Créez une fonction qui mélange les $n$ premiers éléments d'un tableau d'entier. Sa signature doit être :

```c
void nb_chiffres(int *t, size_t n);
```

Vous utiliserez l'algorithme de [mélange de Knuth](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), improprement appelé algorithme de Fisher-Yates par les mathématiciens.

{% endfaire %}
{% faire %}
Testez la fonction précédente en tirant mélangeant plusieurs fois le tableau contenant les 10 premiers entiers et en affichant le résultat.
{% endfaire %}

## Compilation séparée

Le but de cet exercice est de comprendre [la compilation séparée](../gestion-code-source/compilation-séparée/), tout en jouant avec les nombres.

{% faire %}
Décomposez le code en deux unités fonctionnelles :

- le programme principal (fichier `main.c`{.fichier})
- le module aléatoire (deux fichiers `aleatoire.c`{.fichier} et `aleatoire.h`{.fichier})

Créez un fichier `Makefile`{.fichier} pour gérer la compilation de ce projet.
{% endfaire %}
