#include<stdio.h>

void	decoupeMinute(int *hours,int *minutes);
int main(void)
{
	int hours = 0;
	int minutes = 90;
	decoupeMinute(&hours,&minutes);
	printf("il est %dH %dmin",hours,minutes);
	return(0);
}
void	decoupeMinute(int *hours,int *minutes)
{
	*hours = *minutes / 60;
	*minutes = *minutes % 60;
}
