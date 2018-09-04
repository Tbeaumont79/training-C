#include <stdio.h>
int	bublesort(int tableau[], int tailletableau);

int		main(void)
{
	int tab[6] = {3,11,25,43,1,43};
	printf("%d",bublesort(tab, 6));

}

int	bublesort(int tableau[], int tailletableau)
{
	int i;
	int temp;
	
	temp = 0;
	i = 0;

	while(i < tailletableau)
	{
		if(tableau[i+1] > tableau[i])
		{
			temp = tableau[i];
			tableau[i+1] = tableau[i];
			temp = tableau[i+1];
			i = 0;
		}
		i++;
	}
	return (0);

}

