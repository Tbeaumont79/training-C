/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/07/29 12:05:45 by bod               #+#    #+#             */
/*   Updated: 2018/07/29 12:08:11 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <unistd.h>

void	ft_putchar(char c)
{
	write(1,&c,1);
}

void ft_print_numbers(void)
{
	int i;

	i = 0;

	while(i < 10)
	{
		ft_putchar(i + '0');
		i++;
	}
}
int	main(void)
{

	ft_print_numbers();
	return (0);
}
