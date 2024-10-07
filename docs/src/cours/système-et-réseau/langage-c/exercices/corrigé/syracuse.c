

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int syracuse_nb(int nombre) {
  int nb = 0;

  while (nombre > 1) {
    if (nombre % 2) {
      nombre = 3 * nombre + 1;
    } else {
      nombre = nombre / 2;
    }
    nb++;
  }
  return nb;
}

int *syracuse_tab(int nombre) {
  int n = syracuse_nb(nombre);

  if (n == 0) {
    return NULL;
  }

  int *t = (int *)malloc((n + 1) * sizeof(int));
  t[0] = nombre;
  int i = 0;
  while (nombre > 1) {

    if (nombre % 2) {
      nombre = 3 * nombre + 1;
    } else {
      nombre = nombre / 2;
    }

    i++;
    t[i] = nombre;
  }

  return t;
}

int main(int argc, char *argv[]) {
  int montre_nombre = 0;
    char opt;

    while ((opt = getopt(argc, argv, "l")) != -1) {
      switch (opt) {
      case 'l':
        montre_nombre = 1;
        break;
      case '?':
      default:
        printf("Format : syracuse [-n] nb\n");
        return EXIT_FAILURE;
      }
    }

  if (optind != argc -1) {
    printf("Format : syracuse [-n] nb\n");
    return EXIT_FAILURE;
  }


  int u0 = atoi(argv[optind]);

  if (u0 <= 0) {
    printf("Format : syracuse [-n] nb\n");
    return EXIT_FAILURE;
  }

  int n = syracuse_nb(u0);
  int *t = syracuse_tab(u0);

    if (montre_nombre) {
        printf(" Syracuse %i : %i.\n", u0, n);
    }
        

    for (int i = 0; i <= n; i++) {
      printf("%i ", t[i]);
    }
    printf("\n");

  return EXIT_SUCCESS;
}
