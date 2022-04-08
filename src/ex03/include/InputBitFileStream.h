#pragma once

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BITS_IN_BYTE 8

typedef struct {
    FILE *file;
    uint8_t buffer;
    size_t count;
} InputBitFileStream;

int in_bit_file_stream_open(InputBitFileStream *stream, const char *filename);

int in_bit_file_stream_read_bit(InputBitFileStream *stream, uint8_t *bit);

void in_bit_file_stream_rewind(InputBitFileStream *stream);

int in_bit_file_stream_read_byte(InputBitFileStream *stream, uint8_t *byte);

int in_bit_file_stream_read_str(InputBitFileStream *stream, char *str);

void in_bit_file_stream_destroy(InputBitFileStream *stream);
