#include <stdio.h>
int ft_is_prime(int nb)
{
	int i;
	i = 1;
	if(nb == 0 || nb ==1)
	{
		return(0);
	}

	while(nb / i == nb && i / 1 == nb)
	{
	
	printf("%d\n",i);
	if(nb / i == nb && i / 1 == nb)
		return(1);

	else
		return(0);

	i++;
}
	return(nb);
}
int main()
{
	printf("%d",ft_is_prime(2));
	return(0);
}
