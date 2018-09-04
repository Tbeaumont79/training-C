/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   static.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/07/04 16:57:36 by bod               #+#    #+#             */
/*   Updated: 2018/07/04 17:01:45 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<stdio.h>
int test();
int main(void)
{
	printf("%d",test());
	printf("%d",test());
	printf("%d",test());
	printf("%d",test());

	return(0);
}
int test()
{
	static int result = 0;
	
	result++;
	return(result);

}
