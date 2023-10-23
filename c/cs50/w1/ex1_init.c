// initialize
int i = 0;
while (i < 10)
{
    printf("%i\n", i)
    i = i + 1;
}

// while - i can be used outside (initialized outside of while loop already)
int i = 0;
while (i < 10)
{
    printf("%i\n", i);
    i = i + 1;
}

// for loop case - can use i inside of for loop, not outside of it.
for (int i = 0, i < 10; i++)
{
    printf("%i\n", i);
}