---
layout: page
title:  "Projet numérologie : niveau 1 - front (code js)"
category: cours
author: "François Brucker"
---


> TBD : en chantier
{: .note}


## structure du projet

### dossiers

* dossier : *"numérologie-niveau-1"* :
    * fichier : *"mes_tests_.js"*
    * dossier : *"user stories"*
      * fichier : *"connaitre-son-numero.md"*
      * fichier : *"todo.md"*

### todos

Il faut tout faire :

- [ ] associer un chiffre à un nom
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter



## première tâche

> Quelle est la tâche la plus simple à réaliser dans notre todo ?

Le cœur du projet est d'associer un numéro à un nom, donc autant essayer de faire ça en javascript.

> On modifie le fichier todo/md pour refléter le fait qu'on travaille sur cet item : 
{: .note}

- [X] associer un chiffre à un nom
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

Bon c'est pas encore très détaillé. Comment faire ça ? 

1. déjà un nom c'est une chaine de caractère codée en utf-8
2. on peut prendre le numéro unicode/utf8 de chaque caractère et les sommer
3. il faut un chiffre donc comment passer d'un nombre à un chiffre ?
4. on peut sommer les chiffre du nombre pour obtenir un autre nombre strictement plus petit ($10.x + y < x + y$) et recommencer la procédure si ce n'est pas un chiffre.


Ajoutons nos réflexions à la todo list (fichier *"todo.md"*) :

```markdown
- [X] associer un chiffre à un nom
    - [ ] numéro unicode/utf8 d'un caractère
    - [ ] sommer des numéro des caractères d'une chaine de caractères
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter
```

> Au passage, vous avez vu comment on a mis des maths dans du markdown ? Lorsque vous transformerez le markdown en html, [Mathjax](https://www.mathjax.org/) rendra ces équations toutes jolies.

> Quel est l'item le plus simple à résoudre ?
{: .note}

A mon avis c'est lui :

- [X] associer un chiffre à un nom
    - [X] numéro unicode/utf8 d'un caractère
    - [ ] sommer des numéro des caractères d'une chaine de caractères
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

> On va aller plus vite dans ce cours ensuite. Mais lidée est tojours la suivante :
> dans votre todolist vous devez avoir un item qui vous semble *facile* à résoudre.
> Si ce n'est pas le cas, c'est que vous items sont trop gros et qu'il faut les décomposer en unité plus fine.

### tests js

On va commencer par faire des petits tests en js pour voir comment on peut résoudre notre tâche (trouver les bonnes méthodes à utiliser), puis un codera la fonction proprement dite.

On peut faire les tests dans un interpréteur node s'ils sont tout petit (on peut utiliser le node dans un terminal vscode par exemple), ou bien exécuter un programme de test. 

On va préférer la première option ici car il nous faut juste découvrir la méthode [`charCodeAt`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt) :
```javascript
fbrucker@emma cours/numerologie-niveau-1 » node             
Welcome to Node.js v16.9.0.
Type ".help" for more information.
> ('coucou').charCodeAt(1)
111
> ('你好').charCodeAt(0)
20320
```

> 'o' c'est de l'ascii et a donc gardé un petit nombre, '你' c'est un [sinogramme](https://unicode-table.com/fr/4F60/) de numéro unicode U+4F60 ce qui en décimal vaut `parseInt("4F60", 16)`
(qui est l'inverse de `(20320).toString(16)`, testez-le...)

> que vaut le code unicode de `꧁` ?
{: .note}


### code js

Fort de nos expérimentations, on peut maintenant écrire un fichier *"numerologie.js"* qui va rendre la somme de tos les code unicode de ses caractères le constituant.

> Je jette ici un voile pudique sur ce qu'est un "caractère" dans une chaine unicode. Cela peut vite être [très compliqué](https://fr.wikipedia.org/wiki/%C3%89quivalence_Unicode). 

Fichier *"numerologie-niveau-1/numerologie.js"* :

```javascript
function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += sommeFinale(chaine.charCodeAt(i))
    }
    return somme
}
```

### updade toto

Note todo devient : 

- [X] associer un chiffre à un nom
    - [X] numéro unicode/utf8 d'un caractère
    - [X] sommer des numéro des caractères d'une chaine de caractères
    - [ ] sommer les chiffre d'un nombre
    - [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


On a bien progressé.

