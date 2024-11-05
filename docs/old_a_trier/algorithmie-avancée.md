---
layout: layout/post.njk 
title: "S5 : Algorithmie avancée"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

## TBD

> TBD exos graphes <http://www.discmath.ulg.ac.be/cours/Graphes22-23.pdf>


> TBD théorie de Galois : <https://www.maths.ed.ac.uk/~tl/galois/> et version papier <https://arxiv.org/abs/2408.07499>
>
> TBD voir plan de ce truc :
>
> - <https://www.youtube.com/watch?v=nRA2unaJZIc&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh>
> - MIT algo. <https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp>

### Hasard

- proba : <https://www.youtube.com/watch?v=pxzbbP7FmPA&list=PLYhJxc3T5xALIscExdC0YqPKdBgSp6EfP>

Démon de Laplace : <https://fr.wikipedia.org/wiki/D%C3%A9mon_de_Laplace>

- ring oscillator :
  - <https://www.uio.no/studier/emner/matnat/ifi/INF4420/v12/undervisningsmateriale/INF4420_12_Ringoscillators.pdf>
  - <https://link.springer.com/content/pdf/10.1007/s00145-010-9089-3.pdf>
  - <https://www.iacr.org/archive/ches2014/87310122/87310122.pdf>
  - <https://www.untruth.org/~josh/security/An%20Approach%20for%20Entropy%20Assessment%20of%20Ring%20Oscillator-Based%20Noise%20Sources.pdf>
  - <https://perso.univ-rennes1.fr/david.lubicz/articles/ieee.pdf>
  - <https://perso.univ-rennes1.fr/david.lubicz/articles/gda.pdf>

- <https://www.youtube.com/watch?v=iT20A4KQxyM>
- les décimales de pi :
  - <https://www.youtube.com/watch?v=FDXf1XxCXAk>
  - sont aléatoires si tu ne sais pas que c'est elles.
  - prendre les bits de la représentation binaire des décimales de pi et leur faire passer des tests d'aléatoire.
- "vrai" aléatoire :
  - Johnson-Nyquist noise.
  - quantum random
  - humain pas bon pour faire du hasard : <https://www.youtube.com/watch?v=tP-Ipsat90c>

<https://www.youtube.com/watch?v=RcXmhKF9ewo>

#### mélanger

- permutation : <https://en.wikipedia.org/wiki/Permutation>
- proba et compression : <https://www.youtube.com/watch?v=RFWJM8JMXBs>

#### pseudo-aléatoire

- entropie Shanon : <https://www.youtube.com/watch?v=ErfnhcEV1O8>
- xorshift :
  - <https://en.wikipedia.org/wiki/Xorshift>
  - <https://www.codeproject.com/Articles/5264513/XorShift-Jump-101-Part-1-Matrix-Multiplication>
  - <https://www.jstatsoft.org/article/download/v008i14/916>
  - <https://www.iro.umontreal.ca/~lecuyer/myftp/papers/xorshift.pdf>
  - <https://www.jstatsoft.org/index.php/jss/article/view/v008i14/xorshift.pdf>
- vote majoritaire : fonctionne si >50% bonne réponse. Donc si éduqué. Si l'algorithme/peuple est con, la réponse sera conne. Rapport au parlement Suisse
- <https://www.youtube.com/watch?v=nBq4sFg3at0>
- <https://www.youtube.com/watch?v=YvH53vJM69E&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=38>
- randomness extractor :
  - <https://en.wikipedia.org/wiki/Randomness_extractor>
  - <https://www.youtube.com/watch?v=YvH53vJM69E&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=38>
  - <https://people.seas.harvard.edu/~salil/pseudorandomness/extractors.pdf>
  - <http://archive.dimacs.rutgers.edu/Workshops/Pseudorandom/Slides/extractors.pdf>
  - <https://cryptography.fandom.com/wiki/Randomness_extractor>
  - entropy :
    - <https://www.2uo.de/myths-about-urandom/>
    - <https://www.linuxfromscratch.org/hints/downloads/files/entropy.txt>
    - <https://www.blackhat.com/docs/us-15/materials/us-15-Potter-Understanding-And-Managing-Entropy-Usage.pdf>
    - <https://blog.boot.dev/cryptography/what-is-entropy-in-cryptography/>
    - <https://en.wikipedia.org/wiki/Fortuna_(PRNG)>
    - <https://en.wikipedia.org/wiki/Entropy_(information_theory)>
  - CSPRNG :
    - <https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator>
    - <https://cryptobook.nakov.com/secure-random-generators/secure-random-generators-csprng>
  - explicit extractor
  - graphe de ramanujan :
    - <https://fr.wikipedia.org/wiki/Graphe_de_Ramanujan>
    - <https://mast.queensu.ca/~murty/ramanujan.pdf>
    - random walk on graphs :
      - <https://www.lirmm.fr/~sau/JCALM/Josep.pdf>
      - <https://www.fi.muni.cz/usr/gruska/random19/random1909_2_2.pdf>
      - <https://www.cs.cmu.edu/~15859n/RelatedWork/random-walks-on-graphs.pdf>
      - <https://www.youtube.com/watch?v=tZse1YyiHdg&list=PLZNqNoh4u1gzKMYgrrgcKK5ozNQ7f_OMP>
      - <https://www.youtube.com/watch?v=aEJB8IAMMpA>

#### Randomized algorithms

1. rappeler quicksort
2. random select
3. las Vegas et Monte Carlo
4. Utilitaire :
   1. linéarité de l'espérance
   2. inégalités de Markov et Tchebychev
   3. coupon's collector
   4. Chernov bounds 4.1 et application en 4.2
5. La méthode probabilistes
   1. Lovász Local Lemma application à k-sat
6. chaines de Markov et graphes
7. Techiniques algébriques
   1. Multiplication de matrices
   2. vérification de valeur de polynomes
   3. PCP et vérification de preuve

- problème du mariage random 3.5 livre random algo qui amène au problème du collecteur de pokemon 3.6

Ne faire ici que les choses générale et reprendre dans chaque partie un cas d'utilisation d'algo random.

- max-sat 5.2
- min-cut
- 
- algorithmes :
  - exemple : <https://perso.eleves.ens-rennes.fr/people/clement.legrand-duchesne/TIPE.pdf>
  - cours ens introduction aux algorithmes d'approximation et randomisés : <https://pauillac.inria.fr/~quercia/documents-info/Luminy-2003/schabanel/schabanel.pdf>
  - livre approximation algorithm de Vazirani : <https://ics.uci.edu/~vazirani/book.pdf>
- <https://www.youtube.com/watch?v=4y_nmpv-9lI>
- page rank = Markov chain.
- dérandomization exemple dans randomized algorithm
- meme si on ne gagne pas en O, parfois on gagne sur la constante multiplicative (ex. médiane)
- random placement = nlogn en moyenne = coupon collector
- <https://www.youtube.com/watch?v=gKuzFZ9ko7I&list=PLwp5OpRmcl_HPVnrDNmQ9cMbYiiFxZ19d&index=1>
- cours mit :
  - <https://ocw.mit.edu/courses/6-856j-randomized-algorithms-fall-2002/pages/lecture-notes/>
  - <https://ocw.mit.edu/courses/6-856j-randomized-algorithms-fall-2002/pages/assignments/>
- différence entre : avoir des données random ou avoir un algorithme random (hasard indef des données). eg quicksort.
- universal hash function : déplace le hasard des clé aux fonctions de hash.
- universal hash family
- <https://www.cs.cmu.edu/~venkatg/teaching/15252-sp20/notes/notes-probabilistic-method.pdf> et <https://www.cs.cmu.edu/~15850/handouts/matousek-vondrak-prob-ln.pdf> <https://ocw.mit.edu/courses/18-226-probabilistic-method-in-combinatorics-fall-2020/pages/lecture-notes/>
- random median las-vegas : <https://math.mit.edu/~goemans/18310S15/rand_median_quicksort-notes.pdf>. PLus simple a implementer que le lineaire
- livre de harvey : <https://www.cs.ubc.ca/~nickhar/Book1.pdf>
- 1er algorithme randomizé : vote majoritaire
- matching randomisé : <https://people.csail.mit.edu/virgi/6.890/lecture17.pdf>, <https://web.eecs.umich.edu/~pettie/matching/Rabin-Vazirani-randomized-maximum-matching.pdf>
- mediane et quicksort :<https://math.mit.edu/~goemans/18310S15/rand_median_quicksort-notes.pdf>
- exemples : <https://www.youtube.com/watch?v=0r2D32esF3Y> et <https://www.youtube.com/watch?v=GS2MxmorEzc>
- Hasard ? Intros :
  - court : <https://www.youtube.com/watch?v=nBq4sFg3at0>
  - TB : <https://www.youtube.com/watch?v=_tN2ev3hO14>
  - le hasard est dans l'œil de celui qui regarde. SI on ne peut pas prédire le suivant, pseudo-random = random. C'est comme le démon de Laplace.
- regarder dans le Kleinberg/Tardos
- cours Dieter Kratch
- <https://www.youtube.com/watch?v=0r2D32esF3Y> et <https://www.youtube.com/watch?v=GS2MxmorEzc>
- <https://www.youtube.com/watch?v=01ohO542NMI&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO>
- ? <https://www.youtube.com/watch?v=bsZXgXdSomc&list=PLOMwD5hwqoJ_slbq9iSE6tURVqX5eLKq8>
- bpp :
  - <https://cs.uwaterloo.ca/~eblais/cs365/PandBPP.html>
  - <https://www.youtube.com/watch?v=CinKHIkJKu0&list=PLdUzuimxVcC0DENcdT8mfhI3iRRJLVjqH&index=64>
- <https://www.columbia.edu/~cs2035/courses/csor4231.S19/rand.pdf>
- <https://theory.stanford.edu/people/pragh/amstalk.pdf>
- monte carlo : <https://www.youtube.com/watch?v=CmpWM2HMhxw>
- las vegas : <https://en.wikipedia.org/wiki/Las_Vegas_algorithm>
- randomized cut : <https://www.youtube.com/watch?v=KqMGeNZuwfI>
- Krager's algorithm <https://web.stanford.edu/class/archive/cs/cs161/cs161.1166/lectures/lecture15.pdf> <https://www.youtube.com/watch?v=KqMGeNZuwfI> <https://cadmo.ethz.ch/education/lectures/FS18/SAADS/papers/SODA93_Global_Mincuts.pdf>. Utiliser union-find ? <https://fr.wikipedia.org/wiki/Union-find>
- markov chain : graph et random
- prime number en polylog. Random et dérandomisation : <https://www.math.toronto.edu/swastik/courses/rutgers/ANT-F14/lec14.pdf>
- chebychef <https://math.univ-angers.fr/documents/08-ep2.pdf>

- <https://www.youtube.com/watch?v=QPk8MUtq5yA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=9>
- chaine de markov = graphe. fortement connexe = irreducible. Gatlon/watson.
  - galton watson branching process : <https://www.youtube.com/watch?v=s8-hhLdxWhI&list=PLu0UjEkXuQyo_tqRSqht_vNyB8zeejSx-&index=11>

- td :
  - <https://courses.cs.washington.edu/courses/cse312/18wi/312A/lecture23.pdf>
  - <https://people.engr.tamu.edu/j-chen3/courses/658/2016/notes/s6.pdf>
- 2-sat via Davis et Putnam
- <https://www.cs.ubc.ca/~nickhar/Book.pdf>

### Cryptographie

- vente de secrets sans savoir lequel. Truc de Pascal. Dans le bouquin ?
- zéro knowledge proof. Livre + 3 coloration.
- attention aux attaques :
  - qui rendent les nombre aléatoire pas aléatoire : signal injection
  - qui mesurent l’énergie prisent pour les calculs
- low density attack :
  - <https://web.stevens.edu/algebraic/Files/SubsetSum/p229-lagarias.pdf>
  - <https://eprint.iacr.org/2007/066.pdf>
- reprendre cours 23-24
- zero knowledge proof :
  - <https://www.youtube.com/watch?v=5ovdoxnfFVc>
  - <https://www.youtube.com/watch?v=V5uVKZn3F_4>
- factorization :
  - statut inconnu : <https://en.wikipedia.org/wiki/Integer_factorization>
  - mais sûrement pas NP-complet <https://cstheory.stackexchange.com/a/160> car dans np/co-np
  - <https://www.youtube.com/watch?v=vfjN7MmSB6g&list=PLkvhuSoxwjI_UudECvFYArvG0cLbFlzSr>
- problèmes dont on ne sait pas s'il sont NPC. Ils sont dures partout et pas seulement au max. Exemple du protocole avec sac a dos qui ne fonctionne pas car les instances dures sont rares (<https://www-users.cse.umn.edu/~odlyzko/doc/arch/knapsack.survey.pdf>) Idem pour 3-coloriable si K4 c'est foutu c'est non.
- LLL : <https://www.youtube.com/watch?v=U8MI2a_BHHo>

### C et structures de données

- <https://www.youtube.com/@TheatricalTheta> les corrigés du K&R

- <https://www.ens-lyon.fr/DI/wp-content/uploads/2010/12/poly09.pdf>
- perfect hashing.
  - <https://en.wikipedia.org/wiki/Dynamic_perfect_hashing>
  - chichelli : <https://courses.cs.vt.edu/~cs3114/Summer13/Notes/T12.PerfectHashFunctions.pdf>
  - <https://www.cs.otago.ac.nz/cosc242/pdf/L11.pdf>
- liste chaînée, doublement chaînée :
  - usage. Attention aux O(n) pour la recherche même si la liste est triée (ou a pas de ram) et au défaut de cache.
  - skip list comme la remontée en log dans les arbres mais pour structure dynamique <https://fr.wikipedia.org/wiki/Skip_list>.<https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/skiplists.pdf>
  - <https://ticki.github.io/blog/skip-lists-done-right/>
  - <https://www.cloudcentric.dev/implementing-a-skip-list-in-go/>
  - hash à trou à la Knuth
  - pourquoi les utiliser vs arbre de recherche : <https://stackoverflow.com/a/260277>. Mais c'est rare que ce soit important. Donc dans le doute, arbre de recherche
  - <https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf>
  - <https://www.singlestore.com/blog/what-is-skiplist-why-skiplist-index-for-memsql/>

- gestion de la mémoire :
  - noyau programme et mémoire
  - données : dépend du type des données.

- C : compilation et pointeurs
- binary search <https://www.youtube.com/watch?v=GU7DpgHINWQ&list=PLl0KD3g-oDOHpWRyyGBUJ9jmul0lUOD80&index=3>
- python et C
- structures de données en C :
  - <https://www.youtube.com/watch?v=VOpjAHCee7c&list=PL9IEJIKnBJjFiudyP6wSXmykrn67Ykqib>
  - pile/file : pointeur et à la Knuth
  - graphes et arbres : exemple de la FAT
  - B-tree : <https://www.youtube.com/watch?v=K1a2Bk8NrYQ>
  - LSM-tree : <https://www.youtube.com/watch?v=I6jB0nM9SKU> et <https://www.youtube.com/watch?v=ciGAVER_erw>

### Graphes

- 2-sat et graphes :
  - Graphes médians = 2-sat
  - composantes fortement connexes :
    - <https://cp-algorithms.com/graph/2SAT.html>
    - <https://fr.wikipedia.org/wiki/Algorithme_de_Kosaraju>
- cascade in networks. Kleinberg. Tardos 2003.<https://www.youtube.com/watch?v=gw8Hgx-EtJQ&list=PLriUvS7IljvkGesFRuYjqRz4lKgodJgh2&index=14>
- <https://lgayral.pages.math.cnrs.fr/fr/agreg/>
- random graphs. Friendship paradox. Tes amis ont plus d'amis que toi (existence de sommets avec beaucoup de voisins)
- Matrice d'adjacence :
  - chemins
  - valeurs/vecteur propre : markov et sommets importants (pagerank)
- urne de polya <https://www.youtube.com/watch?v=lqec2my4gtg> comme idée de réseau par renforcement graphe
- small world graph <https://en.wikipedia.org/wiki/Watts%E2%80%93Strogatz_model>

- en moyenne tes voisins ont plus de voisins que toi (network 6 fin)
- liste degré vers graphe :
  - <https://en.wikipedia.org/wiki/Havel%E2%80%93Hakimi_algorithm>
  - <https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem>
  - <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FCA8B7DC763D3D504C68E3A5FDD8DE45/S0004972700002872a.pdf/simple_proof_of_the_erdosgallai_theorem_on_graph_sequences.pdf>
- graphes aléatoire a k sommets : <https://egtheory.wordpress.com/2012/03/29/random-regular-graphs/>
- graphes comme réseaux <https://www.youtube.com/watch?v=1T5-BG6yngM&list=PLriUvS7IljvkGesFRuYjqRz4lKgodJgh2&index=1>
  - arbre = petit monde (profondeur en log)
- random graphs <https://www.youtube.com/watch?v=WABtTfTnVCI>
  - phase transition
  - unique graphe infini
- spectral graphs : <https://www.youtube.com/watch?v=uTUVhsxdGS8>
- playlist <https://www.youtube.com/watch?v=7T-webnamho&list=PLzXFiYlgM72LMHOeTaZSHvkREdLbKBxLI>

- graphe de Rado pour preuve aléatoire et graphe infini :
  - <https://www.youtube.com/watch?v=3QjZ31lj974>
  - <https://www.youtube.com/watch?v=XwVZ5VttrW0&t=3s>
- vertex cover
- Christophides : <https://pages.cs.wisc.edu/~shuchi/courses/787-F09/scribe-notes/lec9.pdf>
- structures implique de nombreuses classes de problèmes et donc d'algorithmes. POuvant être adaptés a ses propres solution s. eg voyageur de commerce. matching. etc.
- bi-parti

- postier chinois
- couplage
- graphes infinis
- random graphs
- union-find
- nombres de Ramsey :
  - <https://www.youtube.com/watch?v=eHXeOnIrVxU&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=19>
  - <https://en.wikipedia.org/wiki/Ramsey%27s_theorem>
  - preuve du théorème de Ramsey : <https://uu.diva-portal.org/smash/get/diva2:1729430/FULLTEXT01.pdf>
  - <https://www.youtube.com/watch?v=GS6tknuyV1g&list=PLCgtM0JzEuDOI6dYyK20U6tdy_km3RcfM&index=2>
  - <https://math.uchicago.edu/~may/REU2020/REUPapers/Wang,Cathy.pdf>

- independant set : <https://www.youtube.com/watch?v=eXYXWbMs5lw&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=20>
- LLL in graphs : <https://www.youtube.com/playlist?list=PLCgtM0JzEuDOI6dYyK20U6tdy_km3RcfM>

- arbre binary lifting : <https://www.youtube.com/watch?v=oib-XsjFa-M&list=PLl0KD3g-oDOHpWRyyGBUJ9jmul0lUOD80&index=15>

- mineur : en parler un peu et donner les principaux résultats que l'on précisera dans des cas particuliers : <https://fr.wikipedia.org/wiki/Mineur_(th%C3%A9orie_des_graphes)>
  - <https://www.labri.fr/perso/bousquet/Exposes/forum-fr.pdf>
  - bel ordre et mineurs : <https://perso.ens-lyon.fr/eric.thierry/Graphes2007/denis-kuperberg.pdf>

### Complexité

#### Complexité et cryptographie

- nombres premiers :
  - <https://en.wikipedia.org/wiki/AKS_primality_test>
  - <https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p12.pdf>

#### Algorithmes d'approximation

- exos : <https://people.irisa.fr/Francois.Schwarzentruber/algo2/03approximation.pdf>
- approximation algorithm.
- multiplication de matrice <https://www.youtube.com/watch?v=sZxjuT1kUd0>

- random :
  - random et polynomial. Classes de problèmes : <https://fr.wikipedia.org/wiki/BPP_(complexit%C3%A9)> : <https://www.youtube.com/watch?v=mZck0N_T9Cs>
  - k-sat et random : random qui prouve <https://www.youtube.com/watch?v=F2JdDIMi2A0&list=PLkvhuSoxwjI_JL7GYcJHK7-EK55t0KYGO&index=22>
  - 2-sat random : <https://people.seas.harvard.edu/~cs125/fall14/lec19.pdf>
  - LLL :
    - <https://courses.cs.washington.edu/courses/cse525/13sp/scribe/lec10.pdf>
    - <https://arxiv.org/pdf/0903.0544>
  
## TBD2 le retour

1. Couplage :
    1. valué : Lovaz dans Matching theory
    2. donner algo couplage Edmonds fleur + autre.
2. aléatoire, algorithme randomisé et approximation
    1. Commencez par les considération probabilistes sous-jacentes et exemples direct pour chaque
    2. exemples classiques
3. retour sur le couplage et algo randomisé
