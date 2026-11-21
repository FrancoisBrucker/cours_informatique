---
layout: layout/post.njk

title: Redirection de ports

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD faire grossir et expliquer mieux

Amusons-nous avec la redirection de ports.

## Passerelle

```shell
ssh -J sas1.ec-m.fr roucas100.etu.ec-m.fr
```

Pratique lorsque l'on veut modifier son site perso statique depuis chez soit en utilisant [le remote-ssh](https://learn.microsoft.com/fr-fr/azure-sphere/app-development/ssh-build-vscode?view=azure-sphere-integrated) de vscode.

## Une redirection de port

```
              22               22
so-high ---------  sas1  --------- roucas100.etu
```

La commande `ssh -L4000:roucas100.etu:22 fbrucker@sas1.ec-m.fr` depuis ma machine nommée so-high demande à :

1. faire une connexion ssh (depuis le port 22) sur le sas
2. que cette connexion fasse un lien entre :
   - le port 4000 de so-high
   - le port 22 de roucas100.etu

Ceci est possible puisque sas1 "voit" roucas100.etu et so-high.

En laissant cette connexion ouverte, dans un autre terminal on peut maintenant se connecter directement sur le port 22 de roucas100.etu (c'est à dire le démon ssh de roucas100.etu) en utilisant le port 4000 de so-high :

```
ssh -p4000 fbrucker@localhost
```

## Plusieurs redirection de port

On suppose que la première redirection est faite :

```
ssh -L4000:roucas100.etu:22 fbrucker@sas1.ec-m.fr`
```

Le port 4000 de so-high est le port 22 de roucas100.etu (via la connexion sas puisqu'il est impossible d'aller directement de l'un à l'autre)

On peut maintenant ramener un autre port de roucas100.etu sur notre machine, par exemple le port 9090 :

```
ssh -L9090:localhost:9090 -p4000 fbrucker@localhost
```

On effectue une connexion sur le port 4000 de localhost (qui est du coup aussi le port 22 de roucas100.etu) et on demande de faire une redirection du port 9090 sur cette machine sur notre machine locale.

Attention, il y a deux fois marqué `localhost` mains ce nest pas le même :

1. le deuxième localhost correspond à la machine qui se connecte, ici so-high
2. le premier localhost correspond à la machine connectée, ici roucas100.etu

Supposons que l'on ait un service uniquement accessible depuis roucas100.etu sur le port 9090. Par exemple une écoute de port (que vous aurez lancé depuis un autre terminal connecté sur roucas100.etu) :

```
nc -l -p 9090 127.0.0.1
```

On peut maintenant directement y accéder avec `nc 127.0.0.1 9090`
