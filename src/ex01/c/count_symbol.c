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
 * To run:   gcc count_symbol.c -o count_symbol && ./count_symbol
 */
int main(int argc, char const *argv[])
{
    int no_of_tests = 3;
    int no_of_passed_tests = 0;

    //---Test1---
    printf("Test1:\n");
    int test1_res = count_symbol("count_ones.c", 'a');
    int test1_expected = 28;
    printf("Expected: %d; Received: %d\n", test1_expected, test1_res);
    no_of_passed_tests += (test1_res == test1_expected);
    if (test1_res == test1_expected)
        printf("Test1 passed.\n\n");
    else
        printf("Test1 failed.\n\n");

    //---Test2---
    printf("Test2:\n");
    int test2_res = count_symbol("count_symbol.c", ' ');
    int test2_expected = 357;
    printf("Expected: %d; Received: %d\n", test2_expected, test2_res);
    no_of_passed_tests += (test2_res == test2_expected);
    if (test2_res == test2_expected)
        printf("Test2 passed.\n\n");
    else
        printf("Test2 failed.\n\n");

    //---Test3---
    printf("Test3:\n");
    int test3_res = count_symbol("print_bits.c", '^');
    int test3_expected = 0;
    printf("Expected: %d; Received: %d\n", test3_expected, test3_res);
    no_of_passed_tests += (test3_res == test3_expected);
    if (test3_res == test3_expected)
        printf("Test3 passed.\n\n");
    else
        printf("Test3 failed.\n\n");

    printf("Tests runned: %d; Tests passed: %d; Tests failed: %d\n", no_of_tests, no_of_passed_tests, no_of_tests - no_of_passed_tests);

    return 0;
}
