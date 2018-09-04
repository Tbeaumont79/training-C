#include <unistd.h>



void ft_putchar(char c)
{
	write(1,&c,1);

	
}
void ft_print_comb(void)
{
	int x;
	int y;
	int z;

	x = 0;
	y = 0;
	z = 0;

	while(x < 10)
	{
		if (x == 9)
		{
	
			x = 0;
			y++;

			if(y == 9)
			{
				y = 0;
				z++;	
	
			}	

		}			

						

		
		x++;

		if (x > y && y > z )
		{
			ft_putchar(z + '0');
			ft_putchar(y + '0');
			ft_putchar(x + '0');
		
		if(x == 9 && y == 8 && z == 7)
		{
			break;
		
		}
		
			ft_putchar(',');
			ft_putchar(' ');
		}
	
	}
		 

	}
int main(void)
{

	ft_print_comb();
	return(0);
}
