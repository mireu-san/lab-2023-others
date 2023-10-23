#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What is your name?\n");
    int age = get_int("What's your age? ");
    string number = get_string("What's your phone number? ");
    // Phone number is 10 digits long, so higher than positive number.

    printf("Age is %i. Name is %s. Phone number is %s.", age, name, number);
}

// And made a phonebook with C.

int main(void)
{
    for (int i = 0; i < 10; i++)
    {
        for (int j = i; j < 10; j++)
        {
            
        }
    }
}

// do, while
int main(void)
{
    int age;
    do
    {
        age = get_int("Age: ");
    }
    while (age < 15 || age > 20);

    for (int i = 1; i <= 5; i++)
    {
        printf("%i\n", i);
    }
}