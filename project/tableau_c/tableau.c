#include <unistd.h>

void ft_putchar(char c)
{
	write(1,&c,1);
}
int		main(void)
{
	char tab[16];
	
	tab[0] = 'j';
	tab[1] = 'e';
	tab[2] = ' ';
	tab[3] = 'm';
	tab[4] = 'e';
	tab[5] = ' ';
	tab[6] = 'f';
	tab[7] = 'a';
	tab[8] = 'i';
	tab[9] = 's';
	tab[10]	= ' ';
	tab[11] = 'c';
	tab[12] = 'h';
	tab[13] = 'i';
	tab[14] = 'e';
	tab[15] = 'r';
	int i;
	i = 0;
while (tab[i])
{

	ft_putchar(tab[i] - 48);
	ft_putchar('\n');
	i++;

}
}
