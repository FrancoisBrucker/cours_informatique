# Zéro tracash, Zéro blablash, SSH
Mettre des sites / refs / sources
L’étape numéro 1 est d’avoir la bonne console. Moi, j’utilise Ubuntu (WSL 2).

L’étape numéro 2 est d’avoir un agent ssh, c’est le maître des clefs. 
Vous trouverez toutes les informations necessaires pour installer WSL2 et l’agent sous windows ici : [installation_W10](https://francoisbrucker.github.io/cours_informatique/cours/dfs/installation_W10.html)

Si vous utilisez linux ou mac tout est déjà là (normalement)

Comparer les OS expliquer ce qu’est l’agent

### Vérifiez que ça fonctionne
Ouvrez une fenêtre powershell et, en remplaçant login par votre login unix de l’école tapez la commande : `ssh-add -l`
Vous devriez avoir une phrase vous disant que l’agent n’a pas d’identité. Si vous n’avez pas d’agent installé (ou si vous l’avez stoppé) cela devrait vous dire qu’on arrive pas à se connecter à l’agent.
 
## SSH, c’est quoi ?
**Secure Shell (SSH)** est à la fois un programme informatique et un protocole de communication sécurisé. Le protocole de connexion impose un échange de clés de chiffrement en début de connexion. Par la suite, tous les segments TCP sont authentifiés et chiffrés. Il devient donc impossible d'utiliser un sniffer pour voir ce que fait l'utilisateur.
Avec SSH, l'authentification peut se faire sans l'utilisation de mot de passe ou de phrase secrète en utilisant la cryptographie asymétrique. Le protocole utilise deux clés complémentaires, la clé publique et la clé privée.
La clé publique est distribuée sur les systèmes auxquels on souhaite se connecter. La clé privée, qu'on prendra le soin de protéger par un mot de passe (elle est donc stockée cryptée), reste uniquement sur le poste à partir duquel on se connecte. L'utilisation de l’agent ssh permet de stocker le mot de passe de la clé privée pendant la durée de la session utilisateur.
 

 

##Générer une clé
Et ne pas se la faire voler par des hackers malveillants

Pour créer sa paire de clés :
ssh-keygen

On lui donne un nom (ex: keyblade95) et une passphrase (à ne pas oublier) et TaDaaa on a maintenant deux fichiers keyblade95 et keyblade95.pub.

keyblade95.pub est votre clé publique à donner à vos amis
keyblade95 est votre clé privée à ne montrer à personne sous aucun prétexte

Se placer au préalable dans un dossier adapté au stockage de données sensibles comme .ssh 

explication encryption : https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work

DES MATHS
Authorized keys
Reconnaître les machines qu’on connaît




Trouver sa clé publique
ssh identifiant@sas1.ec-m.fr (zzidane@sas1.ec-m.fr ou fbrucker@sas2.ec-m.fr, sas2 pour les profs)
ls -a permet de voir les dossiers cachés (commençant par un .)
cd .ssh
la clé publique se trouve dans id_rsa.pub
cat id-rsa.pub permet de l’afficher




ovh1.ec-m.fr
Go sur http://node.ail.ovh1.ec-m.fr/ et se connecter avec identifiant centrale
Copier la clé publique en entier (en 3 mots, commence par “ssh-rsa”, se termine par “identifiant@sas1.ec-m.fr”)
Valider puis attendre manip du prof (Il a fait quoi btw?)
Herbe
Serveur et Identifiant qu’on va utiliser par la suite


A chaque nouvelle session (redémarrage ordi)

A chaque fois que vous fermez et rouvrez une session (par ex en redémarrant votre ordi), il faut récupérer votre clé publique là où vous l’avez laissé.
En démarrant la session et en exécutant ssh-add -l, vous aurez le message “the agent has no identities”
Il faut récupérer la clé ssh là où on l’a laissée, ici sur sas1.


ssh -A identifiant@sas1.ec-m.fr
entrer le mot de passe
ssh-add
entrer passphrase
exit
(ssh-add -l) si on veut vérifier 
ssh herbe@ovh1.ec-m.fr


scp  : copier un dossier d’un ordi vers un autre
changement de port redirection
prendre une clé usb, copier les fichiers.
Aller sous le cri, brancher la clé sur le troisième serveur de la deuxième rangée.





cp : copier un fichier (sur une même machine)
cp -r => récursif
cp -p => garde les droits
cp [option] source destination

scp : commande pour transfert de fichiers via connexion ssh
s pour secure

monde UNIX: archives tar (mieux que zip car conserve les droits ?)

bsdtar cvf /tmp/node_ssh_keys.tar node.ssh.keys
/!\ fichier tar n’est pas encore compressé

xz /tmp/node_ssh_keys.tar
=> devient /tmp/node_ssh_keys.tar.xz
désormais compressé

bsdtar cf - node_ssh_keys | ssh herbe@ovh1.ec-m.fr “cd /tmp: tar xJf -”

tar      c        v         x           f
       créer   voir  extraire  utilise
                                      fichier en paramètres


scp fichier_source fichier_destination:www/


TL;DR
Mise en page Markdown : 

# en debut de ligne pour h1 ( plusieurs ## pour h2..3… )

Pour des lignes de code dans le shell
~~~sh
code
code 
code
~~~

[titre du lien](http:...)

les trucs entre `gnau` sont en gris très visible dans un paragraphe (attention c’est pas des apostrophes alt gr + 7 sur mon clavier)
les trucs entre ** ** sont en gras
les trucs entre * * sont en itallique

les tirets 
permettent
de faire 
des liste 
en markdown


