---
layout: layout/post.njk

title: Routage IP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Internet Protocol (IP)](https://fr.wikipedia.org/wiki/Internet_Protocol)
{% endlien %}

## Adresse IP

{% lien %}

- [adresse IP](https://fr.wikipedia.org/wiki/Adresse_IPv6)
- [RFC IPv6](https://www.rfc-editor.org/rfc/rfc4291)

{% endlien %}

Une adresse IP est un nombre sur 16B = 128b décrit mot par mot (2B par 2B) sous sa forme hexadécimale. Par exemple (repris de Wikipedia):

```
2001:0db8:0000:85a3:0000:0000:ac1f:8001
```

Ou de façon abrégée (0 de tête supprimés et une suite de 0 concaténée):

```
2001:db8:0:85a3::ac1f:8001
```

Une adresse IP différente est associée à toute machine sur le réseau internet, c'est ce qui permet de les différentier. Il y a donc $2^{128}$ adresses possibles, ce qui en fait plus que de particules dans l'univers ($10^{80}$)

Actuellement coexiste deux standard pour les adresse IP, les adresse IPv6 qu'on vient de voir et les adresse IPv4, sur 4B, écrite byte par byte sous sa forme décimale. Par exemple :

```
172.18.32.190
```

{% info %}
On a du changer de version d'adressage car on est arrivé à court d'adresse disponibles pour les adresses IPv4 ($2^32$).
{% endinfo %}

Nous allons essentiellement parler ici de IPv6, la plupart des concepts étant identiques en IPv4 et IPv6.

On fait parfois suivre l'adresse par un `/x` où `x` est un nombre entre 1 et 128. Ce type d'adresse représente un réseau et sont pour cela appelé [masque de sous réseau](https://fr.wikipedia.org/wiki/Adresse_IPv6#Notation_des_masques_de_sous-r%C3%A9seau). Par exemple (encore une fois repris de Wikipédia) :

```
2001:db8:1:1a0::/59
```

Cette adresse correspond aux adresses dont :

- les 59 premiers bits correspondant à l'adresse
- les $128-59 = 69$ derniers bits sont libres

Elle encode donc au maximum $2^{69}$ machines possibles pour ce sous-réseau.

{% info %}
Le préfixe 2001:db8::/32 est un préfixe IPv6 spécial utilisé spécifiquement dans les exemples de documentation.
{% endinfo %}

La commande [ip](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf) permet d'identifier toutes les adresses IP, par exemple :

```shell
$ ip addr show dev en0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether f8:4d:89:8e:77:7e
	inet6 fe80::418:6a98:fca5:e83f/64 secured scopeid 0xf
	inet 172.18.32.190/22 brd 172.18.35.255 en0
	inet6 2001:660:5404:f232:1ccc:db68:4b11:59dc/64 autoconf secured
	inet6 2001:660:5404:f232:a4b7:59d7:f780:855c/64 autoconf temporary
```

On y voit :

- l'adresse mac (ether)
- une adresse ipv6 locale (de type `fe80::/10`)
- l'adresse IPv4 et sont broadcast
- deux adresse IP en /64

> TBD :
> There appear to be four different types of IPv6 addresses:
>
>Main address, using your ISP prefix + derivation of your network-interface MAC-address.
>[Temporary addresses](https://www.rfc-editor.org/rfc/rfc4941), based on your main address but with randomization to prevent tracking. (a new one is generated every so often)
>Link-local address, identified by starting with fe80:. (not usable globally, tied to routing)
>Unique local address, identified by starting with fd00:. (not usable globally, not tied to routing)

Ceci signifie que l'adresse IP de ma machine est `2001:660:5404:f232::/64` c'est à dire que j'ai en fait $2^{64}$ adresses possibles et que mon ordinateur a choisi d'utiliser `2001:660:5404:f232:a4b7:59d7:f780:855c`.

{% info %}
Il y a tellement d'adresse IPv6 de disponibles (en tous cas, [pour l'instant...](https://xkcd.com/865/)) qu'on assigne par défaut un réseau en `/64` à toute machine. Quite à elle d'en choisir une (ou plusieurs) parmi toute ces possibilités.
{% endinfo %}

On peut trouver une machine sur le réseau en la *pinguant*. On peut ainsi d'une autre machine de l'internet trouver ma machine en :

```
ping6 2001:660:5404:f232:a4b7:59d7:f780:855c
```

{% faire %}
Pinguez vous les uns les autres.
{% endfaire %}
{% info %}
Comme n'importe qui peut le faire depuis n'importe où, il arrive que les paquets ping soient bloqués par le routeur de votre sous-réseau.
{% endinfo %}

Il existe également la version IPv4 :

```shell
ping 172.18.32.190
```

Attention, contrairement à IPv6, IPv4 a de nombreux [réseaux locaux](https://fr.wikipedia.org/wiki/R%C3%A9seau_priv%C3%A9), inaccessible de l'internet. Mon adresse IPv4 en fait parti. Ces réseaux locaux existent de part la pénurie des adresse Ipv4, ils n'ont plus de raison d'être en IPv6.

{% info %}
Les messages ping sont envoyés en utilisant le protocole [ICMP](https://fr.wikipedia.org/wiki/Internet_Control_Message_Protocol), qui est un protocole de contrôle (Internet Control Message Protocol) également utilisé pour de nombreuses autres opérations de maintenance du système. Il est aussi détourné pour réaliser  les [attaques DDos](https://www.cloudflare.com/fr-fr/learning/ddos/glossary/internet-control-message-protocol-icmp/)

{% endinfo %}

## Routage

Cette notion de sous-réseau est importante pour l'organisation des machines sur le réseau. On considère que des machines de numéro proches donc d'un même sous-réseau, sont aussi proche physiquement et peuvent être routé par le même routeur.

{% note "**définition**" %}
Un ***routeur*** est un ordinateur du réseau permettant de rediriger des paquets IP d'un sous-réseau à un autre.

{% endnote %}

On peut considérer le réseau ci-après, à 5 machines (de A à E) et 4 routeurs (1 à 4)

```
A----1---2---4----E
      \ /    |    
       3 --- D
      / \
     B   C
```

Pour envoyer un paquet de l'ordinateur A à E il y a plusieurs chemins, par exemple A-1-2-4-E ou encore A-1-3-2-4-E. Savoir à quel route aller, se fait via une [table de routage](https://en.wikipedia.org/wiki/Routing_table) qui determine le prochain routeur

Par exemple la table de routage de A ressemble à :

```
dest.  via coût
A       A    0
B       1    3
C       1    3
D       1    4
E       1    4
default 1
```

Où la route `default` correspond à toutes les autres destinations possibles. Et celle du routeur 2 pourrait ressembler à :

```
dst.   via coût
2       2    0
A       1    2
B       3    2
B       1    3  # non optimal
C       3    2
D       3    2
D       4    2
E       4    2
```

Les autres routes sont à accès direct et n'ont donc pas de routage. Remarquez que on peut aller à D de deux façon différentes, qui sont listées dans la table.

Des différentes tables un paquets peut aller à bon port en suivant la prochaine direction à prendre à chaque routeur, pour finalement arriver à bon port.

On peut voir la table de routage de sa machine avec la commande :

- `ip route show` pour le routage IPv4, qui est plus simple
- `ip -6 route show` pour le routage IPv6

Cette table est également accessible via la commande [netstat](https://www.quennec.fr/trucs-astuces/syst%C3%A8mes/windows/toutes-versions/la-commande-netstat) :

```shell
netstat -r
```

Ce n'est que la table de notre propre ordinateur qui va le plus souvent avoir 3 types de routes :

- si on reste sur la machine, on ne prend pas le réseau
- si on reste dans le réseau local, on va directement à la machine concernée
- sinon on passe par le routeur de la box.

Lorsque le réseau va grossir, on ne peut plus garder les route vers toutes les machines du réseau, on est obligé d'utiliser les sous-réseaux qui vont donner des directions générales à prendre, selon le début de l'adresse.

Pour que ceci fonctionne :

- il faut *en gros* qu'un routeur route son sous-réseau.
- il faut que des ordinateurs d'adresses proches soient proche physiquement

## Structure d'internet

Du petit réseau géré de façon ad-hoc, internet est devenu un réseau mondial composé d'une myriade de petites area interconnectées entre elle.

### LAN

- LAN : **Local Area Network**. Le réseau de la maison où toutes les machines sont connectée les unes au autres. Ce réseau ne possède qu'une porte de d'entrée/sortie, son routeur (la box).
Il n'y a pas besoin de routeur pour fire transiter des paquets à l'intérieur d'une LAN car chaque machine peut communiquer directement avec une autre. La nécessité d'un routeur vient lorsque l'on veut faire sortir ou entrer des paquet dans la LAN. Le routeur est ainsi connecté à0 deux réseaux, celui de la LAN et l'extérieur.

Ce réseau extérieur est de notre provider internet, et plus vraisemblablement à une partie de celui-ci (celui de notre région).

### Réseau ad-hoc

Un réseau ad-hoc est un réseau qui s'auto-configure et ne repose sur aucune unité centralisée. C'est pour ça que le réseau initial ([ARPANET](https://fr.wikipedia.org/wiki/ARPANET)) a été crée. Il devait survivre à une attaque nucléaire qui détruirait tout réseau centralisé.

Le protocole RIP de configuration des tables de routage en est issu.

### Internet

De nombreux réseaux connectés ensembles. Des routeurs se chargeant de gérer le traffic interne au réseau et les interconnections. De grosses entités autonomes liées entre elle par des GGP. Chaque entité autonome étant à son tour formées d'aires elles mêmes encore subdivisées en sous-aires.

L'entrée dans ces aires et sous-aires se fait par un nombre très limité de routeurs (souvent 1) garantissant une certaine protection du réseau, via des firewall par exemple.

Ce fonctionnement en entités (plus ou moins) autonomes interconnectées permet de maintenir des tables de routages petites sans perdre en efficacité.

#### Area et AS

Le réseau géré par notre provider est une région (area.1) relié à un *backbone* reliant un ensemble de région formant une ***région autonome (Autonomous System)*** d'internet. Disons, l'internet Français. Une [région autonome](https://fr.wikipedia.org/wiki/Autonomous_System) est une partie d'internet stable d'un point de vue du routage. Région autonome (AS) :

```
  LAN                            ... 
   |                              |
  ...                     ...  subarea - ...
   |                        \   /
area.1   area.2   .....     area.i
   |      |                   |
---------------------------------- : backbone
```

Dans ce genre de réseau, les routeurs sont dédiés soit à la connection entre sub-area, soit au routage d'une subarea en elle-même.

Exemple :

1. AS : eduroam
2. area : universités de France
3. sub-area :
   1. salles informatiques
   2. réseaux des départements de recherche
      1. info
      2. math
      3. biologie
      4. ...

L'accès à chaque aire et sous-aire est faite via un routeur qui autorise les entrée et gère le routage à l'intérieur de son aire et liens avec ses sous-aires.

#### BGP

Enfin les différentes régions autonomes d'internet sont reliées entre elle par des routers [BGP](https://fr.wikipedia.org/wiki/Border_Gateway_Protocol)
Impossible de tout garder dans les réseaux actuel. On segmente le réseau en régions autonomes liées par des routeurs spécialisés. Routeurs BGP (O) entre AS :

```
AS-O-----O-AS-O-AS
    \   /
     \ /
      O 
      |
   AS-O-AS
```

Ces différentes structuration de routage assurent une fluidité du routage sans surcharger les tables des routeurs qui la constitue. Un peu comme un réseau routier.

## paquets IP

> TBD : structure paquet

- si choix alors le plus court et sinon, random : routage de toutes les adresses Et donne direction 1 hop (prog dynamique)
- 255 hop = discard

## Mise à jour des tables de routage

mise à jour des table grace à des [protocole de routage](https://en.wikipedia.org/wiki/Routing_protocol) :

### Protocole RIP

- réseau petit ou très changeant : [RIP](https://en.wikipedia.org/wiki/Routing_Information_Protocol)
- métrique du hop.

Chemin calculé avec . Toutes les 30s, chaque routeur reçoit la table de routage de sous ses voisins (il envoie également la sienne à ses voisins) avec la métrique du nombre de hop. Il peut alors mettre à jour sa propre table en utilisant l'algorithme de [Bellman ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford).

### Protocole OSPF

- moyen (autonomous system) : [OSPF](https://fr.wikipedia.org/wiki/Open_Shortest_Path_First)
- autre métrique que hop

Dijkstra

### Protocole BGP

Relie des gros réseaux entre eux : [BGP](https://fr.wikipedia.org/wiki/Border_Gateway_Protocol)
