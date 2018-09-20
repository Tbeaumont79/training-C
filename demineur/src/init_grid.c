/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_grid.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/11 17:56:07 by bod               #+#    #+#             */
/*   Updated: 2018/09/20 21:40:49 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"

char    init_grid(char grid[size][size])
{
    int i;
    int j;
    int count;
    char motif;
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
            if (grid[i][j + 1] == '#')
            {
                motif = '1';
                grid[i][j] = motif;
            }
            j++;
        }
        i++; 
    }
    return (**grid);
}
