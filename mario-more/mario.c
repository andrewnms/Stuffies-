#include <cs50.h>
#include <stdio.h>

int main(void) 
{
    //Initialize Variables
    int height;
    int sp_space;
    int hs_space = 1;
    int s_hash = 0;
    
    //get user height prompt, while loop.
    do
    {
        height = get_int("Height: ");
    } while (height < 1 || height > 8);
    for (int j = 0; j < height; j++)
    {
        sp_space = height - j - 1;
        //Spaces 
        for (int i = 0; i < sp_space; i++)
            {
                printf(" ");
            }
        //Hashes
        for (int x = 0; x < hs_space; x++)
            {
                printf("#");
            }
        //Two middle spaces lol
        printf("  ");
        //now backwards hashes
        for (int z = 0; z < hs_space; z++)
            {
                printf("#");
            }
        hs_space++;
        printf("\n");
    }
}