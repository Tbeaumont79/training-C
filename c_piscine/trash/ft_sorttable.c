#include<stdio.h>

void	ft_sort(int tabsize, int *tab)
{
	int temp;
	int i;

	temp = 0;
	i = 0;

	while(tabsize > i)
	{
		while(tab[i] > tab[i+1])
		{
			temp = tab[i];
			tab[i] = tab[i+1];
			tab[i+1] = temp;
			i = 0;
		}
	i++;
	}


}
int main()
{
	int tab[5] = {10,20,30,12,233};
	ft_sort(5,tab);
	printf("%d %d %d %d %d",tab[0],tab[1],tab[2],tab[3],tab[4]);
	return(0);
}
