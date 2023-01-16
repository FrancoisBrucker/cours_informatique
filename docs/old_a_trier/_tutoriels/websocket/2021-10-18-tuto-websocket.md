---
layout: layout/post.njk 
title:  "Tuto Websocket"
tags: websocket
authors: 
  - "Axel Chouraki"
  - "Jean Martinez"
---

Ce tutoriel explique comment utiliser le websocket pour créer un chat.

### Prérequis

* javascript
* html

## Fonctionnement du Websocket

Le protocole Websocket a été construit par dessus le protocole TCP. 
C’est donc un protocole réseau de la couche application (cf [modèle OSI](https://fr.wikipedia.org/wiki/Modèle_OSI)). 
Il permet d’ouvrir un canal de communication bidirectionnel sur un socket TCP. 
Un socket est une “prise” permettant à une application d’envoyer et de recevoir des données (et concrètement c’est une interface de programmation). 
Il permet donc de notifier au client un changement du côté serveur ou l’envoi de données du serveur vers le client sans avoir besoin de requête.

![image socket]({{ "/assets/tutos/websocket/socket.png" | relative_url }}){:style="margin: auto;display: block;width: 400px;"}

Pour cela, un handshake doit être réalisé. C’est une “négociation” des paramètres de connexion. 
Le client envoie une requête au serveur. Dans cette requête, tout ne se rapporte pas au websocket, mais elle peut demander des extensions de protocoles ou des sous-protocoles. 
On voit ci-dessous un exemple de requête du client. Le serveur renverra alors une réponse avec notamment la valeur hachée de la clé. 
On notera que le serveur peut également envoyer d’autres entêtes comme des demandes d’authentification, de création de cookies, etc…
Ce handshake est automatiquement réalisé avec les bibliothèques récentes.

![image handshake]({{ "/assets/tutos/websocket/handshake.png" | relative_url }}){:style="margin: auto;display: block;width: 500px;"}

Ce protocole est très utile pour beaucoup d'applications où les utilisateurs doivent se connecter en même temps comme une application de coopération en temps réel ou un jeu vidéo. 
Son architecture a, au début, été critiquée car il aurait mieux fallu résoudre les problèmes de la couche réseau au lieu de construire un protocole par dessus celui existant.

## Installations

*Toutes les commandes se font dans l'invite de commande (cmd) si vous êtes sous Windows.*

On créé le dossier du projet : `mkdir ChatWebsocket`

On se place dans le dossier : `cd ChatWebsocket`

On installe, nodemon qui permettra au serveur node de se relancer automatiquement pour prendre en compte les modifications :
`npm install --save-dev nodemon -g`

On installe la bibliothèque express pour réaliser le serveur : `npm install express`

On installe ws pour réaliser le seveur websocket : `npm install ws`


## Partie front

On va réaliser le front end. On crée un fichier index.html dans le répertoire du projet. On crée un titre :

```html
<h1>RealTime Chat</h1>
```

On ajoute un emplacement où lister les messages, un pour écrire des messages et un bouton pour envoyer un message :

```html
<pre id="messages" style="height: 400px; overflow: scroll"></pre>
<input type="text" id="messageBox" placeholder="Type your message here" style="display: : block; width: 100%; margin-bottom: 10px; padding: 10px;">
<button id="send" title="Send Message" style="width: 100%; height:30px;">Send Message</button>
```

Ensuite, dans une balise `<script> </script>`, on va écrire du javascript. 
On va créer une fonction qui va se lire dès la lecture du fichier. 
Pour cela, on utilise la syntaxe `(function() { //instruction })()`. 
Les `()` permettent de dire que l’on souhaite exécuter ce qu’il y a écrit avant celles-ci. 
Dans cette fonction, on initialise tout d’abord les variables. 
On récupère les éléments du front end en créant une variable qui contiendra l’objet websocket :

```html
<script>
    (function(){
        const sendBtn = document.querySelector('#send');
        const messages = document.querySelector('#messages');
        const messageBox = document.querySelector('#messageBox');

        let ws;
     })()
</script>
```

Mettons dans cette fonction une fonction qui affiche les messages sur la page :

```html
    function showMessage(message){
        messages.textContent += '\n\n' + message
        messages.scrollTop = messages.scrollHeight;
        messageBox.value = '';
    }
```

Ajoutez à cela, toujours dans la fonction, la fonction **init**. 
Celle-ci doit initialiser notre objet websocket et détruire l’ancien s’il existe :

```html
    function init(){
        if(ws){
            ws.onerror = ws.onopen = ws.onclose = null;
            ws.close();
        }

        ws = new WebSocket('ws://localhost:8999');
        ws.onopen = () => {
            console.log('Connection opened');
        }
```

Ici on utilise le port 8999 pour le websocket. Les fonctions **onopen**, **onerror**, etc... sont des fonctions qui sont exécutées lorsqu’un évènement est déclenché (plus d’informations [ici](https://fr.wikipedia.org/wiki/Programmation_événementielle)). 
Ainsi, **onopen** s'exécute lorsque le client se connecte au serveur websocket, la fonction **onclose**, lorsque la connexion se coupe et la fonction **onmessage**, lorsque le client reçoit un message. 
Ajoutons ces deux dernières fonctions dans la fonction **init** :

```html
    ws.onmessage = ({ data }) => {
        var textToDisplay = fromDataToText(data); 
        showMessage(textToDisplay);
    }
    ws.onclose = function(){
        ws = null;
    }
```

La fonction **onmessage** reçoit en argument le message reçu. 
Rappelons nous que le message est encapsulé, il faut donc le traiter avant de l’afficher. 
On ajoute donc cette fonction dans la fonction **init** :

```html
    function fromDataToText(data){
        var array = JSON.parse(data);
        array = array.data;
        var text = "";
        array.forEach(element => text += String.fromCharCode(element));
        return text;
    }
```

JSON.parse renvoie un objet et le texte recherché est contenu dans son attribut data. 
Ce data est un tableau de int qui sont les lettres du message en ASCII, d’où la boucle et l’utilisation de la fonction fromCharCode.

Il nous manque juste une fonction qui envoie le message au serveur lorsqu'on clique sur le bouton *Send Message* :

```html
    sendBtn.onclick = function(){
        if(!ws){
            showMessage("No Websocket connection");
            return
        }

        ws.send(messageBox.value);
    }
```

Enfin, il ne faut pas oublier d’exécuter la fonction **init** qui n’a été que rédigée jusque là :

```html
    init();
```

Si vous vous êtes un peu perdu, voici le script final de index.html :

```html
<h1>RealTime chat</h1>

<pre id="messages" style="height: 400px; overflow: scroll"></pre>
<input type="text" id="messageBox" placeholder="Type your message here" style="display: : block; width: 100%; margin-bottom: 10px; padding: 10px;">
<button id="send" title="Send Message" style="width: 100%; height:30px;">Send Message</button>

<script>
    (function(){
        const sendBtn = document.querySelector('#send');
        const messages = document.querySelector('#messages');
        const messageBox = document.querySelector('#messageBox');

        let ws;

        function showMessage(message){
            messages.textContent += '\n\n' + message
            messages.scrollTop = messages.scrollHeight;
            messageBox.value = '';
        }

        function init(){
            if(ws){
                ws.onerror = ws.onopen = ws.onclose = null;
                ws.close();
            }

            ws = new WebSocket('ws://localhost:8999');

            ws.onopen = () => {
                console.log('Connection opened');
            }

            ws.onmessage = ({ data }) => {
                var textToDisplay = fromDataToText(data); 
                showMessage(textToDisplay);
            }

            ws.onclose = function(){
                ws = null;
            }

            sendBtn.onclick = function(){
                if(!ws){
                    showMessage("No Websocket connection");
                    return
                }

                ws.send(messageBox.value);
            }

            function fromDataToText(data){
                var array = JSON.parse(data);
                array = array.data;
                var text = "";
                array.forEach(element => text += String.fromCharCode(element));
                return text;
            }
        }

        init();
    })()
</script>
```

## Partie back

Dans le fichier ChatWebsocket, créer un fichier server.js et inscrire dedans :

```javascript
'use strict';
const http = require('http');
const express = require('express');
const WebSocket = require('ws');

const app = express();
const port = 8999;

//initialize a simple http server
const server = http.createServer(app);

//initialize the WebSocket server instance
const wss = new WebSocket.Server({ server });


wss.on('connection', (ws) => {
//connection is up, let's add a simple simple event
    ws.on('message', (message) => {

        //log the received message and send it back to the client
        console.log('received: %s', message);

        //send back the message to the other clients
        wss.clients.forEach(function each(client) {
            if (client.readyState === WebSocket.OPEN) {
                client.send(JSON.stringify(message));
            }
        });
    });
});

server.listen(port, function() {
    console.log("Server is listening on "+ port);
})
```

Expliquons ce qu’il se passe (quelques commentaires aident à la compréhension). 
Le `'use strict'` passe le script en mode *strict* ce qui, entre autres, fait passer quelques warnings en erreurs et permet une exécution plus rapide.
Ensuite on réalise les importations. On a besoin de :
* http : une bibliothèque standard pour le web
* express : une bibliothèque très utilisée pour créer des serveurs
* ws : une bibliothèque permettant de créer des serveurs websocket

On crée ensuite l’application express et on définit le port qu’elle utilisera. 
On initialise le serveur et on initialise une instance d’un serveur websocket.
On donne ensuite à la fonction wss.on un argument qui déterminera l'évènement choisi et une fonction qui sera exécutée lorsque l'évènement sera appelé. 
Ici, cet évènement 'message' correspondra à l'envoi d'un message avec `ws.send(messageBox.value)` dans la fonction *sendBtn.onclick* du fichier html.

Les instructions console.log permettent d’afficher des chaînes de caractères dans la console du navigateur (clic droit -> inspecter -> onglet console), et sont surtout utiles lors du développement (debug). 
On itère ensuite parmi les clients, on vérifie que la connexion est ouverte et on envoie le message que l’on encapsule dans un json (pour éviter que ce soit un objet blob généré). 
Enfin, on indique au serveur d’écouter les requêtes sur le port défini plus tôt avec la fonction listen.

On va maintenant lancer le serveur. Dans une console cmd, dans le répertoire du fichier server.js, lancer le serveur avec :
`nodemon server.js`

La commande `node server.js` fonctionne également mais si vous comptez changer le code, je vous conseille nodemon. 
Il ne faut pas fermer la console tant qu’on travaille, cela éteindrait le serveur.

#### Sources

* [https://www.xul.fr/html5/websocket.php](https://www.xul.fr/html5/websocket.php)
* [https://www.youtube.com/watch?v=RL_E56NPSN0](https://www.youtube.com/watch?v=RL_E56NPSN0)
* [https://github.com/websockets/ws](https://github.com/websockets/ws)
* [https://fr.wikipedia.org/wiki/WebSocket](https://fr.wikipedia.org/wiki/WebSocket)
* [https://developer.mozilla.org/fr/docs/Web/API/WebSockets_API/Writing_WebSocket_servers](https://developer.mozilla.org/fr/docs/Web/API/WebSockets_API/Writing_WebSocket_servers)