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

> TBD à mettre lorsque l'on ssh


## Personnalisation


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
