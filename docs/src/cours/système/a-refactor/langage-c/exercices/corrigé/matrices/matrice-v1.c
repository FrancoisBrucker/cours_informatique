#include <stdio.h>
#include <stdlib.h>

int **matrice_create(size_t nombre_lignes, size_t nombre_colonnes) {
    int **matrice = (int **)malloc(nombre_lignes * sizeof(int*));
    for (size_t i = 0 ; i < nombre_lignes ; i++) {
        matrice[i] = (int *)malloc(nombre_colonnes * sizeof(int));
        for (size_t j = 0 ; j < nombre_colonnes ; j++) {
            matrice[i][j] = 0;
        }
    }
    return matrice;
}

void matrice_show(int **matrice, size_t nombre_lignes, size_t nombre_colonnes) {
    for (size_t i = 0 ; i < nombre_lignes ; i++) {
        for (size_t j = 0 ; j < nombre_colonnes ; j++) {
            printf("%3i ", matrice[i][j]);
        }
        printf("\n");
    }

}

void matrice_destroy(int **matrice, size_t nombre_lignes) {
    for (size_t i = 0 ; i < nombre_lignes ; i++) {
        free(matrice[i]);
    }
    free(matrice);
}


int main() {
    int **matrice = matrice_create(4, 6);
    for (size_t i = 0 ; i < 4 ; i++) {
        for (size_t j = 0 ; j < 6 ; j++) {
            matrice[i][j] = i + j;
        }
    }

    matrice_show(matrice, 4, 6);

    matrice_destroy(matrice, 4);
    matrice = NULL;
}
