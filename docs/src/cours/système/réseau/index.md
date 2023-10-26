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

{% info %}
Vous aurez besoin d'avoir la commande `ip` très utile en réseau. Ils font parti de la suite logicielle [iproute2](https://en.wikipedia.org/wiki/Iproute2) et s'installe via les paquets `iproute2` sous Debian et `iproute2mac` avec brew.

{% endinfo %}

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

### IP et Routage

{% aller %}
[Routage IP](./ip){.interne}
{% endaller %}

### DNS

Transformer un nom en numéro IP : [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System), voir comment faire avec [dig](https://www.hostinger.fr/tutoriels/comment-utiliser-la-commande-dig-sous-linux)

Un nom de machine se fini toujours par un `.` qui est invisible. C'est lui le premiers serveur dns à être appelé, et qui transmet ensuite au serveur plus précis. Exemple :

Machine : `www.google.fr`. En vrai : `www.google.fr.` et se lit de droite à gauche :

1. `.`
2. `fr`
3. `google`
4. `www` : trouve la machine et renvoie le résultat

```shell
$ $ dig +trace www.google.fr

; <<>> DiG 9.18.18-0ubuntu0.22.04.1-Ubuntu <<>> +trace www.google.fr
;; global options: +cmd
.			54887	IN	NS	e.root-servers.net.
.			54887	IN	NS	a.root-servers.net.
.			54887	IN	NS	l.root-servers.net.
.			54887	IN	NS	g.root-servers.net.
.			54887	IN	NS	i.root-servers.net.
.			54887	IN	NS	j.root-servers.net.
.			54887	IN	NS	b.root-servers.net.
.			54887	IN	NS	d.root-servers.net.
.			54887	IN	NS	f.root-servers.net.
.			54887	IN	NS	k.root-servers.net.
.			54887	IN	NS	m.root-servers.net.
.			54887	IN	NS	c.root-servers.net.
.			54887	IN	NS	h.root-servers.net.
;; Received 811 bytes from 127.0.0.53#53(127.0.0.53) in 19 ms

fr.			172800	IN	NS	d.nic.fr.
fr.			172800	IN	NS	e.ext.nic.fr.
fr.			172800	IN	NS	f.ext.nic.fr.
fr.			172800	IN	NS	g.ext.nic.fr.
fr.			86400	IN	DS	29133 13 2 1303E8DA8FB60DB500D5BEA1EE5DC9A2BCC93DFE2FC43D346576658F ECCF5749
fr.			86400	IN	RRSIG	DS 8 1 86400 20231106150000 20231024140000 46780 . ruIcbHCdiNOjKUJzWsoR6MnU9sAO6afz6pA1MS4MtKnfih3GReBvHtFy eoD9bVPzVeT9Y22u5Pg6e3vrQiUOV3Jg6B3hTwUs9+6qJVrzqMV3gw/p ev5I3tvURv40ALXV63guLc/DG/Gpw62NdVtNyPWXKP6+n+KeWL13kjcZ kCU9ZvVxMD9rfxa75BNELsJ2opRBgI6Pv2hG6ZDMCg+hVMLNeVEEklmj 2fDZoQG65G4JPhjUj25hTVZEJp65cKo1WWtgTcHjvWtjW/AHwXTDMEJX DuRxWhhsTJz0eoNhhzBxxXasHc0y6nzpdxbiP/5VqoKKWa6SdqOvj8dK Odqy1g==
;; Received 625 bytes from 2001:503:c27::2:30#53(j.root-servers.net) in 15 ms

google.fr.		3600	IN	NS	ns4.google.com.
google.fr.		3600	IN	NS	ns1.google.com.
google.fr.		3600	IN	NS	ns2.google.com.
google.fr.		3600	IN	NS	ns3.google.com.
SFBLG7NFATQ81CQJGT5Q91BQS3H9V6ND.fr. 600 IN NSEC3 1 1 0 - SFBN9RJNNUEVSB0GNER878N1GN41D23I NS SOA TXT NAPTR RRSIG DNSKEY NSEC3PARAM
SFBLG7NFATQ81CQJGT5Q91BQS3H9V6ND.fr. 600 IN RRSIG NSEC3 13 2 600 20231126061750 20230920091841 60747 fr. 2aNPNCwEc2TuAOAEAxUddgw9PVwEEM+9iJFKXID4y94kaQBKGza3bkqY fFXJcXEVXH1yWT/XvEiaBcqV0NfZVg==
B3RAI8IOHVA9825CHT27ROCMR6SJOIS0.fr. 600 IN NSEC3 1 1 0 - B3RC45JNQDO5CU29PAFJU8VHS6032FQF NS DS RRSIG
B3RAI8IOHVA9825CHT27ROCMR6SJOIS0.fr. 600 IN RRSIG NSEC3 13 2 600 20231212005810 20231013001314 60747 fr. AFHSWOaxw4mJUy2z/3zziFaqGOGB0FeweV7jSpAY1BAFgLWwFLBbORpR G3HO5GJ81j7EQfjdDXyjTkT++EfCMg==
;; Received 509 bytes from 2001:678:4c::1#53(g.ext.nic.fr) in 19 ms

www.google.fr.		300	IN	A	142.251.37.227
;; Received 58 bytes from 216.239.32.10#53(ns1.google.com) in 23 ms

```

### Ethernet et Liaison

Dans la partie liaison on a soit affaire à deux ordinateurs (2 routeurs ou 1 ordinateur et un routeur) relié par une liaison physique. ce lien peut être :

- un câble [RJ45](https://sitelec.org/cours/caleca/pc/cablage_reseau.html) qui est une simple communication série [Tx/Rx](https://www.youtube.com/watch?v=-Wx-_dUh3ME) (attention aux cables direct ou croisés)
- une [onde](https://www.youtube.com/watch?v=Uz-RTurph3c)
- une [fibre optique](https://www.youtube.com/watch?v=eGNHZC4FkAg)

Chaque moyen de communication nécessite son propre protocole permettant la transmission et a ses propres limitations :

- câble : distance courte, il faut avoir un cable
- wifi : [bruit wifi](https://www.youtube.com/watch?v=vvKbMueRzrI)
- fibre : cher pour un usage purement local.

Un routeur est forcément relié physiquement à plusieurs autres routeurs, selon les routes qu'il peut disposer. De même votre ordinateur est relié à d'autres ordinateur via le réseau wifi de votre maison par exemple. Ce réseau minimal est appelé [LAN](https://fr.wikipedia.org/wiki/R%C3%A9seau_local) : Local Area Network

Dans une LAN, tous les ordinateurs sont connectés entre eux : ils sont tous à 1hop les uns de autres. Ceci peut se faire directement en connectant physiquement les ordinateurs 2 à deux, mais le plus souvent on utilise des :

- [hubs](https://fr.wikipedia.org/wiki/Hub_Ethernet) qui renvoient ce qu'il reçoivent à tous les autres ports.
- ou des [switch](https://fr.wikipedia.org/wiki/Commutateur_r%C3%A9seau) qui renvoient les données uniquement au port concerné (ils maintiennent une table de correspondance à jour)

Une LAN peut-être très petite (au pire un routeur et l'ordinateur) ou contenir de [nombreuses machines](https://en.wikipedia.org/wiki/LAN_party) utilisant des [bridges](https://fr.wikipedia.org/wiki/Pont_(r%C3%A9seau)) qui permettent la réémission des signaux.

Classiquement, une LAN est un réseau familial :

```
       W --- A
     /   \
    /     B
Z -R- C
    \
     D
```

- W : borne wifi
- Z : box (routeur)
- R : [switch ou hub](https://fr.wikipedia.org/wiki/Commutateur_r%C3%A9seau)
- A : ipad
- B : iphone
- C : imac
- D : imprimante

Dans un réseau LAN toutes les machines sont connectée 2 à 2 : elles se voient sans passer par un procédé de routage. Elles n'ont donc pas besoin de IP pour communiquer et utilisent un protocole particulier [Ethernet](https://fr.wikipedia.org/wiki/Ethernet).

{% aller %}
[Ethernet](./ethernet){.interne}
{% endaller %}

## Odds and ends

### Default gateway

> adresse de routage par défaut

### dhcp

> TBD : dhcp (ou trouver les infos recueillies ?), ....
>

### Firewall

> TBD : firewall qui bloque les syn entrant ( et donc laisse les syn-ack sortant, ce qui permet de garder les connexions ou l'ordi est le client)

Si firewall il block les syn entrant : donc aucune communication n'est possible sur le port demandé de la machine.

Le firewall peut être configuré pour bloquer (ou non) les communications entrantes (ou sortantes) pour un port donné.

```
                 firewall
                  entrée
          |    syn   |
Client -- | -------->X --> Serveur:port
          |          |

```

### NAT IPv4

> nat ipv4 : avec 

### Taille des paquets

> TBD MTU 1500 : <https://test-ipv6.com/faq_pmtud.html> <https://www.bgpexpert.com/article.php?article=117>

### Taille de la FIFO d'un routeur

La taille de la FIFO d'un routeur est dépendante du réseau. Allant de $C\cdot T$ où $C$ est le débit du réseau (10Gb/s par exemple) et $T$ le temps moyen allant de la demande à la réception d'une donnée (classiquement, on utilise 250ms) dans des réseau très congestionné à $\frac{C\cdot T}{\sqrt{N}}$, avec $N$ le nombre de communications simultanées dans le réseau pour de grands réseaux homogènes.

Voir [cette référence](https://web.stanford.edu/class/cs244/papers/SizingRouterBuffersAppenzeller.pdf).

## Bibliographie

- [Linux Networking-concepts HOWTO](https://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)
- [Beej's Guide to Network Concepts](https://beej.us/guide/bgnet0/html/)
- [Introduction to computer network](https://intronetworks.cs.luc.edu/)
