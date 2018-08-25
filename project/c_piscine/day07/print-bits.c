/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print-bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/06 22:09:34 by bod               #+#    #+#             */
/*   Updated: 2018/08/08 21:16:22 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
void	ft_putchar(char c)
{
	write(1,&c,1);
}
void	print_bits(unsigned char octect)
{
	int bit = 128;
	int i = 0;
	int oct = octect;
	while (bit != 0)
	{
		if (bit <= oct)
		{
			ft_putchar('1');
		}
		else
		{
			ft_putchar('0');
		}
		bit = bit / 2;
	}
	}

int main(void)
{
	print_bits(145);
	return (0);
}
