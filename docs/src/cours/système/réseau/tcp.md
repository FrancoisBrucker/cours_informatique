---
layout: layout/post.njk

title: Protocole TCP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le protocole TCP permet une communication sûre et ordonnée entre deux applications. Il est donc utilisé pour des communication où chaque donnée est importante et où l'ordre dans lequel sont envoyé des paquets doit être respecté (pour l'envoi de fichiers par exemple).

{% lien %}
[protocole TCP](https://fr.wikipedia.org/wiki/Transmission_Control_Protocol)
{% endlien %}

Ce protocole est certainement le plus utilisé sur internet. D'un point de vue protocole, TCP est bien plus compliqué que UDP car il garantit non seulement l'exactitude des données mais également :

- que toutes les données envoyées sont reçues
- que l'ordre d'envoi et de réception des données soient conservé
- que les données sont envoyées le plus rapidement possible

Tout ceci sans congestionner le réseau.

## Entête TCP

L'[entête de chaque paquet TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure) est de taille variable. On retrouve les données de l'entêtes UDP :

- le port de départ (2B)
- le port destination (2B)
- un checksum du message (2B)
- taille du header TCP (4b)

Notez que la taille du message n'est pas directement donnée, mais peut être déduite de la taille du header (allant de 20B à 60B) et de la taille du paquet de la couche IP qui le contient.

S'y ajoute des informations permettant la communication sûre et ordonnée :

- numéro de séquence
- numéro d’acquittement
- des FLAGS de type de paquets (SYN, ACK, FIN)

Nous passerons sous silence le reste des champs, moins important pour une compréhension globale du système.

## Transfert de données

{% faire %}
Retrouver avec Wireshark la connexion http liée au `curl http://www.google.fr`.

La réponse du serveur est constituée de plusieurs paquets TCP, tous (sauf le dernier) de payload 1208. Les retrouver.

Vous devriez voir :

- les numéros de paquet augmenter (à partir d'un début qui ne vaut pas 0)
- les réponses du client qui envoie des requêtes ACK au serveur.

{% endfaire %}
{% info %}
La taille totale du ficher html transmis peut être encodé dans l'entête http (c'est l'option `Content-length`), ou si elle n'est pas connu à l'avance, déterminée dynamiquement grâce à l'option [Transfer-Encoding: chunked](https://fr.wikipedia.org/wiki/Chunked_transfer_encoding) (c'est le cas de cette requête).
{% endinfo %}

Une connexion TCP se fait sous un mode client-serveur bi-directionnelle. Elle contient 3 phases :

1. **connexion** entre le client et le serveur
2. **transmission** du serveur ver le client ou du client vers le serveur
3. **fin** de l'un des deux participants

### Connexion

Initier une connexion TCP se fait avec le (fameux) *three-way handshake* :
{% lien %}
<https://fr.wikipedia.org/wiki/Three-way_handshake>
{% endlien %}

```
                SYN
Client:port -----------> Serveur:port
               SYN-ACK
Client:port <----------- Serveur:port
                ACK
Client:port -----------> Serveur:port
```

1. Le client demande une SYNchronisation avec le serveur.
2. le serveur ACKnowledge cette demande et demande lui aussi une SYNchronisation avec le client
3. Le client ACKnowledge à son tour cette demande.

Une fois ces trois paquets transmis, le client et le serveur sont prêt à envoyer/recevoir des données. D'un commun accord, la transmission des données peut commencer.

{% info %}
Une fois que la connexion est établie, le flag ACK est toujours positionné.

Il n'est important qu'à l'établissement de la connexion.
{% endinfo %}

{% faire %}
Reprenez avec Wireshark la connexion http liée au `curl http://www.google.fr`, et cherchez le three-way handshake de la connexion.
{% endfaire %}

### Transmission

Comme la transmission TCP est bi-directionnelle, le client et le serveur peuvent s'envoyer des messages. Les deux programmes ont deux numéros et qui rendent comptes du nombre de bytes envoyés (***numéro de séquence***) et reçus (***numéro d'aquittement***).

Si tout se passe comme prévu, les nombres doivent coïncider :

```
    A                       B

envoyé : X               envoyé : Y
reçu   : Y               reçu   : X
```

#### Envoi et bonne réception d'un paquet

Supposons que A envoie un paquet de K bytes à B. Dans l'entête de ce paquet :

- le numéro de séquence sera X
- le numéro d’acquittement sera Y

A met alors à jour ses données envoyées :

```
    A                       B

envoyé : X+K             envoyé : Y
reçu   : Y               reçu   : X
```

Lorsque B reçoit ce paquet, il envoie un paquet d'acquittement qui rendra compte de la bonne reception du paquet. L'entête de ce paquet d'acquittement aura :

- son numéro de séquence sera Y+K (il a bien reçu K données de plus)
- le numéro d’acquittement sera X

Et B met à jour ses données reçues :

```
    A                       B

envoyé : X+K             envoyé : Y
reçu   : Y               reçu   : X+K
```

Enfin, lorsque A reçoit le paquet d'acquittement, il sait que B a bien reçu toutes les données qu'il a envoyé.

Il est nécessaire de garder les deux numéros car en même temps que A envoie des données à B, B peut envoyer des données à A.

{% faire %}
Reprenez avec Wireshark la connexion http liée au `curl http://www.google.fr`, et cherchez y les 2 transferts :

1. client vers serveur demandant le GET
2. serveur vers client donnant le fichier html

{% endfaire %}
{% info %}
Vous pouvez restreindre l'affichage des paquets à ceux qui vous intéresse. Dans ma session, le port éphémère était le 52765, j'ai donc tapé dans la barre de filtre : `tcp.srcport == 52675 or tcp.srcport == 80`
{% endinfo %}

#### Temporisation

Il n'est pas nécessaire ni surtout utile de répondre à chaque paquet reçu. Souvent le récepteur attend quelque temps avant de répondre. Ceci lui permet :

- de ne pas envoyer des paquets d'acquittement inutiles
- de laisser du temps pour remettre dans l'ordre des données dans le cas où elles arriveraient dans le désordre

Ce temps d'attente avant réponse doit être supérieur au temps nécessaire pour une donnée de faire l'aller et le retour entre l'émetteur et le récepteur. Cette valeur est actualisée au cours de la connexion.

{% faire %}
Reprenez avec Wireshark la connexion http liée au `curl http://www.google.fr`. Vous devriez voir que le client ne renvoie que très peu de packets d'acquittements par rapport aux paquets qu'il reçoit.

{% endfaire %}

### Fin

La fin d'une transmission se fait comme la connexion, d'un commun accord. L'initiateur de la fin de la connexion peut être soit le client, soit le serveur.

```
                FIN
initiateur -----------> récepteur
               FIN-ACK
initiateur <----------- récepteur
                ACK
initiateur -----------> récepteur
```

{% info %}
Le récepteur peut accuser réception de la demande de fin, sans envoyer dans le même paquet sa propre demande de fin.
{% endinfo %}

Terminer d'un commun accord permet de finaliser les paquets envoyés et de s'assurer que les paquets envoyés sont bien les paquets reçu avant de stopper la communication.

{% faire %}
Reprenez avec Wireshark la connexion http liée au `curl http://www.google.fr`. Vous devriez voir la procédure de fin initiée par le client.

{% endfaire %}

## Retransmission

Deux types de paquets peuvent se perdre.

### Perte d'un paquet d'acquittement

Si l'émetteur ne reçoit pas un acquittement de la part du récepteur, il va renvoyer le paquet suivant le dernier acquittement reçu.

De son côté le récepteur, lorsqu'il va à nouveau recevoir un paquet déjà pris en compte il va renvoyer un paquet d'acquittement correspondant au nombre de byte déjà reçu, c'est à dire au-delà du paquet re-émis.

Si ce paquet arrive à l'émetteur cela va resynchroniser le tout (et sinon cette étape va recommencer).

### Perte d'un paquet émis

A chaque paquet reçu, le récepteur va envoyer un acquittement du dernier paquet reçu. Il va donc envoyer le même acquittement à chaque fois que l'émetteur va envoyer un paquet.

Recevoir 2 fois le même acquittement est un signe pour l'émetteur que le récepteur n'a pas reçu tous les paquets envoyés.

## Gestion de la vitesse de transmission

### Buffer récepteur

Lors d'un paquet d'acquittement, le récepteur indique le nombre de byte restant dans son buffer, c'est à dire le nombre de byte qu'il peut recevoir avant que l'émetteur ne doivent attendre un paquet d'acquittement avant de ré-envoyer des données.

### Contrôle de la congestion

{% lien %}

[transmission tcp rate](https://www.youtube.com/watch?v=LfiRKZze0HM&list=PLhy9gU5W1fvUND_5mdpbNVHC1WCIaABbP&index=32)

{% endlien %}

Si le réseau est saturé, tous les émetteurs vont constamment renvoyer des données, ce qui va à son tour ajouter de la congestion : les FIFOs des routeurs ne se désengorgent pas. Pour éviter ça :

1. le débit initial est très bas (slow start)
2. puis il augmente rapidement jusqu'à la première perte de paquet.
3. On divise alors le débit par deux et on le réaugmente lentement jusqu'à la prochaine perte de paquet
4. on revient en 1.

```
           perte de paquets
          |               |
débit     |               |
^         v               v
|
|         X            ___X
|        /|      ___---   |
|       / |___---         |   /
|      /   (croissance    |  /
|     /     additive)     | /
|    /                    |/
-------------------------------------------> temps    
|    ^                    ^
     |                    | 
           slow start  
  (croissance exponentielle)
```

Ce contrôle dynamique de la vitesse de transmission de données permet de s'adapter au réseau sans le casser.
