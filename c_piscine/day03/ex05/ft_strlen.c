void ft_strlen(char *str)
{
	int i;
	i = 0;

	while(str[i] != '\0')
	{
		ft_putchar(str[i]);
		i++;
		
	}
	return(i);
}

