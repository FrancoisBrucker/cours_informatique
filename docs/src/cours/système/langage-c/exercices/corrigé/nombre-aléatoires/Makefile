CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x
TARGET = nombre-aléatoires

all: main

main: main.o nombre-aléatoires.o
	$(CC) $(CFLAGS) main.o nombre-aléatoires.o -o $(TARGET)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

celcius.o: celcius.c
	$(CC) $(CFLAGS) -c nombre-aléatoires.c

clean:
	rm *.o $(TARGET)