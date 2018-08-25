#include<unistd.h>

void	ft_putchar(char c)
{
	write(1,&c,1);
}

void ft_print_comb(void)
{
	int unite;
	int dizaine;
	int centaine;

	unite = 0;
	dizaine = 0;
	centaine = 0;

	while (unite < 10)
	{
		unite++;
		
		if(unite == 9)
		{
			dizaine++;
			unite = 0;
			if (dizaine == 9)
			{
				centaine++;
				dizaine = 0;
			}
		}

			ft_putchar(centaine + '0');
			ft_putchar(dizaine + '0');
			ft_putchar(unite + '0');

			ft_putchar(',');
			ft_putchar(' ');
		if (unite == 9 && dizaine == 9 && centaine == 9)
		{
			break;
		}
	}	




}
int		main(void)
{
	ft_print_comb();
}
