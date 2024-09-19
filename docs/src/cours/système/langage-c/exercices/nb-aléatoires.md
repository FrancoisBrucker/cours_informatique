---
layout: layout/post.njk

title: Nombres aléatoires

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Vous implémenterez les fonction de cet exercice dans le fichier `nombre-aléatoires.c`{.fichier}.

- Toutes les fonctions sont à écrire dans le programme principal, en dehors de la fonctions main.
- Le programme main doit permettre de tester chaque fonction demandée

## <span id="entier-aléatoire"></span>Entier aléatoire

{% faire %}
Créez une fonction de signature :

```c
int aleatoire_int(int min, int max);
```

permettant de rendre un entier aléatoire entre `min`{.language-} et `max`{.language-} inclus (les deux paramètres de la fonction).

Pour cela, vous pourrez utiliser les fonctions (de la `libc`) suivantes définis dans `<stdlib.h>`{.fichier} :

- [`srand`{.language-}](https://koor.fr/C/cstdlib/srand.wp) dont le but est d'initialiser l'algorithme de nombres aléatoire avec ue seed. Attention cette fonction n'est à n'utiliser qu'une fois par programme, dans la fonction `main`{.language-}, au tout début.
- [`rand`{.language-}](https://koor.fr/C/cstdlib/rand.wp) qui rend un entier aléatoire entre 0 et et RAND_MAX
- le  modulo  (`%`{.language-}) qui permet de conserver l'équiprobabilité.
{% endfaire %}
{% faire %}
Testez la fonction précédente dans la fonction `main`{.language-} en faisant la moyenne de 100 tirages de nombres entre -50 et +50 (vous devez trouver quelque chose proche de 0).
{% endfaire %}

## Liste d'entiers aléatoires

{% faire %}
Créez une fonction de signature :

```c
int *aleatoire_tab(int max, size_t nombre);
```

Qui tire `nombre`{.language-} nombres aléatoires entre 0 et max (exclu) et les rend dans un tableau de taille nombre. Vous créerez un tableau de `nombre`{.language-} entiers `int`{.language-} avec une [allocation dans le tas](../../langage/gestion-tas/){.interne}.

{% endfaire %}
{% faire %}
Testez la fonction précédente avec `int *t = aleatoire_tab(10, 100)`{.language-} et en remplissant le tableau `int n[10]`{.language-} tel que `n[i]`{.language-} contienne le nombre de fois où le nombre `i`{.language-} est présent dans `t`{.language-}.
{% endfaire %}

{% exercice %}
Pourquoi faire l'allocation avec un `mallloc`{.language-} ?
{% endexercice %}
{% details "corrigé" %}
Toute variable déclarée dans une fonction est placée dans la pile et disparaît à la fin de l'exécution de la fonction. Pour rendre un pointeur par une fonction il faut que l'objet pointé reste valide à la fin de son exécution.
{% enddetails %}

## <span id="proba-aléatoire"></span>Probabilité

{% faire %}
Créez une fonction de signature :

```c
double aleatoire_01();
```

permettant de rendre un réel aléatoire entre 0 et 1.
{% endfaire %}

{% faire %}
Utilisez la fonction précédente pour créer une fonction de signature :

```c
void aleatoire_01_liste(double proba, size_t nombre, int *t);
```

Cette fonction doit remplir `nombre`{.language-} cases d'un tableau `t`{.language-} passé en paramètre valant chacun 1 avec une probabilité `proba`{.language-} et 0 sinon.
{% endfaire %}

{% faire %}
Testez la fonction précédente en tirant une liste de taille 100 avec une probabilité de .5.
{% endfaire %}

## Compilation séparée

En utilisant la partie sur [la gestion du code source](../../gestion-code-source){.interne} :

{% faire %}
Décomposez le code en deux unités fonctionnelles :

- le programme principal (fichier `main.c`{.fichier})
- le module aléatoire (deux fichiers `aleatoire.c`{.fichier} et `aleatoire.h`{.fichier})

Créez un fichier `Makefile`{.fichier} pour gérer la compilation de ce projet.
{% endfaire %}
