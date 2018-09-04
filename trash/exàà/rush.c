/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/04 22:26:10 by bod               #+#    #+#             */
/*   Updated: 2018/08/04 23:43:39 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar();

int		top_and_botton(int x, int y)
{
	if (x == 1 && y == 1)
	{
		ft_putchar('o');
		ft_putchar('\n');
	}
	ft_putchar('o');
	while (x > 2)
	{
		ft_putchar('-');
		x--;
	}
	ft_putchar('o');
	return (0);
}
int		left_and_right(int x, int y)
{
	while (y >= 2)
	{ 
		if (y >= 2 && x >= 2)
		{
			ft_putchar(' ');
		}
		ft_putchar('|');
		ft_putchar('\n');
		y--;
	}


	ft_putchar('\n');
	return(0);
}

int		rush(int x, int y)
{

	left_and_right(x,y);
	top_and_botton(x,y);
	top_and_botton(x,y);
	left_and_right(x,y);
	return (0);
}
