
#include "ft.h"

int     main()
{
    int x;
    int y;
    while (1)
    {

        printf("\n\nplease enter a value for x and y : ");
        scanf("%d",&x);
        scanf("%d",&y);
        printf("x = %d y = %d",x,y);
        display_grid(x,y);
    }
    return (0);
}
/* le but est de read les coordonées entrer pas les utilisateurs les valeur son sur une bombe il pert sinon ...
 *
 */

