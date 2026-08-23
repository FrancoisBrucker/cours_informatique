#include "nombre-aléatoires.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int NB_TIRAGE = 100;

int main() {
  // srand(0);
  srand(time(NULL)); // pour avoir une initialisation différente à chaque fois

  int valeur = 0;
  double moyenne = 0;

  for (size_t i = 0; i < NB_TIRAGE; i++) {
    valeur = aleatoire_int(-50, +50);
    // printf("Valeur %i.\n", valeur);

    moyenne += valeur;
  }
  moyenne /= NB_TIRAGE;

  printf("La moyenne de %i tirage entre -50 et +50 vaut %f.\n", NB_TIRAGE,
         moyenne);

  int n[10] = {0};
  int *t = aleatoire_tab(10, NB_TIRAGE);

  for (size_t i = 0; i < NB_TIRAGE; i++) {
    n[t[i]] += 1;
  }
  for (int i = 0; i < 10; i++) {
    printf("Nombre de %i est %i\n", i, n[i]);

    moyenne += valeur;
  }

  int proba[NB_TIRAGE] = {0};
  int k = 0;

  aleatoire_01_liste(.5, NB_TIRAGE, proba);

  for (int i = 0; i < NB_TIRAGE; i++) {
    printf("%i ", proba[i]);

    if (proba[i]) {
      k++;
    }
  }
  printf("\n %i.\n", k);

  return EXIT_SUCCESS;
}
