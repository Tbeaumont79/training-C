/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_integer_table.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/05/30 14:30:21 by bod               #+#    #+#             */
/*   Updated: 2018/05/30 14:33:34 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
void ft_sort_integer_table(int *tab, int size)
{
	int tmp;
	int i;
	i = 0;
	
	while( i < size)
	{

		if (tab[i] < tab[i+1])
		{
			tab[i] = tmp;
			tab[i+1] = tab[i];
			tmp = tab[i+1];
			i = 0;	
		}
		else
		{
			i++;		
		}

	}

}
int main(void)
{
	int *tab;
	tab[0] = 23;
	tab[1] = 2;
	tab[2] = 29;
	tab[3] = 54;
	tab[4] = 4;
	ft_sort_integer_table(tab,5);
	printf("%d\n",*tab);
	return(0);
}
