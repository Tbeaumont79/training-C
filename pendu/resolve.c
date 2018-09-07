/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resolve.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/05 19:59:40 by bod               #+#    #+#             */
/*   Updated: 2018/09/07 22:18:43 by bod              ###   ########.fr       */
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
       while (str[i] != '\0')
       {
            ft_putchar('*');
            if (check(str,c))
                str[i] = c;
            i++;
        }
       ft_putstr(str);
    return (0);
}
