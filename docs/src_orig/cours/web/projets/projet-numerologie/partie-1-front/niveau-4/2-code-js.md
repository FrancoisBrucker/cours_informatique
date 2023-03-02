---
layout: layout/post.njk 
title:  "Projet numérologie : partie 1 / niveau 4 / code"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numérologie/index.md %}) / [partie 1]({% link cours/web/projets/numérologie/partie-1-front/index.md %}) / [niveau 4]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/index.md %}) / [code]({% link cours/web/projets/numérologie/partie-1-front/niveau-4/2-code-js.md %})
{.chemin}

Nous allons après chaque tâche faire un commit et, à la fin de chaque étape envoyer les modifications sur le serveur.

> Un commit doit être de taille raisonnable et, si possible, ne concerner qu'une seule tâche.

Le message de commit (obligatoire) est très important lorsque l'on fera l'historique du projet. De pus, il faut savoir qui a fait quoi et pouvoir le contacter au besoin : votre nom et mail *doivent* être correct

> le nom utilisé dans un commit reste toute la durée de vie du projet (et ça peut être très long). Donc gardez votre nom réel, il est peu probable que vous ayez à en changer.

## log

L'historique sous git est donné par les logs. La [documentation de git sur les log](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) donne de nombreuses options pour voir l'hisorique de son projet. 

Si par exemple je tape `git log` dans un terminal, j'obtient :

```text
commit 83830d1fbb28d9e8fb1e437bbd325ffebccdeceb (HEAD -> main, tag: niveau1-2, origin/main, origin/HEAD)
Author: François Brucker <francois.brucker@gmail.com>
Date:   Tue Oct 12 15:47:13 2021 +0200

    ajout des tests

commit f96dd16e9271804bd4f8afd2f1b01a6a6ec3740f (tag: niveau1-1)
Author: François Brucker <francois.brucker@gmail.com>
Date:   Tue Oct 12 15:30:45 2021 +0200

    Update README.md

commit 75c256df635b91dc15abfee83e897aeed05371d1
Author: François Brucker <francois.brucker@gmail.com>
Date:   Tue Oct 12 15:18:20 2021 +0200

    Initial commit
```

Du haut en bas on remonte l'histoire de notre (court) projet.

> J'ai ajouté des [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging)qui permettent de fixer des endroits dans le projet  aux 2 dernières commits : les débuts de chaque partie.

## tâche 1

Il n'y a pas de fichier écrit, donc aucune raison de faire de commit.

## tâche 2

On implémente la [tâche 2 du niveau 1]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/2-code_js.md %}#tache-2)

Un `git status` à la fin de cette tache donne :

```text
Sur la branche main
Votre branche est à jour avec 'origin/main'.

Fichiers non suivis:
  (utilisez "git add <fichier>..." pour inclure dans ce qui sera validé)
	numérologie.js

aucune modification ajoutée à la validation mais des fichiers non suivis sont présents (utilisez "git add" pour les suivre)

```

On a un fichier non suivi (*numérologie.js*). On procède à notre petit workflow habituel :
1. `git add --all`poura ajouter *"numérologie.js"* à notre projet
2. un `git status` nous indique maintenant qu'on a un fichier dans le stage, c'est à dire dans l'endroit où sont consignés les modifications à commiter.
3. On commit `git commit -am"add file numérologie.js"

Après ce commit, un `git status`  nous indique que l'on est 1 commit plus loin que l'origin.

>Ce n'est que sa connaissance de l'origine (la dernière fois qu'on a push), il n'est pas allé le vérifier. POur le faire, on utilise la commande `git fetch` qui récupère l'état de l'origin. Si on le fait là il n'y aura pas de modification puisque l'on a rien fait sur le serveur.
{.attention}

Nous n'allons pas pousser tout de suite nos changement sur le serveur. On va attendre d'avoir fait des changements significatifs dans le code.

> Ne poussez pas chaque commit sur le serveur. Attendez d'avoir fait des changements significatifs. Mais commitez tout de même au moins 1 fois par jour sur le serveur (règle au doigt mouillé), pour montrer vos progrès au reste de l'équipe.

## tâches 3 et 4

On implémente les [tâche 3 du niveau 1]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/2-code_js.md %}#tache-3) et [tâche 4 du niveau 1]({% link cours/web/projets/numérologie/partie-1-front/niveau-1/2-code_js.md %}#tache-4).

Le `git status` après ces étapes montre que nous avons 1 changements : la modification du fichier *"numérologie"*.

Si l'on veut voir les changements on peut taper la commande `git diff`. 

Chez moi elle donne :

```text
diff --git a/numérologie.js b/numérologie.js
index f7f51ed..c039bbc 100644
--- a/numérologie.js
+++ b/numérologie.js
@@ -1,11 +1,29 @@
 function nombre(chaine) {
     var somme = 0
-    for (var i=0; i < chaine.length; i++) {
+    for (var i = 0; i < chaine.length; i++) {
         somme += chaine.charCodeAt(i)
     }
     return somme
 }
 
+function somme(nombre) {
+    var somme = 0
+    chaine = String(nombre)
+    for (var i = 0; i < chaine.length; i++) {
+        somme += parseInt(chaine.charAt(i))
+    }
+    return somme
+}
+
+function chiffreAssocie(chaine) {
+    valeur = nombre(chaine)
+
+    while (valeur > 9) {
+        valeur = somme(valeur)
+    }
+    return valeur
+}
+
 // test de nombre(chaine)
 
 // est-ce 2x plus ?
@@ -13,7 +31,28 @@ console.log(nombre("cou"))
 console.log(nombre("coucou"))
 
 // chaque caractère :la somme est-elle correcte ?
-for (c of "cou") { 
+for (c of "cou") {
     console.log(c + " : " + nombre(c))
 }
 // fin de test de nombre(chaine)
+
+// test de somme(nombre)
+console.log(somme(132))
+
+// avec un chiffre : charAt != charCodeAt
+console.log(somme(4))
+console.log("4".charCodeAt(0))
+console.log("4".charAt(0))
+
+// conversion chaine de caracteres et nombre
+console.log(typeof "4".charAt(0))
+console.log(parseInt("4".charAt(0)))
+console.log(typeof parseInt("4".charAt(0)))
+// fin de test de somme(nombre)
+
+// test de chiffreAssocie(chaine)
+
+//test valeur somme des chiffres
+console.log(nombre("coucou"))
+console.log(chiffreAssocie("coucou"))
+// fin de test de chiffreAssocie(chaine)
```

Cette commande montre les différences entre les deux fichiers numérologie.js : celui actuel sur notre disque dur et celui du précédent commit.

> la commande diff vient souvent avec la commande patch qui permet de transformer un fichier en un autre en utilisant le résultat de diff. Pour nous c'est git qui fera cette opération nous n'utiliserons donc pas patch directement. Pour plus d'infos sur diff et patch [suiverz le tuto](https://wiki.debian-fr.xyz/Utiliser_diff_et_patch)

git ne va stocker que les différences entre les fichiers et pas tous les fichiers à chaque commit, cela permet de gagner de la place.

On peut maintenant commit nos changements : `git commit -am"rend un chiffre à partir d'une chaine de caractères"`

Le résultat est :
```text
[main e8e3c30] rend un chiffre à partir d'une chaine de caractères
 1 file changed, 41 insertions(+), 2 deletions(-)
 ```

 Les insertions et les délétions sont les insertions et délétions du diff précédent.

Un `git status` nous informe qu'on est 2 commit plus loin que l'origine.

## modification d'un fichier depuis le site de github

Pour illustrer le `git fetch` et l'état du serveur allons sur la page github de notre projet et modifions le fichier *"README.md"*.

Pour cela on clique sur le fichier puis on l'édite :

```text
# numérologie

Voyez la vie en base 10 en associant un chiffre à votre prénom.
```

Puis on commit nos changements en appuyant sur le bonton vert *commit changes*

De retour sur mon ordinateur, j'essaie de pousser mes 2 commits d'avance sur le serveur avec un `git push` et on ne me laisse pas faire :

```text
To github.com:FrancoisBrucker/numérologie.git
 ! [rejected]        main -> main (fetch first)
error: impossible de pousser des références vers 'github.com:FrancoisBrucker/numérologie.git'
astuce: Les mises à jour ont été rejetées car la branche distante contient du travail que
astuce: vous n'avez pas en local. Ceci est généralement causé par un autre dépôt poussé
astuce: vers la même référence. Vous pourriez intégrer d'abord les changements distants
astuce: (par exemple 'git pull ...') avant de pousser à nouveau.
astuce: Voir la 'Note à propos des avances rapides' dans 'git push --help' pour plus d'information.
```

Faisons un `git fetch` (on récupère l'état du serveur) puis un `git status` pour voir ce qu'il se passe :

```text
Sur la branche main
Votre branche et 'origin/main' ont divergé,
et ont 2 et 1 commits différents chacune respectivement.
  (utilisez "git pull" pour fusionner la branche distante dans la vôtre)

rien à valider, la copie de travail est propre
```

## synchronisation des dossiers

On a maintenant quelque chose qui se passe souvent lorsque l'on code à plusieurs :

* j'ai avancé de mon côté (j'ai 2 commit qui n'ont pas encore été mis sur le serveur)
* le serveur a avancé de son côté et à 1 commit de plus que le serveur que je connais.

Ca donne quelque chose comme ça au niveaux des commit :

```text
  D : le commit du serveur
 /
A - B - C : mes commits
```

Il faut remettre tout ça à l'endroit. L'usage veut que l'on continue **toujours** depuis ce qu'il y sur le serveur. Il faut donc que l'on arrive à quelque chose du style :

```text
A - D - B' - C' : mes commits
```

Avant de repousser le tout sur le serveur.

Mes commits sont `B'` et `C'` puisque je dois les écrire depuis un code qui fait `D` alors que `B` et `C` ont été écrit depuis un code qui était À`.

C'est exactement ce qu'il va se passer si vous avez fait les [configurations nécessaires]({% link cours/git_et_github/index.md %}#configuration) :

1. on récupère les commits du serveur avec un `git pull`. Vous devriez obteir ce message `Rebasage et mise à jour de refs/heads/main avec succès.` ce qui est encourageant.
2. tout est maintenant ok, on push sur le serveur : `git push`.

Git nous informe que tout est ok :

```text
Sur la branche main
Votre branche est à jour avec 'origin/main'.

rien à valider, la copie de travail est propre
```

Notre serveur et notre ordinateurs sont synchronisés !

L'opération de rebrancher tout sur le serveur ne se passe pas toujours aussi bien. Il faudra alors [résoudre à la main les conflits](https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase).
