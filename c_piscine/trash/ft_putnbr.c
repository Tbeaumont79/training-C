/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/07/29 12:08:35 by bod               #+#    #+#             */
/*   Updated: 2018/07/29 15:11:23 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<unistd.h>

void	ft_putchar(char c)
{
	write(1,&c,1);
}
void	ft_putnbr(int nb)
{

	if(nb < 0)
	{
		nb *= -1;
		ft_putchar('-');
		ft_putchar(nb + '0');
	}

	if (nb > 9)
	{
	while (1)
	{
		nb = nb / 10;
		nb = nb % 10;
		ft_putchar(nb + '0');
	}
	}
}

int	main(void)
{

	ft_putnbr(42);
	return (0);
	
}


