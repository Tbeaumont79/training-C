#include <stdio.h>

void timeconvert(int *hours, int *minutes);

int main()
{
	int hours = 0;
	int minutes = 90;

	timeconvert(&hours,&minutes);
	printf("il est %d H %d",hours,minutes);

	return(0);
}
void timeconvert(int *hours,int *minutes)
{
	*hours = *minutes / 60;
	*minutes = *minutes % 60;

}
