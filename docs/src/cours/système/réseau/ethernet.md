---
layout: layout/post.njk

title: Ethernet

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% aller %}
[Ethernet](./ethernet){.interne}
{% endaller %}

Le schema classique d'un réseau Ethernet est :

```
   A  B     C
   |  |     |
----------------- : hub
         |
         D
```

Toutes les machines sont connectées deux à deux, Le hub permettant de retransmettre une donnée arrivant à tous les participants du réseau. Il n'est donc pas nécessaire d'avoir de routage puisque toutes les données sont envoyées à tout le monde, mais il faut tout de même un protocole pour s'assurer que chaque participant puisse reconnaître les données qui lui sont adressées. Ceci se fait via l'adresse MAC de la carte réseau.

## Adresse MAC

Chaque `interface` (ie carte réseau, comme `en0` par exemple) a une [adresse MAC](https://fr.wikipedia.org/wiki/Adresse_MAC) :

```shell
$ ip link show en1
en1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 38:f9:d3:17:40:bd 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active

```

L'adresse MAC de cet ordinateur (un mac) est : `38:f9:d3:17:40:bd`. Les 3 premiers octets (moins les 2 premiers bits) correspondent au fabriquant (ici apple) et les trois derniers sont aléatoires.

{% lien %}
[MAC address lookup](https://aruljohn.com/mac.pl)
{% endlien %}

L'idée est que dans un réseau local, il n'y ait pas deux machine avec la même adresse MAC, ce qui va identifier de façon unique un ordinateur.

{% info %}
On peut changer la mac adresse de façon logicielle, et donc se faire passer pour quelqu'un d'autre sur un réseau Ethernet. C'est le [MAC spoofing](https://wiki.archlinux.org/title/MAC_address_spoofing_(Fran%C3%A7ais)).
{% endinfo %}

## Ethernet

On parle de ***trame Ethernet*** (*Ethernet frame*) et non pas de paquet Ethernet. L'[entête](https://fr.wikipedia.org/wiki/Ethernet#Trames_Ethernet) du paquet Ethernet contient principalement :

- l'adresse MAC source
- l'adresse MAC destination
- la taille du paquet
- un checksum

Le paquet est émit sur toute la lan et seule la machine correspondant à l'adresse MAC destination l'ouvre. Ce protocole est donc tout simple : on hurle dans le réseau et celui qui doit écouter entent, les autres font semblant de ne rien avoir entendu.

Le problème arrive quand deux ordinateurs parlent en même temps. Les deux messages vont arriver détériorés à l'arrivée. Le protocole Ethernet gère cela de façon simple, en utilisant l'algorithme dit [CSMA/CD](https://fr.wikipedia.org/wiki/Carrier_Sense_Multiple_Access_with_Collision_Detection), comme on le ferait dans une salle bondée :

1. on commence par attendre que personne n'émette
2. puis on envoie son message par trame, en attendant entre chaque trame un temps déterminé
3. s'il y a une collision on arrête d'émettre pendant un temps aléatoire et retour en 1.

L'attente entre chaque trames permet à plusieurs communication d'avoir lieu simultanément. Dans les réseau LAN Wifi (ou avec des ponts), il faut un peu modifier cet algorithme car il devient impossible de détecter des collisions. Dans le cas ci-après, A et B voient la borne mais ils ne voient pas leurs ondes respectives :

```
  A     X      B
```

Dans ce cas là, il faut demander la permission à la borne Wifi d'émettre  et c'est elle qui intime aux autres ordinateurs de ne rien émettre. Cette méthode est appelée CSMA/CA. Voir le lien ci-après :

{% lien %}
[hidden node problem](https://www.youtube.com/watch?v=UgQM0rVDIQE)
{% endlien %}

Plus le réseau est brouillé, plus il va y avoir de collisions et, pire encore, il va s'adapter à l'émetteur le plus lent. C'est pourquoi il ne faut pas jouer sur un réseau Wifi : trop de paquets sont perdus.

Il reste un problème à résoudre, comment connaître l'adresse MAC du destinataire alors que l'on a que son adresse IP à disposition.

## ARP et NDS

IL existe un protocole spéciale lié à IP pour retrouver l'adresse MAC à partir d'une adresse IP. Ce protocole s'appelle [ARP](https://fr.wikipedia.org/wiki/Address_Resolution_Protocol) pour IPv4 et [NDP](https://fr.wikipedia.org/wiki/Neighbor_Discovery_Protocol) pour IVv6

{% lien %}
[NDP vs arp](https://docs.oracle.com/cd/E19957-01/820-2982/chapter1-41/index.html)
{% endlien %}

Ce protocole envoie simplement une requête sur la LAN et demande qui possède cette adresse IP. Pour éviter de faire cette demande à chaque fois, l'ordinateur demandeur va conserver une table de correspondance.

```
ip nei
```

Permet de connaître cette table de correspondance.
