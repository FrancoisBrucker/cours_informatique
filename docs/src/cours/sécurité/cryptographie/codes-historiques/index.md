---
layout: layout/post.njk

title: Codes historiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



En analysant 4 codes historiques, on verra quelques concepts utile pour l'analyse.

## Code de césar

### <span id="César-chiffre"></span>Chiffrement

Chaque lettre est décalée dans l'alphabet :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m) &=& m + k \mathbin{\small\\%} 26\\
    D(k, c) &=& c - k \mathbin{\small\\%} 26\\
  \end{array}
\right.
$$
</div>

{% info %}
Le [ROT(13)](https://fr.wikipedia.org/wiki/ROT13), César où $k=13$ (`A` est remplacé par `N`) est l'ancêtre du floutage NSFW.
{% endinfo %}

Le code de César est un exemple de ***Codage par flux*** (*stream cipher*) : chaque lettre est chiffrée une à une avec le même algorithme (il ne change pas à chaque lettre à coder)

lettre |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
-------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
code   |N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|D|E|F|G|H|I|J|K|L|M|

Faisons ça en shell, parce que pourquoi pas. Chaîne à coder :

```
Longtemps je me suis couché de bonne heure.
```

On ne peut avoir que des code ASCII, don con transforme tout, pour supprimer les accents :

```
❯ echo "Longtemps je me suis couché de bonne heure." | recode -f utf8..flat

Longtemps je me suis couche de bonne heure.
```

On chiffre :

```
❯ echo "Longtemps je me suis couché de bonne heure." | recode -f utf8..flat | tr "A-Za-z" "N-ZA-Mn-za-m"

Ybatgrzcf wr zr fhvf pbhpur qr obaar urher.
```

On déchiffre. L'intérêt du ROT13 est que c'est le même algorithme pour le chiffrage et le déchiffrage :

```
❯ echo "Ybatgrzcf wr zr fhvf pbhpur qr obaar urher." | recode -f utf8..flat | tr "A-Za-z" "N-ZA-Mn-za-m"

Longtemps je me suis couche de bonne heure.
```

Le tout en une seule fois (avec des tee pour afficher les résultats intermédiaires) :

```
❯ echo "Longtemps je me suis couché de bonne heure." | recode -f utf8..flat | tee /dev/tty | tr "A-Za-z" "N-ZA-Mn-za-m" | tee /dev/tty | tr "A-Za-z" "N-ZA-Mn-za-m"

Longtemps je me suis couche de bonne heure.
Ybatgrzcf wr zr fhvf pbhpur qr obaar urher.
Longtemps je me suis couche de bonne heure.
```

### <span id="César-analyse"></span>Cryptanalyse

1. Ne résiste pas au calcul exhaustif des clés : 26
2. Ne résiste pas à l'analyse en [fréquence de chaque lettre](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d'apparition_des_lettres)

"Longtemps je me suis couche de bonne heure.". les 4 premières fréquences:

- `E` 22%85
- `U` 8%57
- `S` 8%57
- `O` 8%57

Français :

-|-----|-|-----|-|-----|
E|17.76|O| 5.34|B| 0.80|
S| 8.23|D| 3.60|H| 0.64|
A| 7.68|C| 3.32|X| 0.54|
N| 7.61|P| 3.24|Y| 0.21|
T| 7.30|M| 2.72|J| 0.19|
I| 7.23|Q| 1.34|Z| 0.07|
R| 6.81|V| 1.27|K| 0.00|
U| 6.05|G| 1.10|W| 0.00|
L| 5.89|F| 1.06|

{% lien %}
<https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres>
{% endlien %}

La lettre arrivant le plus souvent dans le message chiffré, `r` a donc toute les chances d'être `e` ce qui donne le décalage.

## Vigenère

### <span id="Vigenère-chiffre"></span>Chiffrement

Remplace la clé unique par un tableau de clés $k =[k_0,\dots, k_{p-1}]$

Le chiffrement de $m = m_0 \dots m_L$ en $c = c_0 \dots c_L$ de fait avec l'équation :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m_i) &=& m_i + k_{(i \mathbin{\small\\%} p)} \mathbin{\small\\%} 26\\
    D(k, c_i) &=& c_i - k_{(i \mathbin{\small\\%} p)} \mathbin{\small\\%} 26\\
  \end{array}
\right.
$$
</div>

Le code de Vigenère est un exemple de ***Codage par blocs*** (*bloc cipher*) : chaque bloc de $p$ lettres est codé avec le même algorithme.

Par exemple, si on encode notre chaîne par `PROUST`, cela revient à encoder toute les 7 lettres par un césar commençant par `P`, toutes les 8 lettres par un césar commençant par `R`, etc... Notre texte se code alors par :

```
Message : Longtemps je me suis couché de bonne heure.
Clé     : PROUSTPRO US TP ROUS TPROUS TP ROUST PROUS
Chiffre : AFBALXBGG DW FT JICK VDLQBW WT SCHFX WVILW.
```

### <span id="Vigenère-analyse"></span>Chiffrement

{% lien %}
[Chiffre de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)
{% endlien %}

1. Calcul exhaustif des clés : $26^p$, si $p \geq 30$ alors environ $2^{128}$ opérations, c'est safe.
2. si la clé est choisie de façon aléatoire, par bloc cela semble sécurisé, chaque lettre peut équiprobablement être choisie. Mais :
   1. si on a la taille on refait de l'analyse par fréquence
   2. [on peut trouver la taille](https://www.bibmath.net/crypto/index.php?action=affiche&quoi=poly/viganalyse)

Pour retrouver la taille de la clé, on utilise [l'indice de coïncidence mutuelle](https://fr.wikipedia.org/wiki/Indice_de_co%C3%AFncidence), développé par Friedman dans les années 1920, qui calcule pour une langue donnée la probabilité que deux lettres choisie aléatoirement dans un texte soient égales.

Soit $T = c_1\dots c_n$ un texte de longueur $n>>1$ formé des 26 lettres de l'alphabet $\mathcal{A} = \\{a_1, \dots,. a_{26}\\}$. On suppose que la lettre $a_i$ apparaît $n_i$ fois dans $T$ ($\sum_i n_i = n$). On note :

<div>
$$
\text{IC}(T) = \sum_{1\leq i \leq 26}\frac{n_i(n_i-1)}{n(n-1)}
$$
</div>

L'indice de coïncidence de $T$. Il correspond à la probabilité de prendre deux lettres au hasard dans le texte et qu'elles soient égales. En effet, cela revient à considérer un tirage de 2 boules parmi $n$ de 26 couleurs différentes. La probabilité que les deux boules tirées soient de la couleur de $a_i$ est $C_2^{n_i}/C_2^{n} = \frac{n_i(n_i-1)}{n(n-1)}$.

Friedman a remarqué que ce nombre dépend de la langue choisie. En Français c'est de l'ordre 0.074.

Pour un codage de Vigenère, le même chiffrement est utilisé tout les $m$ caractères où $m$ est la taille de la clé, on devrait donc retrouver l'IC Français tous les 6 caractères de notre texte chiffré. En les classant par ordre croissant, de 1 à 10 on a :

- IC = 0.033333 décalage = 10
- IC = 0.038095 décalage = 5
- IC = 0.042857 décalage = 7
- IC = 0.044118 décalage = 2
- IC = 0.045378 décalage = 1
- IC = 0.054167 décalage = 8
- IC = 0.055556 décalage = 9
- IC = 0.057576 décalage = 3
- IC = 0.062500 décalage = 4
- IC = 0.072222 décalage = 6

C'est bien pour un décalage de 6 que l'IC est le plus proche d'un texte Français. Une fois la longueur de clé trouvée, on continue comme un César, le caractère le plus fréquent est le `E`.

En prenant les fréquences les plus élevées :

- toutes les 6 lettres à partir de la 1ere position  : `'T'` à 33% : clé `P`. Ok !
- toutes les 6 lettres à partir de la 2nde position  : `'V'`, `'S'`, `'L'`, `'J'` à 16%.  Ko !
- toutes les 6 lettres à partir de la 3eme position  : `'I'` à 33% : clé `E`.  Ko !
- toutes les 6 lettres à partir de la 4eme position  : `'L'`, `'H'`, `'D'` 16%.  Ko !
- toutes les 6 lettres à partir de la 5eme position  : `'W'` à 50%: clé `S`. Ok !
- toutes les 6 lettres à partir de la 6eme position  : `'X'` à 33% : clé `T`. Ok !

On trouve une clé potentielle de `PVELST` :

```
Message : Longtemps je me suis couché de bonne heure.
Décrypte  LKXPTEMLC SE ME OERS COQMQE DE XYWNE HAEAE
```

Il suffit ensuite d'affiner avec les mots reconnus ou de poursuivre les investigations sur les bouts de clés où les pourcentages sont trop proches. On trouve cependant la moitié des clés pour un texte devenu très petit. Plus le texte à chiffré est grand par rapport à la clé plus cette méthode devient efficace.

En prenant [les premières phrases du roman](https://fr.wikipedia.org/wiki/Longtemps,_je_me_suis_couch%C3%A9_de_bonne_heure#Premier_chapitre) :

```
Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte,
mes yeux se fermaient si vite que je n’avais pas le temps de me dire : « Je m’endors. »
Et, une demi-heure après, la pensée qu’il était temps de chercher le sommeil
m’éveillait ; je voulais poser le volume que je croyais avoir encore dans les mains
et souffler ma lumière ; je n’avais pas cessé en dormant de faire des réflexions sur 
ce que je venais de lire, mais ces réflexions avaient pris un tour un peu particulier ;
il me semblait que j’étais moi-même ce dont parlait l’ouvrage : une église, un quatuor,
la rivalité de François Ier et de Charles Quint. Cette croyance survivait pendant
quelques secondes à mon réveil ; elle ne choquait pas ma raison mais pesait comme des
écailles sur mes yeux et les empêchait de se rendre compte que le bougeoir n’était plus
allumé. Puis elle commençait à me devenir inintelligible, comme après la métempsycose
les pensées d’une existence antérieure ; le sujet du livre se détachait de moi, j’étais
libre de m’y appliquer ou non ; aussitôt je recouvrais la vue et j’étais bien étonné de
trouver autour de moi une obscurité, douce et reposante pour mes yeux, mais peut-être 
plus encore pour mon esprit, à qui elle apparaissait comme une chose sans cause, 
incompréhensible, comme une chose vraiment obscure. Je me demandais quelle heure il 
pouvait être ; j’entendais le sifflement des trains qui, plus ou moins éloigné, comme 
le chant d’un oiseau dans une forêt, relevant les distances, me décrivait l’étendue de 
la campagne déserte où le voyageur se hâte vers la station prochaine ; et le petit 
chemin qu’il suit va être gravé dans son souvenir par l’excitation qu’il doit à des 
lieux nouveaux, à des actes inaccoutumés, à la causerie récente et aux adieux sous la 
lampe étrangère qui le suivent encore dans le silence de la nuit, à la douceur 
prochaine du retour.
```

On obtient le texte :

 ```
AFBALXBGGDWFTJICKVDLQBWWTSCHFXWVILWIPITIALPGSCFXBRPIMZXVSNWBCKSGWLNVIRKX
UVFGSBTEHMAOXKSKMXYVBUNTXJDUKETKSGHLSVAYVBGVXYEXCUCLKXILBYVXBZVYMKTRDLWL
ARDYFLTVEOAETKOCLMTDDMVXRYSLUATIZYKHBDSCDFTMSCDEPZHDWODLZUALEFGYJETMCFMF
THIYBXRICSSBHRJIAKTEQIJXSRBMDXHDOCFLTKGIMYUCSLETALACWKTASHSOPZGJSLRVGMWX
CUCLETCKRYXTXISXWLGVTFWQXFBMKNGTSKMXYVJYFTXJRYDBGVAUALRVGLWYAVLCGGHRJUAX
CKDLALJEHIMKJEDYMIPIHCUNAZSLAEBVGYEUARWNINTASNSBHDCCEXBVQYVHCKDUJEPZHFGN
KIOAWNCVSADBHVIHINPKIIJEPIWPSEXKSXWYGRBWGBHZSLWMSVQBSKAVGKMBCKQYLMTTFIQT
CTSMMKKZJUAMEVBXSGIHIYDJJVGMWVDERYKTBFBLWOTZZYDETESWZHFLOCLIPJAUJTXJCHET
XJDYKTXKQIEFTUSMWVPZZFWLHLFGWLNVIRWMAVGYEITTVUAMSVGYJXCUFYUHBGHYINTCSVGN
VVCCJGTKOCLIALGUDEJDSJMBHVZFWVDDAYFVPZHUEXSVJYFBGZBCFMTCZCYBQCSWGFBVOJJX
HCOGWMTDDMQVDJSFWLEVBMWXHUIHWXMZGNWGRVOHLXGZSOJXAVGOBXIUIFAOGVGYVXIRQBSB
IUSGGBYVHUALAZPLWWTDMUHIAZEOWKDLBIFTJJGCLHIASLWVDLJLSBHCOPMXTKXYLTXJPCWG
TKCHFXSVHLGNKVFUMMDLFXWFDZIHWHQJQOJBIVRIMVTVHLWIDJOHLXEFILEXHPSOPFPZGJWN
IVHLWIALGYFVDISJGNGDCHWLEIWNSJJZSFDXPGDUJTXJGUAMRFAGWNCVQBGLTJOHKVPLGYAG
RFAJJXWVBMAUAVQIEFTLBYUADJSPJTXDSHLHQJQOJXYVAYVXBRBXSBHHIYDETYSOJXXCDIMO
PZHYLKTASHLXCUOCKETJWZXETDSHLWTJHLSBCJEOAIALGIMFDZBMWEDZUHWVDDAYDXRYOHLW
JECCKXPLRUFLJESZGKTKFYDXKRBNDXHUWMLTCTSMEXSVQLAOPZHFWMTEROWWTCOWSFERUHWW
TJSLLXDLZYNHNRUYMKHVVULXKVFMDTHKONAHCGFIUAPZBYWMAVDYLBITVYEBCHICDLJZHPSX
IISAJTKVRUFLHFBMGNKVBCJIPIZYPVXKONAHCHICDWDZHUVXHCWYMQCFIPWTJOOXWLPTHYKB
CRQWGNILAYKTARQUMLTIWYJXRVBNWXIRIRSWXVIRKHJJZUDTBGSYLKPEUYJXFLWFWLJZJYFM
TEQIJXSRBMDXHZZYFVTUSFSGJZHUDTSFIWWNGGFIUAPZBYVNGVHIMK
 ```

 Ce texte a un IC de 0.08 pour 6 et c'est le plus proche de 0.074 pour les 10 premiers IC (si vous faites le test chez vous, n'oubliez pas d'enlever les retour à la ligne du texte). Les fréquences par position sont alors :

- toutes les 6 lettres à partir de la 1ere position  : `'T'` à 17% : clé `P`. Ok !
- toutes les 6 lettres à partir de la 2nde position  : `'V'` à 21% : clé `R`. Ok !
- toutes les 6 lettres à partir de la 3eme position  : `'S'` à 16% : clé `O`. Ok !
- toutes les 6 lettres à partir de la 4eme position  : `'Y'` à 20% : clé `U`. Ok !
- toutes les 6 lettres à partir de la 5eme position  : `'W'` à 20% : clé `S`. Ok !
- toutes les 6 lettres à partir de la 6eme position  : `'X'` à 20% : clé `T`. Ok !

On retrouve notre clé ! Le texte n'est de plus vraiment pas long.

{% lien %}
[Décrypter Vigenère](https://www.youtube.com/watch?v=yHXOnCKh4iE)
{% endlien %}

On voit que le décryptage d'un texte peut prendre des voies détournées. Il ne faut **jamais** sous-estimer l'intelligence et l'inventivité de l'adversaire : il est nécessaire en sécurité et en cryptographie de se munir d'outils théorique permettant de garantir et de démontrer la sécurité d'un système de chiffrement.

### One time Pad (OTP)

L'idée est de faire un Vigenère avec comme taille de clé le message !

C'est la technique du :
{% lien %}
[masque jetable](https://fr.wikipedia.org/wiki/Masque_jetable), *One Time Pad*.
{% endlien %}

Technique utilisée pour le téléphone rouge lors de la guerre froide.

{% info %}
[Chiffre du Che](https://www.bibmath.net/crypto/index.php?action=affiche&quoi=moderne/che)
{% endinfo %}

Ce qui donne :

```
Longtemps je me suis couche de bonne heure.
ALarecher ch ed utem psperd ud eMarc elPro
LZNXXGTTJ LL QH MNME RGJGYH XH FANEG LPJIS
```

Ce code est réputé (on va le prouver) inviolable. S'il n'est pas réutilisé.

## Chiffre Vernam

La version informatisée du OTP est appelée [chiffre de Vernam](https://www.cryptage.org/vernam.html).

Ici les messages, les chiffres et les clés sont des mots de $\\{0, 1\\}^L$ et on a, avec $\oplus$ le ou exclusif binaire :

<div>
$$
\left\{
  \begin{array}{lll}
    E(k, m) &=& k \oplus m\\
    D(k, c) &=& E(k, c) = k \oplus c\\
  \end{array}
\right.
$$
</div>

On a bien $m = k \oplus c$ puisque $k \oplus k \oplus m = m$.

```shell
❯ echo -n "fascina" | xxd -ps
66617363696e61
❯ echo -n "message" | xxd -ps
6d657373616765
❯ printf "0x%x\n" $((0xb040010080904 ^ 0x66617363696e61))
0x6d657373616765
❯ echo 0x6d657373616765 | xxd -r ; echo
message
❯ 
```

Intuitivement, comme $k$ peut être ce que l'on veut, $k \oplus m$ l'est aussi. En particulier pour tous $m$ et $c$ on peut trouver $k$ tel que $c = k \oplus m$ (il suffit de prendre $k = c \oplus m$).

En conséquence, un attaquant devant un message crypté de peut le décrypter s'il ne connaît pas $k$ puisque $m$ pouvant être tout élément de $\\{0, 1\\}^L$

Formalisons cette intuition.

{% note "**Théorème**" %}
Si $X$ et $Y$ deux variables aléatoires indépendantes sur $M = \\{0, 1\\}$ et telle que $X$ soit uniforme.

Alors la variable aléatoire $X \oplus Y$ est uniforme sur $\\{0, 1\\}^L$
{% endnote %}
{% details "preuve", "open" %}
Plaçons nous à un index $i$ fixé. On a :

- $Pr[X_i = 0] = Pr[X_i = 1] = .5$ car la variable aléatoire $X$ est uniforme et il y a exactement la moitié de M dont le $i$ème indice vaut 0 (pour l'autre moitié cet indice vaut 1).
- $Pr[Y_i = 0] = p_i$ et donc $Pr(Y_i = 1) = 1-p_i$

Comme $(X \oplus Y)_i$ vaut 0 que si $X_i$ et $Y_i$ valent conjointement 0 ou 1, on en déduit que :

$$
Pr[(X \oplus Y)_i = 0] = Pr[X_i = 0, Y_i = 0] + Pr[X_i = 1, Y_i = 1]
$$

Comme $X$ et $Y$ sont indépendants, $X_i$ et $Y_i$ le sont également et on a : $Pr[X_i = a, Y_i = b] = Pr[X_i = a]\cdot Pr[Y_i = b]$. Donc :

- $Pr[X_i = 0, Y_i = 0] = Pr[X_i = 0]\cdot Pr[Y_i = 0] = .5\cdot p_i$
- $Pr[X_i = 1, Y_i = 1] = Pr[X_i = 1]\cdot Pr[Y_i = 1] = .5\cdot (1-p_i)$

Ce qui entraîne que $Pr[(X \oplus Y)_i = 0] = Pr[X_i = 0, Y_i = 0] + Pr[X_i = 1, Y_i = 1] = .5$, et donc que $(X \oplus Y)$ est une variable aléatoire uniforme.

{% enddetails %}

On déduit du résultat précédent que si la clé est une variable aléatoire uniforme indépendante du texte à chiffré, le chiffre $c$ ne donne aucune information sur $m$. Ce résultat est remarquable car il ne présuppose rien sur le message $m$ et prouve bien l'inviolabilité du code de Vernam.

Enfin, un chiffre $c$ peut être issu de n'importe quel message original $m$, il suffit de choisir $k = c\oplus m$.

{% note %}

Ceci pose les bases que tout code doit avoir une clé choisie uniformément et indépendante du message.

{% endnote %}

Attention cependant.

### Ne répétez pas la clé

La code de Vernam est inviolable si on ne possède aucune information supplémentaire. Si on chiffre deux messages différents avec la même clé $k \oplus m$ et $k \oplus m'$, Eve na qu'à combiner les deux messages chiffrées pour faire disparaître la clé : $k \oplus m \oplus k \oplus m' = k \oplus k \oplus m \oplus m' = m \oplus m'$. De là, si Eve sait que le message est en Français, il lui suffit de déplacer des mots sur le code pour voit apparaître d'autres mots :

```
  Je suis très bien protégé
+ Il mangeait des escargots
  XXXXXXXXXXXXXXXXXXXXXXXXX
```

En faisant glisser "suis" par exemple, lorsqu'il arrive sur l'emplacement de la première ligne on obtient :

```
     suis
  Je suis très bien protégé
+ Il mangeait des escargots 
  XXXmangXXXXXXXXXXXXXXXXXX
```

Ce qui nous donne :

- une position dans le premier mot
- un début de mot dans la seconde phrase que l'on peut chercher à completer

```
     mangeait
  Je suis très bien protégé
+ Il mangeait des escargots 
  XXX        XXXXXXXXXXXXXX
     suis trè 
```

Et petit à petit on casse le chiffre....

{% info %}
C'est arrivé en vrai.
[Projet Venona](https://fr.wikipedia.org/wiki/Projet_Venona)

{% endinfo %}

### <span id="Vernam-intégrité"></span>Intégrité

Si le message est inviolable, il n'est pas infalsifiable.

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
------------------------------
  YYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

Certes. Mais je peux ajouter des informations si je le désire

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
------------------------------
  YYYYYYYYYXXXXXXXXYYYYYYYYYYY
```

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
+ 0000000009999999€00000000000
------------------------------
  YYYYYYYYYZZZZZZZZYYYYYYYYYYY
```

Ce qui est donne une fois déchiffré :

```
  Je donne 12 euros à François
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+ 00000000012 euros00000000000
+ 0000000009999999€00000000000
+ XXXXXXXXXXXXXXXXXXXXXXXXXXXX
------------------------------
  Je donne 9999999€ à François
```

Ce qui est super Sympa de votre part !

Ça à l'air un peu tiré par les cheveux vu comme ça, mais si vous chiffrés des mails par exemple, ils commencent tous par un champ `FROM` et un champ `TO`, si le cryptanalyse sait ce que vous codez et que c'est issu d'un protocole, il y a de forte chances qu'il y ait des paramètres à emplacement fixe que l'on peut modifier.

### Authentification

Rien ne garanti que c'est bien l'expéditeur voulu qui a envoyé le message :

```
           cle k                   cle k'
Alice <-------------> Mallory <--------------> Bob

```

Si Mallory se fait passer d'un côté pour Bob et de l'autre côté pour Alice, aucun des deux ne peux le soupçonner.
