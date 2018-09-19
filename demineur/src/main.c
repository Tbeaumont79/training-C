
#include "ft.h"

int     main()
{
    int x;
    int y;
    int boolean;
    char grid[size][size];
    char num;
    
    num = 0;
    boolean = 0;
    init_grid(grid);
    display_grid(grid,boolean,num);
    boolean = 1;
    while (1)
    {
        if (ft_check(x,y,grid,boolean) == 1)
            break;
        //probleme generation de bombe aléatoire en boucle
        printf("please enter a value for x : ");
        scanf("%d",&x);
        printf("please enter a value for y : ");
        scanf("%d",&y);
        display_grid(grid,boolean,num);// <-- on la change en check
    }
    return (0);
}
/* le but est de read les coordonées entrer pas les utilisateurs les valeur son sur une bombe il pert sinon ...
 *
 */

