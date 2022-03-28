#include <stdio.h>

/*
 * Function: count_symbol
 * ----------------------------
 * Returns the number of times a symbol occurs in a file.
 *
 * file_name: name of the file
 * symbol:    symbol to count occurrences
 *
 * returns: number of occurrences
 */
int count_symbol(char *file_name, char symbol)
{
    int count = 0;

    FILE *f = fopen(file_name, "r");
    char c;

    while ((c = fgetc(f)) != EOF)
        count += (c == symbol);

    return count;
}

/*
 * Function: count_symbol test function
 */
int main(int argc, char const *argv[])
{
    printf("%d\n", count_symbol("count_ones.c", 'a'));
    return 0;
}
