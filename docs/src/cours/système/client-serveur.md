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

### Connexion TCP

Si firewall il block les syn entrant : donc aucune communication n'est possible sur le port demandé de la machine.

Le firewall peut être configuré pour bloquer (ou non) les communications entrantes (ou sortantes) pour un port donné.

```
                 firewall
                  entrée
          |    syn   |
Client -- | -------->X --> Serveur:port
          |          |

```

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

Nc n'admet qu'une connexion. Pour créer un serveur acceptant plusieurs client, il faut utiliser une autre commande : [socat](https://www.redhat.com/sysadmin/getting-started-socat) :

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
