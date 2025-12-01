---
layout: layout/post.njk

title: Principes réseaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but d'un réseau est de faire communiquer deux applications situées sur deux ordinateurs différents. Cette tâche est effectuée en appliquant le théorème fondamentale de l’ingénierie logiciel : l'indirection.

L'indirection étant ici matérialisée par des [couches](https://fr.wikipedia.org/wiki/Suite_des_protocoles_Internet). Prenons l'exemple d'un navigateur qui essaie d'ouvrir la page web d'une url située sur un serveur distant :

```
application  : navigateur -------------------------------- serveur
```

Pour que ces deux applications puissent communiquer, il faut que des données puissent être transmises du navigateur au serveur. Il faut donc au minimum s'assurer que les données transmises ne soient pas corrompues et au maximum s'assurer que toute donnée envoyée est bien reçue.

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

Chaque couche encapsule le message de la couche précédente en ajoutant son header en début de message.

{% attention "À retenir" %}
Cette séparation en quatre couches est appelé **_modèle TCP/IP_**.
{% endattention %}
{% info %}
Vous verrez aussi un modèle plus ancien (et moins adapté au réseau moderne) appelé [modèle OSI](https://fr.wikipedia.org/wiki/Mod%C3%A8le_OSI) qui sépare le réseau en 7 couches ([TCP/IP vs OSI](https://fr.wikipedia.org/wiki/Suite_des_protocoles_Internet#Couches_TCP/IP)).
{% endinfo %}

A l'arrivée c'est le contraire, chaque couche supprime son header avant de passer le message à la couche suivante. Ce principe général de transmission en couches permet de faire communiquer plusieurs machines entre-elles quelques soient leurs emplacement dans le réseau (deux machines éloignées de plusieurs milliers de kilomètres ou deux fois la même machine) du moment que la machine appelante connaisse l'adresse dans le réseau de la machine appelée.

## Adresse

L'adresse d'une machine sur le réseau est géré par la couche de routage, c'est un nombre sur 128 bits (avec le protocole [IPv6](https://fr.wikipedia.org/wiki/IPv6)) qui permet d'adresser plus de $10^{38}$ machines. On ne manipulera (presque) jamais directement ce nombre car un autre protocole (le [protocole DNS](https://fr.wikipedia.org/wiki/Domain_Name_System)) associe de façon unique un nom à ce numéro.

{% attention "À retenir" %}
Chaque machine sur le réseau est identifiée par un nom.
{% endattention %}

Sous Linux on utilise [la commande `dig`](https://fr.wikipedia.org/wiki/Dig_(programme_informatique)) pour connaître le numéro IP associé à un nom. Par exemple la machine `www.google.fr` :

```shell
❯ dig AAAA sas1.ec-m.fr +short
2001:660:5404:191::21
```

On peut aussi faire la réciproque :

```shell
❯ dig -x 2001:660:5404:191::21 +short
sas1.ec-m.fr.
```

{% info %}
Une même adresse IP peut être associée à plusieurs noms et réciproquement. Ceci permet de toujours répondre à une requête même si une machine est occupée (on prend la suivante de la liste). Par exemple :

```shell
❯ dig AAAA www.google.com +short
2a00:1450:4007:80d::2004
❯ dig -x 2a00:1450:4007:80d::2004 +short
par10s21-in-x04.1e100.net.
par10s41-in-x04.1e100.net.
❯ dig AAAA par10s21-in-x04.1e100.net +short
2001:4860:4802:36::4
2a00:1450:4007:80d::2004
```

{% endinfo %}

Si le nom suffit pour accéder à la machine, il ne suffit pas pour entamer une communication réseau qui se déroule entre deux applications. En effet laquelle choisir sur la machine appelée ?

## Port

Chaque machine possède des points d'entrées, appelés [ports](<https://fr.wikipedia.org/wiki/Port_(logiciel)>) (un nombre entre 0 et $2^{16}-1 = 65535$), pouvant chacun associés à une application. On dit que l'application écoute un port $p$ si elle est :

1. en fonctionnement
2. est associée au port $p$

Sous Linux on utilise [la commande `nmap`](https://nmap.org/book/man.html) pour connaître l'état d'un port,  ouvert (c'est à dire qu'une application écoute ce port) ou non. Par exemple :

```shell
❯ nmap -p 443 www.google.com
Starting Nmap 7.98 ( https://nmap.org ) at 2025-11-30 07:55 +0100
Nmap scan report for www.google.com (142.250.75.228)
Host is up (0.016s latency).
Other addresses for www.google.com (not scanned): 2a00:1450:4007:80d::2004
rDNS record for 142.250.75.228: par10s41-in-f4.1e100.net

PORT    STATE SERVICE
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
```

La commande précédente montre que le port 443 est _*ouvert*_ sur la machine `www.google.fr`. Une application sur la machine `www.google.fr` écoute ce port : on peut communiquer avec elle.

En revanche, le statut du port 8080 est inconnu, son état est _*filtré*_ :

```shell
❯ nmap -p 8080 www.google.com
Starting Nmap 7.98 ( https://nmap.org ) at 2025-11-30 07:55 +0100
Nmap scan report for www.google.com (142.250.75.228)
Host is up (0.017s latency).
Other addresses for www.google.com (not scanned): 2a00:1450:4007:80d::2004
rDNS record for 142.250.75.228: par10s41-in-f4.1e100.net

PORT     STATE    SERVICE
8080/tcp filtered http-proxy

Nmap done: 1 IP address (1 host up) scanned in 0.25 seconds
```

Un port sur une machine à 3 états :

- ouvert : une application écoute ce port et peut être appelée
- fermé : aucune application n'écoute ce port
- filtré: le statut du port est inconnu, souvent à cause d'un [firewall](https://fr.wikipedia.org/wiki/Pare-feu_(informatique)) dont le but est de bloquer la communication des ports non ouvert.

{% attention "À retenir" %}

Pour entamer une communication réseau avec une application il faut posséder 2 informations :

- le nom de la machine sur laquelle tourne l'application
- le port d'écoute de l'application

{% endattention %}
{% info %}
Il existe des ports par défaut pour certains types d'applications. Par exemple le port part défaut des serveurs web https est 443. C'est pourquoi lorsque l'on communique avec google les deux urls suivantes sot équivalentes (faites l'expérience) :

- <https://www.google.com>
- <https://www.google.com:443>

{% endinfo %}

## Socket

Une fois la machine à appeler trouvée sur le réseau la communication effective entre deux ordinateurs se fait via un tuyau appelé [socket](https://fr.wikipedia.org/wiki/Berkeley_sockets) qui relie le port appelé de la machine distante à un port de l'ordinateur appelant :

```
               socket
 -----------             ---- -------
| ordi. | 0 |       =====| 0 |=prg b |
|   A   | 1 |      /     | 1 |       |
| prg a=| 2 |======      | 2 |   B   |
 -----------             ---- -------
  ordi. ports            ports ordi. 
```

Dans le schéma ci-dessus le programme a de l'ordinateur A a établi une connection avec le programme b l'ordinateur B qui écoute sur le port 0. Le choix des ports utilisés est régit par la règle suivante :

Les ports sont répartis en trois catégories, selon leurs usages :

- de 0 à 1023 : **_system ports_** (aussi appelés _well known ports_) qui sont utilisés par le système (22 pour ssh, 443 pour https, 80 pour http, ...)
- de 1024 à 49151 : **_user ports_** (aussi appelés **_registered ports_**) sont utilisés soit par des protocoles utilisateurs (ces protocoles peuvent être connus comme bittorrent, des ports 6881 à 6999 ou des ports de tests comme 8080 qui est souvent utilisé pour des serveurs web locaux)
- de 49152 à 65535 : [**_Ephemeral port_**](https://en.wikipedia.org/wiki/Ephemeral_port) (aussi appelés **_private ports_**) utilisés par le système le temps d'une connexion.

{% lien %}
[Liste des ports communément utilisés](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
{% endlien %}

Les ports systèmes étant réservés à des protocoles connus, si l'on ne précise pas le port lors d'une connexion. c'est le port par défaut qui est utilisé. Par exemple pour une connexion de notre ordinateur sur le site de google avec le protocole https :

```
      A                        www.google.com

    système             ----- 443 système
utilisateur           /           utilisateur
   éphémère  65000 ---            éphémère
```
