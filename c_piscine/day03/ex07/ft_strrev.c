char *ft_strrev(char *str)
{
	int i;
	char lettre;
	int j;
	j = 0;
	i = 0;
	
	while(str[i] != '\0')
		i++;
	i--;
	while( i >= j )
	{
		lettre = str[i];
		str[i] = str[j];
		str[j] = lettre;
		i--;
		j++;
	}
	return(str);
}

