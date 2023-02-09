---
layout: layout/post.njk

title:  "DM 1 : Suite de nombres"
---

On considère une chaîne de caractères $s=s_0 \dots s_{n-1}$ de longueur $n$ composée uniquement des caractères $+$ et $-$.

{% info %}
Comme en python, on considérera que le $k$ème caractère de $s$ ($1 \leq k \leq n$) est noté $s[k-1]$ et vaut $s_{k-1}$.
{% endinfo %}

On note $u(s)_i$ la suite finie valant pour $0 \leq i < n$ :

<div>
$$
u(s)_i = \left\{
    \begin{array}{ll}
        1 & \text{si } s[i] = + \\
        -1 & \text{sinon.}
    \end{array}
\right.
$$
</div>

On note $\mathcal{L}$ l'ensemble de chaînes de caractères défini tel que $s \in \mathcal{L}$ si une deux conditions suivante est vraie :

* $\sum_{0 \leq i < n}u(s)_i = -1$
* $\sum_{0 \leq i < k}u(s)_i \geq 0$ pour tout $0 < k < n$.

{% note %}
Le but de ce DM est caractériser $\mathcal{S}$.
{% endnote %}
{% info %}
Ce DM a pour but de vous faire travailler vos démonstrations et il mettra à épreuve votre capacité à écrire des boucles, créer des listes et à faire très attentions aux indices que vous manipulez.
{% endinfo %}

## Rapport à rendre

Le DM est à rendre sous forme électronique. Il doit contenir :

1. Un fichier markdown contenant les réponses aux questions (suivez ce [tutoriel]({{"/tutoriels/format-markdown" | url}}) pour savoir écrire en markdown) et une version convertie en html de celui-ci
2. un dossier contenant votre code python. Ce code doit contenir :
   * un fichier contenant le code de vos fonctions
   * un fichier de tests de vos fonctions
   * un fichier contenant le programme principal. Ce programme doit :
     * générer tous les mots de $\mathcal{L}$ plus petit qu'un entier donné
     * générer des chaînes aléatoires de $\mathcal{L}$

## Des mots

### Décrire

Donner tous les mots $\mathcal{L}$ de longueur 1, 2 et 3.

### Longueur paire

Montrer que pour toute suite $v = (v_0, \dots, v_{n-1})$ telle que $n$ est paire et $v_i \in \\{-1, 1\\}$ pour tout $i$, la somme $\sum_{i < n} v_i$ est paire.

En déduire qu'il n'existe pas de chaîne de longueur paire dans $\mathcal{L}$

### Python : vérification

Écrire une fonction qui indique si un mot est dans $\mathcal{L}$. Cette fonction devra être de complexité $\mathcal{O}(n)$ (que l'on justifiera) où $n$ est la longueur du mot en entrée.

## Décomposition

Soit $s \in \mathcal{L}$ de longueur $n \geq 3$

### Valeurs spéciales

Que valent $s[0]$ et $s[-1]$ ?

{% info %}
Comme en python, on considérera que le dernier caractère de $s$ est noté $s[-1]$ et vaut $s_{n-1}$.
{% endinfo %}

### Constatation

Montrez que si $s_1$ et $s_2$ sont dans $\mathcal{L}$ alors le mot $+ \oplus s_1 \oplus s_2$ l'est aussi.

{% info %}
On note $\oplus$ l'opérateur de concaténation de deux chaînes.
{% endinfo %}

### Début de mot

Montrez que si $0 \leq m' < n$, $s[:m']$ ne peut être dans $\mathcal{L}$.

{% info %}
Comme en python, pour une chaîne de caractères $s$, $s[:k]$ correspond à la chaîne $s_0\dots s_{k-1}$ formée des $k$ premiers éléments de $s$.
{% endinfo %}

### Sommes

Que vaut $\sum_{0 \leq i < n -1} u(s)_i$ ?

En déduire qu'il existe $m$ le plus petit entier tel que $\sum_{0 \leq i < m} u(s)_i = 0$

### Un sous-mot

Soit $m$ le plus petit entier tel que $\sum_{i < m} u(s)_i = 0$.
Montrez que :

* $s1 = s[1:m]$ est dans $\mathcal{L}$
* $s2 = s[m:]$ est dans $\mathcal{L}$

{% info %}
Comme en python, pour une chaîne de caractères $s$ :

* $s[k:k']$ avec $k \leq k'$ correspond à la chaîne $s_k\dots s_{k'-1}$ formée des $k'-k$ caractères de $s$ à partir du $k+1$ ème.
* $s[k:]$ correspond à la chaîne $s_k\dots s_{n-1}$ formée de tous les caractères de $s$ à partir du $k+1$ ème.
{% endinfo %}

### Le sous-mot

Déduire de ce qui précède que pour tout $s \in \mathcal{L}$ de longueur $n \geq 3$, il existe un **unique** entier $m$ tel que $s[1:m]$ et $s[m:]$ sont dans $\mathcal{L}$.

### Python : décomposition

Écrire une fonction qui, à partir d'un mot $s \in \mathcal{L}$ de longueur supérieure ou égale à 3 rend les deux mots $s_1$ et $s_2$ de $\mathcal{L}$ tels que $s = + \oplus s_1 \oplus s_2$

## Tous les mots

En utilisant ce qui précède, écrire une fonction python qui rend une liste de tous les mots de $\mathcal{L}$ de taille plus petit qu'en entier `n` donné en paramètre.

Essayez de ne pas recalculer des mots déjà utilisés.

## Conjugaison

### Permutation

Montrer que si $s \in \mathcal{L}$ est un mot de longueur $n$, alors pour tout $0 < m < n$, $s[m:] \oplus s[:m]$ ne peut être dans $\mathcal{L}$.

### Unique permutation

Montrer que si pour une chaîne de caractères $c$ composée uniquement de $+$ et de $-$ (elle n'est pas forcément dans $\mathcal{L}$), il existe un entier $m$ tel que $c[m:] \oplus c[:m]$ est dans $\mathcal{L}$, alors il est unique.

### Existence de la permutation

Soit $c$ une chaîne de caractères composée uniquement de $+$ et de $-$ telle que $\sum_{0 \leq i < n}u(c)_i = -1$.

En utilisant le fait que pour tout $p < q < n$ on a (clairement) :

<div>
$$
\sum_{p \leq i < q}u(c)_i = \sum_{0 \leq i < q}u(c)_i - \sum_{0 \leq i < p}u(c)_i
$$
</div>

Montrez que si $p$ est le plus petit entier tel que :

<div>
$$
\sum_{0 \leq i < p}u(c)_i = \min_{k}(\sum_{i < k}u(c)_i)
$$
</div>

Alors $c[p:] \oplus c[:p]$ est dans $\mathcal{L}$.

En déduire qu'il existe un **unique** $m$ tel que $c[m:] \oplus c[:m]$ est dans $\mathcal{L}$. Ce mot est appelé ***conjugué*** de c

### Python : conjugaison

Écrire une fonction qui rend le conjugué d'une une chaîne de caractères $c$ composée uniquement de $+$ et de $-$ telle que $\sum_{0 \leq i < n}u(c)_i = -1$.

### Résultat intermédiaire

Montrez que si pour deux chaînes non vides $u$ et $v$ on a $u \oplus v = v \oplus u$ alors il existe une chaîne $w$ et deux entiers $k$ et $l$ tels que :

* $u$ est la concaténation de $k$ fois la chaîne $w$
* $u$ est la concaténation de $l$ fois la chaîne $w$

### Permutations de $\mathcal{L}$

En utilisant le résultat précédent, montrer que si $s$ est dans $\mathcal{L}$ alors $s[m_1:] \oplus s[:m_1]$ est différent de $s[m_2:] \oplus s[:m_2]$ pour tout $m_1$ différent de $m_2$.

### Dénombrement

Combien y a-t-il de mots de longueur $2n + 1$ composés uniquement de $+$ et de $-$ tels que $\sum_{0 \leq i < n}u(c)_i = -1$ ?

### Dénombrement de $\mathcal{L}$

Déduire de ce qui précède le nombre de mots de $\mathcal{L}$ de longueur $2n + 1$.

## Capsules

On appelle ***capsule*** la chaîne de caractère $+--$

On note $\rho(s)$ la fonction qui prend en entrée une chaîne de caractère $s=s_0\dots s_{n-1}$ et rend en sortie :

* $s$ si $s$ ne contient pas de capsule
* $s_0 \dots s_{i-1}s_{i+2} \dots s_{n-1}$ si $s_is_{i+1}s_{i+2}$ est la première capsule contenue dans $s$.

### Python : capsule

Écrire une fonction qui calcule $\rho(s)$ pour une chaîne de caractère donnée en entrée.

### Limite

Montrez que pour toute chaîne de caractère $s$, il existe une valeur $n$ telle que $\rho^{n+1}(s) = \rho^n(s)$. La chaîne de caractère limite $\rho^{n+1}(s)$ est notée $\rho^*(s)$.

### Python capsules (le retour)

Écrire une fonction qui calcule $\rho^*(s)$ pour une chaîne de caractère donnée en entrée.

### Tout ça pour ça

Montrez qu'une chaîne de caractère $s$ est dans $\mathcal{L}$ si et seulement si $\rho^*(s)$ vaut $-$

Écrivez une fonction python qui rend un mot de $\mathcal{L}$ *aléatoire* de taille $2n+1$.
