#ifndef FILE_MATRICE
#define FILE_MATRICE

#include <stdlib.h>

typedef struct matrice* matrice_t;

matrice_t matrice_create(size_t nombre_lignes, size_t nombre_colonnes);
void matrice_destroy(matrice_t m);
void matrice_show(matrice_t m);
int matrice_get(matrice_t m, size_t ligne, size_t colonne);
void matrice_set(matrice_t m, int element, size_t ligne, size_t colonne);
void matrice_transpose(matrice_t m);

#endif
