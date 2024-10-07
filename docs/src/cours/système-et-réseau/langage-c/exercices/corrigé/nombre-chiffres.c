#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nb_chiffre_v1(int i) {
  int nb = 1;

  if (i < 0) {
    i = -i;

    nb++;
  }
  while (i > 10) {
    i /= 10;

    nb++;
  }

  return nb;
}

int nb_chiffre_v2(int i) {
  int nb = 0;

  if (i < 0) {
    i = -i;

    nb++;
  }
  if (i < 10) {
    return nb + 1;
  } else {
    return nb + ceil(log10(i));
  }
}

int nb_chiffre_v3(int i) {
  // char *s = (char *)malloc(100 * sizeof(char));
  char s[100];

  sprintf(s, "%i", i);

  return strlen(s);
}

int VALEURS[4] = {123456, 0, -1, 0};
size_t LENGTH = 4;

int main() {
  int nb = 0;

printf(" Tapez un entier : ");
  scanf("%i", VALEURS + 3);  

  printf("V1.\n");
  
  for (size_t i = 0; i < LENGTH; i++) {
    nb = nb_chiffre_v1(VALEURS[i]);
    printf("L'entier %i a %i chiffres.\n", VALEURS[i], nb);
  }

  printf("V2.\n");
  for (size_t i = 0; i < LENGTH; i++) {
    nb = nb_chiffre_v2(VALEURS[i]);
    printf("L'entier %i a %i chiffres.\n", VALEURS[i], nb);
  }

  printf("V3.\n");
  for (size_t i = 0; i < LENGTH; i++) {
    nb = nb_chiffre_v3(VALEURS[i]);
    printf("L'entier %i a %i chiffres.\n", VALEURS[i], nb);
  }
  return EXIT_SUCCESS;
}
