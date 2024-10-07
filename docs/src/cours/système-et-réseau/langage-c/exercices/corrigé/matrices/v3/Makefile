CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x
TARGET = matrice

all: main

main: main.o matrice.o
	$(CC) $(CFLAGS) main.o matrice.o -o $(TARGET)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

matrice.o: matrice.c
	$(CC) $(CFLAGS) -c matrice.c

clean:
	rm *.o $(TARGET)