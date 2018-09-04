#include<stdio.h>

void maximumTableau(int tableau[], int tailleTableau, int valeurMax)
{
	 int i;
	 i = 0;

	while(i < *tableau)
	{
		if(tableau[i] > valeurMax)
			tableau[i] = 0;
		printf("%d\n", tableau[i]);
		i++;
	}
	

}

int main(void)
{
	int tab[5] = {5,10,25,12,3};
	maximumTableau(tab, 5,20);
	return(0);
}
