#include "liste.h"

liste liste_creation() {
  liste l = (liste)malloc(sizeof(_liste));

  l->taille = 1;
  l->nombre = 0;
  l->t = (int *)malloc(l->taille * sizeof(int));

  return l;
}

void liste_ajoute(liste l, int x) {

  if (l->taille == l->nombre) {
    void *p = realloc(l->t, 2 * l->taille * sizeof(int));

    if (p) {
      l->taille *= 2;
      l->t = p;
    } else {
      return;
    }
  }

  l->t[l->nombre] = x;
  l->nombre++;

}

int liste_valeur(liste l, size_t i) { return l->t[i]; }

void liste_remplace(liste l, size_t i, int x) { l->t[i] = x; }
void liste_supprime_dernier(liste l) {
  l->nombre--;

  if (l->nombre <= l->taille / 2 && l->taille > 1) {
    void *p = realloc(l->t, l->taille / 2 * sizeof(int));

    if (p) {
      l->taille /= 2;
      l->t = p;
    } else {
      return;
    }
  }
}

void liste_supprime(liste l) {
        free(l->t);  // ne pas oublier, sinon fuite de mémoire.
        free(l);
}
