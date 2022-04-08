#pragma once

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BITS_IN_BYTE 8

typedef struct {
    FILE *file;
    uint8_t buffer;
    size_t count;
} OutputBitFileStream;

int out_bit_file_stream_open(OutputBitFileStream *stream, const char *filename);

int out_bit_file_stream_write_bit(OutputBitFileStream *stream, uint8_t bit);

int out_bit_file_stream_flush(OutputBitFileStream *stream);

int out_bit_file_stream_write_byte(OutputBitFileStream *stream, uint8_t byte);

int out_bit_file_stream_write_str(OutputBitFileStream *stream, const char *str);

void out_bit_file_stream_destroy(OutputBitFileStream *stream);