---
layout: layout/post.njk

title: Écrire du Code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[Un programme](../bases-théoriques/définition/#règles-générales) est un algorithme qui ne s'arrête pas forcément. On les décrit en algorithmie avec du [pseudo-code](../écrire-algorithmes/pseudo-code/) mais lorsque l'on veut exécuter ses programmes sur un ordinateur, on est obligé de transcrire le pseudo-code dans un langage de programmation (on utilisera le python dans ce cours) puis de l'exécuter sur un ordinateur.

Nous allons voir dans cette partie qu'écrire du code ou du pseudo-code est équivalent.


> TBD plan
> pseudo-code <=> langage (via compilateur : chaque langage est décrit par une grammaire <https://docs.python.org/fr/3.11/reference/grammar.html>
> <https://fr.wikipedia.org/wiki/Analyse_syntaxique> facile à fire. C'est pourquoi créer des programme est facile. Mais il ne font pas tous quelque chose et même parfois plantent (s'il font des division par 0 par exemple)
> TBD faire un exemple
> Si on peut écrire un interpréteur en pseudo-code, le langage est contenu dans ce qu'on peut faire en pseudo-code) <=> asm (pas de boucles) <=> taille fixe <=> von neumann
> 
> #### Langages informatiques

> TBD : le plus clair car le pseudo code s'écrit presque directement, par exemple en python
> TBD pas exécuté directement. Traduit en un autre langage compréhensible par ce qui va l'exécuter.
> TBD : compilé en langage machine (montrer des exemples). Souvent actuellement en byte code (module dis en python pour le voir <https://docs.python.org/fr/3/library/dis.html> ou <https://www.fevrierdorian.com/carnet/pages/python-sous-le-capot-chapitre-1-fonctionnement-de-la-vm-cpython.html>) qui est lui-même exécuté par une machine virtuelle.

> TBD :
> 1. interprété (python, js)
> 2. compilé :
>   1. pour la machine : C
>   2. bytecode : java, wasm
> 3. [ésotérique](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique) : brainfuck

#### Modèle de Von Neumann

> TBD : le langage des processeurs
> assembleur = transcription. Mais c'est déjà une interprétation
> nom => nombre, saut
> mais aussi le système va ajouter des chose pour être exécuté (elf)

#### Circuits logique

> TBD : <https://www.youtube.com/@CoreDumpped/videos>. <https://www.amazon.fr/Code-Language-Computer-Hardware-Software/dp/0137909101/ref=sr_1_1>
> TBD un processeur est codé en porte logiques,
>
> TBD tout est basé sur les opérations booléennes, logiques car algorithme = fonction booléenne.

> <https://people.csail.mit.edu/rrw/week1.pdf>
> <https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter9.pdf>
> sert pour la dé-randomisation : <https://www.youtube.com/watch?v=mZck0N_T9Cs>
> 
> Gros : <https://en.wikipedia.org/wiki/Circuit_complexity#History>
> TBD circuit logiques ?