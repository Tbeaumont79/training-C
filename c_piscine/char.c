#include <unistd.h>

int	main(void)
{
	char c;
	c = "hello world";
	write(1,&c,11);
	return(0);
}
