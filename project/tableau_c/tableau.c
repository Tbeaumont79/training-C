#include <unistd.h>

void ft_putchar(char c)
{
	write(1,&c,1);
}
int		main(void)
{
	char tab[5];
	
	tab[0] = 'h';
	tab[1] = 'e';
	tab[2] = 'l';
	tab[3] = 'l';
	tab[4] = 'o';
	
	int i;
	i = 0;
while (tab[i])
{

	ft_putchar(tab[i]);
	ft_putchar('\n');
	
	i++;

}
}
