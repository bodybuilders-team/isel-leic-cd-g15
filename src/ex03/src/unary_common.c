#include "unary_common.h"
#include <stdint.h>
#include <string.h>
#include "utils.h"
#include <math.h>

int get_unary_count(unary_model *model, uint8_t symbol) {
    for (size_t i = 0; i < model->num_symbols; i++) {
        if (model->data[i] == symbol)
            return (int) i;
    }
    return -1;
}

int unary_write_encoded_data(OutputBitFileStream *out_stream, unary_model *model, FILE *src_fp) {
    for (int c = fgetc(src_fp); c != EOF; c = fgetc(src_fp)) {
        int unary_cnt = get_unary_count(model, c);

        if (unary_cnt < 0)
            return -1;

        for (size_t i = 0; i < unary_cnt; i++) {
            if (out_bit_file_stream_write_bit(out_stream, 1) < 0)
                return -2;
        }
        if (out_bit_file_stream_write_bit(out_stream, 0) < 0)
            return -3;
    }

    return 0;
}

int unary_symbol_data_cmp(unary_symbol_data *a, unary_symbol_data *b) {
    // We don't use subtraction because of size_t
    return (b->count == a->count) ? 0 : (b->count < a->count) ? -1
                                                              : 1;
}

int unary_calculate_model(FILE *src_fp, unary_model *model) {
    size_t symbols_table[SYMBOLS_SIZE];
    memset(symbols_table, 0, SYMBOLS_SIZE * sizeof(size_t));
    unary_calculate_symbols_table(src_fp, &model->data_len, &model->num_symbols, symbols_table);

    unary_symbol_data unary_data[model->num_symbols];
    unary_calculate_data(model, symbols_table, unary_data);

    for (size_t i = 0; i < model->num_symbols; i++)
        model->data[i] = unary_data[i].symbol;

    return 0;
}

void unary_calculate_data(unary_model *model, size_t *symbols_table, unary_symbol_data *unary_data) {

    for (size_t i = 0, j = 0; i < SYMBOLS_SIZE; i++) {
        if (symbols_table[i] > 0) {
            unary_symbol_data *symbol_data = &unary_data[j++];
            symbol_data->symbol = (uint8_t) i;
            symbol_data->count = symbols_table[i];
        }
    }

    qsort(unary_data, model->num_symbols, sizeof(unary_symbol_data),
          (int (*)(const void *, const void *))
                  unary_symbol_data_cmp);
}

void unary_calculate_symbols_table(FILE *src_fp, size_t *data_len, size_t *num_symbols, size_t *symbols_table) {
    *data_len = 0;
    for (int c = fgetc(src_fp); c != EOF; c = fgetc(src_fp), (*data_len)++)
        symbols_table[c]++;
    rewind(src_fp);

    *num_symbols = 0;
    for (size_t i = 0; i < SYMBOLS_SIZE; i++) {
        if (symbols_table[i] > 0)
            (*num_symbols)++;
    }
}

size_t unary_get_model_size(unary_model *model) {
    size_t model_size = 0;

    char num_chars_str[MAX_SIZE_T_CHAR_LEN + 4];
    sprintf(num_chars_str, "%zu\n", model->data_len);

    model_size += strlen(num_chars_str);

    char num_symbols_str[MAX_SIZE_T_CHAR_LEN + 4];
    sprintf(num_symbols_str, "%zu\n", model->num_symbols);

    model_size += strlen(num_symbols_str);

    model_size += model->num_symbols;

    return model_size;
}

int unary_get_encoded_size(FILE *src_fp, size_t *size) {
    unary_model model;

    *size = 0;

    if (unary_calculate_model(src_fp, &model) < 0)
        return -1;

    *size += unary_get_model_size(&model);

    rewind(src_fp);

    size_t num_bits = 0;
    for (int c = fgetc(src_fp); c != EOF; c = fgetc(src_fp)) {
        int unary_cnt = get_unary_count(&model, c);
        if (unary_cnt < 0)
            return -2;

        num_bits += unary_cnt + 1;
    }
    rewind(src_fp);

    *size += ceil(num_bits / 8.0);

    return 0;
}

int unary_get_average_length(FILE *src_fp, long double *avg_length) {
    unary_model model;
    size_t symbols_table[SYMBOLS_SIZE];
    memset(symbols_table, 0, SYMBOLS_SIZE * sizeof(size_t));
    unary_calculate_symbols_table(src_fp, &model.data_len, &model.num_symbols, symbols_table);

    unary_symbol_data unary_data[model.num_symbols];
    unary_calculate_data(&model, symbols_table, unary_data);

    rewind(src_fp);

    size_t file_size = fget_file_size(src_fp);

    *avg_length = 0;
    for (int i = 0; i < model.num_symbols; i++) {
        unary_symbol_data *data = &unary_data[i];

        long double symbol_prob = (long double) data->count / file_size;

        *avg_length += symbol_prob * (i + 1);
    }

    return 0;
}

int unary_get_entropy(FILE *src_fp, long double *entropy) {
    unary_model model;
    size_t symbols_table[SYMBOLS_SIZE];
    memset(symbols_table, 0, SYMBOLS_SIZE * sizeof(size_t));
    unary_calculate_symbols_table(src_fp, &model.data_len, &model.num_symbols, symbols_table);

    unary_symbol_data unary_data[model.num_symbols];
    unary_calculate_data(&model, symbols_table, unary_data);

    rewind(src_fp);

    size_t file_size = fget_file_size(src_fp);

    *entropy = 0;
    for (int i = 0; i < model.num_symbols; i++) {
        unary_symbol_data *data = &unary_data[i];

        long double symbol_prob = (long double) data->count / file_size;

        *entropy += symbol_prob * log2l(symbol_prob);
    }
    *entropy = -*entropy;

    return 0;
}

void unary_print_test(const char *file_path, const char *encoded_file_path, const char *decoded_file_path) {
    size_t file_size = get_file_size(file_path);

    size_t encoded_size = get_file_size(encoded_file_path);

    size_t decoded_size = get_file_size(decoded_file_path);

    FILE *src_fp = fopen(file_path, "rb");

    size_t expected_encoded_size;
    if (unary_get_encoded_size(src_fp, &expected_encoded_size) < 0) {
        printf("Error calculating expected encoded size\n");
        return;
    }

    long double avg_length;
    unary_get_average_length(src_fp, &avg_length);

    long double entropy;
    unary_get_entropy(src_fp, &entropy);

    printf("File %s\n\n", file_path);
    printf("File size: %zu bytes\n", file_size);
    printf("Decoded size: %zu bytes\n", decoded_size);
    if (file_size != decoded_size)
        printf("Error: decoded file size does not match original file size\n");

    printf("Expected encoded size: %zu bytes\n", expected_encoded_size);
    printf("Encoded size: %zu bytes\n", encoded_size);
    if (encoded_size != expected_encoded_size)
        printf("Error: encoded file size does not match expected file size\n");

    printf("Compression ratio: %.2f%%\n", (double) encoded_size / file_size * 100);
    printf("Average length: %.2Lf bits/symbol\n", avg_length);
    printf("Entropy: %.2Lf bits/symbol\n", entropy);
    printf("Encoding efficiency: %.2Lf%%\n", entropy / avg_length * 100);

    printf("-----------------------------------------------------\n");
}
