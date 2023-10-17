---
layout: layout/post.njk

title: Sockets réseaux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Pour le C communication :

- [fork](https://www.youtube.com/watch?v=cex9XrZCU14)
- [socket et fichier](https://www.youtube.com/watch?v=il4N6KjVQ-s)
- sur la même machine :
  - parent/enfant issu de fork. Comme copie les file descriptor, ce sont les mêmes et on peut utiliser des pipe <https://stackoverflow.com/questions/14170647/fork-parent-child-communication>
  - [unix domain socket](https://copyconstruct.medium.com/file-descriptor-transfer-over-unix-domain-sockets-dcbbf5b3b6ec)

_ <https://stackoverflow.com/questions/28003921/sending-file-descriptor-by-linux-socket/>

Faire en C exemple :

```
         pipe         socket
serveur ------ fork1 --------  client1
         \
           --- fork2 --------  client2
```

- [pipes pour communiquer](https://www.youtube.com/watch?v=dhFkwGRSVGk)
- [ipc avec fifo](https://www.softprayog.in/programming/interprocess-communication-using-fifos-in-linux)

- [named pipe plus rapide que sockets](https://www.youtube.com/watch?v=dhFkwGRSVGk)
- [ipC](https://www.youtube.com/watch?v=BU9m45WWqjM)
- [communication par message](https://www.studocu.com/row/document/comsats-university-islamabad/operating-systems/lab-manual-8-abc/50895124)
- [message queue vs pipe](https://www.geeksforgeeks.org/difference-between-pipes-and-message-queues/)
- message queue C :
  - <https://www.baeldung.com/linux/kernel-message-queues>
  - <https://www.youtube.com/watch?v=fjJliu9iViw>