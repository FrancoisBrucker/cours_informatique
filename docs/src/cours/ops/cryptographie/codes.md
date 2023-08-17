---
layout: layout/post.njk

title: Codes de cryptographie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

De façon formelle on peut décrire la [cryptographie](https://fr.wikipedia.org/wiki/Cryptographie) comme l'utilisation de deux fonctions injectives $f$ et $g$ telles que :

* $f: \mathcal{M} \rightarrow \mathcal{M}'$ qui permet de ***coder*** le message
* $g: \mathcal{M}' \rightarrow \mathcal{M}$ qui permet de ***décoder*** le message
* $g(f(m)) = m$

Les espaces $\mathcal{M}$ et $\mathcal{M}'$ sont quelconques, ils sont souvent les mêmes (l'ensemble des chaînes de caractères par exemple), mais peuvent être différents ($\mathcal{M}'$ est une suite de chiffre dans le [grand chiffre de Louis XIV](https://fr.wikipedia.org/wiki/Grand_Chiffre)). La cryptographie n'est cependant pas de la traduction, puisqu'il n'y a pas de place pour l'interprétation.

Ainsi si Alice veut envoyer un message $m$ à Bob sans que Eve ne puisse le connaître il faut que :

* Alice ait en sa possession la fonction $f$ et envoie à Bob le message $f(m)$
* Bob ait en sa possession la fonction $g$ pour qu'il puisse retrouver $m = g(f(m))$
* Eve ne connaisse pas la fonction $g$

Si Alice est la seule à connaître $f$ et Bob le seul à connaître $g$, Mallory ne peut intercepter que le message codé $f(m)$. Il **faut** donc, pour que tout ceci puisse fonctionner, il faut qu'il soit ***difficile*** à Mallory de décoder le message, c'est à dire de trouver $m$ à partir de $f(m)$ sans connaître $g$.

Pour que Alice et Bob puisse s'échanger des messages il faut a priori que Alice ait en sa possession un couple de fonctions $(f, g')$ et Bob le couple associé $(f', g)$ tel que :

* $g(f(m)) = m$ : Alice peut envoyer un message à Bob qui peut le décoder
* $g'(f'(m)) = m$ : Bob peut envoyer un message à Alice qui peut le décoder

Pour simplifier sans perdre en généralité on va considérer ici que :

* $\mathcal{M} = \mathcal{M}' \subseteq \mathbb{N}$, un sous-ensemble de l'ensemble des entiers positifs
* $f$ est une bijection et $g = f^{-1}$

Alice et Bob n'ont donc besoin que d'une fonction $f$ pour l'un et $f^{-1}$ pour l'autre pour communiquer.

## Code et clés

Pour que le codage et décodage puissent être automatisés, il faut que $f$ et $f^{-1}$ soient des algorithmes. Ces algorithmes possèdent souvent des paramètres permettant de produire plusieurs couples de fonctions. L'ensemble de ces couples, ou de façon équivalente l'algorithme permettant de les produire est appelé un ***code***.

Par exemple le [code de César](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage) sur notre alphabet à 26 lettres permet de produire 26 couples différents, correspondant chacun à un décalage différent.

{% note "définition" %}
Un ***code*** est composé de deux algorithmes :

* `code(clé_chiffrement)` qui rend une fonction $f: \mathcal{M} \rightarrow \mathcal{M}$
* `décode(clé_déchiffrement)` qui rend une fonction $g: \mathcal{M} \rightarrow \mathcal{M}$

Pour toute `clé_chiffrement` il existe une `clé_déchiffrement` telle que :

* $f = $`code(clé_chiffrement)`
* $f^{-1} = $ `décode(clé_déchiffrement)`
* $f(g(m)) = m$

{% endnote %}

Si Alice et Bob veulent s'échanger des messages, ils suffit qu'ils se mettent d'accord sur le code à utiliser et sur la paire de clés. Eve peut être au courant du code utilisé, s'il ne connaît pas la clé utilisée pour le codage du message, il lui est ***a priori*** impossible de trouver la clé de déchiffrement lui permettant de décoder le message (via la création de la fonction $g$ avec le code).

> TBD algo de césar.
>
> * M = 0 à 25
> * code(c) rend la fonction $f(m) \mapsto x + c mod 26$
> * décode(c) rend la fonction $f(m) \mapsto x - c mod 26$
> déchiffrement = chiffrement

## Cryptanalyse

<https://fr.wikipedia.org/wiki/Cryptanalyse>

{% note "définition" %}
En cryptographie, la ***difficulté*** de décodage est mesurée par le temps nécessaire pour trouver $m$ à partir de $f(m)$ sans connaître $g$.

S'il faut plus de temps à décoder le message que la durée de vie utile du message, c'est un bon code.
{% endnote %}

<https://fr.wikipedia.org/wiki/Alice_et_Bob>

Par exemple si Alice et Bob s'envoient leurs emploi du temps du lendemain, s'il faut plus d'une journée à Mallory pour décoder le message, c'est un bon code.

On supposera toujours que :

* Mallory connaît le code utilisé
* qu'il a a sa disposition une puissance de calcule actuelle
* qu'il est intelligent

> ex césar. Que 26 essais en brute force + dictionnaire
> encore moins en analyse fréquentielle

## Codage par bloc

En informatique un message est toujours une succession de bits. Comme le message est peut être aussi long que l'on veut mais que (usuellement) les clés sont dépendantes de la taille du message à coder, on a coutume de coder un message par bloc.

Par exemple, le code de César d'un texte peut être vu comme un codage par bloc d'un caractère d'un texte de plusieurs caractères.

Le principe est le suivant. On crée des codes (les fonctions $f$ et $g$) faits pour coder et décoder des messages de taille fixe, disons $T$ bits. Coder (ou décoder) un message $m$ revient à appliquer le codage/décodage à des paquets de $T$ bits successifs de $m$. Si $m$ vaut :

$$
m = m^1_1\dots m^1_T\cdots m^i_1\dots m^i_T\cdots m^K_1\dots m^K_T
$$

Son codage $f(m)$ vaudra :

$$
f(m) = f(m^1_1\dots m^1_T)\cdots f(m^i_1\dots m^i_T)\cdots f(m^K_1\dots m^K_T)
$$

Si le message n'est pas de longueur un multiple de $T$ bits, on commence par lui appliquer un [algorithme de remplissage](https://fr.wikipedia.org/wiki/Remplissage_(cryptographie)) pour lui conférer une bonne taille (par exemple ajouter des 0 au début ou à la fin du message, mais il existe ds méthode plus sophistiquées).

{% note %}
La plupart des codes à clés secrètes utilisés en informatique sont des codes par blocs. La taille du bloc est variable, mais plus elle augmente, plus la sécurité du code augmente. Ceci se fait bien sur qu détriment de la rapidité de codage.

{% endnote %}

La taille d'un bloc - donc la taille de la clé utilisée - est  un **paramètre important** à considérer lorsque l'on utilise une méthode de codage. Il faut faire un arbitrage entre rapidité de codage et sécurité : plus le message est critique ou de validité longue plus il faudra un bloc de grande taille.

## Code à clé secrète

{% note "définition" %}
Un code est dit ***symétrique*** lorsque la clé de déchiffrement est identique ou s'il est *facile* de la déterminer à partir de la clé de chiffrement.
{% endnote %}

Dans le cas de code symétrique, il est indispensable de garder la clé de chiffrement secrète sans quoi Eve pourra aisément décoder le message

Le principal intérêt des codes à clés secrètes est leur simplicité. Il sont très rapide à coder et décoder des messages.

De plus, les seuls codes prouvés inviolables sont des codes à clés secrètes.

> sensible à l'analyse en fréquence pour la cryptanalyse <https://fr.wikipedia.org/wiki/Analyse_fr%C3%A9quentielle>

### Masque jetable

taille max ou Vigenère plus petit. Mais attention à l'analyse en fréquence (ex césar)

> Vernam, ou encore masque jetable <https://fr.wikipedia.org/wiki/Masque_jetable> inviolable
> mais clé trop longue, impossible à mettre ne oeuvre ne pratique, on découpe le message en bout de taille = longueur de la clé.
> clé = 1 = césar
> clé = k = vigenere <https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re>

> Ex césar et découpe par caractère
> dire que ca simplifie le code mais affaiblie sa sécurité :
>  * césar que 26 possibilité
>  * si cesar avec un décalage différent pour chaque case, le message est inviolable (on peut potentiellement retrouver tous les textes français ! C'est la [bibliothèque de Babel](https://fr.wikipedia.org/wiki/La_Biblioth%C3%A8que_de_Babel))
>

### XOR

<https://en.wikipedia.org/wiki/XOR_cipher>

> TBD lien ci-dessus tout dedans sur Vernam et block

## Code à clé publique

> def : asymétrique : clé de chiffrement != clé de déchiffrement.
> 

> si clé de déchiffrement difficile à trouver à partir de la clé de chiffrement, la clé de chiffrement peut être connue.
>
> intérêt :

> TBD durée de vie du message
> exemple : <https://fr.wikipedia.org/wiki/Chiffrement_RSA>
Nous ajouterons égale

Le but de la  est de permettre :

<https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique>

1. de transformer un message $m$ en un message $m'$ ne permettant pas de connaître $m$
2. de transformer $m'$

{% aller %}

[code RSA](../RSA){.interne}
{% endaller %}
