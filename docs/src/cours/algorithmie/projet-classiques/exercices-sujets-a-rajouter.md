---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD regardez tous les exos d'avant et le remettre s'ils sont chouettes, genre ceux des piles/file, fibo, etc. Et ajouter les questions suivantes si nécessaire.


## Decurryfications

> TBD McCarty, Ackerman, etc.

#### Ackermann, le retour

Essayons de voir comment écrire l'algorithme d'Ackermann sans toutes ces récurrences, comme on l'a fait avec la fonction 91.

Pour calculer $\text{Ack}(m, n)$ :

1. soit $m=0$ alors $A = n+1$
2. soit $m>0$ et $n=0$ et alors $A = \text{Ack}(m-1, 1)$
3. soit $m>0$ et $n>0$ et alors :
     1. $A = \text{Ack}(m, n-1)$
     2. $A = \text{Ack}(m-1, A)$

On voit que ce n'est pas une formulation récursive terminale à cause du troisième cas. En 3.2 :

- on utilise la valeur de $A$ calculée en 3.1
- on utilise la valeur que valait $m$ avant 3.1

Il faut donc se rappeler de $m$ pour le calcul de 3.2 tout en utilisant la valeur de $A$ calculée précédemment. Pour ce genre de récursion, on peut utiliser une [TODO list](https://fr.wikipedia.org/wiki/To-do_list) qui nous permet de nous rappeler toutes les tâches à effectuer et des variables à sauvegarder :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs et $A$ à 0
3. on ajoute à la liste le triplet (1, m, n)
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste)
      1. si le premier élément de l'item vaut 1 alors on affecte :
         1. $m$ au second élément du triplet
         2. $n$ au troisième élément du triplet
      2. si le premier élément vaut 2 alors on affecte :
         1. $m$ au second élément du triplet
         2. $A$ à $n$
   2. On fait le calcul :
      1. si $m=0$ alors $A=n+1$
      2. si $m>0$ et $n=0$ alors on ajoute $(1, m-1, 1)$ à la TODO list
      3. si $m>0$ et $n>0$ alors :
          - on ajoute $(2, m-1)$ à la TODO list
          - on ajoute $(1, m, n-1)$ à la TODO list
5. rendre $A$

> TBD faire $A(2, 3)$

On peut même se passer de $A$ complètement :

1. on commence avec une TODO liste vide
2. positionner les variables $m$ et $n$ à leurs valeurs
3. on ajoute à la liste l'entier $m$
4. tant que la TODO liste n'est pas vide :
   1. prendre le dernier item de la list (en le supprimant de la liste) et en l'affectant à $m$
   2. On a un choix selon les valeurs de $m$ et $n$ :
      - si $m=0$ alors $n=n+1$
      - si $m>0$ et $n=0$ alors (récursion terminale):
          - $n = 1$
          - ajoute l'entier $m-1$ à la TODO  List
      - $m>0$ et $n>0$ alors :
          - ajoute l'entier $m-1$ à la TODO  List
          - ajoute l'entier $m$ à la TODO  List
          - $n=n-1$
5. rendre $A$

{% info %}
Implémentation en python en utilisant une liste comme TODO-list :

```python
def Ack(m, n):
    s = [m]
    while (s):
        m = s.pop()
        if m == 0:
            n += 1
        elif n == 0:
            s.append(m - 1)
            n = 1
        else:
            s.append(m - 1)
            s.append(m)
            n -= 1
        return n
```

{% endinfo %}

> pas récursivité terminale = il faut faire des trucs en plus de la récursion. Il faut se rappeler de que l'on veut faire. Avec une TODO list (faire exemple avec ack petit) = pile en informatique
> faire un item de la todo list = dépile.
>

> 
> truc à faire = empile
> <https://www.cs.odu.edu/~zeil/cs361/latest/Public/recursionConversion/index.html#conversion-using-stacks>
> 1. curryfication puis decurryfication
> A(m, n) = A(0, n')
> A'(s, n) = A'(s[:-1], A(s[-1], n))
> A'([m], n) = A(m, n) par récurrence sur m+n = k
>
> TBD faire la preuve que c'est ok (voir <https://stackoverflow.com/a/54356919>)

{% info %}
Notez que tout algorithme récursif peut s'écrire de façon itérative avec une TODO-list (une pile).
{% endinfo %}

## Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>

- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

### Corrigé Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>

- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

## Algorithmes arithmétique

- addition de listes de chiffres
- multiplications de listes de chiffres

(- [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba))

## Matrices

- structure
- addition
- produit par un scalaire
- produit naïf

(- [produit de Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen))

## Odds and ends


> TBD faire un lien avec les exos vu en écriture d'algo + complexité pour que tout soit aussi là.

> TBD lièvre et lapin.
