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