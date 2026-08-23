---
layout: layout/post.njk

title: Structure liste

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Une [structure de liste](/cours/algorithmie/structure-conteneurs/liste/){.interne} en python est une version améliorée d'un tableau. On vous demande d'implémenter cette structure en `C` dans deux fichiers `liste.c`{.fichier} et `liste.h`{.fichier} dont vous testerez les fonctions dans un fichier `main.c`{.fichier}.

En `C` on utilisera [les structures](../../langage/structures/){.interne} pour gérer des type composés comme les listes qui nécessitent à la fois un tableau, sa taille et le nombre actuel d'éléments présents.

## Implémentation

Vous utiliserez la compilation séparée vue dans la partie sur [la gestion du code source](../../gestion-code-source){.interne} :

{% faire %}
Créez le type `liste` associé à la structure `struct liste`{.language-} dans un fichier `liste.h` :

```c
typedef struct liste {
        int *t;
        size_t taille;
        size_t nombre;
} liste;
```

Cette structure permet de stocker une structure de liste contenant des entiers (via le pointeur `t`). La création d'une structure par une fonction doit nécessairement rendre un pointeur car il faut créer l'élément dans le tas.
{% endfaire %}
{% faire %}
Dans un fichier `liste.c`, créez les fonctions :

- de création d'une liste vide (par défaut la taille sera de 1 et ne contiendra aucun élément) : `liste liste_creation()`{.language-}
- d'ajout d'un élément à la fin de la liste : `void liste_ajoute(liste*, int)`{.language-}
- d'évaluation d'un élément de la liste : `int liste_valeur(liste*, size_t)`{.language-}
- de remplacement d'un élément : `void liste_remplace(liste*, size_t, int)`{.language-}
- de suppression de l'élément en fin de liste : `void liste_supprime_dernier(liste*)`{.language-}

{% endfaire %}
{% info %}
Vous pourrez utiliser la fonction [`realloc`{.language-}](https://www.scaler.com/topics/c-realloc/) pour le dimensionnement du tableau lorsqu'il faut ajouter un élément à une liste pleine ou que l'on supprime un élément d'une liste dont le nombre d'éléments restant est deux fois plus petit que sa taille.
{% endinfo %}

Quelques questions pour voir si vous avez compris (faites des tests et comprenez avant de regarder la réponse) :

{% exercice %}
Pourquoi une fonction avec la signature suivante ne fonctionnerait pas ?

```c
void liste_ajoute(liste, int)
```

{% endexercice %}
{% details "corrigé" %}
Le paramètre est copié dans la pile. Comme liste ajoute doit modifier l'attribut nombre de liste, il ne modifierait que la copie et pas l'original.

Il est important de passer des pointeurs sur la liste lorsqu'on la modifie, sinon le contenu est copié et placé dans la pile et on ne modifie que la copie et pas la liste originelle.

{% enddetails %}

Cependant :

{% exercice %}
Pourquoi une fonction avec la signature suivante fonctionnerait parfaitement ?

```c
void liste_remplace(liste, size_t, int)
```

{% endexercice %}
{% details "corrigé" %}

Cette fonction remplace une valeur à un endroit *pointé* par la structure. Ce qui est dupliqué c'est l'adresse, mais c'est la même adresse : on ne modifie pas la structure on modifie un endroit pointé par elle.
{% enddetails %}

Testons nos fonctions :

{% faire %}
Dans le programme principal `main.c` :

1. ajoutez les 100 entiers positifs
2. affichez le contenu de la liste
3. affichez la taille et le nombre d'élément de la liste
4. supprimez un à un tous les éléments de la liste
5. affichez la taille et le nombre d'élément de la liste
{% endfaire %}

## Amélioration

On remarque que presque toutes les fonctions manipulant les listes la modifie. Seule la création rend un objet de type liste. L'usage veut que l'on ne manipule les structures en C que via des pointeurs. On utilise alors plutôt ce type de structure :

```c
typedef struct _liste {
        int *t;
        size_t taille;
        size_t nombre;
} _liste;
typedef _liste* liste;
```

Ce qui fait que l'on a à notre disposition deux types :

- `_liste`{.language-} qui est la composition de la structure, utile pour le `malloc`{.language-} de la création,
- `liste`{.language-} qui est un pointeur sur la structure. C'est elle qui est utilisée par l'utilisateur.

{% faire %}
Reprenez le code des fichiers pour rendre compte de cette nouvelle structure.
{% endfaire %}

L'utilisation de la structure est maintenant transparente pour l'utilisateur. Il nous rete qu'une chose à faire : supprimer la liste.

{% faire %}
Ajoutez la fonction `void supprimer_liste(liste)`{.language-} qui supprime la liste aux possibilités de liste.
{% endfaire %}

## Cerise sur le gateau : liste générique

Pour l'instant notre liste est constituée uniquement d'entier.

{% exercice %}
Comment procéderiez vous pour créer une liste pouvant contenir tout ce qu'on veut ?
{% endexercice %}
{% details "solution" %}
On utilise une double indirection et on crée des tableaux de type `void** t`{.language-} qui permettent de stocker des pointeurs sur des objets.

Il faudra cependant faire un cast pour chaque élément pour qu'il soit du bon type, ce qui est loin d'être pratique.
{% enddetails %}
