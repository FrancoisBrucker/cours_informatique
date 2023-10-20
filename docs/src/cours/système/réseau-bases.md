---
layout: layout/post.njk

title: Réseau

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



{% lien %}

- [Beej's Guide to Network Concepts](https://beej.us/guide/bgnet0/html/)
- [Linux Networking-concepts HOWTO](https://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)

{% endlien %}

Réseau filaire : une ligne par communication de bout en bout

A et B et B et C communiquent : chacun un fil :

```
              ============= B
           //
A ---------
           \
            ---------- C
```

Réseau par paquet un fil sert à plusieurs choses. A et B (-) et B et C (+) communiquent simultanément sur le même fil :

```
            ++--++--+ B
           /
A ---------
           +
            ++++++++++ C
```

Le problème est de remettre les paquets dans la bone conversation et le bon ordre.

Comme un réseau postal, chaque paquet peut prendre un chemin différent pour arriver à bon port. Il arrivent donc que :

- des paquets plus anciens arrivent avant de nouveaux paquets
- des paquets vont se perdre et ne jamais arriver (ou arriver trop tard).

## tbd

- <https://www.youtube.com/watch?v=KobYWL1LtW4>

- [transmission tcp rate](https://www.youtube.com/watch?v=LfiRKZze0HM&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=32)

[Introduction to computer network](https://intronetworks.cs.luc.edu/)

- [Beej's Guide to Network Programming Using Internet Sockets](https://beej.us/guide/bgnet/)
- <https://opensource.com/article/19/4/interprocess-communication-linux-networking>

- <https://www.youtube.com/watch?v=As6g6IXcVa4&list=PLG49S3nxzAnlCJiCrOYuRYb6cne864a7G> ?

> en python : <https://www.youtube.com/watch?v=Ftg8fjY_YWU>
