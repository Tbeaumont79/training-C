/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/11 17:33:46 by bod               #+#    #+#             */
/*   Updated: 2018/09/16 21:28:37 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft.h"

int     main(void)
{
    int x;
    int y;

    printf("entrez une valeur pour y");
    while ((x = getchar() != EOF))
    {
        printf("entrez une valeur pour y");
        break;
    }
    display_grid(x,y);
    return (0);
}
/* le but est de read les coordonées entrer pas les utilisateurs les valeur son sur une bombe il pert sinon ...
 *
 */

