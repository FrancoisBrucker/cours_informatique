---
layout: layout/post.njk

title: Protocole http

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons illustrer ce type de protocole en utilisant le protocole http 1.1 encore très utilisé (et le dernier facilement manipulable).

{% lien %}
[Aperçu du protocole http](https://developer.mozilla.org/fr/docs/Web/HTTP/Overview)

{% endlien %}

Avec le protocole http le client est souvent un navigateur web, par exemple [chrome](https://fr.wikipedia.org/wiki/Google_Chrome), qui accède à l'application serveur via une [url](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) comme <http://www.google.fr>, qui lie le nom de la machine qui héberge le serveur (ici `www.google.fr`) et le protocole (http) : il n'y a qu'un seul serveur et de multiples clients.

Exemple de requête et de réponse en utilisant la commande [`curl`](https://curl.se/) :

```shell
$ curl http://www.google.fr 

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="fr"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type">

[snip]
```

On ne voit que la réponse du serveur, qui est la page web d'accueil de Google. Plus précisément on ne voit que la partie *body* du message http.

Tout message http est constitué de deux parties séparées par une ligne vide :

```
headers

body
```

De façon pratique, seule la partie *body* est utilisée puisqu'elle contient la page html, la partie headers contient des informations complémentaires, utiles au navigateur et c'est pourquoi curl ne l'affiche pas par défaut.

Affichons toute la réponse :

```shell
curl http://www.google.fr -s -D -

HTTP/1.1 200 OK
Date: Sun, 22 Oct 2023 11:48:07 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-sGPqt8KFPVp8rNGgfz-I9Q' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: AEC=Ackid1RFMolAVTxqHjvwg9GzsSPD8fcT1i7nKjUNCLbruMDT3tdfEZprh_E; expires=Fri, 19-Apr-2024 11:48:07 GMT; path=/; domain=.google.fr; Secure; HttpOnly; SameSite=lax
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="fr"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type">

[snip]
```

On voit bien la séparation entre la partie header et body.

De la même manière, une requête est composée d'un header et d'un body. Le body peut cependant être vide, comme c'est le cas de notre requête :

```shell
curl http://www.google.fr -s -v > /dev/null                                           
*   Trying [2a00:1450:4007:81a::2003]:80...
* Connected to www.google.fr (2a00:1450:4007:81a::2003) port 80 (#0)
> GET / HTTP/1.1
> Host: www.google.fr
> User-Agent: curl/8.1.2
> Accept: */*
> 

[snip]
```

{% faire %}
Avec Wireshark, attrapez la communication http lié à la commande

```shell
curl http://www.google.fr -s -v > /dev/null
```

Retrouvez les messages transmis (headers et body) de la requête et de la réponse.
{% endfaire %}

> TBD header GET + host en 1.1
> option nom:valeur
>
> body peut être ce que l'on veut. Aide avec le type mime.