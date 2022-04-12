#include <stdint.h>
#include "unary/unary_decode.h"
#include "streams/InputBitFileStream.h"
#include "utils.h"

int unary_parse_model(FILE *src_fp, unary_model *model) {
    if (fscanf(src_fp, "%zu%*1[\n]", &model->data_len) != 1)
        return -1;

    if (fscanf(src_fp, "%zu%*1[\n]", &model->num_symbols) != 1)
        return -2;


    for (size_t i = 0; i < model->num_symbols; i++) {
        int c = fgetc(src_fp);
        if (c == EOF)
            return -3;

        model->data[i] = (uint8_t) c;
    }
    return 0;
}

int unary_decode(const char *src_filename, const char *dst_filename) {
    FILE *src_file = fopen_mkdir(src_filename, "rb");
    if (src_file == NULL)
        return -1;

    unary_model model;
    if (unary_parse_model(src_file, &model) < 0)
        return -2;

    InputBitFileStream in_stream = {src_file, 0, 0};
    FILE *dst_file = fopen_mkdir(dst_filename, "wb");
    if (dst_file == NULL)
        return -3;

    size_t unary_count = 0;

    size_t remaining_symbols = model.data_len;
    while (remaining_symbols > 0) {
        uint8_t bit;
        if (in_bit_file_stream_read_bit(&in_stream, &bit) < 0)
            return -4;

        if (bit == 0) {
            if (fputc(model.data[unary_count], dst_file) < 0)
                return -5;

            unary_count = 0;
            remaining_symbols--;
            continue;
        }

        if (unary_count >= model.num_symbols)
            return -6;

        unary_count++;
    }

    fflush(dst_file);
    fclose(dst_file);
    in_bit_file_stream_destroy(&in_stream);

    return 0;
}
