#include <stdio.h>
int ft_sqrt(int nb)
{
	float i;
	int value1;

	value1 = 0;
	
	if(nb < 0)
		return(0);
	
	while(value1 * value1 != nb)
	{
	
		value1++;
		
		if(value1 * value1 == i || value1 * value1 > nb)
		{
			return(0);
		}
	}
	
	return(value1);


}
int main(void)
{
	printf("%d",ft_sqrt(1024));
	return(0);
}
