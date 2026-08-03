---
layout: layout/post.njk

title: Nouvelle installation de son système
authors: 
    - François Brucker


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'installation anarchique de logiciels et d'extension à son système génère inévitablement de l'instabilité. Si vous ordinateur réagit bizarrement, est lent, produit de nombreuses erreurs incompréhensible une installation fraîche de son système est souvent une solution efficace. Bien préparée elle ne requiert de plus que peu de temps.

{% info %}

Il est souvent possible de réinstaller un nouveau système en conservant vos données. C'est souvent très pratique mais pour une première fois, je vous conseille de faire une installation sur un disque vierge, c'est à dire en ne **conservant rien** de ce qu'il y avait sur votre disque dur.

{% endinfo %}

## Préparation

Installer un nouveau système nécessite de reformater votre disque dur. Avant cela il vous faut faire trois choses :

{% faire %}

- sauvegardez vos données sur une clé pour que vous puissiez facilement les remettre sur votre nouveau système
- vérifier les différentes applications actuellement installées et listez celles que vous voulez à nouveau installer.
- lister les différents compte et mots de passe dont vous aurez besoin (wifi, steam, google, ...)

{% endfaire %}

L'installation devra très certainement aller sur internet pour récupérer les données du système ou retrouver vous données sauvegardées sur le cloud ([icloud](https://support.apple.com/fr-fr/guide/icloud/welcome/icloud) sur mac ou [one drive](https://www.microsoft.com/fr-fr/microsoft-365/onedrive/online-cloud-storage) sous windows). Pour que tout se passe au mieux :

{% faire %}

- notez le login et le mot de passe du cloud pour pouvoir y accéder lors de l'installation
- notez le nom de votre wifi et son mot de passe.
{% endfaire %}

## Installation

{% faire %}
Procédez à l'installation de votre système en suivant les recommandations ci-après.
{% endfaire %}

### Sous mac

{% lien %}
<https://support.apple.com/fr-fr/HT204904>
{% endlien %}

Notez votre login et mot de passe icloud. Vous en aurez besoin à l'installation

### Sous Windows

{% lien %}
<https://www.microsoft.com/fr-fr/software-download/windows11>

En suivant les instructions de *Installer une nouvelle installation à l’aide d’un support d’installation*.
{% endlien %}

### Sous Linux

{% lien %}
<https://doc.ubuntu-fr.org/installation>
{% endlien %}

## Mise à jour du système

Une fois installé, il faut mettre le système à jour pour installer les toutes dernières versions.

### Sous Windows 11

{% lien %}
[Mise à jour de Windows 11](https://support.microsoft.com/fr-fr/windows/obtenez-la-derni%C3%A8re-mise-%C3%A0-jour-7d20e88c-0568-483a-37bc-c3885390d212)

{% endlien %}

### Sous Macos

{% lien %}

[Mise à jour de Macos](https://support.apple.com/fr-fr/HT201541)

{% endlien %}

### Sous Linux/Ubuntu

{% lien %}

[Software Updater](https://en.wikipedia.org/wiki/Software_Updater)

{% endlien %}

Ou dans [un terminal](../terminal){.interne} :

```
sudo apt update && sudo apt full-upgrade -y
```

### Installation des Drivers

#### Windows 11

- carte graphique
- clavier/souris si nécessaire
- imprimante

#### Macos

- _icloud_ drive
- imprimante
- tablette graphique si vous en avez une

#### Linux/Ubuntu

- imprimante
- tablette graphique si vous en avez une

## Utilitaires de tous les jours

Non indispensable mais que vous utilisez tous les jours

- steam, gog, epic, battle.net, origin, u-play, etc
- vlc, office 360
- discord
- ...