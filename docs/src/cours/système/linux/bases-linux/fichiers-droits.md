---
layout: layout/post.njk

title: Droits et fichiers

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<https://www.cekome.com/blog/permissions-utilisateurs-linux/>


- un seul propriétaire et un seul groupe. 
- fichiers : droits
- groups : /etc/group

> - dossier x
> - fichiers x

- changer droits et group gou+ et chiffres

- tout est fichier (pseudo-device. dev est chargé à chaque démarrage)
- liens symbolique et pas symboliques

- droit d'un process : dépend de celui qui exécute.

- setuid : passwd /etc/passwd et /etc/shadow
- uid 0 = root

- sticky bit pour dossiers /tmp
- flags


> 
> TBD quand on parlera process > Idem pour le process qui hérite des droits du fichier qui l'exécute
> important lorsque l'on utilise u serveur web par exemple. group qui peut lire/exécuter

> groupe important lorsque l'on utilise u serveur web par exemple. group qui peut lire/exécuter


> TBD bouger dans /, ls puis revenir au dossier précédent. POur cela lire la doc google, et le man dans bash. On peut aller plus vite en cherchant "cd" et n pour la prochaine. on peut encore aller plus vite en cherchant "   cd" car c'est une commande
> Ceci permet de parler des variables.
> 

> TBD path : which, type whereis

