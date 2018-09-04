#include<stdio.h>

void sorttable(int tab[],int sizeoftab)
{
	int i;
	int temp;
	
	temp = 0;
	i = 0;

	while(i < sizeoftab)
	{
		if(tab[i+1] > tab[i])
		{
	
			temp = tab[i];
			tab[i] = tab[i+1];
			tab[i+1] = temp;
			i = 0;
		}
		i++;
		printf("%d\n",tab[i]);
	}


}




int main(void)
{
	int tab[5] = {19,3,2,10,5};
	sorttable(tab,5);

}
