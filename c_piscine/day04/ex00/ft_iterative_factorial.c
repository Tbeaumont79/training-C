#include <stdio.h>

int ft_iterative_factorial(int nb)
{
	int result;
	
	result = nb;

	while((nb - 1) > 0)
	{
		result = result * (nb-1);
		nb--;
	}
	return(result);
}

int main(void)
{
	printf("%d",ft_iterative_factorial(5));
	return(0);
}
