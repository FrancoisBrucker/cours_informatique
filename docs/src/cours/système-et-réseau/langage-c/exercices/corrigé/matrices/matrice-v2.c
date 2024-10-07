#include <stdio.h>
#include <stdlib.h>

int *matrice_create(size_t nombre_lignes, size_t nombre_colonnes) {
  int *matrice = (int *)malloc(nombre_lignes * nombre_colonnes * sizeof(int));
  for (size_t i = 0; i < nombre_lignes * nombre_colonnes; i++) {
    matrice[i] = 0;
  }
  return matrice;
}

int matrice_get(int *matrice, size_t ligne, size_t colonne, size_t nombre_colonnes) {
    return matrice[ligne * nombre_colonnes + colonne];
}

void matrice_set(int *matrice, int element, size_t ligne, size_t colonne, size_t nombre_colonnes) {
matrice[ligne * nombre_colonnes + colonne] = element;
}

void matrice_show(int *matrice, size_t nombre_lignes, size_t nombre_colonnes) {
  for (size_t i = 0; i < nombre_lignes; i++) {
    for (size_t j = 0; j < nombre_colonnes; j++) {
      printf("%3i ", matrice_get(matrice, i, j, nombre_colonnes));
    }
    printf("\n");
  }
}

void matrice_destroy(int *matrice) {
  free(matrice);
}

int main() {
  int *matrice = matrice_create(4, 6);
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 6; j++) {
      matrice_set(matrice, i+j, i, j, 6);
    }
  }

  matrice_show(matrice, 4, 6);

  matrice_destroy(matrice);
  matrice = NULL;
}
