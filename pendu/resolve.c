/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resolve.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/05 19:59:40 by bod               #+#    #+#             */
/*   Updated: 2018/09/07 23:28:31 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"

void    ft_putchar(char c)
{
    write(1,&c,1);
}

void    ft_putstr(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
        ft_putchar(str[i++]);
}

int     ft_resolve(char c)
{
    char str[255] = "maison";
    int i;

    i = 0;
    while (str[i] != '\0')
    {
        if (check(str,c) > 0)
        {
            if (str[0] == c)
            {
                str[0] = c;
            }
            while (i < check(str,c))
            {
                str[i] = '*';
                i++;
            }
            if (i == check(str,c))
            {
                str[i] = c;
                ft_putstr("test\n");
                i++;
            }
            str[i] = '*';
        }
        i++;
    }
    if (check(str,c) != 0)
        ft_putstr(str);
    return (0);
}
