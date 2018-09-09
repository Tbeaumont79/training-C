/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resolve.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/05 19:59:40 by bod               #+#    #+#             */
/*   Updated: 2018/09/09 17:53:05 by bod              ###   ########.fr       */
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
char     *ft_strcopy(char *src, char *dest)
{
    int i;
    int j;

    i = 0;
    j = 0;
    if (src[i] == '\0')
        return (0);
    while (src[i] != '\0')
    {
        dest[j] = src[i];
        i++;
        j++;
    }
    dest[j] = '\0';
    return (dest);
}
int     ft_resolve(char c)
{
    char str[255] = "maison";
    char *str2;
    int i;
    int j;

    j = 0;
    i = 0;
    if (check(str, c) == 1)
        return (0);
    while (str[i] != '\0')
    {
            while (i < check(str,c))
            {
                str[i] = '*';
                i++;
            }
            if (i == check(str,c))
            {
                str[i] = c;
                printf("\033[32m OK \033[0m");
                ft_strcopy(str,str2);
                i++;
            }
            if (str[i] == '\0')
                break;
            str[i] = '*';
        i++;
    }
    ft_putstr(str2);
    return (0);
}
