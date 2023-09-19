---
layout: layout/post.njk

title: Shell scripting DM

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- [python stdin](https://www.digitalocean.com/community/tutorials/read-stdin-python)
- [tuto](https://www.youtube.com/watch?v=tK9Oc6AEnR4)
- [un autre tuto](https://www.youtube.com/watch?v=KG97VzMjfMg)

[quel shebang utiliser](https://www.baeldung.com/linux/bash-shebang-lines)
exemple + DM

<https://www.youtube.com/watch?v=8L7cM4q6TL8>

- curl un fichier puis grep dessus
- donner des ressources (yt, man) pour comprendre les outils utilisés
- shebang. Faire avec python.
- diff entre `/usr/bin/python3` et `/usr/bin/env python3`
- on fait du shell scripting
- <https://dev.to/husseinalamutu/bash-vs-python-scripting-a-simple-practical-guide-16in> : manipulation fichier, bash plus utile que python.

1. exos : prendre un yt pour faire des exos
2. shell script

```
curl https://www.gutenberg.org/cache/epub/1184/pg1184.txt 2>/dev/null | wc
```

https://itslinuxfoss.com/how-parse-json-shell-scripting-linux/

### exo final

1. nb de lignes, mots
2. mettre sur un fichier dans tmp (nom pas encore existant)
3. longueur moyenne de chaque mot avec un awk
4. faire automatiquement dans un script ajouter des options (nb mot, longueur moy, fichier à télécharger ou stdin)
5. et suppression du fichier ensuite

### exo préparatoire

1. récupérer et nb de ligne marseille
2. création d'un script avec boucle
3. json : nombre de villes ?

> <https://www.baeldung.com/linux/csv-parsing>
> <https://www.joeldare.com/wiki/using_awk_on_csv_files>
> <https://www.malekal.com/comment-utiliser-la-commande-awk-avec-des-exemples/>
> <https://linuxhint.com/20_awk_examples/>

## tests ecm

### Fichiers

1. quel est le chemin de votre dossier maison
2. quels sont les fichiers présents ?
3. Quel est la différence entre :
   - `ls`
   - `ls -l`
   - `ls -a`
   - `ls -la`
4. créez un dossier `temporaire` dans votre dossier maison. Quels sont les droits de ce fichier ?
5. affichez la liste des fichiers par date de modification/création (option de `ls`). 
   1. le dossier temporaire devrait être en premier
   2. modifier la date de modification du dernier dossier (grace à la commande touch) et vérifier qu'il est maintenant en premier dans la liste
   3. à quoi sert habituellement la commande touch ?
6. affichez les 3 plus récemment modifié, puis les 5 moins récemment modifié (head et tail)
7. copiez le fichier `/etc/passwd` dans le dossier temporaire de maison et appelez le mot-de-passe en une seule commande
8. supprimez le dossier `temporaire` en une seule commande
9. Créez un dossier `private` dans maison et modifiez ses droit pour qu'il ne soit accessible que de vous même. Faites cette modification en utilisant la notation symbolique.
10. à quoi correspond ces droits en notation octale ?
11. créez un fichier nommé `hello.txt` dans votre dossier maison contenant le texte "bonjour" avec un éditeur de texte (nano par exemple)
12. ajoutez " monde !" à la fin du fichier `hello.txt` avec une commande commande echo
13. déplacez le fichier `hello.txt` dans le dossier `private`
14. créez un lien symbolique dans votre maison vers le fichier `hello.txt` de votre dossier private.
15. modifiez le contenu du fichier symbolique pour qu'il ne fasse plus qu'une seule ligne
16. afficher  avec un cat le contenu du fichier dans `private/hello.txt`
17. que se passe-t-il si vous supprimer le fic hier originel du lien ?
18. créez avec nano un fichier nommé `brise marine.txt` et mettez-y le poème le Mallarmé
19. affichez ce fichier avec cat puis déplacez le dans votre dossier private
20. renommez le fichier `brise_marine.txt`

### Process

1. lister tous les process de tous les utilisateurs
2. les compter (avec wc)
3. comptez uniquement les process de root puis les vôtres (avec un grep)
4. deux terminaux, ouvrir un nano et le tuer depuis une autre fenêtre

### Sur une machine de l'ecm

#### connections

1. connectez-vous tous sur la même machine de l'ecm avec l'url <https://machines.centrale-marseille.fr/#/>, et ouvrez un terminal.
2. vérifiez que vous êtes tous connecté sur cette machine (who, w, users)
3. créez un fichier vide de nom votre prénom dans le dossier `/tmp` (faite le avec la commande touch)
4. essayez de supprimer un fichier créé par un de vos camarades
5. vous devriez avoir un groupe en commun : commande `groups` ou `id -a`
6. Modifiez les droits de votre fichier dans /tmp pour que son groupe soit le groupe que vous avez en commun et permettez son écriture.
7. Modifiez le contenu d'un fichier de votre voisin en y ajoutant votre nom
8. connectez vous sur le sas1 depuis votre machine perso avec ssh
9. depuis cette machine connectez vous sur la même machine que celle sur laquelle vous êtes connectés depuis <https://machines.centrale-marseille.fr/#/>
->Il faut vous "passer" par un sas / vous connecter sur sas1.centrale-marseille.fr en utilisant un protocole securise (ssh/scp/sftp)
54-AVEC L'ACCORD DE VOTRE VOISIN !!!!
   Connectez vous sur sa machine ( commande ssh son_login@nom_de_sa_machine ) et reciproquement.
   Tuez tous ses processes et reciproquement
   jusqu'a ce que l'un de vous deux soit deloggue.

#### web

Vous avez un repertoire html sur votre compte.
Tout ce qui est place dans ce repertoire est accessible via le serveur web.
Vous pouvez donc l'utiliser pour creer votre site perso ou tout simplement pour mettre a disposition certains fichiers.


Verifiez que tout fonctionne:
  a)lancez le navigateur/browser web 
		$firefox 
  b)verifiez que vous accedez a votre espace web perso sous la forme http://prenom.nom.perso.centrale-marseille.fr
---> Notez les autres facons d'acceder a ce meme espace web.

Le principe est simple:
 Tout ce qui est precise apres http://prenom.nom.perso.centrale-marseille.fr est relatif a votre repertoire html.
 Ainsi http://prenom.nom.perso.centrale-marseille.fr/toto.txt  designe le fichier toto.txt qui est dans votre repertoire html (~/html/toto.txt)
 	http://prenom.nom.perso.centrale-marseille.fr/a/b/c/d/tutu.txt designe le fichier qui est dans votre repertoire ~/html/a/b/c/d	 

copiez avec scp depuis votre ordi jusqu'au sas1 le fichier brise marine et placez le dans html pour que tout le monde puisse l'admirer.

Faites en sorte de rendre le sujet de ce TP (TP12) disponible sur internet sous la forme  http://prenom.nom.perso.centrale-marseille.fr/brise_marine.txt

Récupérez le chez vous avec curl


28-Deplacez le fichier ~/html/brise_marine.txt dans le repertoire ~/html/visible  
29-Essayez de voir le contenu de ce repertoire via le navigateur.
Quelle difference de fonctionnement avec le cas precedent ? 

30-Deplacez le fichier  ~/html/visible/coursunix dans le dossier ~/html/intranet
31-Quelle difference de fonctionnement avec les 2 cas precedents ?

32-En conclusion, Que devez vous faire pour:
	-mettre a disposition du monde entier ce magnifique fichier
	-mettre a disposition d'un membre de votre famille un document confidentiel ?
  > TBD : faire Un dossier mot de passe
	-mettre a disposition du service stages votre rapport ?



### TP 2

récupérer le projet avec avec git.
trouver le fichier je-suis-le-corrigé-du-dm-unix (avec un find)

ce fichier est codé en base64. décodez le.

trouver les fichier qui ont été modifié il y a moins de 7 jours (find . -mtime +30 -print)

Determinez quel est le plus gros repertoire des sources du projet (docs/src),(du -h | sort -h | tail)


---- A FAIRE APRES LE COURS 3 ----

### autre

52-Creez les aliases ll ld latr correspondants aux commandes ls -l, ls -ld , ls -latr.
   Profitez en pour creer d'autres aliases que vous jugerez opportuns.

1. faire un script shell qui affiche bonjour $1
2. qui ajoute à la fin de chaque ligne une nouvelle ligne "putaing cong !" en lisant un fichier.
3. - en $!
4. en stdin
5. si pas de $1 stdin
6. modifiez pour qu'il puisse faire en alsacien em mettant "Hopla," au début de chaque ligne.
7. Avec une option faite en sorte que l'on puisse choisir décrire en alsacien, toulousain ou aucun.
8. ajoutez ce super script script shell  .local/bin  faites en sorte que ce soit appelable en modifiant le path.


### TP 3

faire avec du json sur les villes. ou les naissances des français.jq

15/Affichez les login Prenom Nom des eleves  de la promo2012 triee selon leur nom ( c.f fichier passwd.2012 )
16/Comptez combien d'eleves se prenomment julien 

créer un fichier texte à awker. Puis sort puis uniq

La commande $ awk -F "delimiteur" '{print $NF}'  < fichier permet d'afficher le dernier champ d'une ligne, en precisant le delimiteur 
17/Affichez tous les prenoms de tous les utilisateurs
18/Triez par ordre alphabetique ces prenoms
La commande $ uniq -c < fichier permet d'afficher le nbre d'occurences de lignes identiques consecutives
19/Affichez le nombre d'occurence de chaque prenom
20/Affichez le Top 5 des prenoms les plus usuels
21/idem en limitant aux eleves
22/idem en limitant aux personnels 
 