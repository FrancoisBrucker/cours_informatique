CC=clang
CFLAGS=-Wall -Wextra -pedantic -std=c2x

OBJECTS=main.o celcius.o 
NAME=celcius

all: $(NAME)

$(NAME): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c %.h
	$(CC) $(CFLAGS) -c $^

clean:
	rm *.o $(NAME)
