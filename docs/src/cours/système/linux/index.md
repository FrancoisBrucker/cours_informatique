---
layout: layout/post.njk

title: Linux
authors:
    - "François Brucker"

eleventyNavigation:
    prerequis:
        - "/tutoriels/ordinateur-développement/"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
On suppose que vous avez suivi les tutos sur la [navigation dans un système de fichiers](/tutoriels/fichiers-navigation/), sur l'existence du [terminal](/tutoriels/terminal/) et [son utilisation](/tutoriels/terminal-utilisation)
{% endinfo %}

Histoire d'Unix :

- [frise historique](https://www.youtube.com/watch?v=AEsdyAeumVQ)
- les [débuts d'Unix](https://www.youtube.com/watch?v=boahlBmc-NY)

Plusieurs unix, Linux en est une version. POSIX pour unifier (mais attentions aux variantes et aux extensions à POSIX qui sont système dépendant)

1. [installation Linux](installation-linux){.interne}
2. [base Linux](bases-linux){.interne}
3. [scripting](scripting){.interne}
4. [système d'exploitation Linux/Ubuntu](./système-exploitation-linux){.interne}
