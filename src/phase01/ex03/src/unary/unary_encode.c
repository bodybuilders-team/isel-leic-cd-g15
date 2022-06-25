#include "unary/unary_encode.h"
#include <string.h>
#include "utils.h"

int unary_write_model(OutputBitFileStream *out_stream, unary_model *model) {

    char num_chars_str[MAX_SIZE_T_CHAR_LEN + 4];
    sprintf(num_chars_str, "%zu\n", model->data_len);
    if (out_bit_file_stream_write_str(out_stream, num_chars_str) < 0)
        return -1;

    char num_symbols_str[MAX_SIZE_T_CHAR_LEN + 4];
    sprintf(num_symbols_str, "%zu\n", model->num_symbols);
    if (out_bit_file_stream_write_str(out_stream, num_symbols_str) < 0)
        return -2;


    for (size_t i = 0; i < model->num_symbols; i++) {
        if (out_bit_file_stream_write_byte(out_stream, model->data[i]) < 0)
            return -3;
    }

    return 0;
}

int unary_encode(const char *src_filename, const char *dst_filename) {
    FILE *src_fp = fopen_mkdir(src_filename, "rb");

    if (src_fp == NULL)
        return -1;

    unary_model model;
    unary_calculate_model(src_fp, &model);

    OutputBitFileStream out_stream;
    if (out_bit_file_stream_open(&out_stream, dst_filename) < 0)
        return -2;

    // Printing model
    unary_write_model(&out_stream, &model);

    // Printing encoded data
    if (unary_write_encoded_data(&out_stream, &model, src_fp) < 0)
        return -3;

    if (out_bit_file_stream_flush(&out_stream) < 0)
        return -4;

    out_bit_file_stream_destroy(&out_stream);

    fclose(src_fp);

    return 0;
}
