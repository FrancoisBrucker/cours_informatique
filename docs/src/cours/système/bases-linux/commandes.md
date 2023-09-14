---
layout: layout/post.njk

title: Commande

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les commandes Unix sont faites pour être :

- être spécialisées : elles ne font qu'un seule chose
- paramétrables : des options permettent de changer son comportement par défaut

De plus, unix présuppose que les utilisateurs savent ce qu'ils font et cherchent à automatiser leurs actions par des scripts. Il n'y a donc (pratiquement) pas de demande de confirmation. Le corollaire de cette philosophie est que chaque commande est documentée.

Enfin, la plupart des commandes fonctionnent sous différents systèmes unix (Linux, Macos, Bsd, ...). Le fonctionnement général de chaque commande est dicté par la norme [POSIX](https://fr.wikipedia.org/wiki/POSIX), mais des variations existent il est crucial de se référer à l'aide de son système.


- `ls`

1. commandes :
   1. option et man
   2. commandes simples et qui suppose que l'utilisateur sait ce qu'il fait
   3. entrée, sortie, erreur
   4. tout est fichier
2. fichiers, droits, utilisateurs, filesystem

{% info %}
On suppose que vous avez suivi les tutos sur la [navigation dans un système de fichiers](/tutoriels/fichiers-navigation/), sur l'existence du [terminal](/tutoriels/terminal/) et [son utilisation](/tutoriels/terminal-utilisation)
{% endinfo %}
commandes unix : man pour connaître toutes les options possibles. Commandes courantes cd ls, pushd 

- Anatomie d'une commande : ls commandes : man
- `ls -l -a` vaut `ls -la` deux `--` pour les options longues (voir playlist youtube)
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

## Lire les fichiers d'un dossier

{% exercice %}

1. positionnez vous dans votre dossier maison
2. affichez le contenu de ce dossier

{% endexercice %}
{% details "corrigé" %}

```
$ cd ~
$ ls
Bureau  Documents  Images  Modèles  Musique  Public  snap  Téléchargements  Vidéos
```

Notez que dossier par défaut de la commande `cd` est la maison. La première ligne de la commande précédente aurait donc aussi pu être juste : `cd`.
{% enddetails %}

> man ls pour voir les options.
> man est très pratique. PLus rapide que google et on est sur que c'est votre version de ls (il y a parfois des différences)


> TBD : ls -la chez soit et chez / (sans changer de dossier)
> TBD explication droits :
> - dossier x
> - fichiers x
> - un seul propriétaire et un seul groupe. 
> 
> TBD quand on parlera process > Idem pour le process qui hérite des droits du fichier qui l'exécute
> important lorsque l'on utilise u serveur web par exemple. group qui peut lire/exécuter


> TBD autre fichier lorsque l'on parlera de l'environnement. pour aller plus loin (ensuite). Lorsque l'on a parlé des variables. PWD, OLDPWD

> TBD bouger dans /, ls puis revenir au dossier précédent. POur cela lire la doc google, et le man dans bash. On peut aller plus vite en cherchant "cd" et n pour la prochaine. on peut encore aller plus vite en cherchant "   cd" car c'est une commande
> Ceci permet de parler des variables.
> 
> TBD dans les env parler de PWD et poser la question de : <https://stackoverflow.com/questions/41147818/no-man-page-for-the-cd-command>


> TBD toute exécution d'un fichier crée un processus fils du shell appelant
> TBD path : which, type whereis
> TBD ; pour finir une instruction
> TBD retour de process 0/1
> TBD le && 
> TBD if then else est fait comme ça