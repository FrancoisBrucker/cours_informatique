---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Définitions

{% aller %}
[Définitions](./définitions){.interne}
{% endaller %}

## Outils de mesure

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.
>
> C'est un peut chiant de faire comme ça et c'est pas très utile de faire tous ces détails :
> 
> 1. pas se faire suer avec tous les détails. Par exemple, comment fonctionne la boucle for ? Juste une affectation on bien c'est une somme si on l'écrit avec un tant que ?
> 2. ce qui nous intéresse c'est les grosses valeurs, lorsque c'est petit ça va vite et on s'en fiche.
> 3. la tendance de la complexité est cruciale : faire schéma des complexités.
> solution = $\mathcal{O}$, oméga et théta.
>
> enfin 
De plus 
> allure similaire, même si on va plus vite/plus lentement.

## Astuces de calcul

- règles
- structures