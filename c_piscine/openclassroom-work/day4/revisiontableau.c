#include<stdio.h>

void sorttable(int tab[], int tailletableau);

int main(void)
{
	int tab[5] = {12,10,111,3,1};
	sorttable(tab, 5);
}

void sorttable(int tab[],int tailletableau)
{
	int i;
	int temp;
	
	temp = 0;
	i = 0;

	while(i < tailletableau)
	{
		if(tab[i+1] > tab[i])
		{
			temp = tab[i];
			tab[i+1] = tab[i];
			tab[i+1] = temp;
			i = 0;
		}

		i++;
		printf("%d\n", tab[i]);
	}

}
