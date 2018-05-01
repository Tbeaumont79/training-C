#include <unistd.h>
#include <stdio.h>

void ft_putchar(void)
{
	char a = 'a';
	write(1,&a,1);

}
int		main(void)
{
ft_putchar();
int *a;
int b;
b = 6;
a = &b;
printf("la valeur est %d ",*a);
}
