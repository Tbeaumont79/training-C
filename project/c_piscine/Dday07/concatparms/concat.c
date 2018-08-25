/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   concat.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/20 23:36:20 by bod               #+#    #+#             */
/*   Updated: 2018/08/21 00:05:43 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>
int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}
char *ft_strcat(char *dest,char *source)
{
	int i;
	int j;

	i = 0;
	j = 0;
	while (dest[i] != '\0')
	{
		i++;
	}
	while (source[j] != '\0')
	{
		dest[i + j] = source[j];
		j++;
	}
	dest[i + j] = '\0';
	return (dest);
}
char *ft_concatparm(int argc, char **argv)
{
	int i;
	int length;
	char *str;

	i = 0;
	length = 0;
		while (i < argc)
		{
			length += ft_strlen(argv[i]);
			i++;
		}
	str = malloc(sizeof(char) * length + 1);
	i = 0;
	while (i < argc)
	{
		ft_strcat(str,argv[i]);
		ft_strcat(str,'\n');
		i++;
	}
	str[i] = '\0';
	
	return (str);
}
int main(int ac, char **argv)
{
	char *str;

	str = ft_concatparm(ac,argv);
	printf("%s",str);
	return (0);
}


