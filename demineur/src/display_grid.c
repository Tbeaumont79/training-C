/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   display_grid.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/19 16:41:30 by bod               #+#    #+#             */
/*   Updated: 2018/09/19 22:22:46 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"

void    display_grid(char str[size][size], int boolean, char num)
{
    int i;
    int j;

    i = 0;
    while (i < size)
    {
        j = 0;
        while (str[i][j] != '\0' && size > j)
        {
            if (str[i][j] == '#' && boolean == 0)
            {
                ft_putchar('.');
            }
            else
                ft_putchar(str[i][j]);
            j++;
        }
        i++;
        ft_putchar('\n');
    }
    printf("la valeur de i est %d et la valeur de j est: %d\n",i,j);
}
