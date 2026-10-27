---
layout: layout/post.njk

title: "Projet : mesurer la complexité d'un code"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un moyen efficace de mesurer la complexité d'un code est de mesurer le temps qu'il met à être exécuté. Pour la mesure soit conforme à la complexité il faut que :

1. les instructions basiques durent un temps similaire pour le processeur,
2. l'on ait un moyen efficace de mesurer le temps
3. le système ne doit exécuter que l'algorithme et n'avoir aucun autre [processus concurrent](https://fr.wikipedia.org/wiki/Programmation_concurrente) (en temps partagé).
4. les paramètres d'entrées doivent  :
  - réaliser le maximum si on cherche à mesurer la complexité (maximum),
  - réaliser le minimum si on cherche à mesurer la complexité minimum,
  - être aléatoire si on cherche à mesurer la complexité moyenne.

{% info %}
On présuppose que vous avec fait les prérequis du cours d'algorithmie, en particulier que vous savez coder en python et/ou que vous avez suivi [le cours d'introduction à python](/cours/coder-et-développer/apprendre-programmation/), en particulier les parties 1 et 2.
{% endinfo %}
{% prerequis %}
- [Installation d'un ide et de modules python](/cours/coder-et-développer/apprendre-programmation/coder-projets/outils/)
- [Écriture de projets informatique](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/)
{% endprerequis %}

## Comment mesurer la complexité

Reprenons les 4 conditions que l'on vient d'expliciter.

> TBD prendre recherche comme exemple.

### 1. temps processeur

> TBD en 2 temps : le proc. Ajouter que prédiction font que de toute façon des variation
> temps 2 ajout de la couche python. Parler de bytecode. Certaines instruction longues et d'autre courte.

> TBD instruction python vs instruction basiques et temps qu'ils mettent pur s'en sortir.

#### instruction python
 
> TBD ici dire byte code python. Et on montre le résultat.
> TBD temps pour addition.

#### instructions processeur

Les instructions du processeur sont très différentes du pseudo-code tel que nous l'avons vu. Outre le cadencement (la vitesse) du processeur, les différentes instructions ne prennent pas le même temps : certaines sont très rapides, un test booléen par exemple, d'autres prennent "_beaucoup_" de temps, comme lire une donnée depuis la mémoire. Enfin les instructions diffèrent selon le type de processeur : les processeur intel (en gros les PC) sont ainsi des [processeur CICC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_%C3%A9tendu) qui possèdent des instructions complexes et les processeur ARM (portables, tablettes et mac) sont à contrario des [processeurs RISC](https://fr.wikipedia.org/wiki/Processeur_%C3%A0_jeu_d%27instructions_r%C3%A9duit) avec peu d'instructions mais toutes de même temps.



En pratique ceci importe peu puisque cela va influer sur les constantes additives et multiplicatives du code, pas sur l'allure générale de la courbe : on cherchera à optimiser le code processeur qu'après avoir choisi le bon algorithme et on ne le fera jamais directement, on laissera le compilateur faire.

{% retenir %}
Même si les instructions processeurs sont très différentes du pseudo-code et que leur durée d'exécution n'est pas homogènes, mesurer le temps permet d'avoir l'allure générale de la courbe de complexité.
{% endretenir %}


### 2. mesure du temps

On possède de deux outils pour mesurer le temps :

- une horloge : <https://docs.python.org/fr/3.15/library/datetime.html>
- un chronomètre : <https://docs.python.org/fr/3.15/library/time.html#time.perf_counter_ns>

Le premier va rendre une date (ce que l'on cherche est un temps et faire des différences de date est compliqué), dépendante du [fuseau horaire](https://fr.wikipedia.org/wiki/Fuseau_horaire) et  finalement moins précise (à la microseconde prêt) qu'un chronomètre (à la nanoseconde prêt).

> TBD exemple de code.

### 3. Isoler l'algorithme du système

> TBD ramasse-miette. MOntrer ce qu'il fait. IL NE FAUT PAS L'ENLEVER ! Sinon la mémoire voir se remplir.
> 3. voir que sur 5 essais ça change un peu : prendre le min

## Paramètres

> TBD recherche
> TBD faire sauvegarde fichier (pdf et png)
>   - recherche (retrouve-t-on les graphiques du cours ?)
>   - dichotomique en log
> 1. boucles /n = cte sum_{k \leq i \leq n}

> 4. faire varier k aléatoirement et montrer que du coup il faut prendre la moyenne.
>   - boucles imbriquées dépendantes = n^2

## A vous

### Mot de 01

> égalité mots de 01
> max/moyenne ?
> TBD faire les tests et séparer main et fct pour qu'ils puissent reprendre le code fait dans les prochains tds.

### Max chgt
> 
> TBD nb de mise à jour du maximum. 
> 1. calcul max
> 2. nombre de mise a jour de l'algo simple : Max n et en moyenne ln(n) (Knuth) (avec les main le prochain > est à la moitié.)




> TBD pour aller plus loin
> TBD ajouter pyperf pour les perf d'un programme et cprofile pour le profilage des bootleneck <https://www.stephane-robert.info/docs/developper/programmation/python/profiling/>
> 3. modif pour mise a jour dans une fonction et vérifier que cprofile ou pyperf le voit

>


## Maximum d'un tableau

{% aller %}
[Création et preuve de l'algorithme maximum récursif](../../1-algorithme/projet/#algorithme-max-tableau-rec)
{% endaller %}

<span id="algorithme-max-tableau-complexité"></span>
{% exercice %}
 Donnez sa complexité de l'algorithme `maximum_rec`{.language-}.

{% endexercice %}
{% details "corrigé" %}

Toutes les lignes de l'algorithme sont en $\mathcal{O}(1)$ à part la récursion. Comme la récursion est faite sur la taille du tableau, on va noter $C(n)$ sa complexité où $n$ est la taille du tableau passé en paramètre. Elle satisfait alors l'équation :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1)
$$
</div>

On a vu en cours que cette équation se résout en : $C(n) = \mathcal{O}(n)$.

{% enddetails %}