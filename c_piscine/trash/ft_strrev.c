#include <unistd.h>
#include<stdio.h>
void	ft_putchar(char c)
{
	write(1,&c,1);
}



char	*ft_strrev(char *str)
{
	int i;
	int j;
	int temp;

	i = 0;
	j = 0;
	temp = 0;

	while(str[i] != '\0')
	{
		i++;
	}
	i -= 1;
	while (i > j)
	{
		temp = str[i];
		str[i] = str[j];
		str[j] = temp;
		i--;
		j++;

	}
	return(str);
}
int main(void)
{
	char test[255] = "bonjour";
	printf("%s",ft_strrev(test));
	return (0);
}
