#include <stdio.h>

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
 */
int main(int argc, char const *argv[])
{
    printf("%d\n", count_ones(7));
    return 0;
}
