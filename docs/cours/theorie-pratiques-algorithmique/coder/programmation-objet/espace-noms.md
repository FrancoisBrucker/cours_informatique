---
layout: page
title:  "espaces de noms"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [programmation objet]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/index.md %}) / [espace de noms]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/espace-noms.md %})
{: .chemin}


faire des dessins ave des tableau (mémoire) et des objets (d'abord dans la méméoire puis des liens.)
1. memoire = tableau de 1 octet.
2. valaible = endroit dans la mémoire
3. soucis : combien de case mémoire pour chaque objet. Dépedn de l'objet (ex des entier 16, 32 ou 64 bit er qu'est ce qu'il se passe si on fait +1)
4. on change de point de vue : on ne donne que des "références" vers les objets (vous entendrez souvent ça chez les boomer de l'informatique :-). 
5. objet est stocker dans la mémoire. Il est unique, mais on meut le référence plein de fois.
6. respace de noms = lien entre variable et objet
7. si un objet n'est plus dans aucun espace de nom il disparait (on libère de la méméoire). Ex.
8. pluseirus espaces de noms, il faut pouvoir s'y retrouver. 
   1. lorsque l'on crée on crée dans l'espace le plus proche.
   2. Si on ne le trouve pas on remonte
   3. ex de la création de fonction. 
      1. espace de nom par défaut
      2. lorsque l'on exécute une fonction on crée un espace de nom
      3. on y place les entrées
      4. à la fin de la fonction, on supprime l'espace de nom si on en a plus besoin.
9. règle des espaces de noms
10. exemples d'espace de noms: 
   1.  fnction
   2.  modules
   3.  objets et classes (on va le voir
11. ex 2 : fonction de fonctions. O garde l'espace de nom car on en a encore besoin

   
Comment rendre compte d'une variable, et de la portée de celles-ci

> * variable != objet (à répéter 20000 fois)
> * les noms représentes des objets
> * que des variables globales c'es nulles : variables dans les fonctions (c'est le cas par défaut en javascript)
> * quelle portée choisi ? Le bloc for ? non, la fonction ? les modules ?
> * comment savoir quelle variable utiliser si les espaces de noms s'embriquent?
> * et comment de temps en temps modifier un objet au-dessus
> * donner des exemples récursifs
{: .tbd}