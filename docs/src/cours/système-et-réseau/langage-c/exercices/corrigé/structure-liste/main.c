#include "liste.h"
#include <stdio.h>
#include <stdlib.h>

const int NB_TIRAGE = 100;

int main() {
  liste l = liste_creation();
  for (int i = 0 ; i < NB_TIRAGE ; i++) {
    liste_ajoute(l, i);
  }

  for (size_t i = 0 ; i < l->nombre ; i++) {
    printf("%i ", liste_valeur(l, i));
  }
  printf("/n");

  printf("taille et nombre de la liste %li %li \n", l->taille, l->nombre);

  while (l->nombre) {
    liste_supprime_dernier(l);
  }
  printf("taille et nombre de la liste %li %li \n", l->taille, l->nombre);
  return EXIT_SUCCESS;
}
