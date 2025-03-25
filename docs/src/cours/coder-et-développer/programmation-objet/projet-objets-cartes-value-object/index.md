---
layout: layout/post.njk
title: "Projet : Amélioration des objets cartes"

eleventyNavigation:
  prerequis:
    - "../projet-objets-cartes/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une fois la carte créée, il ne faudrait plus pouvoir la modifier. Or pour l'instant on a directement accès aux attributs, donc rien n'interdit de le faire.

Pour pallier ça, il suffit de définir un accesseur sans mutateur pour les 2 attributs valeur et couleur. Cela permet :

- d'accéder aux attribut
- une tentative de modification produira une erreur

On a alors créé un **_value object_** c'est à dire un objet non mutable, comme un entier ou une chaîne de caractères en python.
{% faire %}

En utilisant [`@property`{.language-}](../projet-objets-dés#property){.interne}, créez et testez des accesseurs pour les attributs valeur et couleur.

{% endfaire %}

Si on a le choix :

{% note "**Méthode de conception**" %}
Lorsque l'on crée un objet, si on a pas de raison particulière de le rendre modifiable on crée un **_value object_**. Cela évite les effets de bords (et rend la programmation concurrente et parallèle bien plus simple).
{% endnote %}
