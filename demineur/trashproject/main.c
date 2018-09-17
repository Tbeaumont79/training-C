#include <time.h>
#include <stdio.h>
#include <stdlib.h>
int ft_atoi(char *str);
int main(int argc, char **argv)
{
	int i = 0;
	int c = 0;
	char str[255];
	if ( argc >= 2 )
		for (i = 1; i<argc; i++)
			printf("Test \'%s\': atoi > %d VS %d < ft_atoi => %s\n", argv[i], atoi(argv[i]), ft_atoi(argv[i]), (atoi(argv[i]) == ft_atoi(argv[i]) ? "\033[32m OK \033[0m" : "\033[31m FAIL \033[0m"));
	else
	{
		srand(time(NULL));
		for (i = 0; i<1000000; i++)
		{
			for(c = 0; c < rand()%20; c++)
				str[c]=rand()%126+1;
			str[c]='\0';
			printf("Test \"%s\": atoi > %d VS %d < ft_atoi => %s\n", str, atoi(str), ft_atoi(str), (atoi(str) == ft_atoi(str) ? "\033[32m OK \033[0m" : "\033[31m FAIL \033[0m"));
		}
	}
}
