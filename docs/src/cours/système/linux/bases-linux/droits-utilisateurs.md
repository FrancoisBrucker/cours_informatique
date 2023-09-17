---
layout: layout/post.njk

title: Droits des process et des utilisateurs

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<https://www.cekome.com/blog/permissions-utilisateurs-linux/>

- tout est fichier (pseudo-device. dev est chargé à chaque démarrage)
- fichiers : droits
- groups : /etc/group
- changer droits et group gou+ et chiffres
- exécution d'un dossier fichier
- droit d'un process : dépend de celui qui exécute.
- /etc/passwd et /etc/shadow
- uid 0 = root
- setuid : passwd
- sticky bit pour dossiers /tmp
- flags
- liens symbolique et pas symboliques

> TBD explication droits :
> - dossier x
> - fichiers x
> - un seul propriétaire et un seul groupe. 

> 
> TBD quand on parlera process > Idem pour le process qui hérite des droits du fichier qui l'exécute
> important lorsque l'on utilise u serveur web par exemple. group qui peut lire/exécuter

> groupe important lorsque l'on utilise u serveur web par exemple. group qui peut lire/exécuter


> TBD bouger dans /, ls puis revenir au dossier précédent. POur cela lire la doc google, et le man dans bash. On peut aller plus vite en cherchant "cd" et n pour la prochaine. on peut encore aller plus vite en cherchant "   cd" car c'est une commande
> Ceci permet de parler des variables.
> 

> TBD path : which, type whereis
> TBD ; pour finir une instruction
> TBD retour de process 0/1
> TBD le && 
> TBD if then else est fait comme ça