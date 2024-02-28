---
layout: layout/post.njk 
title: "Projet : objets cartes"

eleventyNavigation:
    prerequis:
        - "../projet-objets-cartes-value-object/"

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

{% faire %}

En utilisant [`@property`{.language-}](../projet-objets-dés#property){.interne},

créez et testez des accesseurs pour les attributs valeur et couleur.

{% endfaire %}
