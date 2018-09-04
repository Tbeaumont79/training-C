#include<unistd.h>
void ft_putchar(char c);
char ft_putstr(char *content)
{
	int i;
	i = 0;

	while(content[i] != '\0')
	{
	
		ft_putchar(content[i]);
		i++;
	
	}
	return (0);
}

void ft_putchar(char c)
{
	write(1,&c,1);
}


