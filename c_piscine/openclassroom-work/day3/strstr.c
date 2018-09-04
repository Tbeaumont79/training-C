#include<stdio.h>

void copie(int tableauOriginal[], int tableauCopie[], int tailleTableau)
{
	int i;

	i = 0;

	while(tableauCopie[i] < (tableauOriginal[i]) )
	{

		tableauCopie[i] = tableauOriginal[i];
		printf("%d\n",tableauCopie[i]);
		i++;
	}
}
int main(void)
{
	int tab[5] = {5,10,20,5,10};
	int tab_cop[5] = {};
	copie(tab,tab_cop,5);
	return(0);
}
