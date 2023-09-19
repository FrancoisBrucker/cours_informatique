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

### TP 1

##############################
# unix - TP 1 - Olivier Pagé #
##############################

1-Quel est votre Home directory ?
2-Qu'y a t il dans votre Home directory ?
3-Copier le fichier a-supprimer en .a-supprimer
4-Qu'y a-t-il desormais dans votre home directory ?; pourquoi ne voit on pas le fichier .a-supprimer ?
5-Quelle(s) option(s) permet(tent) de voir VRAIMENT TOUT ce qu'il y a dans votre home directory
6-Effacer le fichier nommé a-supprimer qui se trouve dans votre repertoire personnel (homedirectory) 
(vous verrez plus tard l'interet de cette étape)
7-Quelle(s) option(s) permet(tent) de voir toute l'arborescence du repertoire html ?
8-Quel est  l'ordre d'affichage par defaut ?
9-Comment afficher les derniers fichiers modifiés/crées en premier/dernier ?
(sort veut dire trier ...)


10- Creez un repertoire nomme coursunix dans votre "home directory"
11- Creez un repertoire nomme bidon dans le repertoire coursunix
12- Effacez bidon
13- Effacez coursunix

14-creez en une seule commande le(s) repertoire(s) coursunix/bidon/tp1
15-copiez dans ce rep tp1 le fichier .a-supprimer
16-effacez le rep tp1; quel est le probleme ? quelle(s) option(s) de rm permet d'effacer un rep et tout ce qu'il contient




Aller dans le repertoire /tmp
En restant dans /tmp 
18-effacez le repertoire bidon cree en 14
19-creez un repertoire nomme cours1 dans le repertoire coursunix


20-copiez le rep bidon (et tout ce qu'il contient) qui est dans le rep coursunix de l'utilisateur olivier  dans votre repertoire coursunix
21-Copiez tous les fichiers dont le nom commence par les lettres comprises entre c et l  qui sont dans le repertoire coursunix de l'utilisateur olivier dans un repertoire cours1 situe dans votre repertoire coursunix ...
22-idem mais en copiant tous les fichier ET repertoires dont le nom commence par les lettres comprises entre c et l
 
23-Copiez le fichier nomme -avec des espaces- du meme endroit que precedemment dans ce meme repertoire cours1


L'infrastructure informatique de l'etablissement vous permet d'acceder vous meme aux sauvegardes automatiques.
Ces sauvegardes ont lieu a 8,10,12,14,16,18 heures chaque jour, chaque nuit a minuit, ainsi que chaque dimanche.
Chaque repertoire contient un repertoire .snapshot dans lequel vous trouverez les sauvegardes effectuées.
La sauvegarde la plus récente se nomme xxxx.0, xxxx pouvant etre hourly, daily ou weekly.
24-Recuperez le fichier a-supprimer que vous avez supprimé au point 6- et recopiez le dans votre homedirectory.
ATTENTION: Si il n'a jamais ete sauvegarde dans les snapshots. Effacez un fichier ou un repertoire sur votre compte et essayez de retrouver ce fichier ou repertoire dans le snapshot le plus recent.

 

------
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


25-Faites en sorte de rendre le sujet de ce TP (TP12) disponible sur internet sous la forme  http://prenom.nom.perso.centrale-marseille.fr/TP12

26-Recuperez le fichier logcri.jpg qui vous voyez dans votre navigateur avec l'URL http://olivier.page.perso.centrale-marseille.fr/logcri.jpg et faites en sorte de le rendre accessible par internet avec l'URL de la forme http://prenom.nom.perso.centrale-marseille.fr/logcri2.jpg  


27-Creez un repertoire coursunix dans votre repertoire html, copiez le fichier logcri.jpg dedans.
28-Essayez de voir le contenu de ce repertoire via le navigateur.
Que faut il (URL) donc communiquer a votre interlocuteur pour qu'il accede a ce document via le web ?
--> Le contenu des repertoires crees dans votre espace web n'est pas visible par defaut pour des raisons de confidentialite.


28-Deplacez votre repertoire ~/html/coursunix/ dans le repertoire ~/html/visible  
29-Essayez de voir le contenu de ce repertoire via le navigateur.
Quelle difference de fonctionnement avec le cas precedent ? 


30-Deplacez le repertoire ~/html/visible/coursunix dans le repertoire ~/html/intranet
31-Quelle difference de fonctionnement avec les 2 cas precedents ?

32-En conclusion, Que devez vous faire pour:
	-mettre a disposition du monde entier ce magnifique sujet de TP ?
	-mettre a disposition d'un membre de votre famille un document confidentiel ?
	-mettre a disposition du service stages votre rapport ?

### TP 2


1-Quels sont les droits de votre repertoire html ?
2-Quelle(s) option(s) vous permettent d'afficher les informations relatives aux repertoires sans afficher leur contenu   ?
3-a)Quelles options utiliser pour afficher par ordre chronologique tous les fichiers de votre home directory ainsi que leurs dates de modification ?
3-b)et dans l'ordre inverse ?

4-Copiez le rep bidon (et tout ce qu'il contient) qui est dans le rep coursunix de l' utilisateur olivier  dans votre repertoire coursunix
5-Comment expliquer ce(s) message(s) d'erreur  ?

6-Verifiez les droits du repertoire private qui est sur votre compte. 
7-Concluez sur l'usage qui peut en etre fait. 

8-Faites en sorte que le repertoire coursunix qui est sur votre compte ne soit accessible que par vous meme
a)en utilisant la notation symbolique
b)en utilisant la notation octale


9-Faites en une copie nommee coursunix2 
10-Changez les droits des fichiers de ce repertoire tels que:
	vous avez tous les droits
        le groupe promo2013 peut les lire
        les autres n'ont aucun droit
11-Donnez ce repertoire au groupe "tdunix" dont vous faites partie (id -a pour verifier a quels groupes vous appartenez)
12-Quelle option vous permet de changer tous les droits de tous les fichiers et repertoires d'un repertoire  

13-Changez les droits de votre repertoire html pour empecher "qui que ce soit a part vous meme" de regarder ce qu'il contient. Verifiez que vous pouvez tjrs y acceder par le web.

14-Creez le repertoire TD2 dans votre repertoire coursunix2
15-Donnez pour ce repertoire tous les droits a votre promotion
16-Copiez dans ce repertoire les fichiers fic1 et fic2 situes dans le repertoire coursunix de l'utilisateur olivier
17-Verifiez les droits de ces deux fichiers
18-Demandez � votre voisin de supprimer le fichier fic1. Qu'en conlure ?
19-Demandez � votre voisin de copier les fichiers fic1 et fic2 situes dans le repertoire coursunix de l'utilisateur olivier dans votre repertoire TD2.Qu'en conclure ?
20-Effacez ces 2 fichiers.

21-Creez l'archive compressee du repertoire coursunix2 et nommez la coursunix.tar.gz
22-"Donnez" (via votre espace web par exemple) cette archive compressee a votre binome ou voisin qui devra l'extraire sur son compte ... et reciproquement.
23-Effacez tout ce qui a ete extrait. effacer l'archive compressee

24-Copiez le fichier TP12 du repertoire coursunix de l'utilisateur olivier dans votre repertoire coursunix.
   Creez un lien nomme TP12 dans votre home directory qui pointe sur le fichier TP12 de votre repertoire coursunix 
25-changez les droits de ce lien pour supprimer tous droits aux autres utilisateurs 
26-quel est l effet de la commande chmod sur un lien ?
27-effacez le lien
28-quel est l effet de la commande rm sur un lien 
29-Creez un lien nomme musique qui pointera sur le repertoire Musik de l'utilisateur etchalikokia 
30-Pour ceux qui sont dans une salle unix: ecoutez un morceau de musique situe dans ce repertoire si vous avez un casque ou des enceintes !!
(mpg123 fichier_son ou play fichier_son ou xmms fichier_son)  


SI IL VOUS RESTE MOINS DE 45mn AVANT LA FIN DE LA SEANCE ALLEZ DIRECTEMENT A LA QUESTION 38 EN LISANT TOUTEFOIS LE PARAGRAPHE INTRODUCTIF 

31-affichez/cherchez tous les fichiers et repertoires situ�s dans le repertoire coursunix de l'utilisateur olivier 
a)nommes  -avec des espaces-
b)plus recents que le fichier TP12
c)qui ont plus de 10 jours
d)moins de 10 jours
e)10 jours

32-Creez un repertoire coursunix2 dans votre homedirectory
33-Creez dans ce repertoire coursunix2 un lien nomme coursunix qui pointera sur le repertoire coursunix qui est chez olivier
34-Grace a ce lien, copiez dans ce repertoire coursunix2 le fichier passwd.2013 qui est chez olivier dans le repertoire coursunix.
35-Effacez le repertoire coursunix2 cree en 32- 

36-Determinez quel est le plus gros repertoire de votre compte, repertoires caches compris. La commande est $du. Aidez vous du man .... )
37-Quel est le plus gros fichier de ce reprtoire (fichier caches compris).


Connexion vers/de l'exterieur - Les regles:
-Vous pouvez vous connecter vers n'importe quelle machine exterieure depuis les machines situ�es dans le campus
-Vous ne pouvez pas vous connecter directement depuis l'exterieur sur une machine situ�e dans le campus. 
->Il faut vous "passer" par un sas / vous connecter sur sas1.centrale-marseille.fr en utilisant un protocole securise (ssh/scp/sftp)


38-Connectez vous sur la machine distante ii.dgeos.net (qui est situ�e dans un datacenter � Paris) en tant qu'utilisateur coursunix (man ssh)
Le Mot de passe est tres long et tres difficile=Mdptl&td 
39-Profitez en pour "voir" qui est connect� en meme temps que vous.
40-Il y a sur ce compte une archive compressee. Trouvez la. ATTENTION: ELLE N EST PAS DANS LE REPERTOIRE tmp !!!!
41-Creez un repertoire a votre nom sur cette machine dans le repertoire tmp du homedirectory de l'utilisateur coursunix ....
42-Decompressez cette archive dans le repertoire que vous venez de creer.
43-Recuperez cette archive (man scp) afin de la copier sur votre compte ECM  
44-Verifiez que vous savez extraire tout ce qu'il y a dans cette archive et utiliser tous les fichiers 	
(voir les images: $display fichier, ecouter de la musique: $mpg123 fichier, editer un fichier texte: $nedit fichier)
(en cas de doute sur le type d'un fichier: $file fichier) 


---- A FAIRE APRES LE COURS 3 ----

Revenez sur votre machine !!!!
45-Retrouvez le fichier il.est.la situe qqpart sur le compte de l'utilisateur gt 
46-Copiez le dans votre repertoire coursunix
47-Lancez ce programme il.est.la . Il doit afficher "C est tout bon".
 Regardez ce que contient ce fichier. Reflechissez. Concluez......Essayez encore ....
48-Faites en sorte de pouvoir lancer tous les programmes situes dans votre repertoire courant sans specifier de chemin.
49-Creez un repertoire bin dans votre home directory. Faites en sorte de toujours pouvoir lancer les programmes situes dans ce repertoire sans specifier de chemin.

50-Recopier le fichier main.c du rep coursunix habituel dans votre repertoire.
   Lancer la commande $ cc  main.c -o main -lm (sans vous soucier du sens de ctte commande)
   Lancer maintenant le programme main dans une fenetre.  
   Dans une autre, evaluez la charge ( %CPU + taille memoire ) 
   Suspendez le process sans le tuer. Observer dans la fenetre top ce qu'il devient.
   Passez ce process en tache de fond.
51-Copiez l'executable main en main2 main3 main4. Lancez ces 4 process.  evaluez la charge ( %CPU + taille memoire ) 
   Rendez le process main4 plus prioritaire que les autres, verifiez
   Tuez les d'une autre fenetre. 

52-Creez les aliases ll ld latr correspondants aux commandes ls -l, ls -ld , ls -latr.
   Profitez en pour creer d'autres aliases que vous jugerez opportuns.

53-Executez "dans 3 minutes" la commande permettant de 
   copier le fichier "il.est.la"  chez gt sur votre compte sous le nom "il.est.chez.moi". 
   Verifiez que tout c'est bien passe

54-AVEC L'ACCORD DE VOTRE VOISIN !!!!
   Connectez vous sur sa machine ( commande ssh son_login@nom_de_sa_machine ) et reciproquement.
   Tuez tous ses processes et reciproquement
   jusqu'a ce que l'un de vous deux soit deloggue.

-----


### TP 3


1/Listez de maniere detaillee tous les fichiers du repertoire coursunix de l'utilisateur olivier, page par page
2/Comptez le nombre de fichiers et repertoire du repertoire coursunix de l'utilisateur olivier
3/Listez tous les liens (et uniquement ceux ci) dans votre repertoire 
4/Creez defintivement l'alias lsl correspondant
5/Listez tous les fichiers et repertoires qui n'ont pas les droits par defaut (755 pour les rep et 644 pour les fichiers
(changez les droits d'un fichier ou repertoire si necessaire pour verifier)
6/creez l'alias lsmod correspondant
7/Listez tous les process qui vous appartiennent.
8/Definissez un alias xgrep qui ne liste que les processes qui contiennent la chaine passee en argument.
	ex:	$xgrep olivier pour afficher les process qui appartiennent a olivier (entre autres)	
		$xgrep firefox pour n'afficher que les process qui contiennent firefox dans leur nom

9/creez l'alias qui permet de lister par ordre croissant de taille tout ce qu'il y a dans votre homedirectory

Le fichier quotas.2012 contient toutes les informations relatives a l'utilisation de l'espace de stockage pour tous les utilisateurs.
Le 5eme champ correspond a l'espace utilise
Le 6eme champ correspond au quota affecte

10/triez par ordre croissant de quota
11/idem mais en limitant aux eleves, qqsoit la promo
12/Affichez le top 10 des "plus gros" utilisateurs d'espace
13/idem en limitant aux eleves en cours de scolarite 


Pour envoyer un mail en mode CLI (Command Line Interface): $mail [-s sujet] login1 [login2] [...loginn] < fichier
Mettez comme sujet "Desole les TP d Unix recommencent" pour permettre le filtrage des mails que vous allez envoyer ....

14/
a)Groupes 1 & 3: envoyez un mail aux 5 "plus gros" utilisateurs de la promo 
b)Groupes 2 & 4: envoyez un mail aux 5 "plus petits" utilisateurs de la promo 
c)Groupes 5 & 7: envoyez un mail aux 5 "plus gros" utilisateurs de la promo precedente
d)Groupes 6 & 8: envoyez un mail aux 5 "plus petits" utilisateurs de la promo precedente



Le fichier ~olivier/coursunix/passwd.2012 contient toutes les informations relatives a tous les utilisateurs de l'ecole

15/Affichez les login Prenom Nom des eleves  de la promo2012 triee selon leur nom ( c.f fichier passwd.2012 )
16/Comptez combien d'eleves se prenomment julien 

La commande $ awk -F "delimiteur" '{print $NF}'  < fichier permet d'afficher le dernier champ d'une ligne, en precisant le delimiteur 
17/Affichez tous les prenoms de tous les utilisateurs
18/Triez par ordre alphabetique ces prenoms
La commande $ uniq -c < fichier permet d'afficher le nbre d'occurences de lignes identiques consecutives
19/Affichez le nombre d'occurence de chaque prenom
20/Affichez le Top 5 des prenoms les plus usuels
21/idem en limitant aux eleves
22/idem en limitant aux personnels 
 


23-Pour finir: 
        Groupes 1 & 3: 
                envoyez a 20:00 aux 14-b la liste des 14-c 
	Groupes 2 & 4:
		envoyez a 20:00 aux 14-c la liste des 14-d
	Groupes 5 & 7: 
		envoyez a 20:00 aux 14-d la liste des 14-a
	Groupes 6 & 8:
		envoyez a 20:00 aux 14-a la liste des 14-b


24-Lisez le texte suivant: http://www.justpasha.org/folk/whowhat.html
	-Si vous ne riez pas et comprenez moins de 5% de ce texte: reprenez le cours et tous les TP 
	-Vous comprenez entre 5 et 80% de ce texte et souriez (ou pas): Vous avez r�ussi l'examen, c'est deja ca ...
	-Si vous riez � gorge d�ploy�e et comprenez moins de 5% de ce texte: Contactez le BAPU le plus proche  .
	-Si vous riez � gorge d�ploy�e et comprenez plus de 80% de ce texte: Contactez le BAPU ou le CRI le plus proche ... 