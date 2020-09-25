# Le fichier main est le point d'entrée de votre programme.
#
# Pour que ce programme fonctionne, vous avez besoin de code qui sera rangé **de façon sémantique** dans une
# multitude de fichiers, et pour que le code fonctionne vous avez besoin de tests.
#
# On sauvegarde **TOUJOURS** tous les tests comme ça lorsque l'on modifiera le code (ce qui arrive tout le temps) on
# aura pas besoin de tous les retaper.

import random

from figures_des import contient_une_paire,  contient_un_brelan, contient_un_carre, \
    contient_une_double_paire, contient_un_full


def cinq_de():
    des = []

    for i in range(5):
        des.append(random.randint(1, 6))

    return des

nombres_figures = {"paire": 0,
                   "double paire": 0,
                   "brelan": 0,
                   "full": 0,
                   "carré": 0,
                   "rien": 0,
                   }

NOMBRE_LANCER = 1000

for numero_lance in range(NOMBRE_LANCER):
    des = cinq_de()

    if contient_un_carre(des):
        nombres_figures["carré"] += 1
    elif contient_un_full(des):
        nombres_figures["full"] += 1
    elif contient_un_brelan(des):
        nombres_figures["brelan"] += 1
    elif contient_une_double_paire(des):
        nombres_figures["double paire"] += 1
    elif contient_une_paire(des):
        nombres_figures["paire"] += 1
    else:
        nombres_figures["rien"] += 1

print("nombres de figures sur", NOMBRE_LANCER, "lancers")


for nom, nombre in nombres_figures.items():
    print(nom, nombre, str("{:2.1f}%").format(nombre / NOMBRE_LANCER * 100))