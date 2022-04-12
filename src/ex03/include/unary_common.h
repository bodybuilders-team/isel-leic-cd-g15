#pragma once

#include <stdint.h>
#include <stdio.h>
#include "OutputBitFileStream.h"

#define MAX_SIZE_T_CHAR_LEN 20
#define SYMBOLS_SIZE 256

typedef struct {
    uint8_t symbol;
    size_t count;
} unary_symbol_data;

typedef struct {
    size_t data_len;
    size_t num_symbols;
    uint8_t data[SYMBOLS_SIZE];
} unary_model;

int unary_write_encoded_data(OutputBitFileStream *out_stream, unary_model *model, FILE *src_fp);

int get_unary_count(unary_model *model, uint8_t symbol);

int unary_symbol_data_cmp(unary_symbol_data *a, unary_symbol_data *b);

int unary_calculate_model(FILE *src_fp, unary_model *model);

void unary_calculate_data(unary_model *model, size_t *symbols_table, unary_symbol_data *unary_data);

void unary_calculate_symbols_table(FILE *src_fp, size_t *data_len, size_t *num_symbols, size_t *symbols_table);

size_t unary_get_model_size(unary_model *model);

int unary_get_encoded_size(FILE *src_fp, size_t *size);

int unary_get_average_length(FILE *src_fp, long double *avg_length);

int unary_get_entropy(FILE *src_fp, long double *entropy);

void unary_print_test(const char *file_path, const char *encoded_file_path, const char *decoded_file_path);
