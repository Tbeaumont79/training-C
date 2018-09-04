CC= gcc
CFLAGS= -Wall -Wextra -Werror
EXEC=hello

all: $(EXEC)

hello: hello.o main.o
	$(CC) -o hello hello.o main.o $(LDFLAGS)

hello.o: hello.c
	$(CC) -o hello.o -c hello.c $(CFLAGS)

clean:
	rm -rf *.o

mrproper: clean
	rm -rf $(EXEC)
