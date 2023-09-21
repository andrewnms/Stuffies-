#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char plate[7];
    bool is_valid(char s[7]);
    printf("Plate: ");
    scanf("%s", plate);
    if (is_valid(plate))
    {
        printf("Valid\n");
    }
    else
    {
        printf("Invalid\n");
    }
}

bool is_valid(char s[7])
{
    bool check = false;
    // check if the first character is a letter
    if (isalpha(s[0]))
    {
        check = true;
    }
    // check if the length of the string is between 2 and 6
    if (check == true)
    {
        int count = 0;
        for (int i = 0; i < strlen(s); i++)
        {
            count++;
        }

        if (2 <= count && count <= 6)
        {
            // check if there is a digit in the string
            int digit_found = 0;
            int first_digit = true;

            for (int i = 0; i < strlen(s); i++)
            {
                if (isdigit(s[i]))
                {
                    digit_found = true;
                    // check if the first digit is 0
                    if (first_digit && s[i] == '0')
                    {
                        check = false;
                    }
                    first_digit = false;
                }

                if (digit_found && !isdigit(s[i]))
                {
                    check = false;
                }
                // check if there is a special character in the string
                if (
                    (33 <= s[i] && s[i] <= 47) ||
                    (58 <= s[i] && s[i] <= 64) ||
                    (91 <= s[i] && s[i] <= 96) ||
                    (123 <= s[i] && s[i] <= 126))
                {
                    check = false;
                }
            }
        }
        else
        {
            check = false;
        }
    }
    return check;
}
