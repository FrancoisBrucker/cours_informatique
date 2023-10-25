---
layout: layout/post.njk

title: Sockets réseaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


- [tcp par le kernel](https://www.youtube.com/watch?v=ck4WvYM9V4c)
Pour le C communication :

- [Beej's Guide to Network Programming Using Internet Sockets](https://beej.us/guide/bgnet/)
- <https://opensource.com/article/19/4/interprocess-communication-linux-networking>

_ <https://stackoverflow.com/questions/28003921/sending-file-descriptor-by-linux-socket/>

Faire en C exemple :

```
         pipe         socket
serveur ------ fork1 --------  client1
         \
           --- fork2 --------  client2
```

- faire un fork. mettre des données dans le stdin de l'un, passer les données par un pipe et les ressortir sur le stdout de l'autre.

- [pipes pour communiquer](https://www.youtube.com/watch?v=dhFkwGRSVGk)
- [ipc avec fifo](https://www.softprayog.in/programming/interprocess-communication-using-fifos-in-linux)

- [named pipe plus rapide que sockets](https://www.youtube.com/watch?v=dhFkwGRSVGk)
- [ipC](https://www.youtube.com/watch?v=BU9m45WWqjM)
- [communication par message](https://www.studocu.com/row/document/comsats-university-islamabad/operating-systems/lab-manual-8-abc/50895124)
- [message queue vs pipe](https://www.geeksforgeeks.org/difference-between-pipes-and-message-queues/)
- message queue C :
  - <https://www.baeldung.com/linux/kernel-message-queues>
  - <https://www.youtube.com/watch?v=fjJliu9iViw>
- <https://www.youtube.com/watch?v=Nr31eiB5wgc>