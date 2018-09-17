
#include "ft.h"

int     ft_atoi(char *str)
{
    int result;
    int neg; 

    neg = 0;
    result = 0;
    while (*str >= 0 && *str <= 32)
        str++;
    if (*str == '-')
    {
        neg = 1;
        str++;
    }
    if (*str == '-' || *str == '+')
        str++;
    while (*str >= '0' && *str <= '9')
    {
        result *= 10;
        result += *str - 48;
        str++;
    }
    if (neg == 1)
        return (-result);
    return (result);
}
