

#include "ft.h"

void    display_grid(char str[size][size], int boolean)
{
    int i;
    int j;

    i = 0;
    while (i < size)
    {
        j = 0;
        while (str[i][j] != '\0' && size > j)
        {
            if (!(str[i][j+1] == '#' && boolean == 2))
                ft_putchar(str[i][j]);  
            else
                ft_putchar(str[i][j]);
            j++;
        }
        i++;
        ft_putchar('\n');
    }
    printf("la valeur de i est %d et la valeur de j est: %d\n",i,j);
}
