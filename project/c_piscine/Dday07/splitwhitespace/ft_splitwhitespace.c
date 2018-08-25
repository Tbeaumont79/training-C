/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_splitwhitespace.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bod <marvin@42.fr>                         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/08/20 00:03:11 by bod               #+#    #+#             */
/*   Updated: 2018/08/20 22:56:20 by bod              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

char	is_word(char c, char before)
{
	return((c >= '0' && c <= '9') ||( c >= 'A' && c <= 'Z')
			|| ((c >= 'a' && c <= 'z') && (before == ' ' || before == '\n' || before == '\t')));
}

char	count_word(char *str)
{
	int i;
	int word_count;
	char **str1;

	i = 0;
	word_count = 0;
	while (str[i] != '\0')
	{
		if (is_word(str[i],str[i - 1])||(str[i] != ' ' && str[i] != '\t' && str[i] != '\n' && i == 0))
		{
			word_count++;
		}
		i++;
	}
	return (word_count);
}
int		if_new_string(int i, char *str)
{
	return (i > 0 && str[i - 1] == ' ' && str[i - 1] == '\n' && str[i - 1] == '\t');
}

int		*size_of_word(char *str)
{
	int compteur;
	int i;
	int word_count;
	int **word_size;

	i = 0;
	word_count = count_word(str);
	word_size = malloc(sizeof(int) * word_count);
	while (i <= word_count)
	{
		word_size[i] = 0;
		i++;
	}
	i = 0;
	compteur = 0;
	while (str[i] != '\0')
	{
		if (str[i] != ' ' || str[i] != '\t' || str[i] != '\n')
			word_size[compteur]++;
		else if(if_new_string(i ,str))
			compteur++;
		i++;
	}
	return (*word_size);
}
char	**ft_splitwhitespace(char *str)
{
	char **word;
	int	i;
	int j;
	int compteur;
	int *word_size;

	word = malloc(sizeof(char *) * count_word(str));
	word_size = size_of_word(str);
	compteur = 0;
	i = -1;
	j = 0;
	while (str[++i] != '\0')
	{
		if (str[i] != ' ' && str[i] == '\n' && str[i] == '\t')
		{
			if (i == 0 || is_word(str[i],str[i - 1]))
			{
				word[compteur] = malloc(sizeof(char) * word_size[compteur]);
			}
			word[compteur][j] = str[i];
			word[compteur][++j] = '\0';
		}
		if (if_new_string(i ,str) && compteur++)
			j = 0;
		i++;
	}
	word[count_word(str)] = 0;
	return (word);
}
#include <stdio.h>
int main (void)
{
	char txt[255] = "bonjour ceci est un test \n \t mais bon ca remove rien !!";
	printf("%s",*ft_splitwhitespace(txt));
	return (0);

}
