---
layout: layout/post.njk 
title: "S6 : Informatique au concours"

eleventyNavigation:
  order: 4

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

Petit recueil de ce qui peut/est déjà tombé au concours.

## Programme de prépa

{% lien %}
- [Informatique commune](https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/textes/974-programme-informatique-xxsi.pdf)
- [Informatique MPI](https://www.cpgelachenal.fr/documents/Programme%20informatique%20MP2I-MPI.pdf)
{% endlien %}

## Oraux Concours Commun INP

Pas forcément un concours que vous passez, mais peut valoir le coup de regarder puisqu'il y a aussi des corrigés :

<https://www.concours-commun-inp.fr/fr/epreuves/les-epreuves-orales.html>

## QCM GEI
{% lien %}
<https://www.geiuniv.com/wp-content/uploads/2025/11/Reglement-GEI-UNIV-2026.pdf>
{% endlien %}

En page 5 du lien ci-dessus vous aurez les écoles qui prennent en compte l'informatique dans leurs QCM. C'est à dire presque toutes.

### Remarques générales

Au fil des années, les QCM changent de format : moins de C et plus de python. Depuis 2024 il y a même du pseudo-code pour les questions algorithmiques.

{% attention "avec le pseudo-code" %}
Ils prennent parfois (en tous cas pour quelques exemples en 2024, mais pas tous) la convention du [Cormen](https://www.amazon.fr/Introduction-%C3%A0-lalgorithmique-Thomas-Cormen/dp/2100031287) en faisant commencer les tableaux à l'indice 1.

Cela **ne devrait pas être le cas en 2025**, mais méfiez vous !
{% endattention %}

Lisez attentivement chaque question. Il y a de temps en temps des typos, des indentations fantaisistes, des incohérences. Prenez ça comme une feature et non un bug : elles sont là pour voir votre intuition/compréhension informatique. Arriver à comprendre l'esprit de la question, prenez de la hauteur.

{% attention "ne prenez pas la confiance" %}
Ce n'est pas parce que vous ne comprenez pas la question qu'il y a forcément une erreur...
{% endattention %}

### Méthode de résolution

Pour gérer un QCM il y a trois approches qui fonctionnent, par ordre de rapidité :

1. **Connaissance**. Vous reconnaissez l'algorithme, la notion : vous répondez directement la bonne réponse. **Attention** cependant à ne pas aller trop vite, il peut y avoir plusieurs réponses correctes et on est pas à l'abris d'un piège (il y en a...)
2. **Élimination**. On procède par élimination en supprimant itérativement les réponses incorrectes.
3. **Bourrinage**. Pour les questions algorithmiques, déroulez un exemple simple pour voir comment fonctionne l'algorithme et ce qu'il rend.

### Programme

De la [L1](/enseignements/MPCI/programmation-algorithmes/){.interne}, [L2](https://ametice.univ-amu.fr/course/view.php?id=129126) et [L3](/enseignements/MPCI/algorithmie-avancée/){.interne} et un peu de hors programme.

{% info %}
Au doigt mouillé, le cours de L1 doit vous permettre de répondre à prêt de la moitié des questions, le cours de L2 vous permet d'y ajouter un petit quart.
{% endinfo %}

#### Algorithmie

Tout le cours de L1 semble plus ou moins être au programme, ce qui correspond à la partie I du cours d'_algorithmie_ :

{% lien %}
[Partie I du cours d'Algorithmie](/cours/algorithmie/#partie-1){.interne}
{% endlien %}

En particulier :

- pseudocode
- tris
- complexité min, max et en moyenne ; différence entre complexité en temps et en espace
- pile/file

Il faut aussi connaître quelques algorithmes que GEI semble adorer :

- algorithme d'Euclide de calcul du pgcd.
- Bezout aussi appelé Euclide étendu (je crois). Nombre premiers.
- suite de Fibonacci
- la puissance $x^y$
- addition et soustraction binaire (c'est le même algorithme en complément à 2)
- suite de Syracuse
- méthode de chiffrement de César

#### Python

Questions souvent basique ou en lien avec un problème d'algorithmie. Relisez et comprenez la partie _Base de la programmation_ du cours _coder et développer_ :

{% lien %}
[partie Base du Cours Coder et développer](/cours/coder-et-développer/bases-programmation/){.interne}
{% endlien %}

#### Java

Le java n'est pas enseigné en MPCI, mais est présent au concours, en particulier pour le QCM de GIE.

Sarah a effectué un stage sous ma direction visant à apprendre le java et à donner des liens nécessaires aux MPCI pour qu'ils puissent eux aussi l'apprendre. Consultez son rapport pour vous permettre de bien vous préparer :

{% lien %}
[Rapport de Sarah sur son stage d'apprentissage de Java](Rapport_de_stage_KEGHIAN_2024.pdf)
{% endlien %}

En particulier faite attention aux mots clés suivant qui peuvent induire des pièges un peu retors :

- extends
- public et static
- self

#### C

Il ne reste presque plus de C, remplacé par du python dans les derniers QCM.

Je ne sais pas si c'est utile de réviser pour le peu de questions qu'il y a, mais vous pouvez toujours jeter un œil à la partie C du cours _système et réseau_ :

{% lien %}
[langage C](/cours/système-et-réseau/langage-c/){.interne}
{% endlien %}

#### Graphes

Quelques notions sur les Graphes et les arbres. Relisez le début du cours de graphe :

{% lien %}
[Cours de Graphe](/cours/graphes/){.interne}
{% endlien %}

En particulier :

- ordre et taille d'un graphe
- degré d'un sommet et d'un graphe
- graphes Eulérien et Hamiltonien
- graphe complet et connexe
- cycles et chemins
- arbre et forêt, ainsi que les définitions alternatives d'un arbre

Quelques algorithmes ont aussi à connaître :

- parcours en largeur/profondeur d'un graphe
- Dijkstra et son lien avec un parcours en largeur
- problème du voyageur de commerce
- coloration de graphe, en particulier l'algorithme glouton de Welsch et Powell (celui du cours)


> TBD. Chemins de Dyck. Ca tombe régulièrement aux concours (et plutôt en math d'ailleurs) Trouver exam centrale PC 2011 <https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021https://www.doc-solus.fr/prepa/sci/adc/bin/view.corrige.html?q=PC_MATHS_CENTRALE_1_2021>
>

## X

> TBD
> <https://www.lix.polytechnique.fr/Labo/Samuel.Mimram/teaching/INF551/>

## ENS

Le programme en informatique est celui des classes prépa :

{% lien %}

1. [Programme d'informatique tronc commun](https://prepas.org/ups.php?document=72)
2. [Annales écrits prépa](https://diplome.di.ens.fr/informatique-ens/annales.html)

{% endlien %}

Votre programme MPCI en informatique a une très forte intersection avec lui, donc pas de soucis. La seule partie que vous n'avez que peu vu sera [la programmation fonctionnelle en Ocaml](https://fr.wikipedia.org/wiki/OCaml), mais vous devez avoir les bases nécessaire en programmation fonctionnelle avec votre cours sur le lambda calcul

> TBD : tous les cours informatique MPCI à lister.

Ci après une annales des écrits/oraux à l'ENS Lyon :

{% lien %}

[Annales écrits filière universitaire Lyon](https://banques-ecoles.fr/cms/filieres-universitaires-second-concours-scientifique/)

{% endlien %}

Pour vous entraîner, refaites les exercices/projets durs en algorithmie et théorie des graphes.

> TBD donner la liste

## Centrale


{% lien %}
[concours universitaire](https://www.groupe-centrale.com/concours-universitaire/)
{% endlien %}

Le programme est gigantesque et regroupe tous les programmes de toutes les licences d'informatique (ainsi que de leurs options) de toute la France... Que vous n'ayez pas tout fait est normal !

Ne prenez pas peur : vous allez être interrogé sur une intersection entre votre programme MPCI et leur programme.

Donc :

1. lisez le programme en entier
2. faite l'intersection de ce que vous avez vu et le reste
3. révisez l'intersection commune
4. faire un check Wikipedia rapide sur les notions que vous n'avez pas vu, histoire de ne pas mourir idiot et de ne pas passer pour un inculte auprès de l'examinateur mais pas plus.

## Oraux/écrit Algorithmie

Vous pouvez tomber sur le même exercices aux mines ou à l'X/ENS. Ce qui changera c'est les indications et le nombre de questions intermédiaires. Mais en gros tout peut tomber, c'est pourquoi faire les QCM GEI est un bon exercice pour bien asseoir les bases qui vous seront nécessaires pour résoudre les problèmes plus dur..

Préparez vous en reprenant les cours et en comprenant les démonstrations. Ce sont souvent les mêmes chemins qui sont pris. On ne peut pas vous demander de trouver des preuves digne du [book](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK) ou la méga astuce algorithmique, mais vous devez montrer que vous connaissez votre sujet, connaissez les _trucs_ de bases et que vous avez un peu d'intuition (ce qui se travaille en cherchant les ressemblances entre les différentes techniques de preuve).

> TBD exercices oraux blanc

- enveloppe convexe
- variations et calcul sur 3-SUM
- sac à dos en programmation dynamique
- graphes bi-parti
- algorithme du lièvre et de la tortue pour :
  - détecter des cycles
  - trouver des doublons dans un tableau d'entiers ($n$ entiers dont les valeurs vont de $1$ à $n-1$) en $\mathcal{O}(n)$ opérations et $\mathcal{O}(1)$ en mémoire
