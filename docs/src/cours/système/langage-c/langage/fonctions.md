---
layout: layout/post.njk

title: FOnctions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


```c
type_de_retour nom(paramètres) {
  instructions de la fonction 

  return valeur_de_type_de_retour;
}
```

Le type de retour est obligatoire. Si la fonction ne retourne rien son type de retour doit être `void`.

La signature de la fonction est ce qui est nécessaire pour la caractériser :

- son type de retour
- son nom
- ses paramètres et leurs types

Par exemple :

```c
int fahrenheit(int x) {
  return (x * 9/5) + 32;
} 
```

Sa signature est :

```c
int fahrenheit(int);
```

Si on définit une fonction à l'intérieur d'une autre fonction, son scope est réduit à la fonction dans laquelle elle est décrite. Pour vos programmes, il faut doc mettre les fonctions en-dehors de la fonction main :

```c
#include <stdio.h>

int fahrenheit(int x) {
  return (x * 9.0/5) + 32;
} 

int main() {
  printf("%d\n", fahrenheit(0))
}

```

{% exercice %}

Transformez la fonction pour que sa signature soit `double fahrenheit(int);`{.language-} (vérifiez que la fonction rendent bien que 0C soit égal à 33.8F)

{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}
