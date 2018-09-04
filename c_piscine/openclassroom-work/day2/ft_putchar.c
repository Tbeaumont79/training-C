#include <unistd.h>
static char	ft_putchar(char c)
{
	write(1,&c,1);
	return(0);
}

void ft_putstr(char *str)
{
	int i;
	while(str[i])
	{
		ft_putchar(str[i]);
		i++;
	}	
}

