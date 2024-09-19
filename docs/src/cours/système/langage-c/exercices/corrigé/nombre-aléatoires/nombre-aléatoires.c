#include "nombre-aléatoires.h"

int aleatoire_int(int min, int max) { return min + rand() % (max - min); }

int *aleatoire_tab(int max, size_t nombre) {
  int *t = (int *)malloc(nombre * sizeof(int));

  for (size_t i = 0; i < nombre; i++) {
    t[i] = rand() % max;
  }
  return t;
}

double aleatoire_01() { return (double)rand() / RAND_MAX; }

void aleatoire_01_liste(double proba, size_t nombre, int *t) {
  for (size_t i = 0; i < nombre; i++) {
    t[i] = aleatoire_01() <= proba ? 1 : 0;
  }
}
