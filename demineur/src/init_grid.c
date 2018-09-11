/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_grid.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/11 17:56:07 by bod               #+#    #+#             */
/*   Updated: 2018/09/11 22:10:21 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"

void    ft_putstr(char str[size][size])
{
    int i;
    int j;

    i = 0;
    while (i < size)
    {
        j = 0;
        while (str[i][j] != '\0' && size > j)
        {
            ft_putchar(str[i][j]);
            j++;
        }
        i++;
        ft_putchar('\n');
    }
    printf("la valeur de i est %d et la valeur de j est: %d\n",i,j);
}

void    display_grid()
{
    int i;
    int j;
    char grid[size][size]; 

    i = 0;
    while (size > i)
    {
        j = 0;
        while (size > j) 
        {
            j++;
            grid[i][j] = '.';
        }
        i++; 
    }
    ft_putstr(grid);
}
