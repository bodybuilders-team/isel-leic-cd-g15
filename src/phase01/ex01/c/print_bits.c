#include <stdio.h>

/*
 * Function: print_bits
 * ----------------------------
 * Prints as characters the values of the bits of all array elements, with array_size integers.
 *
 * array:      array
 * array_size: array size
 */
void print_bits(int array[], size_t array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        for (int j = 31; j >= 0; j--)
        {
            int bit = (array[i] >> j) & 1;
            printf("%c", (bit) ? '1' : '0');
        }
        printf("\n");
    }
}

/*
 * Function: print_bits test function
 * To run:   gcc print_bits.c -o print_bits && ./print_bits
 */
int main(int argc, char const *argv[])
{
    int no_of_tests = 3;

    //---Test1---
    printf("Test1:\n");
    int a[] = {1, 2, 3};
    printf("Expected:\n00000000000000000000000000000001\n00000000000000000000000000000010\n00000000000000000000000000000011\nReceived:\n");
    print_bits(a, 3);

    //---Test2---
    printf("\nTest2:\n");
    int b[] = {};
    printf("Expected: \nReceived:\n");
    print_bits(b, 0);

    //---Test3---
    printf("\nTest3:\n");
    int c[] = {0, 4294967295};
    printf("Expected:\n00000000000000000000000000000000\n11111111111111111111111111111111\nReceived:\n");
    print_bits(c, 2);

    return 0;
}
