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

- ipv6 et ipv4
- organisation réseau (subnet) machine broadcast
- une interface par réseau
- routeur vs machine

> TBD ping paquets [ICMP](https://fr.wikipedia.org/wiki/Internet_Control_Message_Protocol) : attention ne passent pas partout, car du trafique en plus. De machine à machine (pas de port). Exemple [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/)

## Routage

```shell
netstat -r
```

- structure paquet
- [table de routage](https://en.wikipedia.org/wiki/Routing_table) : si choix alors le plus court et sinon, random : routage de toutes les adresses Et donne direction 1 hop (prog dynamique)
- 255 hop = discard

> TBD exemple table

Impossible de tout garder dans les réseaux actuel. On segmente le réseau en régions autonomes liées par des routeurs spécialisés.

région autonome (AS) :

```
                         ...     subarea - ...
                            \   /
area.1   area.2     .....   area.i
   |      |                   |
-------------------------------------   : backbone
```

Routeurs BGP (O) entre AS :

```
AS-O-----O-AS-O-AS
    \   /
     \ /
      O 
      |
   AS-O-AS
```

- réduire la taille en groupant les adresse par subnet

## Mise à jour des tables de routage

mise à jour des table grace à des [protocole de routage](https://en.wikipedia.org/wiki/Routing_protocol) :

réseau petit ou très changeant : [RIP](https://en.wikipedia.org/wiki/Routing_Information_Protocol).


- moyen (autonomous system) et autre métrique que hop : [OSPF](https://fr.wikipedia.org/wiki/Open_Shortest_Path_First)
- gros réseau : [BGP](https://fr.wikipedia.org/wiki/Border_Gateway_Protocol)




- réseaux privé

- ip4 : existence de réseaux privés et nat

> TBD et parler de dns
> paquet ICMP

wireshark on ne voit que la fin

1. ping6 pour ipv6. Est-ce que ça marche entre ordi de l'élèves ?
2. route en ipv6.
