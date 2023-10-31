---
layout: layout/post.njk

title: Concurrence

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

1. ce qu'est un thread
2. parralèle pourquoi c'est bien : algo + complexité
3. faire ce qui marche si pas partagé :
   1. serveur -> thread
   2. calcul image fractale
4. si partagé :
   1. opération atomique (!)
   2. mutex
   3. non blocking avec opérations atomiques

<https://en.wikipedia.org/wiki/Concurrency_pattern>


<https://www.classes.cs.uchicago.edu/archive/2018/spring/12300-1/lab6.html>


## accès concurrent

atomicité. 

set and check.

algorithme de Dekker

## Atomicité

<https://en.wikipedia.org/wiki/Read%E2%80%93modify%E2%80%93write> et [3 opération dans read modify write](https://stackoverflow.com/questions/49452022/why-its-termed-read-modify-write-but-not-read-write)

plusieurs threads qui font +1. Si atomique ok, sinon peut poser des soucis.

## Threads

<https://www.cs.dartmouth.edu/~campbell/cs50/threads.html>

[locks ?](https://docs.oracle.com/cd/E19455-01/806-5257/sync-12/index.html)
[thread C](https://beej.us/guide/bgc/html/#multithreading)
[thread safety](https://www.youtube.com/watch?v=pWTtPnwialI)
<https://web.mit.edu/6.005/www/fa14/classes/18-thread-safety/>
[programming with threads playlist](https://www.youtube.com/watch?v=uA8X5zNOGw8&list=PL9IEJIKnBJjFZxuqyJ9JqVYmuFZHr7CFM)


<https://fr.wikipedia.org/wiki/Situation_de_comp%C3%A9tition>

si pas de mutex : race condition

si mutex :
  - deadlock
  - starvation

[non blocking](https://en.wikipedia.org/wiki/Non-blocking_algorithm)
[algo thread C++](https://www.youtube.com/watch?v=Zu5JcxZt_f8&list=PLxNPSjHT5qvsGKsAhirvZn7W73pXhXpfv)

blocking algo :

- thread avec le lock est endormi : ça bloque tous les autres.
- non blocking, peut dépasser le max si on fait pas gaffe (+1 si < max por plusieurs threads)

non blocking :

- <https://www.youtube.com/watch?v=Uh6wXoXydAg>
