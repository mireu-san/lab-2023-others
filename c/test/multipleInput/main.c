#include <stdio.h>

int main()
{
    double number;
    char alphabet;

    // printf("Enter double input: ");
    // scanf("%lf", &number);

    printf("Enter input values: ");
    scanf("%lf %c", &number, &alphabet);

    // printf("Enter character input: ");
    // scanf("\n%c", &alphabet);

    printf("Number: %lf", number);
    printf("\nCharacter: %c", alphabet);
}