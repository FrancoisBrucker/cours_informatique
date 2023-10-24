---
layout: layout/post.njk

title: Réseau

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Bases de réseau. On y verra les concepts et protocoles qui régissent le réseau internet. Le réseau est composé de multiples ***liens*** entre deux ordinateurs. Ces liens forment un graphe qui constitue le réseau.

## Communications par paquets

Réseau filaire : une ligne par communication de bout en bout, comme le téléphone à son origine.

{% lien %}
1878 à 1913 : le fonctionnement de la commutation manuelle :

1. [intro](https://www.youtube.com/watch?v=YSYs5TyA3n0)
2. [les centres](https://www.youtube.com/watch?v=vqGk7P-Rwto)
3. [le fonctionnement](https://www.youtube.com/watch?v=qwoFJT7MQBE)

{% endlien %}

Si A communique avec B et C avec D, chacun à besoin d'un fil :

```
             =======------ B
           //       \
A -------- /          -- D
          |
   C ----- 
```

Même si personne ne parle.

Dans une communication par paquets, chaque conversation est découpée en paquet au départ, chaque paquet est ensuite transport2 indépendamment dans le réseau puis les paquets sont réassemblés à l'arrivée. L'analogie de ce système est le système postal où chaque paquet peut transiter par différents endroits et arriver à des moments différents (voir ne pas arriver).

Si A communique avec B (-) et C avec D (+), ils peuvent communiquer via le même fil :

```
             +-+-+----- B
           /     + 
A --------       ++++ D
         +
C ++++++++
```

Ceci à de nombreux avantages :

- plus besoins d'avoir de nombreux câbles, un seul suffit
- si on ne parle pas on n'use pas de ressources

Mais pose des problèmes à résoudre :

- ordre des paquets : les paquets peuvent prendre des chemins différents et arriver dans le désordre
- les jonctions doivent pouvoir envoyer les paquets au bon endroit
- perte de paquets

Pour palier ces potentiels soucis, il faut ajouter des informations aux paquets. Chaque paquet est ainsi composé de deux parties :

- une entête (*header*) véhiculant les informations utiles au protocole mais ne faisant pas partie du message à transmettre
- un corps du message (*payload*)

{% faire %}
Ouvrez un [Wireshark](https://www.wireshark.org/) et regardez tous les paquets qui viennent sur votre machine.

Si peux de paquets arrivent, faîtes une requête google par exemple.
{% endfaire %}
{% info %}
Il vous faudra peut-être exécuter `sudo wireshark` pour pouvoir récupérer tous les paquets passant par votre ordinateur.
{% endinfo %}

## Schéma global

{% lien %}
[Linux Networking-concepts HOWTO](https://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)
{% endlien %}

Le but d'un réseau est de faire communiquer deux applications situées sur deux ordinateurs différents. Cette tâche est effectuée en appliquant le théorème fondamentale de l’ingénierie système : l'indirection.

L'indirection étant ici matérialisée par des *couches*. Prenons l'exemple d'un navigateur qui essaie d'ouvrir la page web d'une url située sur un serveur distant :

```
application  : navigateur -------------------------------- serveur
```

Pour que ces deux applications puissent communiquer, il faut que des données puissent être transmises du navigateur au serveur. Il faut donc au minimum s'assurer que les données transmises ne soient pas corrompue et au maximum s'assurer que toute donnée envoyée est bien reçue.

Il nous faut donc une seconde couche qui assure la transmission des messages entre le navigateur et le serveur :

```
application  : navigateur                                  serveur
transmission :    |__________________________________________|
```

Encore faut-il savoir comment aller d'un ordinateur à l'autre en suivant les nœuds du réseau. Ce qui rajoute une nouvelle couche dont le but est le routage :

```
application  : navigateur                                  serveur
transmission :    |                                          |
routage      :    |__________________________________________|
```

Et enfin, il faut bien faire transiter les bits dans le réseau physique, et passer d'un lien du réseau à l'autre :

```
application  : navigateur                                  serveur
transmission :    |                                          |
routage      :    |                                          |
liaisons     :    |__________________________________________|
```

A chaque couche est associé un protocole dont le but est de résoudre la tâche qui lui est assignée. Dans le cas de notre exemple ces protocoles sont :

- application : [http](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- transmission : [TCP](https://fr.wikipedia.org/wiki/Transmission_Control_Protocol)
- routage : [IP](https://fr.wikipedia.org/wiki/Internet_Protocol)
- liaisons : [Ethernet](https://fr.wikipedia.org/wiki/Ethernet)

Chaque couche encapsule le message de la couche précédente en ajoutant son header en début de message. A l'arrivée c'est le contraire, chaque couche supprime son header avant de passer le message à la couche suivante.

{% faire %}
Avec Wireshark, attrapez une communication http (faite une recherche google depuis votre navigateur) et voyez ses encapsulations.
{% endfaire %}
{% info %}
Une fois la communication http faite avec votre navigateur vous pouvez stopper l'enregistrement des paquets de Wireshark (le carré rouge de la barre d'actions)
{% endinfo %}

Connection entre deux ordinateurs :

```
X--------X
```

La communication n'est quasi jamais directe, il faut le plus souvent passer par des ordinateurs intermédiaires (les O), appelés ***routeurs***.

```
        --O----X
      /   |
X----O----O----X
     |
     |
     X
```

Pour garder les choses organisées et permettre au routeur de traiter chaque paquet arrivant, ils sont placés dans une FIFO qui permet :

- d'avoir un buffer permettant de stocker les élément pendant qu'un autre paquet est traité
- de les traiter dans l'ordre.

C'est la couche de routage qui détermine la direction à prendre :

```
application  : A                                       A
                v                                      ^
transmission : AT                                      AT
                 v                                      ^
routage      : ATI            ATI   > ATI              ATI 
                  v             ^        v               ^ 
liaison      : ATIE --------> ATIE    ATIE   --------> ATIE
                     1 lien     routeur       2 lien
```

Chaque lien de liaison permet de connecter 2 ordinateurs liés, il faut donc à chaque étape refaire cette couche en fonction de la couche précédente (routage) qui détermine la direction.

{% info %}
Ce modèle en quatre couches se décline en granularité plus fine de 7 couche, appelé [modèle OSI](https://fr.wikipedia.org/wiki/Mod%C3%A8le_OSI) (aussi appelé couches ISO).

{% endinfo %}

IL existe de très nombreux protocoles réseaux, et donc de très nombreux types de paquets :

```shell
netstat -s
```

{% lien %}
[Commande netstat](https://docs.oracle.com/cd/E19455-01/806-0916/6ja85399h/index.html)
{% endlien %}

## Couches

{% lien %}
[Beej's Guide to Network Concepts](https://beej.us/guide/bgnet0/html/)
{% endlien %}

> TBD : on se restreint à internet et ipv6 si on peut (on ne parlera de ipv4 que si nécessaire)

### Application : communication client-serveur

Il y a de très très nombreux protocoles applicatif. Chaque application peut avoir le sien. La très grande majorité d'entre eux sont organisés autour de la notion de client et de serveur :

{% note "**definition**" %}
Un [protocole client-serveur](https://fr.wikipedia.org/wiki/Client-serveur) permet à deux applications nommées ***client*** et ***serveur*** respectivement de communiquer par question-réponse.

1. l'application ***cliente*** va faire une ***requête*** au serveur
2. le serveur répond à la requête par une ***réponse***.

Cette relation est éminemment dissymétrique :

- le client demande le serveur répond
- il y a un serveur et une multitude de client
- la communication est initiée par la requête du client et terminée par la réponse du serveur.
{% endnote %}

Nous allons illustrer ce type de protocole en utilisant le protocole http 1.1 encore très utilisé (et le dernier facilement manipulable).

{% aller %}
[Aperçu du protocole http](http){.interne}
{% endaller %}

### Transmission

La transmission se fait d'une application sur un ordinateur A à une application sur un ordinateur B.

Comme il peut y a voir plusieurs communication simultanée sur un même ordinateur (web, mail, jeu en ligne, ...), il faut un moyen de les distinguer : les ports.

{% aller %}
[Port logiciel](./ports){.interne}
{% endaller %}

La transmission de données en elle meme peut se faire selon de multiples protocoles, nous en verront deux qui sont les plus utilisés : UDP et TCP

{% lien %}
[paquets UDP et TCP](https://www.youtube.com/watch?v=V1CxV6Vg7_U)
{% endlien %}

Nous allons utiliser [`nc`](https://doc.fedora-fr.org/wiki/Netcat,_connexion_client/serveur_en_bash) pour gérer nos connexion réseau. Commençons par voir comment tout cela fonctionne en créant une connexion vers l'ordinateur `www.google.fr` sur le port 80 :

```shell
nc www.google.fr 80
```

Nous voilà connecté. On peut maintenant lui parler via stdin qui, une fois la touche entrée appuyée, va transmettre les données à la socket écoutante sur le port 80 de l'ordinateur `www.google.fr`.

Il faut bien sur parler le http, si on ne respecte pas le protocole le serveur va rejeter notre demande et clore la connexion.

```shell
GET / HTTP/1.1
Host: www.google.fr
```

Le serveur nous répond dans notre stdout. On voit bien les entêtes et le body de la réponse. La socket n'est pas close, on peut continuer d'envoyer des requêtes si on le désire.

Une fois la connexion établie, elle l'est dans les deux sens :

- du client vers le serveur :
  - le stdin du client est envoyé sur le stdin du serveur
  - le stdout du serveur est envoyé sur le stdout du client
- du serveur vers le client :
  - le stdin du serveur est envoyé sur le stdin du client
  - le stdout du client est envoyé sur le stdout du serveur

#### UDP

Le protocole UDP est très simple, son principal intérêt est sa rapidité.

{% aller %}
[Protocole UDP](./udp){.interne}
{% endaller %}

 Si l'on veut transmettre des données de façon sûre, il faut utiliser un autre protocole, TCP

#### TCP

Le protocole TCP est utilisé dès qu'il faut transmettre de façon sûre et ordonnée.

{% aller %}
[Protocole TCP](./tcp){.interne}
{% endaller %}

### Routage

{% aller %}
[Routage IP](./ip){.interne}
{% endaller %}

### DNS

Transformer un nom en numéro IP : [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System), voir comment faire avec [dig](https://www.hostinger.fr/tutoriels/comment-utiliser-la-commande-dig-sous-linux)

Un nom de machine se fini toujours par un `.` qui est invisible. C'est lui le premiers serveur dns à être appelé, et qui transmet ensuite au serveur plus précis. Exemple :

Machine : `raifort.ovh1.ec-m.fr`. En vrai : `raifort.ovh1.ec-m.fr.` et se lit de droite à gauche :

1. `.`
2. `fr`
3. `ec-m` : trouve la machine et renvoie le résultat

```shell
$ dig +trace sas1.ec-m.fr

; <<>> DiG 9.16.42-Debian <<>> +trace sas1.ec-m.fr
;; global options: +cmd
.			1975	IN	NS	m.root-servers.net.
.			1975	IN	NS	a.root-servers.net.
.			1975	IN	NS	b.root-servers.net.
.			1975	IN	NS	c.root-servers.net.
.			1975	IN	NS	d.root-servers.net.
.			1975	IN	NS	e.root-servers.net.
.			1975	IN	NS	f.root-servers.net.
.			1975	IN	NS	g.root-servers.net.
.			1975	IN	NS	h.root-servers.net.
.			1975	IN	NS	i.root-servers.net.
.			1975	IN	NS	j.root-servers.net.
.			1975	IN	NS	k.root-servers.net.
.			1975	IN	NS	l.root-servers.net.
.			1975	IN	RRSIG	NS 8 0 518400 20231024050000 20231011040000 46780 . YGyaVKAIF2jzyA53/lHhA8+nNuY/M6mFg8JDqXUggDAFlKfcRavALiyW Wb6I7MF4Kl3N/fBXlAGDezSG770/JPTOjvKpJmFWikU0Jhrw0I4FXssy g3R+SsjUB62EdLgQ1g/Xf1IreJ5DgS27yqO7H4i10XPUzvvvTFz0+7iD SIaoFsr+UzFZ5eJpWl9qDmCC1pjRpVYQtd48drXGFEH7KQVZwrVsN7bm ztjVAGheEHKOaPzucru4cb2IKeHRvpZ54ZgqkFOT5I0u1Qvrft0cmlHm FpJKBhEvDlS8ftol+XbvoeWEGPIKyvhUh5rSTtzbGb+St54Owhfz145B Zhw+eA==
;; Received 525 bytes from 147.94.19.141#53(147.94.19.141) in 4 ms

fr.			172800	IN	NS	d.nic.fr.
fr.			172800	IN	NS	e.ext.nic.fr.
fr.			172800	IN	NS	f.ext.nic.fr.
fr.			172800	IN	NS	g.ext.nic.fr.
fr.			86400	IN	DS	29133 13 2 1303E8DA8FB60DB500D5BEA1EE5DC9A2BCC93DFE2FC43D346576658F ECCF5749
fr.			86400	IN	RRSIG	DS 8 1 86400 20231025050000 20231012040000 46780 . QgIjD3AGZ3bkE43PMFRxMghserL5cr4f6Vog7u/NES3qMuFVaG5XMrMh 2h7a1JgjkmtDfAQiW/83pLGbaD+4gTyykfPfkG4DA79rrwLdYKOWnCzF 90v3M9nbcnJF7KURIiQc01fyWlSXO/EjuEYJGmfaufB219XWbpDCs3Re AL4Z6l9d5Z4ZoQaEvpEbI99DN2sqJlUl0ZXwtqHZuWUzUZTRGWsaHIgQ D4HIracwNtFQ2C4WG3SU1OFcsPrs+3iEQDpHmqJvi9Vg53BuNalRkly1 88+36n47sumU7c9cMyFUUZmWuLBBH+2gYuOq4qTLpGFRBgx+inccQ5ZD ILhAig==
;; Received 624 bytes from 2001:503:c27::2:30#53(j.root-servers.net) in 20 ms

ec-m.fr.		3600	IN	NS	ns.ec-m.fr.
ec-m.fr.		3600	IN	NS	nsii.ec-m.fr.
ec-m.fr.		3600	IN	DS	52027 8 2 3D871FBBA98D510C3DA9708EABCB3692EFFC6EE5D0C372F37C54F922 26DCB7A1
ec-m.fr.		3600	IN	DS	14950 8 2 5B5C60AB452BA8F1455022E81D9B1F6C0C2CC04F142580A3CF602374 C1746E4A
ec-m.fr.		3600	IN	DS	5284 8 2 B4D2F8090F258CE54ECD0F1F54EEED8F92F3117D7B5D37512971DED5 A611293C
ec-m.fr.		3600	IN	RRSIG	DS 13 2 3600 20231117073012 20230929105144 60747 fr. 2iqcy96I51prsZxkU9GVDco+NDnNSUpo+t1UgHf9JuNGmzMKS1FrHvYf GBTuSHm4V4CKswXZ2o34Bg0nXJGJdw==
;; Received 435 bytes from 2001:678:c::1#53(d.nic.fr) in 8 ms

sas1.ec-m.fr.		86400	IN	A	147.94.19.1
sas1.ec-m.fr.		86400	IN	RRSIG	A 8 3 86400 20231118144121 20230919190106 41214 ec-m.fr. nycXsnLPJhrDjAdvoLrZTnPyQqSjCJws5q9jf3ctut7lVzXzWeuJrJO+ 3v0MVf7UDi90DZONSg4JBQzRJ+jNJrMXW8O6kfEj1I2N39OHayo/l2wc jMrGhHqa0LzkR5baJTQdfrwmjfcApVHr67Px7mRNzMMUzwE8E9DsupCl NhU=
ec-m.fr.		86400	IN	NS	ns.ec-m.fr.
ec-m.fr.		86400	IN	NS	nsii.ec-m.fr.
ec-m.fr.		86400	IN	RRSIG	NS 8 2 86400 20231117194511 20230919030106 41214 ec-m.fr. lMvybzKa9AEzgsINY1YypGqfTw9Vl1yUqLUbNbI1UjbmcDN3cI4hobdN hR5m3HNUDniGz5mIrZsXVCdTkCPvzSqcPzJazc8r2c+WU2iclvslvl8W sMMBU1BD999akuWmbRvlxQ1JyL+shXIA3syBjZhWRTYBlBZQW8Z/0ySK bDk=
;; Received 1211 bytes from 147.94.19.248#53(ns.ec-m.fr) in 4 ms

```

### Physique

LAN.

Mais aussi, via une borne wifi ou un hub par exemple :

- lan : tout le monde est connecté à tout le monde
- ethernet : tout le monde est connecté à tous via des hub/switch
- protocole hurle (CSMA : diff pour cable et wifi )
- parler des transmissions physique (2 couches phyisique dans la couche osi, c'est pur ça):
  - cable
  - onde
  - fibre
- mac adresse (NDP ou arp en ipv4)
  - [NDP vs arp](https://docs.oracle.com/cd/E19957-01/820-2982/chapter1-41/index.html)
  - [arp -n](https://superuser.com/questions/621593/whats-ipv6-analogue-for-ipv4-arp-an-and-arp-who-has/621594#621594)
- physique :
  - [wifi lan](https://www.youtube.com/watch?v=Uz-RTurph3c) ; [bruit wifi](https://www.youtube.com/watch?v=vvKbMueRzrI)
  - [rj 45](https://sitelec.org/cours/caleca/pc/cablage_reseau.html) (attention aux cables direct ou croisés) ; [en video](https://www.youtube.com/watch?v=_NX99ad2FUA)
  - [fibre optique](https://www.youtube.com/watch?v=eGNHZC4FkAg)
  - différence entre cable et wifi :
    - congestion du support
    - [hidden node problem](https://www.youtube.com/watch?v=UgQM0rVDIQE)

## Odds and ends

> TBD : dhcp (ou trouver les infos recueillies ?), ....
> TBD : firewall qui bloque les syn entrant ( et donc laisse les syn-ack sortant, ce qui permet de garder les connexions ou l'ordi est le client)
> nat ipv4
> gros réseaux et interconnexion des gros réseaux entre eux

> TBD MTU 1500 : <https://test-ipv6.com/faq_pmtud.html> <https://www.bgpexpert.com/article.php?article=117>
> TBD taille de la fifo d'un routeur
>
{% info %}
La taille de la FIFO est dépendante du réseau. Allant de $C\cdot T$ où $C$ est le débit du réseau (10Gb/s par exemple) et $T$ le temps moyen allant de la demande à la réception d'une donnée (250ms) dans des réseau très congestionné à $\frac{C\cdot T}{\sqrt{N}}$, avec $N$ le nombre de communications simultanées dans le réseau pour de grands réseaux homogènes.

Voir [cette référence](https://web.stanford.edu/class/cs244/papers/SizingRouterBuffersAppenzeller.pdf).

{% endinfo %}

> TBD TCP numéro de séquence initial déterminé


## Bibliographie

- [Linux Networking-concepts HOWTO](https://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)
- [Beej's Guide to Network Concepts](https://beej.us/guide/bgnet0/html/)
- [Introduction to computer network](https://intronetworks.cs.luc.edu/)

## tbd

> en python : <https://www.youtube.com/watch?v=Ftg8fjY_YWU>

- [ip](https://techviewleo.com/how-to-install-ip-ifconfig-commands-on-macos/?expand_article=1)

