#pragma once

#include <stdint.h>
#include <stdio.h>
#include "streams/OutputBitFileStream.h"

#define MAX_SIZE_T_CHAR_LEN 20
#define SYMBOLS_SIZE 256

/*
 * Represents an unary symbol data.
 * ----------------------------
 *
 * symbol: unary symbol
 * count: symbol occurrences
 */
typedef struct {
    uint8_t symbol;
    size_t count;
} unary_symbol_data;

/*
 * Represents an unary data model.
 * ----------------------------
 *
 * data_len: data length
 * num_symbols: total number of symbols in data
 * data: model data
 */
typedef struct {
    size_t data_len;
    size_t num_symbols;
    uint8_t data[SYMBOLS_SIZE];
} unary_model;

/*
 * Function: get_unary_count
 * ----------------------------
 * Gets the number of occurrences of a symbol in a model.
 *
 * model: model
 * symbol: symbol to get number of occurrences
 *
 * returns: the number of occurrences; -1 if the symbol was not found
 */
int get_unary_count(unary_model *model, uint8_t symbol);

/*
 * Function: unary_write_encoded_data
 * ----------------------------
 * Writes encoded data to a OutputBitFileStream.
 *
 * out_stream: stream
 * model: model to write
 * src_fp: source data filepath
 *
 * returns: 0 if successfully writes the encoded data; negative number otherwise
 */
int unary_write_encoded_data(OutputBitFileStream *out_stream, unary_model *model, FILE *src_fp);

/*
 * Function: unary_symbol_data_cmp
 * ----------------------------
 * Compares two unary symbol datas.
 *
 * a: first unary symbol data
 * b: second unary symbol data
 *
 * returns: 0 if the symbols have the same number of occurrences; -1 if a has more occurrences; 1 otherwise
 */
int unary_symbol_data_cmp(unary_symbol_data *a, unary_symbol_data *b);

/*
 * Function: unary_calculate_model
 * ----------------------------
 * Calculates an unary model from a specific source file.
 *
 * src_fp: source data filepath
 * model: model to calculate
 *
 * returns: 0 if the model was calculated successfully
 */
int unary_calculate_model(FILE *src_fp, unary_model *model);

/*
 * Function: unary_calculate_data
 * ----------------------------
 * Calculates an unary symbol data for a specific symbol.
 *
 * unary_model: model
 * symbols_table: table where the symbol is
 * unary_data: data to calculate
 */
void unary_calculate_data(unary_model *model, size_t *symbols_table, unary_symbol_data *unary_data);

/*
 * Function: unary_calculate_symbols_table
 * ----------------------------
 * Calculates a symbols table.
 *
 * src_fp: source data filepath
 * data_len: data length
 * num_symbols: total number of symbols
 * symbols_table: table to calculate
 */
void unary_calculate_symbols_table(FILE *src_fp, size_t *data_len, size_t *num_symbols, size_t *symbols_table);

/*
 * Function: unary_get_model_size
 * ----------------------------
 * Gets the model size.
 *
 * model: model to get size
 *
 * returns: the model size
 */
size_t unary_get_model_size(unary_model *model);

/*
 * Function: unary_get_encoded_size
 * ----------------------------
 * Gets the encoded data size.
 *
 * src_fp: source data filepath
 * size: size to get
 *
 * returns: 0 if the size was calculated successfully; -1 otherwise
 */
int unary_get_encoded_size(FILE *src_fp, size_t *size);

/*
 * Function: unary_get_average_length
 * ----------------------------
 * Gets the average length from a source file.
 *
 * src_fp: source data filepath
 * avg_length: average length to calculate
 *
 * returns: 0 if the length was calculated successfully
 */
int unary_get_average_length(FILE *src_fp, long double *avg_length);

/*
 * Function: unary_get_entropy
 * ----------------------------
 * Gets the entropy from a source file.
 *
 * src_fp: source data filepath
 * entropy: entropy to calculate
 *
 * returns: 0 if the entropy was calculated successfully
 */
int unary_get_entropy(FILE *src_fp, long double *entropy);

/*
 * Function: unary_print_test
 * ----------------------------
 * Prints an unary unit test.
 *
 * file_path: file to encode
 * encoded_file_path: file where the encoded data will be printed
 * decoded_file_path: file where the decoded data will be printed
 */
void unary_print_test(const char *file_path, const char *encoded_file_path, const char *decoded_file_path);
