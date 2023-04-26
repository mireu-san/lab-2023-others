#include <stdio.h>

int main()
{
    char character = 'z';
    printf("%c", character);

    // note: characters are internally stored as integers
    printf(" %d", character);

    return 0;
}