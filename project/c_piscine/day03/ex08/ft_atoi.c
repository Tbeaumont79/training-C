#include <stdio.h>
#include<stdlib.h>
int ft_atoi(char *str)
{
	int i;
	int value;
	int neg;
	neg = 0;
	i = 0;
	value = 0;

	while(str[i] == ' ' || str[i] == str['\n'] || str[i] == str['\t'] ||
			str[i] == str['\r']|| str[i] == str['\f'] || str[i]  == str['\v'])
	{
		i++;
	}
	if(str[i] == '-' && str[i] != 0)
	{
		neg = 1;
	}	
	if (str[i] == '+' || str[i] == '-')
	{
	i++;
	}
	while(str[i] >= '0' && str[i] <= '9' && str[i] != '\0')
	{
		value *=10;
		value += str[i] - 48;
		i++;
	}
	
	return(neg? -value : value);
}




int		main(void)
{
	char str[255] = "+23";
	printf("%d\n",ft_atoi(str));
	printf("%d",atoi(str));
	return(0);
}
