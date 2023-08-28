---
layout: layout/post.njk

title: Bases Linux

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ouvrez un terminal.

## Lire les fichiers d'un dossier

Vous savez déjà le faire, puisque vous avez lu le [tutoriel d'utilisation du terminal](/tutoriels/terminal-utilisation)

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


> TBD pour aller plus loin (ensuite). Lorsque l'on a parlé des variables. PWD, OLDPWD
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