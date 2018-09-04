#include <stdio.h>
#include <stdlib.h>

int		ft_atoi(char *str)
{
	int neg;
	int value;
	int i;
	
	i = 0;
	value = 0;
	neg = 0;
	if (neg == 0 && str[i] == '-')
	{
		printf("-");
		neg = 1;
	}
	while (str[i] == ' ' && str[i] == '\t' && str[i] == '\n' && str[i] == '\r'
	str[i] == '\t' && str[i] == '\v' && str[i] == '\f')
		i++;

	while (str[i] > '0' && str[i] < '9' && str[i] != '\0')
	{
		value *= 10;
		return(value);
	}
	return (0);
}
int		main(void)
{
	printf("%s",ft_atoi(bod23));
}
