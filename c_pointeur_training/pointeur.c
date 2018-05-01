#include <unistd.h>


void ft_putchar(char c)
{

	write(1,&c,1);

}
int		main(void)
{

char a;
char *pointeur;
a = 'b';
pointeur = &a;
ft_putchar(*pointeur);
}

