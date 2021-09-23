import random 

from arbre_binaire import (
    enfant_gauche,
    enfant_droit,
    valeur,
    change_enfant_gauche,
    change_enfant_droit,
    change_valeur,
    hauteur,
)


def recherche(val, racine):
    if racine is None:
        return False
    elif valeur(racine) == val:
        return True
    elif valeur(racine) > val:
        return recherche(val, enfant_gauche(racine))
    else:
        return recherche(val, enfant_droit(racine))


def creation(valeur):
    return [valeur, None, None]


def insertion(val, racine):
    if racine is None or valeur(racine) == val:
        return
    elif valeur(racine) > val:
        if enfant_gauche(racine) is None:
            change_enfant_gauche(racine, creation(val))
        else:
            insertion(val, enfant_gauche(racine))
    else:
        if enfant_droit(racine) is None:
            change_enfant_droit(racine, creation(val))
        else:
            insertion(val, enfant_droit(racine))


liste = list(range(1000))

liste.sort()

abr = creation(liste[len(liste) // 2])

def abr_insere_min(debut, fin):
    if fin > debut + 1:
        x = liste[(debut + fin) // 2]
        insertion(x, abr)
        abr_insere_min(debut, x)
        abr_insere_min(x, fin)

abr_insere_min(0, len(liste) // 2)
abr_insere_min(len(liste) // 2, len(liste))

print("hauteur max : ", len(liste))
print("hauteur min : ", hauteur(abr))

random.shuffle(liste)

abr = creation(liste[0])

for x in liste[1:]:
    insertion(x, abr)

print("hauteur shuffle : ", hauteur(abr))
