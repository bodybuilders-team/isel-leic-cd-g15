#pragma once

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BITS_IN_BYTE 8

/*
 * Represents an input bit stream of a file.
 * ----------------------------
 *
 * file: file associated with the stream
 * buffer: stream bit buffer
 * count: number of read bits
 */
typedef struct
{
    FILE *file;
    uint8_t buffer;
    size_t count;
} InputBitFileStream;

/*
 * Function: in_bit_file_stream_open
 * ----------------------------
 * Opens a InputBitFileStream.
 *
 * stream: stream to open
 * filename: name of the file associated with the stream
 *
 * returns: 0 if successfully opens the stream; -1 otherwise
 */
int in_bit_file_stream_open(InputBitFileStream *stream, const char *filename);

/*
 * Function: in_bit_file_stream_read_bit
 * ----------------------------
 * Reads a bit from the InputBitFileStream stream.
 *
 * stream: stream to read
 * bit: read bit
 *
 * returns: 0 if successfully reads the bit; -1 otherwise
 */
int in_bit_file_stream_read_bit(InputBitFileStream *stream, uint8_t *bit);

/*
 * Function: in_bit_file_stream_read_byte
 * ----------------------------
 * Reads a byte from the InputBitFileStream stream.
 *
 * stream: stream to read
 * byte: read byte
 *
 * returns: 0 if successfully reads the byte; -1 otherwise
 */
int in_bit_file_stream_read_byte(InputBitFileStream *stream, uint8_t *byte);

/*
 * Function: in_bit_file_stream_rewind
 * ----------------------------
 * Rewinds to the beginning of the InputBitFileStream stream.
 *
 * stream: stream to rewind
 */
void in_bit_file_stream_rewind(InputBitFileStream *stream);

/*
 * Function: in_bit_file_stream_destroy
 * ----------------------------
 * Destroyes a InputBitFileStream stream.
 *
 * stream: stream to destroy
 */
void in_bit_file_stream_destroy(InputBitFileStream *stream);
