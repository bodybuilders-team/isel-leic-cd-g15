#include <stdio.h>
#include <check.h>

/*
 * Function: count_ones
 * ----------------------------
 * Counts the number of bits with value "1" in the integer value.
 *
 * val: value to count bits
 *
 * returns: number of bits
 */
int count_ones(int val)
{
    int count = 0;
    unsigned u_val = val;

    for (; u_val; u_val >>= 1)
        count += (u_val & 1);

    return count;
}

/*
 * Function: count_ones test function
 * To run:   gcc count_ones.c -o count_ones && ./count_ones
 */
int main(int argc, char const *argv[])
{
    int no_of_tests = 3;
    int no_of_passed_tests = 0;

    //---Test1---
    printf("Test1:\n");
    int test1_res = count_ones(7);
    int test1_expected = 3;
    printf("Expected: %d; Received: %d\n", test1_expected, test1_res);
    no_of_passed_tests += (test1_res == test1_expected);
    if (test1_res == test1_expected)
        printf("Test1 passed.\n\n");
    else
        printf("Test1 failed.\n\n");

    //---Test2---
    printf("Test2:\n");
    int test2_res = count_ones(0);
    int test2_expected = 0;
    printf("Expected: %d; Received: %d\n", test2_expected, test2_res);
    no_of_passed_tests += (test2_res == test2_expected);
    if (test2_res == test2_expected)
        printf("Test2 passed.\n\n");
    else
        printf("Test2 failed.\n\n");

    //---Test3---
    printf("Test3:\n");
    int test3_res = count_ones(63);
    int test3_expected = 6;
    printf("Expected: %d; Received: %d\n", test3_expected, test3_res);
    no_of_passed_tests += (test3_res == test3_expected);
    if (test3_res == test3_expected)
        printf("Test3 passed.\n\n");
    else
        printf("Test3 failed.\n\n");

    printf("Tests runned: %d; Tests passed: %d; Tests failed: %d\n", no_of_tests, no_of_passed_tests, no_of_tests - no_of_passed_tests);

    return 0;
}
