#include <stdio.h>
int sommeTableau(int tableau[], int tailleTableau)
{
	int i;
	int somme;
	somme = 0;
	i = 0;
	while(i < tailleTableau)
	{
		somme += tableau[i];
		i++;
	}
	return(somme);
}
int main(void)
{
	int tab[5] = {0,5,10,20,30};
	printf("%d",sommeTableau(tab,5));
	return(0);
}
