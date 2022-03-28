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
 * Function: count_symbol test function
 */
int main(int argc, char const *argv[])
{
    int a[] = {1, 2, 3};
    print_bits(a, 3);
    return 0;
}
