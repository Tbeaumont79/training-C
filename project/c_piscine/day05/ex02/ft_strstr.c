/* ************************************************************************** */
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/05/15 17:32:38 by bod               #+#    #+#             */
/*   Updated: 2018/05/18 20:21:56 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
char	*ft_strstr(char *str,char *to_find)
{
	int count;
	char find_size;
	int i;

	i = 0;
	count = 0;
	find_size = 0;	

	while(to_find[find_size])
		find_size++;
	if(find_size == 0)
		return(str);
	while(str[i])
	{
		
	}
	
	}
	return(0);
}
	
int		main(void)
{
	char str[255] = "bonjoure c'est un test";
	char to_find[255] = "un";

	printf("%s",ft_strstr(str,to_find));
	return(0);
}
