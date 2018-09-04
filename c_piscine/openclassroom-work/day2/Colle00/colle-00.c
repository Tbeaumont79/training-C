#include "ft_putchar.h"
#include "colle-00.h"
void colle(int x, int y)
{

	topandbottom(x,y);
	leftandright(x,y);
	
	if(y > 1)
	{
		topandbottom(x,y);
	}

}
int topandbottom(int x,int y)
{

	int i;

	i = 0;

	
	if(x <= 0 && y <= 0)
	{
		return (0);
	}

	else
	{
		if(x > 1)
			ft_putchar('o');

		while(i < x-2)
		{
			ft_putchar('-');
			i++;
		}

		if(x <= 0)
			return(0);
		
		else	
			ft_putchar('o');
	}

	return (0);
}
int leftandright(int x, int y)
{
	ft_putchar('\n');
	int i;
	int count;
	
	i = 0;
	if(x > 1)
	{
		while(i < y-2)
		{
			count = 0;
			ft_putchar('|');
			while(count < x-2)
			{
				ft_putchar(' ');
				count++;
			}
			ft_putchar('|');
			ft_putchar('\n');
			i++;
		}
	}
	else if(x == 1)
	{
		while(i < y-2)
		{
			ft_putchar('|');
			ft_putchar('\n');
			i++;
		}
	}
	return (0);
}

