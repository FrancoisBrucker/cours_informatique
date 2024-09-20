---
layout: layout/post.njk

title: Listes doublement chaînées

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[liste chaînée](https://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e)
{% endlien %}

Une liste doublement chaînées est la structure :

```c
typedef struct element* element_t;
struct element {
  void* data;
  element_t next;
  element_t pred;
};
```

Initialisée telle que :

```c
element_t element_create(void *data) {
  element_t e = malloc(sizeof(struct element));
  e->data = data;
  e->next = NULL;
  e->pred = NULL;

  return e;
}
```

Et détruite telle que :

```c
void* element_destroy(element_t e) {
  void *data = e->data;
  free(e);

  return data;
}
```

Il est important de rendre la donnée pour que l'utilisateur la libère si nécessaire, sinon on risque la fuite de mémoire.

La liste doublement chaînée est une généralisation de la liste chaînée. Son intérêt en général est de garantir un ordre arbitraire dans une suite où l'ajout et la suppression d'élément est courante.

C'est un trade-off. On optimise l'ajout et la suppression d'éléments au détriment de a localisation d'un élément particulier :

- la liste à une complexité en $\mathcal{O}(1)$ pour accéder au $i$ème élément alors que la liste chaînée est en $\mathcal{O}(n)$
- la liste à une complexité en $\mathcal{O}(n)$ pour supprimer un élément donné quelconque alors que la liste chaînée est en $\mathcal{O}(1)$

{% faire %}
Montrer que dans les cas suivants, une liste chaînée n'est ps avantageuse :

1. si l'on ne modifie que peu la structure ou si l'ajoute/supprime que les derniers élément
2. si l'ordre n'est pas important.
{% endfaire %}

## Unité fonctionnelle

Pour garantir l'utilisation d'une liste doublement chaînée il faut implémenter les élément suivants :

```c
element_t element_create(void *data);
void* element_destroy(element_t e);
void element_ajoute_suivant(element_t e, element_t suivant);
void element_ajoute_precedent(element_t e, element_t precedent);
```

{% faire %}
Implémentez les 4 fonctions précédentes.
{% endfaire %}

## Utilisation : parcours

{% lien %}
<https://medium.com/future-vision/data-structures-algorithms-linked-lists-fc0b8a82d609>
{% endlien %}

On a coutume d'appeler `liste`{.language-} un pointeur sur un élément telle que :

- le champ `data`{.language-} contient `NULL`{.language-}
- le champ `next`{.language-} contient le premier élément de la suite d'éléments chaînés
- le champ `pred`{.language-} contient `NULL`{.language-}

Ce premier élément n'est pas un élément de la liste, mais un élément abstrait. Ceci permet de maintenir unique le début de la liste, même si son premier élément change. Le dernier élément de la liste étant facile à trouver c'est celui tel que son champ `next`{.language-} contient `NULL`{.language-}.

{% attention %}
Il ne faut pas confondre la structure de liste que l'on a vu précédemment et la liste chaînée. Les deux structures portent le même non, c;est fâcheux, mais c'est ainsi.
{% endattention %}

Vous allez implémenter un algorithme qui maintient une liste d'éléments dans l'ordre inverse de leur utilisation.

Vous utiliserez pour cela 10 données ayant pour structure :

```c
typedef struct _personne {
  unsigned int id;
  char *nom;
} personne;

```

Où `id` va de 0 à 9, et choisissez le nom comme vous voulez. Par exemple :

```c

personne data[10] = {
      {0, "zéro"}, {1, "un"},  {2, "deux"}, {3, "trois"}, {4, "quatre"},
      {5, "cinq"}, {6, "six"}, {7, "sept"}, {8, "huit"},  {9, "neuf"}};
```

{% faire %}
Créez une liste doublement chaînée contenant les 10 données dans l'ordre de leurs id.
{% endfaire %}

Pour afficher le nom de chaque élément de la liste on vous demande de :

{% faire %}
Implémentez la fonction de signature :

```c
void liste_parcours(element_t liste, void (*f)(void *));
```

Qui va appliquer à tous les éléments `e`{.language-} de la liste la fonction : `f(e->data)`{.language-}

{% endfaire %}
{% faire %}
Utilisez `liste_parcours`{.language-} avec une fonction `f`{.language-} qui affiche à l'écran l'identifiant suivi du nom de la donnée.

{% endfaire %}

## Utilisation : modification de liste

Vous allez maintenant simuler l'utilisation de la liste :

{% faire %}

1. tirer un nombre aléatoire entre 0 et 9
2. placer la donnée d'identifiant le nombre tiré en tête de liste
3. afficher le parcours de la liste

{% endfaire %}
{% info %}
Lorsque l'on supprime ou insère un élément dans une liste doublement chaîné, il faut faire attention au successeur et au prédécesseur dans la liste.
{% endinfo %}
