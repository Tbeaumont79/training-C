#include<stdio.h>
double moyenneTableau(int tableau[], int tailleTableau)
{
	int i;
	double somme;

	i = 0;
	somme = 0;

	while(i < tailleTableau)
	{
		somme += tableau[i];
		i++;
	}
	return(somme/tailleTableau);
}
int main(void)
{
	int tab[5] = {10,15,20,5,10};
	printf("%f",moyenneTableau(tab,5));
	
	return(0);
}
