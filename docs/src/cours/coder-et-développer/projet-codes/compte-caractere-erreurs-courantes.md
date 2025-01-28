---
layout: layout/post.njk

title: "Erreurs courantes : le compte est bon"
---

Je n'ai pas vraiment eu d'erreurs surprenantes. Ce sont des erreurs de débutant et elles sont de deux types :

- une mauvaise compréhension des mécanismes : ça se travaille et vient avec l'expérience
- croire que l'on peut produire du code de qualité et qui marche sans l'exécuter : l'humilité s'apprend aussi avec l'expérience

## Recoder des fonctions

La majorité d'entre vous n'avez pas lu la documentation de la méthode `find`. Du coup vous l'avez recodé, le plus souvent avec des erreurs...

Vous ne perdez pas de temps à comprendre et lire de la documentation. Votre code sera plus clair, plus facile à utiliser et avec moins de bug si vous utilisez les fonctions et méthodes que python met à votre disposition. Apprendre à lire de la documentation vous fera gagner un temps fou !

{% note %}
Pour lire une documentation, en particulier savoir quels sont les paramètres d'une fonction lisez [cette partie du cours](/cours/coder-et-développer/bases-python/fonctions-méthodes/#paramètres).
{% endnote %}

Enfin, on utilise les fonctions testées dans le programme principal. On vous demande de coder des fonctions (et de les tester), ce n'est pas pour rien... Utilisez les !

## Ne pas exécuter son code

De nombreuses erreurs auraient pu être évitées si vous aviez exécuté votre code : programme principal et surtout tests ! L'interpréteur et surtout `pytest` sont meilleurs que l'esprit humain pour voir rapidement les erreurs : cela plante ou rend un résultat incohérent.

Pour que cela fonctionne, il faut faire en sorte de **toujours** pouvoir exécuter votre code :

- écrire **une** ligne du programme principal puis l'exécuter
- écrire **une** fonction puis son test à la fois puis exécuter les tests.

Loin de vous ralentir cela vous fera repérer et corriger rapidement les erreurs. Entraînez vous et vous verrez.

## Ne pas utiliser black pour écrire du code agréable à lire

Cette erreur est inexcusable. Black est accessible à partir d'un raccourci clavier et fonctionne parfaitement. Cela rendra votre code plus lisible pour vous et pour le correcteur.

## Utiliser le typage des fonctions

Préférez définir vos fonctions sans le typage :

- on préférera écrire ça : `def donne_prochain_indice(chaine, indice):`{.language-} puis le reste de la définition de la fonction
- à ça : `def donne_prochain_indice(chaine: str, indice: int) -> int:`{.language-} qui est plus lourd et n'apporte pas grand chose à la lisibilité.

Le typage a bien sur son utilité dans la documentation ou lorsque l'on veut définir précisément les paramètres (pour un test ou en algorithmie par exemple), mais dans le code où la fonction va être utilisée tout de suite après c'est inutile et rend la définition plus dure à lire.

## Erreurs rares

Mais qu'il faut tout de suite arrêter de faire :

- pas de `from fonctions import *` dans le programme principal car on ne sait pas ce qu'on importe
- les commentaires ne se font pas avec `""" ..."""`. Les commentaires en python s'écrivent avec `#`. Si l'on veut commenter plusieurs lignes à la fois vscode a une commande pour cela : `menu édition > afficher/masquer le commentaire de ligne`. On l'utilise tellement souvent qu'il y a souvent un raccourci clavier en plus.
