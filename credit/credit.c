#include <cs50.h>
#include <stdio.h>

int main(void) 
{
    int count = 0;
    long tot_count = 0;
    int checker;

    //Prompt for input
    long CredCheck = get_long("Number: ");
    long Initial_Cred = CredCheck;

    /* The code block you provided is implementing the Luhn's algorithm. This algorithm is used to
    validate credit card numbers. */
    do
    {
        long ch_number = CredCheck % 10;
        count++;
        if ((count % 2 == 0 && count != 0) || (count % 2 != 0 && count == 0))
        {
            ch_number *= 2;
            if (ch_number > 9)
            {
                ch_number = ch_number / 10 + ch_number % 10;
            }
            tot_count += ch_number;
        }
        else
        {
            tot_count = ch_number + tot_count;
        }
        CredCheck = CredCheck/10;
    } while (CredCheck > 0);
    if (tot_count % 10 == 0)
    {
        /* This code block is responsible for determining the type of credit card based on the input
        number and printing the corresponding result. */
        while (Initial_Cred >= 100)
        {
            Initial_Cred /= 10;
        }
        if (count > 16 || count < 13)
        {
            printf("INVALID");
        }
        else if (count == 15 && (Initial_Cred == 34 || Initial_Cred == 37))
        {
            printf("AMEX");
        }
        else if ((count == 13 || count == 16) && (Initial_Cred >= 40 && Initial_Cred <= 49))
        {
            printf("VISA");
        }
        else if (count == 16 && (Initial_Cred >= 51 && Initial_Cred <= 55))
        {
            printf("MASTERCARD");
        }
        else
        {
            printf("INVALID");
        }
    }
    else
    {
        printf("INVALID");
    }
    printf("\n");
}