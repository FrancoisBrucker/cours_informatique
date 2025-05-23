---
layout: layout/post.njk
title: "La file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[La file](https://fr.wikipedia.org/wiki/File_(structure_de_donn%C3%A9es))
{% endlien %}

La **_file_** est la structure de donnée idéale pour gérer un flux de donnée dont on doit conserver l'ordre. On appelle également cette structure **_FIFO_** pour _first in, first out_ : on rend toujours la donnée la plus anciennement stockée. La structure d'une file d'entiers sera alors :

```pseudocode
structure File<T>:
    attributs:
        taille: entier
        
        #  autres attributs
    méthodes:
        fonction enfile(donnée: T) → ∅  # push
        fonction defile() → T           # pop
        fonction nombre() → entier      # number

        fonction vide() → booléen       # empty
        fonction pleine() → booléen     # full
```

La taille de la file doit être déterminée à la création. Comme la pile, son implémentation nécessitera d'autres attributs.

{% attention "**À retenir**" %}

Une file est [un **_buffer_**](https://fr.wikipedia.org/wiki/M%C3%A9moire_tampon) permettant de découpler l'arrivée du traitement de données temporelles.
{% endattention %}

### <span id="structure"></span>Implémentation

On va utiliser 2 indices pour parcourir le tableau de stockage des données :

- un indice `fin`{.language-} permettant de savoir où ajouter le prochain élément
- un indice `début`{.language-} permettant de savoir quel prochain élément rendre

Ces deux indices coïncidaient pour la pile.

<span id="structure-file"></span>

```pseudocode
structure File<Type>:
    attributs:
        taille: entier
        
        T: [Type] ← [Type] de longueur taille
        début: entier ← taille - 1
        fin: entier ← 0
    méthodes:
        fonction enfile(donnée: Type) → ∅:
            T[fin] ← donnée
            fin ← (fin + 1) % longueur
        fonction defile() → Type:
            début ← (début + 1) % longueur
            rendre T[début]
        fonction nombre() → entier:
            rendre (fin - début - 1 + taille) % taille

        fonction vide() → booléen:
            si nombre() == 0:
                rendre Faux
            rendre Vrai
        fonction pleine() → booléen:
            si (nombre() == taille):
                rendre Vrai
            rendre Faux
```

On voit facilement que :

{% note "**Proposition**" %}
Les complexités de toutes les méthodes de la structure `File`{.language-} sont en $\mathcal{O}(1)$.

Utiliser une file peut se voire comme une opération élémentaire.
{% endnote %}

Prenons un exemple de file d'entiers pour comprendre comment cette implémentation fonctionne.

Départ :

```text
       f
          d
File : 0123
```

Ajout d'un élément 1 :

```text
        f
          d  
File : 0123
       1   
```

Ajout d'un élément 2 :

```text
         f
          d  
File : 0123
       12 
```

On défile un élément (1) :

```text
         f
       d  
File : 0123
        2 
```

Cette implémentation permet une gestion _circulaire_ des données.

{% exercice %}
Prolongez l'exemple précédent en enfilant successivement 3, 4, et 5 puis en défilant trois fois. Quel est l'état des indices après ces opérations ?
{% endexercice %}
{% details "corrigé" %}

État initial :

```text
         f
       d  
File : 0123
        2 
```

Enfile 3 :

```text
          f
       d  
File : 0123
        23 
```

Enfile 4 :

```text
       f   
       d  
File : 0123
        234 
```

Enfile 5 :

```text
        f   
       d  
File : 0123
       5234 
```

Défile (2) :

```text
        f   
        d  
File : 0123
       5 34 
```

Défile (3) :

```text
        f   
         d  
File : 0123
       5  4 
```

Défile (4) :

```text
        f   
          d  
File : 0123
       5    
```

{% enddetails %}

## Exemples

### Exemple : un buffer

Cet exemple montre l'usage classique d'une file. On traite de façon différée les entrées et les sorties dans l'ordre d'arrivée en stockant les données dans une file.

```pseudocode
buffer ← File<entier>  {taille: n}

fonction écrire(donnée: entier) → ∅:
    buffer.enfile(donnée)

fonction lire() → entier:
    rendre buffer.defile()
```

Ceci ce passe constamment lorsque l'on lit une vidéo, télécharge un fichier, etc.

La principale problématique est alors, quelle taille de file choisir pour ne pas perdre des données ?

Si la fréquence de lecture est inférieure à la fréquence d'écriture, pas de soucis. La taille de la file peut être de 1 entier : entre 2 écritures, on aura au moins une lecture.

Mais si la fréquence d'écriture est supérieure à la fréquence de lecture, il faut calculer **_la profondeur de file_** permettant de stocker la différence entre le temps d'écriture (qui remplit la file) et de lecture (qui la vide).

Ainsi si :

- $f_e$ est la fréquence d'écriture
- $f_l$ est la fréquence de lecture
- $K$ est le nombre d'entiers à transférer

On aura écrit les $K$ entiers en $K/f_e$ secondes alors pendant ce temps on aura uniquement lu $K\cdot f_l/f_e$ données. La taille $F$ de la file minimale est donc de la différence :

<div>
$$
F = K - K\cdot \frac{f_l}{f_e} = K(1-\frac{f_l}{f_e})
$$
</div>

Dans les cas réels, les données sont envoyés par _burst_ continu de $K$ entiers, puis des pauses permettant de lire la fin des données et de vider la file. Ceci permet d'avoir des tailles de buffer raisonnable même si la différence de lecture et d'écriture est grande.

{% lien %}
[Taille de file selon le problème de transfert](https://hardwaregeeksblog.wordpress.com/wp-content/uploads/2016/12/fifodepthcalculationmadeeasy2.pdf)
{% endlien %}

### Exemple : création des entiers binaires

On peut aussi utiliser la file comme outil d'énumération. Par exemple pour faire un compteur :

```pseudocode
algorithme compteur(n: entier) → ∅:
    F ← File<chaîne> {taille: K}
    F.enfile("1")
    i ← 0
    j ← 1
    répéter n fois:
        c ← F.défile()
        afficher à l'écran c
        si j < n:               # limite la taille de la pile
            F.enfile(c + "0")
            F.enfile(c + "1")
            j ← j + 2
```

L'algorithme va afficher les $n$ premiers entiers sous forme binaire. Il dépend d'une file de taille $K$.

{% exercice %}
Montrer que pour l'algorithme précédent fonctionne, il faut une file de taille au moins $\frac{n}{2}$.
{% endexercice %}
{% details "corrigé" %}

Lorsque l'on crée le $n$ème élément que l'on place dans la file, on le crée avec la chaîne de caractères $n_0\dots,n_k$ que l'on vient de sortir de la file.

Le $n$ nombre est alors de la forme $n_0\dots,n_k0$ ou $n_0\dots,n_k1$. Supposons sans perte de généralité que c'est $n_0\dots,n_k0$.

Comme on vient de sortir $n_0\dots,n_k = n/2$ de la file et qu'on y a placé $n_0\dots,n_k0 = n$, il y a bien $n/2$ élément dans la pile.

{% enddetails %}
