#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

typedef struct element *element_t;
struct element {
  void *data;
  element_t next;
  element_t pred;
};

element_t element_create(void *data) {
  element_t e = malloc(sizeof(struct element));
  e->data = data;
  e->next = NULL;
  e->pred = NULL;

  return e;
}

void *element_destroy(element_t e) {
  void *data = e->data;
  free(e);

  return data;
}

void element_ajoute_suivant(element_t e, element_t suivant) {
  e->next = suivant;
  suivant->pred = e;
}

void element_ajoute_precedent(element_t e, element_t precedent) {
  e->pred = precedent;
  precedent->next = e;
}

void liste_parcours(element_t liste, void (*f)(void *)) {
  element_t current = liste->next;

  while (current != NULL) {
    f(current->data);
    current = current->next;
  }
}

typedef struct _personne {
  unsigned int id;
  char *nom;
} personne;

void personne_show(void *d) {
  personne *p = (personne *)d;

  printf("%i : %s.\n", p->id, p->nom);
}

int main() {

  personne data[10] = {{0, "zéro"},   {1, "un"},   {2, "deux"}, {3, "trois"},
                       {4, "quatre"}, {5, "cinq"}, {6, "six"},  {7, "sept"},
                       {8, "huit"},   {9, "neuf"}};

  element_t liste = element_create(NULL);

  element_t current = liste;
  for (size_t i = 0; i < 10; i++) {
    element_ajoute_suivant(current, element_create(&data[i]));
    current = current->next;
  }

  liste_parcours(liste, personne_show);
  
  printf("\n\n");

  srand(time(NULL));
  // srand(0);
  
  unsigned int pos = rand() % 10;

  // extraction de l'élément identifié par pos
  current = liste->next;
  while (((personne *)current->data)->id != pos) {
    current = current->next;
  }
  current->pred->next = current->next;
  current->next->pred = current->pred;

  // place l'élément identifié par pos en début de liste
  liste->next->pred = current;
  current->next = liste->next;
  liste->next = current;

  liste_parcours(liste, personne_show);

  return EXIT_SUCCESS;
}
