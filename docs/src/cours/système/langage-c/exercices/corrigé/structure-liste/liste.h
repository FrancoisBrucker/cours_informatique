#ifndef FILE_LISTE
#define FILE_LISTE

#include <stdlib.h>

typedef struct _liste {
        int *t;
        size_t taille;
        size_t nombre;
} _liste;
typedef _liste* liste;

liste liste_creation();
void liste_ajoute(liste, int);
int liste_valeur(liste, size_t);
void liste_remplace(liste, size_t, int);
void liste_supprime_dernier(liste);
void supprimer_liste(liste);

#endif
