/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/05 20:22:43 by bod               #+#    #+#             */
/*   Updated: 2018/09/10 21:13:09 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"
int     main(void)
{
    int c;

    printf("enter a value : \n");
    c = getchar();
    printf("\033[33m --Checking--\033[0m\n");
    ft_resolve(c);
    return (0);
}
