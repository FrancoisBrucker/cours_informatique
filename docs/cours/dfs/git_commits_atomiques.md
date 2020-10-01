---
layout: page
title:  "les commits atomiques"
category: tutorial
tags: dev git 
---

## But

Ce tuto vise à apporter **une** réponse (parmi tant d'autres) à la séculaire question : "Mais du coup, quand est-ce que je commit ?".

## Présentation

Lorsqu'on débute avec Git, ou même lorsqu'on est un utilisateur plus confirmé, cette question relative à la fréquence de *commit* revient régulièrement sur la table, notamment lors d'un travail collectif. Disons-le d'emblée, il n'y a pas vraiment de *bonne réponse* à cette question, si ce n'est peut-être celle-ci : utilisez git de la manière la plus efficace et intuitive pour vous et votre workflow personnel, tant que cela ne nuit pas au reste du groupe. Facile, non ?

Ce petit tuto prend toutefois le partie de présenter un mode de fonctionnement spécifique, celui des **commits atomiques**. C'est une méthode assez répandue parmi les développeurs, en particulier dans le monde de l'*open source*. Mais ça ne signifie pas forcément qu'elle vous conviendra. Prêt(e) ? C'est parti !

## L'idée générale

Globalement, l'idée est la suivante : on va découper les modifications apportées au code en tout petits morceaux élémentaires (des *atomes*, du grec ἄτομος [átomos], « insécable » ) que l'on *commit* au fur et à mesure. Une nouvelle fonction écrite ? Un commit. Une correction faite en passant ? Un commit. Etc, etc. Bien sûr, le niveau de granularité de ce découpage arbitraire dépend des goûts et des couleurs de chacun. Là encore, il faut se laisser guider par son *worflow* personnel, et ne pas oublier que git est un outil au service du développeur, et pas l'inverse.

Ensuite, on va souvent vouloir retravailler un peu son historique git pour le rendre plus lisible. En effet, avec tous ces petits *commits* atomiques, un relecteur peut vite être perdu dans la masse.

Mais à quoi bon faire ces petits *commits* si c'est pour ensuite retravailler l'historique ? Imaginons que je travaille sur l'ajout d'une nouvelle fonctionnalité. J'écris de nouvelles lignes de code pour y parvenir et, au passage, je tombe sur une ligne déjà écrite qui aura bien besoin d'une petite correction. Deux options : soit je me la note sur une todo list et j'y reviendrai plus tard, soit je m'en occupe tout de suite. Certains sont plutôt partisan de la première option, car elle permet de rester focus sur la tache en cours. Son principal défaut, cependant, est que la correction prendra ensuite plus de temps, parce qu'il faudra revenir plus tard à la todolist, réouvrir le fichier, retrouver la ligne, comprendre ce qui ne va pas et qui était si évident quelques heures plus tôt mais ne l'est plus forcément.

Si la modification est rapide à faire (une quinzaine de secondes), nous dit la seconde école, autant la faire tout de suite. Chip, chop, je change le type de cette variable, et me voilà reparti sur ma fonctionnalité principale. Sauf que, si je n'y prends pas garde, ma petite correction va être ajoutée au milieu de tout le reste une fois que j'aurai poussé le code de la nouvelle fonctionnalité, ce qui peut perturber la relecture, parfois grandement. On pourrait l'indiquer dans le commentaire du *commit* ou la *pull request* mais, là encore, on risque d'accroitre la confusion plus qu'autre chose.

## Le commit atomique à la rescousse

C'est là que le *commit* atomique intervient. Chip, chop, je change le type d'une variable, et je commit directement cette toute petite modification. Je peux ensuite revenir à ma tache principale l'esprit tranquille. En tout, cette petite digression n'aura duré que quelques secondes, le temps de changer une ligne et de la *commit*.

Mais à force, je risque à la fin d'avoir un gloubi-boulga dantesque de commits consécutifs, certains relatifs à la nouvelle fonctionnalité en cours d'ajout, et d'autres de simple petites modifications annexes réalisées à la volée. Pas tellement plus lisible que si on faisait un seul gros *commit*.

C'est pour ça qu'une fois qu'on a planté tous nos petits *commit* au fur et à mesure, il est bon, une fois qu'on a tout fini, de revenir dessus pour les jardiner. Git permet en effet de déplacer les commits pour les réordonner, et également de fusionner des *commits* entre eux pour qu'ils n'en forment plus qu'un seul. Je peux donc, par exemple, réunir en un seul *commit* toutes mes petites modifications éparses, et un autre les réels ajouts signifiants et utiles à la nouvelle fonctionnalité en cours de développement. Il suffit ensuite de préciser en une ligne de commentaire, lors de la publication, que la partie d'intérêt se trouve dans tel *commit*. Vos relecteurs, incluant votre futur moi, vous en seront très reconnaissants !

## Chouette, mais comment on fait ?

Il y a plusieurs petits *tricks* à connaître et à articuler ensemble pour parvenir au résultat escompté :
1. Comment *commit* un petit bout de fichier (une ligne par exemple)
2. Comment "jardiner" ses *commits* (les déplacer et les fusionner)

### Ajouter un 'tit bout

Pour n'ajouter qu'un morceau de mon fichier index.html (par exemple), on commencer par :

~~~ shell
git add -p index.html
~~~

Cela va ouvrir dans le shell une interface permettant de dire à git, petit bout par petit bout, si l'on souhaite le commit ou pas. Une sorte de *chatbot* avant l'heure. Git réalise de lui-même un découpage en petits morceaux, et il vous soumet les morceaux pour analyse un par un. A vous de lui dire ce que vous voulez en faire, simplement en répondant :
- `y` pour ajouter le morceau au *stage* (l'espace de pré-commit)
- `n` pour ne pas l'y ajouter
- `s` pour demander à git de redécouper ce morceaux en morceaux plus petit (il n'y arrive pas toujours !)
- `e` pour ouvrir l'éditeur (vim par exemple) et enlever manuellement (en les supprimant) les passages qu'on ne souhaite pas *commit*.

On s'en rend compte, c'est un outil très puissant, permettant d'aller vite en répondant petit bout par petit bout, et autorisant une granularité aussi fine que possible grâce au mode manuel `e`.

### Jardinage

Une fois que l'on a fini de cracher du code, vient le moment de réorganiser un peu tout ça pour plus de clarté (notamment à la relecture). Pour cela, on va déplacer les *commits* pour mettre ensemble (côte-à-côte) les *commits* de fonctionnalité, et ensemble ceux qui concernent des fioritures ou de petites modifications éparses. Si j'ai 10 *commits" à réorganiser, il suffit pour commancer d'utiliser :

~~~ shell
git rebase -i HEAD~10
~~~

L'option `-i` signifiant "interactif", et pour cause : la commande nous a ouvert vim, où les 10 derniers commits s'offrent à nous :

~~~ shell
pick d2eb036 updta td gloutons
pick 88af96b add extended git rebase tuto
pick 4da9c73 add how to and first cheatsheet lines
pick 43d2f7e add file
pick 7431bbd add last commands to cheatsheet
pick 40900b9 delete erronous line
pick 298dead add merge how-to
pick ca7b5db add first part
pick 289eb2a add link to rebase tuto
pick a2ce5c6 continue tuto
~~~

**Note :** on remarque que l'ordre de présentation est ici inversé par rapport à celui de la commande `git log` : les plus vieux *commits* sont en haut (c'est donc plus une stalagtique qu'un arbre, ou alors un arbre planté à l'envers).

Nous verrons dans quelques instants ce que signifie le "pick". Détaillons d'abord comment déplacer les lignes. Pour cela, il suffit de déplacer la ligne d'un *commit* à l'endroit où on veut qu'elle apparaisse. Sur vim, `dd` pour couper une ligne, et `p` pour la coller.

~~~ shell
pick 88af96b add extended git rebase tuto
pick 4da9c73 add how to and first cheatsheet lines
pick 7431bbd add last commands to cheatsheet
pick 298dead add merge how-to
pick 43d2f7e add file
pick ca7b5db add first part
pick a2ce5c6 continue tuto
pick d2eb036 updta td gloutons
pick 40900b9 delete erronous line
pick 289eb2a add link to rebase tuto
~~~

Une fois qu'on a tout organisé comme il faut, on va pouvoir passer à l'étape de fusion des commits entre eux. Cela fonctionne un peu à la manière de la coalescence des gouttes d'eau : je peux demander à git de fusionner un *commit* avec celui du dessus. On utilise pour cela `pick` et `squash` : `pick` va conserver un commit, et `squash` va fusionner un commit avec celui juste au-dessus.

~~~ shell
pick 88af96b add extended git rebase tuto
squash 4da9c73 add how to and first cheatsheet lines
squash 7431bbd add last commands to cheatsheet
squash 298dead add merge how-to
pick 43d2f7e add file
squash ca7b5db add first part
squash a2ce5c6 continue tuto
pick d2eb036 updta td gloutons
pick 40900b9 delete erronous line
squash 289eb2a add link to rebase tuto
~~~

On ferme ensuite l'éditeur (en enregistrant bien sûr). Celui-ci va se rouvrir pour que l'on rentre le message de commit du premier groupe de commits (de 88af96b à 298dead, maintenant fusionnés en un seul). On l'écrit, on enregistre et on ferme. L'éditeur se rouvre pour faire de même avec le second groupe, et ainsi de suite. On notera que l'on aurait aussi pu utiliser `fixup`, qui converse le message de commit du commit dans lequel les autres se fusionnent, à la place de `squash`.

Et voilà le résultat, 4 commits au lieu de 10 :

~~~ shell
88af96b add how-to tuto
43d2f7e add atomic commits tuto
d2eb036 updta td gloutons
40900b9 refactor old tutos
~~~


## Conclusion

Les commits atomiques sont un excellent moyen de réorganiser l'historique git, en particulier pour le rendre plus clair pour des relecteurs (ce qui est particulièrement utile sur de gros projets, qu'ils soient internes ou *open source*). Comme on l'a vu, ce n'est absolument pas synonyme de "je pousse plein de petits commits tout le temps", puisque la pratique du commit atomique s'accompagne d'une réorganisation de ces-derniers (encore une fois, pour plus de clarté). Même si cela peut sembler fastidieux à mettre en pratique au début, cela devient rapidement très efficace et rapide à utiliser, une fois qu'on s'est familiarisé avec les outils, et peut réellement augmenter la lisibilité de vos publications et votre clarté mentale.

## Sources et ressources

- [adopteungit.fr](http://adopteungit.fr/methodologie/2017/04/26/commits-atomiques-la-bonne-approche.html)