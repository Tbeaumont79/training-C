/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft.h                                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/05 19:54:38 by bod               #+#    #+#             */
/*   Updated: 2018/09/10 19:43:20 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# ifndef FT_H
# define FT_H

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int     ft_strlen(char *str);
int     check(char *str,char c);
int     ft_resolve(char c);

#endif
