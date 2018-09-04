#include <stdio.h>

char *str_copy(char *cpy, char *origine)
{
	int i;

	i = 0;

	while(origine[i] != '\0')
	{
		cpy[i] = origine[i];
		i++;
	}
	return(cpy);
}
int main()
{
	char txt[255] = "hello les baufs";
	char copy[255] = "";
	str_copy(copy,txt);
	printf("%s et %s",copy,txt);
	return (0);
}

