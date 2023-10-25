---
layout: layout/post.njk

title: Concurrence

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<https://en.wikipedia.org/wiki/Concurrency_pattern>


<https://www.classes.cs.uchicago.edu/archive/2018/spring/12300-1/lab6.html>


## accès concurrent

atomicité. 

set and check.

algorithme de Dekker

## Threads

[thread safety](https://www.youtube.com/watch?v=pWTtPnwialI)
<https://web.mit.edu/6.005/www/fa14/classes/18-thread-safety/>
[programming with threads playlist](https://www.youtube.com/watch?v=uA8X5zNOGw8&list=PL9IEJIKnBJjFZxuqyJ9JqVYmuFZHr7CFM)


<https://fr.wikipedia.org/wiki/Situation_de_comp%C3%A9tition>

si pas de mutex : race condition

si mutex :
  - deadlock
  - starvation