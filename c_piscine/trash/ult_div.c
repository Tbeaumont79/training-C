#include<stdio.h>
void	ft_div(int *a, int *b)
{
	int tmp;

	tmp = 0;

	tmp = *a / *b;
	*b = *a % *b;
	*a = tmp;

}
int		main(void)
{
	int x = 5;
	int y = 7;
	
	ft_div(&x,&y);
	printf("%d %d",x,y);
}
