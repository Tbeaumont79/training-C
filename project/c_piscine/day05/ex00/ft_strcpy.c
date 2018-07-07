/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/05/14 23:03:22 by bod               #+#    #+#             */
/*   Updated: 2018/05/15 00:45:11 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<stdio.h>

char	*ft_strcpy(char *dest, char *src)
{
	int i;



	i = 0;
	
	while(src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	return(dest);
}

int main()
{
	char *src;
	char *dest;
	
	src = "hello";
	dest = "";
	printf("------------------------TEST-------------------------\n");
	printf("\tsrc est : %s et dest est : %s ",src,dest);
	ft_strcpy(src,dest);
	printf("\n\tsrc est : %s et dest est : %s ",src,dest);

	printf("%s\n",ft_strcpy(src,dest));
	printf("-----------------------------------------------------\n");


	return(0);
}
