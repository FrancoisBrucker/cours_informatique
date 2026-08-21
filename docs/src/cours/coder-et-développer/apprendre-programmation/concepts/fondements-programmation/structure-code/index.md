---
layout: layout/post.njk

title: Structure de contrôle en python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Lorsque l'on veut plus que juste utiliser des méthodes et fonctions déjà existantes et que notre code puisse agir différemment selon les objets qu'il manipule : il faut pouvoir  structurer son code en parties utilisables indépendamment, que ce soit sous la forme de code (bloc, fonctions) ou de données (conteneurs).

{% info %}
Rappelez vous qu'il y a 2 exemples de code :

- ceux commençant par un `>>>`{.language-} dont le but est d'être directement exécuté dans [un interpréteur](./principes/interpréteur/){.language-} et dont on verra directement le résultat de chaque instruction,
- les programmes dont le but est d'être exécuté via un éditeur et qui consisteront la grande majorité des exemples donnés.
{% endinfo %}

Python structure son code en [_blocs_ d'instructions](./#bloc){.interne} qui permettent diverses façon de [faire des tests](./#test){.interne} ou de [de répéter du code](./#boucle){.interne}.


## <span id="bloc"></span> Bloc de code

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en blocs.

{% note2 "**Définition**" %}

Les **_blocs_** en python permettent de grouper des lignes de code qui seront exécutées ensemble sous certaines conditions. Un bloc est toujours défini de la même manière :

- Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`{.language-}
- Les instructions le constituant.

{% endnote2 %}

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type_de_bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre :

- d'exécuter des blocs conditionnellement
- de répéter des blocs

Les blocs peuvent bien sur se combiner :

```text
bloc A:
    instruction 1 du bloc A
    bloc B:
        instruction 1 du bloc B
        ...
        instruction m du bloc B
    instruction 2 du bloc A
    ...
    instruction n du bloc A
```

{% attention2 "**À retenir**" %}
L'indentation permet **toujours** de s'y retrouver.

{% endattention2 %}
{% info %}
<span id="interpréteur-blocs"></span>

Lorsque l'on crée un bloc avec l'interpréteur, après la première ligne qui défini le bloc (la ligne avec le `:`{.language-}.
), l'interpréteur passe en _mode bloc_ (il écrit `...` en début de ligne) ce qui permet d'écrire son bloc (en n'oubliant pas l'indentation). Une fois le bloc terminé, pour faire repasser l'interpréteur en mode normal et exécuter le bloc on appuie juste sur la touche entrée pour insérer ue ligne vide.

Par exemple l'exemple suivant crée un bloc qui écrit `coucou`{.language} indéfiniment directement dans l'interpréteur :

```python
>>> while True:
...     print("coucou")
...
```

Le même bloc écrit dans un éditeur puis exécuté aurait été écrit comme ça :

```python
while True:
    print("coucou")
```

{% endinfo %}

## <span id="test"></span>Instructions conditionnelles

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-if-statement>
{% endlien %}

Permet d'exécuter un bloc si une condition logique est vraie :

```python
if <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
elif <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
else:
    instruction 1
    instruction 2
    ...
    instruction n
```

Notez qu'il peut y avoir autant de bloc `elif`{.language-} que l'on veut (même 0) et qu'il n'est pas nécessaire d'avoir de `else`{.language-}.

{% exercice %}
Demandez à l'utilisateur de rentrer un entier au clavier (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}) et de répondre "C'est entre 2 et 8" si le nombre rentré est entre 2 et 8 et de répondre "ce n'est pas entre 2 et 8" sinon.
{% endexercice %}
{% details "solution" %}

```python

entier = int(input("Un entier entre 2 et 8 : "))
if 2 >= entier and entier <= 8:
    print("C'est entre 2 et 8")
else:
    print("ce n'est pas entre 2 et 8")
```

{% enddetails %}

{% exercice %}
Demandez à l'utilisateur de rentrer deux entiers au clavier (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}) et de d'afficher à l'écran si le deuxième est un diviseur du premier (vous pourrez utiliser les [opérateurs](../écrire-code/#opérateurs){.interne} de division entière)
{% endexercice %}
{% details "solution" %}

```python


a = int(input("Un entier : "))
b = int(input("Un entier : "))

if a % b == 0:
    print(b, "divise", a)
else:
    print(b, "ne divise pas", a)
```

{% enddetails %}
{% exercice %}
Demandez à l'utilisateur de rentrer un entier au clavier (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}) et de d'afficher à l'écran la saison associé au mois si l'entier est entre 1 et 12 et répondre que l'entrée est invalide sinon.
{% endexercice %}
{% details "solution" %}

```python


a = int(input("Un entier représentant un mois : "))

if 3 <= a <= 5:
    print("printemps")
elif 6 <= a <= 8:
    print("été")
elif 9 <= a <= 11:
    print("automne")
elif 1 <= a <= 12:
    print("hiver")
else:
    print("votre entier ne représente pas un mois de l'année")
```

On a utilisé le fait que :
- python autorise les expressions de type `x < y < z`{.language-}, équivalente à `(x < y)  and (y< z)`{.language-}.
- pour l'hiver, comme on utilise une structure en `elif`{.language-} la seule possibilité pour `a` est de valoir 12, 1 ou 2 si `1 <= a <= 12`{.language-}

{% enddetails %}

## <span id="boucle"></span>Répétitions

Deux types de boucles existent en python : les boucles _tant que_ (`while`{.language-}) et les boucles _pour chaque_ (`for`{.language-})

### <span id="while"></span>Bloc `while`{.language-} : boucle tant que

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-while-statement>
{% endlien %}

```python
while condition_logique:
    instruction 1
    instruction 2
    ...
    instruction n
```

Par exemple le bloc `while`{.language-} suivant :

```python
b = 6
while b > 0:
    print(b)
    b = b - 1
```

qui va afficher :

```text
6
5
4
3
2
1
```

{% exercice %}
Demandez à l'utilisateur de rentrer un entier au clavier (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}) tant que celui-ci n'est pas égal à 42.
{% endexercice %}
{% details "solution" %}

Il y a deux solutions à ce problème. La première consiste à différentier la première entrée des autres :

```python
a = int(input("Donnez un entier : "))

while a != 42:
    a = int(input("Donnez un entier : "))
```

La seconde est de forcer l'entrée dans la boucle :

```python
a = 0

while a != 42:
    a = int(input("Donnez un entier : "))
```

Selon les cas, on préférera l'une ou l'autre solution. Ici c'est équivalent.

{% enddetails %}
{% exercice %}
Calculez la factorielle de 45.
{% endexercice %}
{% details "solution" %}

```python
factorielle = x = 45

while x > 1:
    x -= 1
    factorielle = factorielle * x

print(factorielle)
```

{% enddetails %}
{% exercice %}
Affichez tous les diviseurs d'un nombre demandé à un utilisateur (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}), et ne s'arrêter que lorsque
{% endexercice %}
{% details "solution" %}

```python
a = int(input("Donnez un entier : "))
b = 1
while b < a:
    if a % b == 0:
        print(b, "divise", a)
    b += 1

```

{% enddetails %}

### <span id="for"></span>Bloc `for`{.language-} : boucle pour chaque

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-for-statement>
{% endlien %}

```python
for <nom> in <itérable>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Le bloc sera exécuté pour chaque élément de l'_itérable_. A chaque exécution, l'élément courant de l'itérateur sera nommé `<nom>`{.language-}.Certaines fonctions vont créer des itérables, la plus connue étant certainement la fonction range que l'on va voir juste après, et certains objets également, comme les chaînes de caractères ([les objets conteneurs](../../conteneurs){.interne} comme les listes, les ensembles ou les dictionnaires que l'on verra plus tard fonctionnent également).

L'exécution du code suivant :

```python
for c in "bonjour":
    print(c)
```

Donnera :

```python
b
o
n
j
o
u
r
```

La boucle for itère sur chaque caractère de la chaîne `"bonjour"`{.language-} et le place dans la variable nommée `c`{.language-}. La valeur de `c`{.language-} vaut donc successivement les caractères `"b"`{.language-}, `"o"`{.language-}, `"n"`{.language-}, `"j"`{.language-}, `"o"`{.language-}, `"u"`{.language-} et enfin `"r"`{.language-}.

{% exercice %}
Écrire un programme qui affiche un mot entrée par un utilisateur (en utilisant la [fonction `input`{.language-}](../écrire-code/#input){.interne}) à l'envers (vous pourrez utiliser le fait que l'[addition de deux chaînes de caractères](../écrire-code/#opérateurs-str){.interne} en python est la concaténation).

{% endexercice %}
{% details "solution" %}

```python

s = input("Tapez une chaîne de caractères :")
s2 = ""
for c in s:
    s2 = c + s2

print(s2)
```

{% enddetails %}


## <span id="range"></span>La fonction range


{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/stdtypes.html#range>
{% endlien %}

L'itérateur le plus utilisé pour les boucle `for`{.language-} est le résultat de la fonction `range`{.language-} qui crée un itérateur de nombres.

Par exemple :

```python
for x in range(10):
    print(x)
```

Affichera les 10 premiers entiers (de 0 à 9). Le résultat de `range(10)`{.language-} est un objet de type range, qui est fait pour être utilisé avec l'instruction for.

{% attention2 "**À retenir**" %}

On peut utiliser la fonction `range`{.language-} de trois façons différentes qu'elle soit appelée avec un, deux ou trois paramètres :

- de `0`{.language-} à juste avant `paramètre`{.language-}. Par exemple `range(10)`{.language-} rendra un itérateur de la suite des 10 entiers allant de 0 à 9.
- de `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}. Par exemple `range(4, 10)`{.language-} rendra un itérateur de la suite des 6 entiers allant de 4 à 9.
- `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}, avec un saut de `troisième paramètre`{.language-}. Par exemple `range(10, -1, -1)`{.language-} rendra un itérateur de la suite 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.

{% endattention2 %}
{% exercice %}
Écrire un programme qui affiche la table de 9 :

```text
1 x 9 =  9
2 x 9 =  18
3 x 9 =  27
4 x 9 =  36
5 x 9 =  45
6 x 9 =  54
7 x 9 =  63
8 x 9 =  72
9 x 9 =  81
10 x 9 =  90
```

{% endexercice %}
{% details "solution" %}

```python

for nombre in range(1, 11):
    print(nombre, "x 9 = ", nombre * 9)
```

{% enddetails %}

{% exercice %}
Écrire un programme qui calcule la somme des chiffres de 1 à 100.

{% endexercice %}
{% details "solution" %}

```python

somme = 0
for k in range(1, 101):
    somme += k
print(somme)
```

{% enddetails %}



{% exercice %}
Afficher à l'écran les 16 premiers entiers, allant de 0 à 15
{% endexercice %}
{% details 'solution' %}

```python
for i in range(16):
    print(i)

```

{% enddetails %}
{% exercice %}
Afficher à l'écran les 13 entiers, allant de 3 à 15
{% endexercice %}
{% details 'solution' %}

```python
for i in range(3, 16):
    print(i)

```

{% enddetails %}

{% exercice %}
Afficher à l'écran les multiples de 3 allant de de 3 à 15
{% endexercice %}
{% details 'solution' %}

```python
for multiple_trois in range(3, 16, 3):
    print(multiple_trois)

```

{% enddetails %}

Le troisième paramètre de la fonction range n'est pas obligatoirement positif. Ceci permet de compter à rebours :

{% exercice %}
Afficher à l'écran les entiers allant de 5 à 0, dans cet ordre.
{% endexercice %}
{% details 'solution' %}

```python
for x in range(5, -1, -1):
    print(x)

```

{% enddetails %}

{% exercice %}
Utilisez ce que vous avez appris pour vérifier la [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour les 100 premiers entiers.
{% endexercice %}
{% details "solution" %}

```python

for x in range(100):
    while x > 1:
        if x % 2  == 0:
            x /= 2
        else:
            x = 3 * x + 1
```

{% enddetails %}

