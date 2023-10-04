---
layout: layout/post.njk

title: Structures

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une structure est un type dérivé permettant de regrouper des données de type hétérogène. Par exemple, on définie une structure `personne`{.language-} :

```c
struct personne {
  char *prénom;
  int age;
};
```

Pour créer une variable de cette structure, comme ce n'est ni un type reconnu ni un typedef il faut :

```c
struct personne x = {"Chun-Li", 55};
```

On peut ensuite accéder à chaque élément avec une notation pointée :

```c
#include <stdio.h>

int main() {

struct personne {
    char *prenom;
    int age;
};

struct personne x = { "Chun-Li", 55};

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

Il est bien sur possible de modifier les variables après la création :

```c
#include <stdio.h>

int main() {

struct personne {
    char *prenom;
    int age;
};

struct personne x = { "", 0};

x.prenom = "Ken";
x.age = 58;

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

Pour ne pas avoir à retaper `struct` avant chaque création, on a l'habitude de passer par un `typedef` : `typedef struct personne personne;`{.language-},
pour ensuite directement créer une personne par : `personne x = {"", 0};`.

On peut aussi tout faire en une fois et la déclaration du struct et le typedef :

```c
#include <stdio.h>

int main() {

typedef struct personne {
        char *prenom;
        int age;
} personne;

personne x = { "Chun-Li", 55};

printf("%s\n", x.prenom);
printf("%d\n", x.age);

}
```

On peut utiliser un struct dans un tableau, comme tout autre type, ou via un pointeur :

```c
personne ken = {"Ken", 56};
personne *p = &ken;
```

{% note %}
Utiliser un pointeur pour accéder à une structure étant tellement utilisée qu'il existe un raccourci : on peut écrire `p->x` à la place de `(*p).x`, ce qui est plus clair.
{% endnote %}
