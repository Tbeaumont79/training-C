#include <unistd.h>

void	ft_putchar(char* c)
{
	write(1,&c,1);

}


int		main()
{
char a;
char *pointeursura;
pointeursura = &a;
ft_putchar(pointeursura);
}
