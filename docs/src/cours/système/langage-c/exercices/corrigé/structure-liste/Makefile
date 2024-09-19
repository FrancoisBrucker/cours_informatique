CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x
TARGET = liste

all: main

main: main.o liste.o
	$(CC) $(CFLAGS) main.o liste.o -o $(TARGET)

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

liste.o: liste.c
	$(CC) $(CFLAGS) -c liste.c

clean:
	rm *.o $(TARGET)