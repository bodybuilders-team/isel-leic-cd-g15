#include <stdio.h>
#include "file_tree_foreach.h"
#include <memory.h>
#include <stdlib.h>
#include <stdint.h>
#include "OutputBitFileStream.h"
#include "InputBitFileStream.h"
#include <stdbool.h>
#include <string.h>

#define MAX_SIZE_T_CHAR_LENGTH 20

void printBits(void const *const ptr, size_t const size) {
    printf("hexVal = %#08x; decVal = %i \n", *(unsigned *) ptr, *(unsigned *) ptr);
    unsigned char *b = (unsigned char *) ptr;
    unsigned char byte;
    int i, j;
    for (i = size - 1; i >= 0; i--)
        for (j = 7; j >= 0; j--) {
            byte = (b[i] >> j) & 1;
            printf(" %u ", byte);
        }
    puts("");
    for (int ind = 31; ind > 9; ind--)
        printf("%d ", ind);
    for (int ind = 9; ind > -1; ind--)
        printf(" %d ", ind);
    puts("");
    puts("");
};

typedef struct {
    int symbol;
    size_t count;
} unary_symbol_data;

int get_unary_count(unary_symbol_data *array, int array_size, int symbol) {
    for (size_t i = 0; i < array_size; i++) {
        if (array[i].symbol == symbol)
            return (int) i;
    }
    return -1;
}

int unary_symbol_data_cmp(unary_symbol_data *a, unary_symbol_data *b) {
    return b->count - a->count;
}

int unary_decode(const char *src_filename, const char *dst_filename) {
    FILE *src_file = fopen(src_filename, "rb");
    if (src_file == NULL) {
        printf("Error opening input stream\n");
        return -1;
    }

    size_t num_chars;
    size_t num_symbols;
    {
        char c;
        int n = fscanf(src_file, "%zu%c", &num_chars, &c);
        if (n != 2 || c != '\n') {
            printf("Error decoding file\n");
            return -1;
        }
    }
    {
        int c;
        int n = fscanf(src_file, "%zu%c", &num_symbols, &c);
        if (n != 2 || c != '\n') {
            printf("Error decoding file\n");
            return -2;
        }
    }

    unary_symbol_data symbolsCount[num_symbols];
    size_t i = 0;
    while (true) {
        {
            int c = fgetc(src_file);

            if (c == EOF) {
                printf("Error decoding file\n");
                return -3;
            } else if (c == '\n') {
                char c2 = fgetc(src_file);

                if (c2 == EOF) {
                    printf("Error decoding file\n");
                    return -4;
                } else if (c2 == '\n') {
                    break;
                }

                if (ungetc(c2, src_file) < 0) {
                    printf("Error decoding file\n");
                    return -4;
                }
            }

            if (ungetc(c, src_file) < 0) {
                printf("Error decoding file\n");
                return -5;
            }
        }

        int c;
        unary_symbol_data data;
        int n = fscanf(src_file, "%c%zu%c", &data.symbol, &data.count, &c);
        if (n != 3 || c != '\n') {
            printf("Error decoding file\n");
            return -6;
        }


        symbolsCount[i++] = data;
    }

    InputBitFileStream in_stream = {src_file, 0, 0};
    FILE *dst_file = fopen(dst_filename, "wb");
    if (dst_file == NULL) {
        printf("Error opening output stream\n");
        return -7;
    }

    size_t unary_count = 0;
    size_t num_chars_left = num_chars;
    while (num_chars_left > 0) {
        uint8_t bit;
        {
            int status = in_bit_file_stream_read_bit(&in_stream, &bit);
            if (status < 0) {
                printf("Error decoding file\n");
                return -8;
            }

        }

        if (bit == 0) {
            int c = symbolsCount[unary_count].symbol;
            char c_char = (char) c;
            int n = fputc(c, dst_file);
            if (n < 0) {
                printf("Error decoding file\n");
                return -9;
            }
            unary_count = 0;
            num_chars_left--;
            continue;
        }

        if (unary_count >= num_symbols) {
            printf("Error decoding file\n");
            return -10;
        }

        unary_count++;
    }

    fflush(dst_file);
    fclose(dst_file);
    in_bit_file_stream_destroy(&in_stream);

    return 0;
}

int unary_encode(const char *src_filename, const char *dst_filename) {
#define symbols_size 256

    int symbols_table[symbols_size];
    memset(symbols_table, 0, symbols_size * sizeof(int));

    FILE *src_fp = fopen(src_filename, "r");
    if (src_fp == NULL) {
        printf("Could not open file %s\n", src_filename);
        return -1;
    }

    size_t num_chars = 0;
    for (int c = fgetc(src_fp); !feof(src_fp); c = fgetc(src_fp), num_chars++)
        symbols_table[c]++;

    size_t num_symbols = 0;
    for (size_t i = 0; i < symbols_size; i++) {
        if (symbols_table[i] > 0)
            num_symbols++;
    }

    unary_symbol_data ordered_symbols[num_symbols];
    memset(ordered_symbols, 0, num_symbols * sizeof(unary_symbol_data));

    for (size_t i = 0, j = 0; i < symbols_size; i++) {
        if (symbols_table[i] > 0) {
            unary_symbol_data *symbol_data = &ordered_symbols[j++];
            symbol_data->symbol = (int) i;
            symbol_data->count = symbols_table[i];
        }
    }

    qsort(ordered_symbols, num_symbols, sizeof(unary_symbol_data),
          (int (*)(const void *, const void *))
                  unary_symbol_data_cmp);

    rewind(src_fp);

    OutputBitFileStream out_stream;
    int stream_err = out_bit_file_stream_open(&out_stream, dst_filename);
    if (stream_err < 0) {
        printf("Error opening file %s\n", dst_filename);
        return -2;
    }

    // Printing model
    {
        char num_chars_str[MAX_SIZE_T_CHAR_LENGTH + 4];
        sprintf(num_chars_str, "%zu\n", num_chars);
        out_bit_file_stream_write_str(&out_stream, num_chars_str);

        char num_symbols_str[MAX_SIZE_T_CHAR_LENGTH + 4];
        sprintf(num_symbols_str, "%zu\n", num_symbols);
        out_bit_file_stream_write_str(&out_stream, num_symbols_str);
    }

    for (size_t i = 0; i < num_symbols; i++) {
        unary_symbol_data *symbol_data = &ordered_symbols[i];

        char msg[MAX_SIZE_T_CHAR_LENGTH + 3];
        sprintf(msg, "%c%zu\n", symbol_data->symbol, symbol_data->count);
        out_bit_file_stream_write_str(&out_stream, msg);
    }

    out_bit_file_stream_write_str(&out_stream, "\n\n");

    // Printing encoded data
    for (int c = fgetc(src_fp); !feof(src_fp); c = fgetc(src_fp)) {
        int unary_cnt = get_unary_count(ordered_symbols, num_symbols, c);

        if (unary_cnt < 0) {
            perror("Error happened while encoding\n");
            return -3;
        }

        char c_char = (char) c;
        for (size_t i = 0; i < unary_cnt; i++) {
            out_bit_file_stream_write_bit(&out_stream, 1);
        }
        out_bit_file_stream_write_bit(&out_stream, 0);

    }

    out_bit_file_stream_flush(&out_stream);
    out_bit_file_stream_destroy(&out_stream);

    fclose(src_fp);

    return 0;
}

void encode_file_directory(const char *file_path, void *context) {

    char *file_name = strrchr(file_path, '/');

    char output_file_path[512];
    sprintf(output_file_path, "../encoded_test_files/%s.unary", file_name + 1);

    int encode_status = unary_encode(file_path, output_file_path);
    if (encode_status < 0) {
        printf("Error encoding file %s\n", file_path);
        return;
    }
}


void decode_file_directory(const char *file_path, void *context) {
    char *file_name = strdup(strrchr(file_path, '/') + 1);
    file_name[strlen(file_name) - 6] = '\0';
    char output_file_path[512];
    sprintf(output_file_path, "../decoded_test_files/%s", file_name);

    int encode_status = unary_decode(file_path, output_file_path);
    if (encode_status < 0) {
        printf("Error decoding file %s\n", file_path);
        return;
    }
    free(file_name);
}

int main() {
    file_tree_foreach("../test_files", encode_file_directory, NULL);
    file_tree_foreach("../encoded_test_files", decode_file_directory, NULL);

}