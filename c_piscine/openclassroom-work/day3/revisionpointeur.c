#include <stdio.h>
#include <stdlib.h>

void decoupeMinutes(int *hours, int *minute);

int main(void)
{
	int hours = 0;
	int minute = 90;

	decoupeMinutes(&hours,&minute);
	
	printf("%d heures et %d minute", hours,minute);
	
	return(0);
}

void decoupeMinutes(int *hours, int *minute)
{
	*hours = *minute / 60;
	*minute = *minute % 60;
}
