---
layout: layout/post.njk
title: "Projet : implémentation des algorithmes d'exponentiation"

eleventyNavigation:
  prerequis:
    - /cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/débogueur/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On vérifie expérimentalement que nos calculs théoriques sont validés expérimentalement. On codera et testera nos algorithmes, donc vérifiez que vous avez les prérequis.

## Mise en place

On va utiliser les méthodes d'écriture de code déjà vues. Pour une piqûre de rappel :

{% prerequis %}
[Écrire du code](/cours/coder-et-développer/apprendre-programmation/coder-projets/écrire-code/)
{% endprerequis %}

### Structures

{% faire %}

1. créez un dossier nommé `exponentiation`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier
3. créez dans ce dossier les 3 fichiers de la trinité du code :
   - `main.py`{.fichier}
   - `exponentiation.py`{.fichier}
   - `test_exponentiation.py`{.fichier}
{% endfaire %}

### Vérifications

{% faire %}

- on vérifie que python est OK avec le terminal et avec vscode
- on vérifie que le linter est actif dans vscode
- on vérifie que les tests fonctionnent (en créant un test bidon dans `tests_exponentiation.py`{.fichier} et en vérifiant que `pytest` et vscode le trouvent)

{% endfaire %}

## Le code

### Algorithme naif

{% faire %}

- dans le fichier `exponentiation.py`{.fichier} : implémentez [l'algorithme naïf itératif](../étude-algorithmique/#algorithme-puissance-naif) dans une fonction nommée `puissance_naif`{.language-} (utilisez des noms explicites).
- dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme naïf itératif :
  - vérifiez que les cas simples avec nombre et/ou exposant à 1 fonctionnent
  - vérifiez qu'un cas général est correct (comme $2^3$ par exemple)

Vérifier que vos tests se lancent bien dans le terminal.

{% endfaire %}

Pour les tests, on utilisera les règles suivantes :

{% retenir %}

Organisation des tests :

- un fichier de test par fichier de code. Chaque fichier de test sea nommé : `test_[nom du fichier de code].py`{.fichier} où _[nom du fichier de code]_ sera le nom du fichier (ne mettez pas les _[]_)
- chaque test sera nommé en 3 parties : `test_[nom de la fonction_testée]_[ce que l'on teste]`{.language-} où `[nom de la fonction_testée]`{.language-} est le nom de la fonction testée (ne mettez pas les `[]`) et `[ce que l'on teste]`{.language-} une description succincte (en 1 ou 2 mots max) de ce que l'on teste.
- un test doit tester **une unique chose**. On peut se permettre d'avoir plusieurs `assert`{.language-} par fonction de test du moment que ce qu'on test peut être qualifié par un nom précis (la partie `[ce que l'on teste]`{.language-} du nom de la fonction de test)

{% endretenir %}

Terminons cette partie en utilisant le débogueur :

{% faire %}

Dans le programme principal, calculez l'exponentiation d'un entier par un autre (ces entiers pourront être issus de deux variables ou demandées à l'utilisateur), puis rendez la.

En utilisant le débogueur, vérifiez l'invariant de boucle (pour pourrez utiliser un espion et un log breakpoint).

{% endfaire %}

### Algorithme rapide

{% faire %}

- dans le fichier `exponentiation.py`{.fichier} : implémentez [l'algorithme rapide](../étude-algorithmique/#algorithme-puissance-indienne) dans une fonction nommée `puissance_rapide`{.language-}
- dans le fichier `test_exponentiation.py`{.fichier} : implémentez les tests de l'algorithme rapide en faisant les mêmes tests que pour l'algorithme naïf.

Vérifier que vos tests se lancent bien dans le terminal.

{% endfaire %}

Terminons cette partie en utilisant le débogueur :

{% faire %}

Dans le programme principal, calculez l'exponentiation d'un entier par un autre (ces entiers pourront être issue de variables ou demandés à l'utilisateur), puis rendez la issue du calcul rapide.

En utilisant le débogueur, vérifiez que l'invariant de boucle est vérifié (pour pourrez utiliser un espion et un log breakpoint).

{% endfaire %}

### Programme principal

{% faire %}

Créer un programme principal (dans le fichier `main.py`{.fichier}) qui demande à l'utilisateur un exposant $n$. Ce programme donne ensuite résultat et le temps mis (utilisez le chronomètre [`time.perf_counter_ns`{.language-}](https://docs.python.org/fr/3.15/library/time.html#time.perf_counter_ns) pour mesurer le temps avant et après exécution du code) pour exécuter $3^n$ avec l'algorithme naïf et avec l'algorithme rapide.

{% endfaire %}

## Mesure de complexité

On va utiliser ce que l'on a fait lorsque l'on a appris à mesurer des complexités :

{% prerequis %}
[Mesures de complexités](../../../2-complexités/complexité-code/)
{% endprerequis %}

Commençons par ajouter nos méthodes de mesures :

{% faire %}

1. Ajoutez [le fichier `mesure_temps.py`{.fichier}](../../../2-complexités/complexité-code/#fichier-mesure-temps) au projet.
2. Créez un fichier `main_temps.py`{.fichier} qui va contenir notre code de mesure.

{% endfaire %}

### Temps de calcul

{% faire %}

Dans le fichier `main_temps.py`{.fichier} déterminez l'exposant max pour  calculer $3^n$ en 0.1 secondes.

{% endfaire %}
{% info %}
Je trouve `N_max = 6553`{.language-} sur mon ordinateur.
{% endinfo %}

On peut maintenant représenter les courbes de complexité :

{% faire %}
Dans le fichier `main_temps.py`{.fichier}, procédez comme dans le cours pour afficher la courbe de complexité de l'algorithme naïf (faites 10 mesures).
{% endfaire %}
{% info %}
Je trouve `N_max = 6553`{.language-} sur mon ordinateur.
{% endinfo %}

La courbe devrait être linéaire alors qu'elle ne l'est pas. [On a déjà vu ce phénomène](../../../2-complexités/projet-code/#nombres-gigantesques), corrigeons le :

{% faire %}

Dans le fichier `exponentiation.py`{.fichier}, commentez la ligne effectuant la multiplication et refaite le graphique.
{% endfaire %}

Comme les multiplication de nombres gigantesques seront aussi effectués par l'exponentiation rapide et que l'on veut que notre algorithme calcule bien ce qu'il doit faire :

{% faire %}
 Dé-commentez la ligne effectuant la multiplication et assurez vous que les tests passent.
{% endfaire %}

On peut maintenant voir le temps mis pour l'exponentiation rapide :

{% faire %}
En gardant le `N_max`{.language-} déterminé en utilisant l'algorithme naïf, procédez comme dans le cours pour afficher la courbe de complexité de l'exponentiation indienne  (faites 10 mesures).
{% endfaire %}

Maintenant que l'on a les deux graphiques séparé, on peut rassembler les deux graphiques :


{% faire %}
Mettez les mesures pour l'algorithme naïf et rapide sur le même graphique 
{% endfaire %}

Le temps mis par l'exponentiation rapide est très inférieur à celui effectué par l'algorithme d'exponentiation naif, on ne le voit pratiquement pas (la courbe semble toute plate).

{% faire %}
Utilisez le code de [ce lien](https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html#multiple-yaxis-with-spines){.externe} pour utiliser `ax.twinx`{.language-} qui permet de partager l'axe des abscisse en ayant deux axes des ordonnées et permettre de voir les 2 courbes,chacune ayant son axe des ordonnées.

Vous pourrez également changer la couleur d'un des dessins en ajoutant le paramètre `color="orange"`{.language-} d'un des 2 plot par pour dessiner en orange.

{% endfaire %}
