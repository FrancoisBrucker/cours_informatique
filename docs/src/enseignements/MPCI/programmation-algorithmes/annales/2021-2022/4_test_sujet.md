---
layout: layout/post.njk 

title:  "sujet Test 4 : classes et objets"
authors:
    - François Brucker
---


## 1

Un morceau (musique, vidéo, ...) est représenté par un objet d’une classe `Morceau`{.language-} précisant son titre et sa durée. Ces deux informations seront transmises au moment de la construction de l’objet. Donnez le diagramme UML (sous la forme d'une liste) de cette classe.

## 2

Écrivez en python un programme principal (c’est à dire que l’on suppose la classe Morceau déjà écrite) qui crée un Morceau dont le titre est *cure toujours* d’une durée de 2 minutes 52.

## 3

Une Playlist est composée d’une liste de Morceaux de musique ou de vidéos. On créera une
Playlist en précisant une liste de Morceaux. Donnez le diagramme UML de cette classe et la nature de son lien avec la classe `Morceau`{.language-}.

## 4

Proposez deux fonctionnalités supplémentaires que devrait avoir la classe Playlist.

## 5

Ajoutez dans le modèle UML de la playlist les méthodes/attributs permettant d'utiliser les fonctionnalités que vous avez proposées.

## 6

Proposez des tests unitaires permettant de vérifier qu'une des fonctionnalités que vous avez ajoutées est correcte.
