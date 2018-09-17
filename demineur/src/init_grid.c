/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_grid.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/11 17:56:07 by bod               #+#    #+#             */
/*   Updated: 2018/09/17 13:10:45 by bod              ###   ########.fr       */
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
void    display_grid(int x, int y)
{
    int i;
    int j;
    int count;
    char motif;
    char grid[size][size]; 
    int  nbgen;
    int  nbgen1;

    i = 0;
    count = 0;
    srand(time(NULL));
    nbgen = 0;
    nbgen1 = 0;
    while (size > i)
    {
        j = 0;
        while (size > j) 
        {
            while (count < 15)//faire un mode hiding pour cacher les bombes.(dépendance de checking)
            {
                nbgen = rand()%size;
                nbgen1 = rand()%size;
                motif = '#';
                grid[nbgen][nbgen1] = motif;
                count++;
            }
            if (grid[i][j] != '#')
            {
                motif = '.';
                grid[i][j] = motif;
            }
            j++;
        }
        i++; 
    }
    ft_putstr(grid);
}
