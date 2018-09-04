#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int		ft_iterative_factorial(int nb)
{
	int i;

	i = nb;
	
	if (nb < 0)
	{
		return (0);
	}
	if (nb == 1 || nb == 0)
	{
		return (1);
	}

	while(i > 1)
	{
		i--;
		nb *= i;
	}
	return (nb);
}
int	main(void)
{
	clock_t debut;
	debut = clock ();
	printf("%d",ft_iterative_factorial(14));
	printf ("Temps consommé : %f\n", (double)(clock () - debut) / CLOCKS_PER_SEC);
	return (0);
}
