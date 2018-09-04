#include<stdio.h>

void	ft_sort_integer_table(int *tab, int size)
{
	int i;
	int temp;

	i = 0;
	temp = 0;

	while(i < size)
	{
		while(tab[i+1] < tab[i])
		{
			temp = tab[i];
			tab[i] = tab[i+1];
			tab[i+1] = temp;
			i = 0;
		}
		i++;
	}
}
int main(void)
{
	int stack[5] = {5,2,12,24,1};
	ft_sort_integer_table(stack,5);
	printf("%d %d %d %d %d",stack[0],stack[1],stack[2],stack[3],stack[4]);

}
