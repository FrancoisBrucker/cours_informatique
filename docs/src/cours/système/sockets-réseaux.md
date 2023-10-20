---
layout: layout/post.njk

title: Sockets réseaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Connexion internet

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

### Socket

Communication entre un client et un serveur

> TBD : connexion au serveur:port -> un programme doit écouter ce port : le système ouvre le port pour une connexion

## ports

{% lien %}
<https://en.wikipedia.org/wiki/Port_(computer_networking)>
{% endlien %}

- `nmap` pour scanner les ports ouverts d'une machine (peut être considéré comme une aggression)
- `netstap -aln` port ouvert sur sa machine

### Connexion UDP

Pa de connexion à proprement parlé. Le système donne un port au client et il envoie directement des données au serveur qui lui répond et c'est tout.

<https://blog.cloudflare.com/everything-you-ever-wanted-to-know-about-udp-sockets-but-were-afraid-to-ask-part-1/>

> TBD exemple d'envoi de donnée UDP.

### Connexion TCP

{% lien %}
<https://fr.wikipedia.org/wiki/Three-way_handshake>
{% endlien %}

Le client tente d'établir une connexion sur un couple serveur:port (un port donné d'un serveur). Le système du client va attributer un port au client pour la connexion, puis tenter d'établir la connexion avec le serveur en effectuant ce qui est appelé le [Three-way_handshake](https://fr.wikipedia.org/wiki/Three-way_handshake) :

```
                syn
Client:port -----------> Serveur:port
               syn-ack
Client:port <----------- Serveur:port
                ack
Client:port -----------> Serveur:port
```

Si firewall il block les syn entrant : donc aucune communication n'est possible sur le port demandé de la machine.

Le firewall peut être configuré pour bloquer (ou non) les communications entrantes (ou sortantes) pour un port donné.

```
                 firewall
                  entrée
          |    syn   |
Client -- | -------->X --> Serveur:port
          |          |

```

Une fois la connexion TCP établie dans les deux sens :

- du client vers le serveur :
  - le stdin du client est envoyé sur le stdin du serveur
  - le stdout du serveur est envoyé sur le stdout du client
- du serveur vers le client :
  - le stdin du serveur est envoyé sur le stdin du client
  - le stdout du client est envoyé sur le stdout du serveur

### Protocole

Le protocole utilisé n'est qu'une convention. Ls socket est le même. Dans beaucoup de cas unix, ce protocole est en mode texte.

Exemple protocole [http](https://developer.mozilla.org/fr/docs/Web/HTTP). Etablissons une connexion  sur le serveur web de google sur le port 80 (port par défaut du protocole http):

```
 nc www.google.fr 80
```

On peut ensuite lui envoyer une demande :

```
GET / HTTP/1.1
Host: www.perdu.com


```

Et le serveur va répondre :

```
HTTP/1.1 200 OK
Date: Thu, 12 Oct 2023 11:57:50 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-yRqhcdSjJE0rRrP9buJJXQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: AEC=Ackid1Rd0P5DJ7_MjPiqO0noGNiVvrkyMu0iZOLjkqZ5u3p9UuDfXceMoQ; expires=Tue, 09-Apr-2024 11:57:50 GMT; path=/; domain=.google.fr; Secure; HttpOnly; SameSite=lax
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

4d94
<!doctype html>

[snip]
```

Http a des entêtes (clé: valeur) puis une ligne vide puis le body.

### socket Client / serveur

la commande [`nc`](https://doc.fedora-fr.org/wiki/Netcat,_connexion_client/serveur_en_bash) permet d'établir une connexion TCP à un serveur ou de créer un serveur.

Serveur :

```
nc -l -p 9090 127.0.0.1
```

Client (dans un autre terminal) :

```
nc 127.0.0.1 9090
```

Les stdin/out sont liés.

Nc n'admet qu'une connexion. POur créer un serveur acceptant plusieurs client, il faut utiliser une autre commande : [socat](https://www.redhat.com/sysadmin/getting-started-socat) :

```sh
#! /bin/sh

socat tcp-listen:9090,fork,reuseaddr \
'system:

echo "Le serveur écoute."

while read CLIENT_MESSAGE; do
  echo "le serveur répond : $CLIENT_MESSAGE"
done
'

```

## Amusons-nous avec la redirection de ports

### Une redirection de port

```
              22               22
so-high ---------  sas1  --------- roucas101.etu
```

La commande `ssh -L4000:roucas101.etu:22 fbrucker@sas1.ec-m.fr` depuis ma machine nommée so-high demande à :

1. faire une connexion ssh (depuis le port 22) sur le sas
2. que cette connexion fasse un lien entre :
   - le port 4000 de so-high
   - le port 22 de roucas101.etu

Ceci est possible puisque sas1 "voit" roucas101.etu et so-high.

En laissant cette connexion ouverte, dans un autre terminal on peut maintenant se connecter directement sur le port 22 de roucas101.etu (c'est à dire le démon ssh de roucas101.etu) en utilisant le port 4000 de so-high :

```
ssh -p4000 fbrucker@localhost
```

### Plusieurs redirection de port

On suppose que la première redirection est faite :

```
ssh -L4000:roucas101.etu:22 fbrucker@sas1.ec-m.fr`
```

Le port 4000 de so-high est le port 22 de roucas101.etu (via la connexion sas puisqu'il est impossible d'aller directement de l'un à l'autre)

On peut maintenant ramener un autre port de roucas101.etu sur notre machine, par exemple le port 9090 :

```
ssh -L9090:localhost:9090 -p4000 fbrucker@localhost
```

On effectue une connexion sur le port 4000 de localhost (qui est du coup aussi le port 22 de roucas101.etu) et on demande de faire une redirection du port 9090 sur cette machine sur notre machine locale.

Attention, il y a deux fois marqué `localhost` mains ce nest pas le même :

1. le deuxième localhost correspond à la machine qui se connecte, ici so-high
2. le premier localhost correspond à la machine connectée, ici roucas101.etu


Supposons que l'on ait un service uniquement accessible depuis roucas101.etu sur le port 9090. Par exemple une écoute de port (que vous aurez lancé depuis un autre terminal connecté sur roucas101.etu) :

```
nc -l -p 9090 127.0.0.1
```

On peut maintenant directement y accéder avec `nc 127.0.0.1 9090`

## outil de connexion

{% lien %}
<https://www.redhat.com/sysadmin/getting-started-socat>
{% endlien %}

- [nc](https://www.varonis.com/blog/netcat-commands)
- [shell server avec nc](https://jameshfisher.com/2018/12/31/how-to-make-a-webserver-with-netcat-nc/)

### echo serveur

```sh
#! /bin/sh

if [ -z "$1" ]; then 
    PORT=9090
else
    PORT=$1
fi

socat tcp-listen:$PORT,fork,reuseaddr \
'system:

echo "Le serveur écoute."

while read CLIENT_MESSAGE; do
  echo "le serveur répond : $CLIENT_MESSAGE"
done
'

```

### mono ligne

```sh
PORT=9090; socat tcp-listen:$PORT,fork,reuseaddr 'system: while read CLIENT_MESSAGE; do echo "le serveur répond : $CLIENT_MESSAGE"; done'
```

### echo à tous serveur

```sh
#! /bin/sh

rm /tmp/pns_* 2>/dev/null

if [ -z "$1" ]; then
    PORT=9090
else
    PORT=$1
fi

socat tcp-listen:$PORT,fork,reuseaddr \
'system:

PIPE=$(mktemp -u /tmp/pns_XXX)
ME=$(echo $PIPE | sed 's:/tmp/pns_::')
mkfifo $PIPE

while read PIPE_MESSAGE<$PIPE; do
  echo $PIPE_MESSAGE
done &
PID=$!

echo "je suis : $ME"
for EACH_PIPE in $(ls /tmp/pns_*); do
   [ $PIPE != $EACH_PIPE ] &&  echo "$ME est connecté" > $EACH_PIPE
done

while read CLIENT_MESSAGE; do
  for EACH_PIPE in $(ls /tmp/pns_*); do
    echo "Message de $ME : $CLIENT_MESSAGE" > $EACH_PIPE
  done
done
kill $PID
rm $PIPE
'

```

### client

Avec socat :

```sh
socat - TCP4:localhost:9090
```

Avec nc :

```sh
nc localhost 9090
```

### web server avec socat

> TBD en écrire un.

- [web minimal](https://gist.github.com/baleyko/003a089deb4f532552ef674e9ff4cea9)
- <https://fabianlee.org/2022/10/26/linux-socat-used-as-secure-https-web-server/>
- <https://stuff.mit.edu/afs/sipb/machine/penguin-lust/src/socat-1.7.1.2/EXAMPLES>

## bibliographie

- [Linux Networking-concepts HOWTO](https://www.netfilter.org/documentation/HOWTO/networking-concepts-HOWTO.html)
- [Beej's Guide to Network Programming Using Internet Sockets](https://beej.us/guide/bgnet/)
- <https://opensource.com/article/19/4/interprocess-communication-linux-networking>

## client serveur

1. socat : un serveur en shell qui répond à un protocole simple :
   1. répond hello à `hello`
   2. donne l'heure
   3. envoie un fichier s'il existe
2. node/express, flask, fastAPI :
   1. route index.html redirection vers /static/index.html
   2. une route qui calcule une somme
   3. un site static simple
   4. un js dedans qui appelle la fonction à calculer avec un /api/calcul
3. deux route en hop. Ramener le port 9090 de roucas sur localhost en suivant la route : localhost <-> ovh <-> sas1 <-> roucas101.

- <https://github.com/denehs/unix-domain-socket-example/blob/master/client.c>
- tcp socket
- <https://www.tala-informatique.fr/wiki/index.php/C_socket>
- [ntp client](https://seriot.ch/projects/tiny_ntp_client.html)
- [iphone firewall](https://www.nstec.com/how-to-disable-firewall-iphone-hotspot/)

## tbd

> en python : <https://www.youtube.com/watch?v=Ftg8fjY_YWU>

<https://www.geeksforgeeks.org/how-to-kill-a-detached-screen-session-in-linux/>


### cours web

remplacer screen par tmux.

Utiliser un shell que l'on sauve. Comme ça on peut y revenir, par exemple si virtualenv.

faire un exemple complet avec [virtualenv](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html)

faire plusieurs petits serveurs avec :

- shell
- python seul
- python + flask + virtualenv
- node seul
- node + express + package.json
