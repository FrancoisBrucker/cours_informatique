---
layout: layout/post.njk

title:  "corrigé Test 5 : classes et objets (le retour)"
authors:
    - François Brucker
---

## 1

### 1.1

Un attribut de `Store`{.language-} est de type `StateObject`{.language-}. Comme il est passé à la construction, c'est une agrégation.

### 1.2

#### 1.2.1

La proposition 3 est fausse car `StateObject`{.language-} n'a pas de paramètre dans son constructeur.

#### 1.2.2

On préférera la proposition 2 car elle garde elle n'accède pas directement aux attributs, elle utilise la méthode `set_state()`{.language-} qui est faite pour ça.

## question 2

### 2.1

Permet aux objets observant un sujet d'être informé des changements d'un sujet par celui-ci.

### 2.2

```python
def add(self, observer):
    self.observer_list.append(observer)
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
