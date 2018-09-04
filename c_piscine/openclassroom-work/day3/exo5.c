#include <stdio.h>
void ordonnerTableau(int tableau[], int tailleTableau)
{
	int temp;
	int i;
	i = 0;

	while( i < tailleTableau)
	{
	if(tableau[i] > tableau[i+1])
	{
		temp = tableau[i];
		tableau[i] = tableau[i+1];
		tableau[i+1] = temp;
		i = 0;
	}
	i++;
	}
}
int main(void)
{
	int tab[5] = {1,20,30,5,3};
	ordonnerTableau(tab,5);
	printf("%d\n",tab[0]);
	printf("%d\n",tab[1]);
	printf("%d\n",tab[2]);
	printf("%d\n",tab[3]);
	printf("%d\n",tab[4]);

}
