---
layout: layout/post.njk

title: UDP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[protocole UDP](https://fr.wikipedia.org/wiki/User_Datagram_Protocol)
{% endlien %}

Communication simple entre deux sockets. Le header du packet est de taille 8B et contient :

- le port de départ (2B)
- le port destination (2B)
- la longueur du message (2B)
- un checksum du message (2B)

Il n'y a aucune garantie de réception du message, mais si le message arrive à destination le [checksum](http://profesores.elo.utfsm.cl/~agv/elo322/UDP_Checksum_HowTo.html) garantit son exactitude. Si le checksum de l'entête ne correspond pas au checksum du message reçu, le paquet est éliminé (*discard*).

{% faire %}
Créez dans un terminal une socket qui écoute en udp avec la commande `nc` : `nc -u -p 5050 -l -s localhost`. Dans un autre terminal, entamez une connexion avec `nc -u localhost 5050`.

Les stdin/out sont liés. Si vous tapez dans un terminal, cela s'écrira dans l'autre.
{% endfaire %}
{% info %}
Sous macos, la commande pour le serveur change : `nc -l -u localhost 5050`
{% endinfo %}
{% faire %}
Dans un Wireshark, récupérez la connexion et vérifiez que les headers udp correspondent.
{% endfaire %}
{% info %}
Il vous faudra écouter le réseau loopback, puisque les données sont envoyées et reçu sur votre ordinateur sans passer par internet
{% endinfo %}

Comme il n'y a a pas de vérification qu'un paquet est bien arrivé, ni de garanties sur l'ordre d'arrivée des paquets, on utilise souvent UDP pour de petits envois (pouvant passer dans un seul paquet), récurrents, de données que l'on peut se permettre de perdre de temps en temps. Par exemple :

- les requêtes DNS
- les informations actualisées d'un joueur de jeu réseau
- le stream de vidéos

Le principal intérêt de l'UDP est sa rapidité.
