---
layout: layout/post.njk

title: Gestion du code source

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour avoir un programme gérable et maintenable, il faut le scinder en unités fonctionnelles chaque unité ayant son propre code.

Pour illustrer cette partie, nous allons utiliser l'exemple de conversion des degrés en supposant que l'on ait le programme suivant, nommé `degres.c`{.fichiers} :

<div id="code"></div>

```c
#include <stdio.h>

double fahrenheit(int celcius) {
  return (celcius * 9.0/5) + 32;
}

int kelvin(int celcius) {
  return celcius + 273;
}

int main() {

printf("%3.2f \n", fahrenheit(37));
printf("%i \n", kelvin(37));

}

```

{% info %}
On a rajouté un format particulier pour les réels, en ajoutant le nombre de chiffres maximum avant et après la virgule.
{% endinfo %}

## Compilation séparée

Il n'est pas bon d'avoir des fichiers de code trop gros, car :

- cela rend le code non lisible
- la compilation va passer osn temps à recompiler du code qui n'a pas changé

On a donc l'habitude de découper le code en unités fonctionnelles, compilées séparément en objet, puis assembler à la fin du processus de compilation. Ceci permet de ne compiler que le code ayant changé.

{% aller %}
[Compilation séparée](compilation-séparée){.interne}
{% endaller %}

## Gestion du build

S'il est tout à fait possible de faire toute la compilation à la main lorsque l'on a 1 ou 2 fichiers, le process devient vite compliquer à gérer s'il on a plusieurs dizaine, voir plusieurs centaines de fichier à compiler. Il existe plusieurs utilitaire permettant d'automatiser le processus de compilation, nous allons montrer le plus simple : la commande `make` et son fichier de configuration `Makefile`{.fichier}.

{% aller %}
[Gestion du build avec `make` et `Makefile`{.fichier}](gestion-build){.interne}
{% endaller %}
