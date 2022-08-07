---
layout: page
title:  "Decathlon Django"
category: projets
tags: decathlon django
author:
- "Solenzio Konlé"
---

Ce projet fut initié à l'origine dans le cadre du projet de Méthode de Développement de l'option Digital.e.
Le git du projet peut être trouvé [ici](https://github.com/sconle/decathlon).

## Décathlon

Le décathlon est un jeu de dé basé sur la discipline du décathlon. Il y a dix épreuves différentes bien qu'il n'y ait pour l'instant qu'une seule de développée: le lancé de javelot.
Les règles sont disponibles sur ce [PDF](http://www.jeuxprintandplay.fr/Jeux/Decathlon/DECATHLONfr.pdf).

### Technologies utilisées

Les technologies utilisées sont Django en back, du simple HTML/CSS/JavaScript pour le front et sqlite3 comme BDD.

>La mise en place d'un projet Django a été expliquée en détail dans un autre projet de MD2, vous pouvez le retrouver [ici](https://francoisbrucker.github.io/cours_informatique/cours/web/projets/md2_vue_drf.html).

Ainsi, je ne vais pas redonner tous les éléments d'installation d'un projet Django mais vais donner quelques petits conseils sur des éléments que j'ai pu relever.

### Déroulé du projet

En première idée je souhaitais utiliser les WebSockets afin d'avoir un jeu en multijoueur. Il fallait donc créer une structure d'utilisateur.
Heureusement Django offre déjà un modèle de User avec des fonctions prédéfinis bien pratique.

Les fonctions les plus utiles des User sont:
- `authenticate` qui permet de trouver si un user exists en fonction d'un pseudo et d'un password
- `login` qui permet de log un user à la session actuelle
- `logout` qui permet de déconnecter le user actuel de la session
- `User.objects.create_user` qui crée un user à partir d'un pseudo, un email et un password

~~~ shell
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as true_logout

def connexion(request, pseudo, pwd, mail):
  user = authenticate(username=pseudo, password=pwd)
  if user is not None:
    login(request, user)
  else:
    user = User.objects.create_user(pseudo, mail, pwd)
    login(request, user)
  return render(request, "connexion.html")
  
 def deconnexion(request):
  true_logout(request)
  return redirect("/")
~~~

Ici un petit exemple de deux vues, l'une qui connecte et l'autre qui déconnecte.
>Lorsque l'on utilise la fonction `logout`, il vaut mieux la renommer car cette dernière peut parfois déjà exister en tant que fonction native.
{.attention}

Pour le reste des modèles du site, nous en créerons un par jeu. Pour l'instant il n'y a donc que la classe JavelotThrow.

~~~ shell
from django.db import models


def dict_scoreboard():
    return {"player1": 0,
            "player2": 0,
            "player3": 0,
            "player4": 0
            }

def dict_dice():
    return {"1": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1
            }


def dict_keeped():
    return {}


class JavelinThrow(models.Model):
    name = models.CharField(max_length=20)
    dice_value = models.JSONField(default=dict_dice())
    dice_keeped = models.JSONField(default=dict_keeped())
    currentPlayer = models.CharField(default="player1", max_length=50)
    scoreboard = models.JSONField(default=dict_scoreboard)
    remaining_attempts = models.IntegerField(default=3)
    is_online = models.BooleanField(default=True)
    number_of_player = models.IntegerField(default=4)
~~~

Pour l'instant, le site a donc comme fonctionnalités de supporter un système de gestion d'utilisateur ainsi que le mini-jeu lancer de javelot où l'on peut choisir de jouer entre 2 et 4 joueurs et où le scoreboard est sauvegardé.

### Lancer le projet en local

Si vous souhaitez installer le projet, il faut d'abord cloner le débot sur votre ordinateur

~~~ shell
git clone git@github.com:sconle/decathlon.git
~~~

Il faut ensuite [créer un venv](https://docs.python.org/fr/3/library/venv.html). Puis enfin installer le requirements.txt:

~~~ shell
cd decathlon
pip install -r requirements.txt
~~~

Enfin il faut effectuer les migrations pour la BDD

~~~ shell
cd src
python manage.py makemigrations
python manage.py migrate
~~~

Il ne suffit plus que lancer le serveur:

~~~ shell
python manage.py runserver
~~~

Il sera ensuite disponible sur 127.0.0.1:8000.
