#include <stdio.h>

int     ft_recursive_power(int nb, int power)
{

        if(power == 0)
            return(1);

        if(power < 0)
            return(0);

        else
        {
                power--;
                return(nb * ft_recursive_power(nb, power));
        }
}

int     main()
{
		printf("%d",ft_recursive_power(16,2));
        return(0);
}
