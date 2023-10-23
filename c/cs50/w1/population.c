#include<stdio.h>
#include<cs50.h>

int main(void)
{
    // Prompting the user for a starting # of llamas
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    // Prompting the user for an ending # of llamas
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);
    // How many years will it take to get to the goal?
    int years = 0;
    while (start < end)
    {
        // 3 llamas pass away , 4 born = ++ 1 llama.
        start += start / 12;
        years++;
    }
    printf("Years: %i\n", years);
}