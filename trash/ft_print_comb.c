/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/07/31 21:41:16 by bod               #+#    #+#             */
/*   Updated: 2018/07/31 22:34:43 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1,&c,1);
}

void	ft_print_comb(void)
{
	int c;
	int d;
	int u;

	c = 0;
	d = 0;
	u = 0;

	while(c < 10)
	{
		if(u == 9)
		{
			u = 0;
			d++;
			if(d == 9)
			{
				c++;
				d = 0;
			}
		}
		u++;
		if(c == '7' && d == '8' && u == '9')
		{
			break;
		}
		if(u > d && d > c)
		{
		ft_putchar(c + '0');
		ft_putchar(d + '0');
		ft_putchar(u + '0');
		ft_putchar(',');
		ft_putchar(' ');	
		}

	}
	
}

int main(void)
{
	ft_print_comb();
	return (0);
}
