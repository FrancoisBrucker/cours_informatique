---
layout: layout/post.njk

title: Ports logiciel

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


La couche de transmission utilise pour cela la notion de [port](https://fr.wikipedia.org/wiki/Port_(logiciel)) :

{% note "**definition**" %}
Un ***port*** est un nombre entre 0 et $2^{16}-1 = 65535$ (codé sur 2B) associé à un système.

Le système peut associer une application à un port particulier via une [socket](https://fr.wikipedia.org/wiki/Berkeley_sockets), on dit que l'application ***écoute*** ce port.

- du point de vue de l'application : cette socket est un fichier ouvert (il a un file descriptor)
- du point de vue du système : toute communication réseau adressée à ce port est transmise en écriture au file descriptor de l'application.
{% endnote %}

Au final, caractériser la destination d'une communication réseau nécessite :

- un ordinateur
- 1 port

Les ports sont répartis en trois catégories, selon leurs usages :

- ***system ports*** (aussi appelés *well known ports*) de 0 à 1023 qui sont utilisés par le système
- ***user ports*** (aussi appelés ***registered ports***) de 1024 à 49151 utilisés soit par des protocoles connus soit pour un usage personnel
- [***Ephemeral port***](https://en.wikipedia.org/wiki/Ephemeral_port) (aussi appelés ***private ports***) de 49152 à 65535 utilisés par le système le temps d'une connexion.

Les ports systèmes sont associés à des protocoles réseaux indispensables et ne devant pas bouger. On peut citer :

- 22 : pour ssh
- 67 et 68 : dhcp
- 80 : http
- 443 : https

Lorsque le port n'est pas précisé dans une url, c'est le port part défaut du protocole qui est utilisé. C'est pourquoi : `curl http://www.google.fr` est équivalent à `curl http://www.google.fr:80`

{% faire %}
Tester les commandes `curl http://www.google.fr` et `curl http://www.google.fr:80` et vérifier quelles sont identiques.

Tester sur un autre port. Conclusion ?
{% endfaire %}

Pour communiquer, il faut à la fois une destination, mais aussi un point de départ. L'ordinateur émetteur de la communication nécessite également une socket, et donc un port dédié à cette communication. Comme ce port n'est nécessaire que le temps de la communication, le système utilise un port éphémère.

```
      A                             B 

    système             ----- 80 système
utilisateur           /          utilisateur
   éphémère  65000 ---           éphémère  
```

{% faire %}
Dans un Wireshark, récupérez la requête de `curl http://www.google.fr`. Regardez la couche Transmission. Quels sont les deux port utilisés ?
{% endfaire %}

Un communication réseau c'est donc deux sockets qui parlent entre elles via la couche de transport par ports interposés. On peut connaître tous les sockets de sa machine avec la commande :

```shell
netstat -aln
```

Attention, il peut y en avoir beaucoup.

Enfin, on peut scanner les ports d'une machine pour connaître les ***ports ouverts***, c'est à dire les ports associés à une socket, en utilsant la commande `nmap` :

```shell
nmap localhost
```

{% attention %}
Scanner les port ouvert d'une machine qui n'est pas la votre peut être considéré comme une aggression.
{% endattention %}
{% lien %}

- [tuto](https://hackertarget.com/nmap-tutorial/)
- [fonctionnement](https://www.malekal.com/types-scan-de-port-nmap/)

{% endlien %}
