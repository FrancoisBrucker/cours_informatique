#include "matrice.h"
#include <stdio.h>
#include <stdlib.h>

struct matrice {
  int *matrice;
  size_t lignes;
  size_t colonnes;
};

matrice_t matrice_create(size_t nombre_lignes, size_t nombre_colonnes) {

  matrice_t m = (matrice_t)malloc(sizeof(struct matrice));
  m->lignes = nombre_lignes;
  m->colonnes = nombre_colonnes;
  m->matrice = (int *)malloc(nombre_lignes * nombre_colonnes * sizeof(int));
  for (size_t i = 0; i < nombre_lignes * nombre_colonnes; i++) {
    m->matrice[i] = 0;
  }
  return m;
}

int matrice_get(matrice_t m, size_t ligne, size_t colonne) {
  return m->matrice[ligne * m->colonnes + colonne];
}

void matrice_set(matrice_t m, int element, size_t ligne, size_t colonne) {
  m->matrice[ligne * m->colonnes + colonne] = element;
}

void matrice_show(matrice_t m) {
  for (size_t i = 0; i < m->lignes; i++) {
    for (size_t j = 0; j < m->colonnes; j++) {
      printf("%3i ", matrice_get(m, i, j));
    }
    printf("\n");
  }
}

void matrice_destroy(matrice_t m) {
  free(m->matrice);
  free(m);
}

void matrice_transpose(matrice_t m) {
  matrice_t m2 = matrice_create(m->colonnes, m->lignes);

  for (size_t i = 0; i < m->lignes; i++) {
    for (size_t j = 0; j < m->colonnes; j++) {
      matrice_set(m2, matrice_get(m, i, j), j, i);
    }
  }
  m->colonnes = m2->colonnes;
  m->lignes = m2->lignes;
  m->matrice = m2->matrice;

  free(m2);
}
