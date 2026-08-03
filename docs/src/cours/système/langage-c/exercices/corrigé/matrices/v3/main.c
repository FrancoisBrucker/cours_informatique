#include "matrice.h"

#include <stdio.h>
#include <stdlib.h>

int main() {
  matrice_t m = matrice_create(4, 6);
  for (size_t i = 0; i < 4; i++) {
    for (size_t j = 0; j < 6; j++) {
      matrice_set(m, i + j, i, j);
    }
  }

  matrice_show(m);
  matrice_transpose(m);
  matrice_show(m);

  matrice_destroy(m);
  m = NULL;
}
