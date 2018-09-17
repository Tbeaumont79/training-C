
#include "ft.h"

int     main(int argc, char **argv)
{
    if (argc > 1)
    {
        //faire un atoi
        display_grid(ft_atoi(argv[1]),ft_atoi(argv[2]));
        return (0);
    }
    else
        printf("please enter a value for x and y");
    return (0);
}
/* le but est de read les coordonées entrer pas les utilisateurs les valeur son sur une bombe il pert sinon ...
 *
 */

