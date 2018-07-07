#include <stdio.h>
int ft_iterative_power(int nb,int power)
{
	int result;
	result = nb;

	while (power > 1)
	{

		result = result * nb;
		power--;
		/* printf pour debug :) 
		printf("%d\n", result);
		*/
	}
	return(result);
}
int main(void)
{
	printf("%d",ft_iterative_power(2,4));
	return(0);
	
}
