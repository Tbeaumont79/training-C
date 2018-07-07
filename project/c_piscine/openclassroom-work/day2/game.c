#include<stdio.h>

void		Turnleft()
{
	printf("Le joueur tourne a gauche");
	static int turn = 1;
	printf("\n vous avez tourner %d fois ! \n",turn);
	turn++;
}
static void dontMove()
{
printf("le joueur ne bouge pas ! ");
}

