#include <stdio.h>
#include <stdlib.h>

int ft_atoi(char *str)
{
	int i;
	int neg;
	int value;

	value = 0;
	i = 0;
	neg = 0;

	while(str[i] == ' ' || str[i] == '\n' || str[i] == '\t' || str[i] == '\v'
	|| str[i] == '\f' || str[i] == '\r' || str[i] == '\b')
	{
		i++;
	}

	if(str[i] == '-')
	{
		neg = 1;
	}

	if(str[i] == '+' || str[i] == '-')
	{
		i++;
	}

	while(str[i] >= '0' && str[i] <= '9' && str[i] != '\0')
	{
		value *= 10;
		value += (int)str[i] - 48;
		i++;
	}

	if(neg == 1)
	{
		return(value *= -1);
	}

	else
	{
		return(value);
	}

}
int main(void)
{
	char var[255] = "-	-42bonjour";
	printf("%d\n",ft_atoi(var));
	printf("%d",atoi(var));

	return(0);
}
