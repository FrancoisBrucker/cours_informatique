---
layout: page
title:  "corrigé Test 5 : classes et objets (le retour)"
category: cours
tags: code python
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [exercices]({% link cours/algorithme-code-theorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-theorie/exercices/2021-2022/index.md %}) / [corrigé Test 5 : classes et objets (le retour)]({% link cours/algorithme-code-theorie/exercices/2021-2022/5_test_corrige.md %})
{: .chemin}

## 1

### 1.1

Un attribut de `Store` est de type `StateObject`. Comme il est passé à la construction, c'est une agrégation.

### 1.2

#### 1.2.1

La proposition 3 est fausse car `StateObject` n'a pas de paramètre dans son constructeur.

#### 1.2.2

ON préférera la proposition 2 car elle garde elle n'accède pas directement aux attributs, elle utilise la méthode `set_state()` qui est faite pour ça. 

## question 2

La figure suivante montre le diagramme UML du design pattern *Observer*. Les objets de la classe `Observer` (ou ceux héritant d'elle) s'inscrivent à un objet de la classe `Subject` (via la méthode `add`) pour être prévenus de chaque changement d'état (via la méthode `notify`).

![observer](./uml_observer.png){:style="margin: auto;display: block;"}

> On vous demande d'écrire le code en python.

### 2.1

permet aux objets observant un sujet d'être informé des changements d'un sujet par celui-ci.

### 2.2

```python
def add(self, observer):
    self.oberver_list.append(observer)
```

### 2.3

```python
def update(self, subject):
    self.subject_update = subject.get_state()
```

### 2.4

```python
def notify(self):
    for observer in self.observer_list:
        observer.update(self)
```

### 2.5

C'est le principe de la programmation événementielle.
