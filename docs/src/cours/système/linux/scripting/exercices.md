---
layout: layout/post.njk

title: Exercices

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Fichiers

1. Quel est le chemin de votre dossier maison
2. Quels sont les fichiers présents ?
3. Quel est la différence entre :
   - `ls`
   - `ls -l`
   - `ls -a`
   - `ls -la`
4. Créez un dossier `temporaire`{.fichier} dans votre dossier maison. Quels sont les droits de ce fichier ?
5. Affichez la liste des fichiers par date de dernière modification/création (c'est une option de `ls`). Le dossier `temporaire`{.fichier} devrait être en premier.
6. Modifier la date de modification du dossier modifié le dernier (grace à la commande `touch`) et vérifier qu'il est maintenant en premier dans la liste
7. Que fait `touch fichier` si `fichier`{.fichier} n'existe pas ?
8. Affichez les 3 éléments plus récemment modifiés, puis les 5 moins récemment modifié (vous pouvez utiliser les commandes `head` et `tail`)
9. Copiez le fichier `/etc/passwd` dans le dossier `${HOME}/temporaire`{.fichier} créé précédemment et appelez le mot-de-passe, le tout en une seule commande
10. Supprimez le dossier `${HOME}/temporaire`{.fichier} en une seule commande `rm`
11. Créez un dossier `private` dans maison et modifiez ses droits pour qu'il ne soit accessible que de vous même. Faites cette modification en utilisant la notation symbolique.
12. À quoi correspondent ces droits en notation [octale](https://docs.oracle.com/cd/E19504-01/802-5750/6i9g464pv/index.html) ?
13. Créez un fichier nommé `hello.txt` dans votre dossier maison contenant le texte "bonjour" avec un éditeur de texte (nano par exemple)
14. Ajoutez " monde !" à la fin du fichier `hello.txt` avec une commande commande echo
15. Déplacez le fichier `hello.txt` dans le dossier `private`
16. Créez un lien symbolique dans votre maison vers le fichier `hello.txt` de votre dossier private.
17. Modifiez le contenu du fichier symbolique pour son contenu soit sur une seule ligne (vous pourrez vous aider de la commande `tr` et de [ce tutoriel](https://www.baeldung.com/linux/join-multiple-lines))
18. Afficher, avec la commande `cat`, le contenu du fichier dans `private/hello.txt`
19. Que se passe-t-il pour le lien si vous supprimez ou renommez le fichier original ?
20. Créez avec `nano` un fichier nommé `brise marine.txt`{,.fichier} et mettez-y le [poème de Mallarmé](https://www.poetica.fr/poeme-109/stephane-mallarme-brise-marine/)
21. Affichez ce fichier avec la commande `cat` en [escapant](https://www.shellscript.sh/escape.html) le métacaractère espace
22. renommez, avec la commande `mv` le fichier `brise marine.txt`{.fichier} en `brise_marine.txt`{.fichier}

## Personnalisation

Le fichier `.bashrc`{.fichier} crée un alias `ll`. À quoi cela correspond-t-il ?

Créez dans un shell les deux alias suivant :

- `cd..` pour `cd ..`
- `cd...` pour `cd ../..`.

Le fichier de configuration `.bashrc`{.fichier} tente d'exécuter un fichier dédié aux alias. Lequel ? Ajoutez y vos deux nouveaux alias pour qu'ils soient toujours disponible.

## find

[find](https://shapeshed.com/unix-find/)
trouver les fichiers qui ont été modifié il y a moins de 7 jours (find . -mtime +30 -print)

Déterminez quel est le dossier contenant le plus de méga de votre système.(du -h | sort -h | tail)

## Process

1. Lister tous les process de tous les utilisateurs (avec la commande `ps` et ses options)
2. Les compter (avec la commande `wc`)
3. Comptez uniquement les process de root puis les vôtres (avec l'aide de la commande `grep`)
4. À l\aide de deux terminaux :
   1. ouvrir un `nano` dans lun,
   2. à l'aide de son PID, tuer le process `nano` dans l'autre terminal.

## Sur une machine de l'ecm

### Connection aux sas

En groupe.

Pour vous connecter à une machine d'un réseau local, il faut souvent se connecter à un sas, le seul qui a une adresse internet réelle. Pour les étudiants de l'ecm cette machine s'appelle `sas1.ec-m.fr`. Une fois connecté sur le sas, il est possible de se connecter à toute autre machine allumé du réseau.

1. Connectez-vous tous sur la même machine de l'ecm :
   1. Si vous êtes sur votre propre machine, commencez par vous connecter sur la machine `sas1.ec-m.fr` avec la commande `ssh` (`ssh son_login@nom_de_sa_machine`).
   2. De la machine `sas1.ec-m.fr` connectez vous tous sur la même autre machine.
2. Vérifiez que vous êtes tous connecté sur cette machine (commandes `who`, `w` ou encore `users`)
3. cCréez un fichier vide de nom votre prénom dans le dossier `/tmp` (faite le avec la commande `touch`)
4. Essayez de supprimer un fichier créé par un de vos camarades
5. Vous devriez avoir un groupe en commun : commande `groups` ou `id -a`
6. Modifiez les droits de votre fichier dans `/tmp`{.fichier} pour que son groupe soit le groupe que vous avez en commun et permettez son écriture.
7. Modifiez le contenu d'un fichier de votre voisin en ajoutant votre nom à la fin de son contenu
8. Connectez-vous depuis un autre terminal de votre machine perso sur le `sas1.ec-m.fr`.
9. Trouve le PID de la première connection et tuez là. La mort de ce process a tué tous ses enfants, y compris la connection sur l'autre machine allumée de l'ecm.
10. Créez un dossier `~/private/`{.fichier} uniquement lisible par vous mais exécutable par tout le monde. Tout le monde peut donc entrer dans `~/private/`{.fichier} mais pas lire son contenu
11. Créez dans `~/private/`{.fichier} un dossier avec un nom secret. Donnez les droits d'écriture à tout le monde à ce dossier
12. demandez à votre voisin de placer un fichier dans ce dossier. Il peut le faire s'il connaît le nom secret, mais il lui est impossible de lire le contenu du dossier `~/private/`{.fichier}.
    1. comment est-ce possible ?
    2. comment peut-on utiliser cette technique ?

### Web

Vous avez un répertoire `html`{.fichier} sur votre compte. Tout ce qui est placé dans ce répertoire est accessible via le serveur web de l'école. Vous pouvez donc l'utiliser pour créer votre site perso ou tout simplement pour mettre a disposition certains fichiers.

Vérifiez que tout fonctionne :

1. lancez le navigateur/browser web `firefox`
2. vérifiez que vous accédez a votre espace web perso sous la forme <http://prenom.nom.perso.centrale-marseille.fr>

Le principe est simple : tout ce qui est précisé apres <http://prenom.nom.perso.centrale-marseille.fr> est relatif a votre repertoire `~/html`{.fichier}. Ainsi <http://prenom.nom.perso.centrale-marseille.fr/toto.txt> désigne le fichier `toto.txt`{.fichier} qui est `~/html/toto.txt`{.fichier}

1. À quel fichier correspond l'url <http://prenom.nom.perso.centrale-marseille.fr/a/b/c/d/tutu.txt> ?
2. Copiez avec [la commande `scp`](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/) depuis votre propre ordinateur jusqu'au dossier `~/html/` de l'ordinateur `sas1.ec-m.fr` le fichier `brise_marine.txt`.
3. Vérifiez que `brise_marine.txt` est bien accessible depuis votre site personnel de l'ecm.
4. Téléchargez `brise_marine.txt` avec la commande [`curl`](https://www.youtube.com/watch?v=APtOavXTv5M&list=PLShDm2AZYnK1SdG3dufPdCqk08sOahUBP&index=9)
5. Déplacez le fichier `~/html/brise_marine.txt`{.fichier} dans le répertoire `~/html/visible`{.fichier}
6. Essayez de voir le contenu de ce repertoire via le navigateur. Quelle difference de fonctionnement avec le cas precedent ?
7. Déplacez le fichier `~/html/visible/brise_marine.txt`{.fichier} dans le dossier `~/html/intranet`.
8. Quelle difference de fonctionnement avec les 2 cas precedents ?
9. Une url peut être utilisée comme un mot de passe pour accéder à une ressource puisqu'il est impossible **depuis l'extérieur** de connaître toutes les url accessibles. En revanche pour une personne connectée au réseau, elle peut visiter l'arborescence de `~/html/`. Comment protéger les fichier à cacher tout en les laissant accessible de l'extérieur ?

## Que fait ça ?

Vu dans un fichier de configuration d'un nouvel utilisateur :

```shell
password=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)
```

> TBD en ajouter d'autres
