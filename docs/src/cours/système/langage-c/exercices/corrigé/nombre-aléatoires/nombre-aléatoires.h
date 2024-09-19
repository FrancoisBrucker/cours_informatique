#include <stdlib.h>

#ifndef FILE_NB_ALE
#define FILE_NB_ALE

int aleatoire_int(int min, int max);
int *aleatoire_tab(int max, size_t nombre);
void aleatoire_01_liste(double proba, size_t nombre, int *t);

#endif
