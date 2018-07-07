/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/05/15 11:32:26 by bod               #+#    #+#             */
/*   Updated: 2018/05/15 11:42:18 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
char	*ft_strncpy(char *dest,char *src, unsigned int n)
{
	int i;
	i = 0;

	while(i <= n)
{
	dest[i] = src[i];
	i++;
}
	return(dest);
}
int main()
{
	char dest[255] = "";
	char src[255] = "hello my brother";
	
	printf("---------------------------Test------------------------\n");
	printf("\tsrc est : %s et dest est : %s\n ",src,dest);
	ft_strncpy(dest,src,5);
	printf("\tsrc est : %s et dest est : %s ",src,dest);
	return(0);
}
