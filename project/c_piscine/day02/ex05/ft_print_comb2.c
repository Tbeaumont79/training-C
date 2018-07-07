#include <unistd.h>



void ft_putchar(char c)
{
	write(1,&c,1);

	
}
void ft_print_comb2(void)
{
	int a;
	int b;
	int c;
	int d;

	a = 0;
	b = 0;
	c = 0;
	d = 0;
	while(a < 10)
	{
		if (a == 9)
		{
	
			a = 0;
			b++;

			if(b == 10)
			{
				b = 0;
				d++;
				if (d == 10)
				{
					d = 0;
					c++;
				}

			}	
		}		
				

						

	
		a++;
		
		
		if (a < 10 && b < 10  && c < 10 && d < 10 && a > d)
		{
		ft_putchar(c + '0');
		ft_putchar(d + '0');
		ft_putchar(' ');
		ft_putchar(b + '0');
		ft_putchar(a + '0');
		
		ft_putchar(',');

		}
		if(c == 9 && d == 7 && b == 9 && a == 9)
		{
			d++;
			if (c == 9 && d == 8 && b == 9 && a == 9)
			{
				ft_putchar(c + '0');
				ft_putchar(d + '0');
				ft_putchar(' ');
				ft_putchar(b + '0');
				ft_putchar(a + '0');
			}
			break;
			}
		}
	}	
	
	
		 

	
int main(void)
{

	ft_print_comb2();
	return(0);
}
