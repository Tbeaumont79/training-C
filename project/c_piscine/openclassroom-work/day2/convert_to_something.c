#include<stdio.h>
int		price(int* Price, int* Taxe)
{
	
	int price_eur = *Price * *Taxe;
	int price_fr = *Price * 7;
	printf("la valeur taxe en eur est %d et en franc : %d",price_eur,price_fr);
	return(0);
}
