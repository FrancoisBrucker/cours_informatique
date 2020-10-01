---
layout: page
title:  "Chiffrement RSA"
category: cours
tags: combat web
---

# Le chiffrement RSA

Cet algorithme a été présenté en 1977 par Ronald Rivest, Adi Shamir et Leonard Adleman.

Le chiffrement RSA s’appuie sur le fait que factoriser un produit de deux nombres premiers distincts est difficile. 

La clé publique et la clé secrète sont calculées grâce a l'**algorithme d’Euclide** et aux **coefficients de Bézout**, et le déchiffrement grâce au **petit théorème de Fermat**.

Quelques outils mathématiques et algorithmiques nécessaires :

- Le **petit théorème de Fermat** dit :
Si p est un nombre premier et a un entier alors *a^p = a mod p*.
**Corollaire** : si p ne divise pas a alors *a^(p-1) = 1 mod p*.

- La **version améliorée du petit théorème de Fermat** nous donne :
Soient p et q deux nombres premiers distincts et soit n = pq. Pour tout a entier tel que pgcd(a,n) = 1 (cad n ne divise pas a) alors : *a^((p-1)(q-1)) = 1 mod n*.

- L’**algorithme d’Euclide** permet de retourner facilement le reste d’une division euclidienne.

L’**algorithme d’Euclide étendu** permet d’obtenir les coefficients de Bézout.

- Soit a un entier, on dit que x entier est un **inverse de a modulo n** si *ax = 1 mod n*. a admet un inverse modulo n si et seulement si pgcd(a,n)=1. De plus si au + nv = 1 (coefficient de bézout) alors u est un inverse de a modulo n.


**Générer une paire de clés :**

- Choix de deux nombres premiers distincts p et q.

- Calcul de n = p x q.

- Calcul de **l’indicatrice d’Euler** Phi(n) = (p-1) x (q-1). *Pour calculer cette fonction il faut connaître p et q, d'où son caractère privé*.

- Choix d’un exposant e tq pgcd(e,Phi(n))=1.

- Calcul de l’inverse d de e mod Phi(n) par l’**algorithme d’Euclide** étendu : d x e = 1 mod Phi(n)

- La clé publique est constituée de **n et e** et la clé privée de **d**.

**Chiffrement du message :**

- II faut décomposer le message secret en paquets de taille **m <n**.

- Calcul du message chiffré **x =  m^e mod n**. *n et e sont connus car on dispose de la clé publique*.

**Déchiffrement du message :**

- le message x est décrypté à l’aide de sa clé privée d : m = x^d mod n

- En effet le **petit théorème de Fermat amélioré** permet d’écrire : Soit d l’inverse de e modulo Phi(n) avec n = pq. Si **x = m^e mod n** alors **m=x^d mod n**.


**Preuve :**

- d est l’inverse de e mod Phi(n) *donc * d.e = 1 mod Phi(n) *donc* il existe k entier tq d.e = 1+ k Phi(n)

- Le petit th de Fermat amélioré donne : si pgcd(m,n)=1 alors m^Phi(n)=m^(p-1)(q-1)= 1 mod n.

- Si pgcd(m,n) = 1 alors modulo n :
 **x** = (m^e)^d = m^(1+k Phi(n)) = m x m^(k Phi(n)) = m x (m^Phi(n))^k = (Fermat) m x 1^k **= m (mod n)^**.

- Si pgcd(m,n) != 1, alors pgcd(m,n)=p et pgcd(m,q)=1 ou inversement.

Si p divise m, alors modulo p : m = 0, **x** = m^(ed) = 0 mod p, donc m^(ed) **= m mod p**.
Et modulo q : **x** = m^(ed) = m x (m^Phi(n))^k = m x (m^(q-1))^k (p-1) **=(Fermat) m mod q**.

pgcd(p,q)=1 permet de conclure **x=m^ed=m (mod n)**.

**Conclusion : on a donc des algorithmes permettant de générer une paire de clés, et on peut chiffrer un message avec une clé, déchiffrable uniquement avec l’autre clé.**

Pour plus d'informations voir : [chiffrement RSA](https://www.youtube.com/watch?v=Xlal_d4zyfo)
