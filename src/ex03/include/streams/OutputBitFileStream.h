#pragma once

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BITS_IN_BYTE 8

/*
 * Represents an output bit stream of a file.
 * ----------------------------
 *
 * file: file associated with the stream
 * buffer: stream bit buffer
 * count: number of written bits
 */
typedef struct {
    FILE *file;
    uint8_t buffer;
    size_t count;
} OutputBitFileStream;

/*
 * Function: out_bit_file_stream_open
 * ----------------------------
 * Opens a OutputBitFileStream.
 *
 * stream: stream to open
 * filename: name of the file associated with the stream
 *
 * returns: 0 if successfully opens the stream; -1 otherwise
 */
int out_bit_file_stream_open(OutputBitFileStream *stream, const char *filename);

/*
 * Function: out_bit_file_stream_write_bit
 * ----------------------------
 * Writes a bit into the OutputBitFileStream stream.
 *
 * stream: stream to write
 * bit: bit to write
 *
 * returns: 0 if successfully writes the bit; -1 otherwise
 */
int out_bit_file_stream_write_bit(OutputBitFileStream *stream, uint8_t bit);

/*
 * Function: out_bit_file_stream_write_byte
 * ----------------------------
 * Writes a byte into the OutputBitFileStream stream.
 *
 * stream: stream to write
 * byte: byte to write
 *
 * returns: 0 if successfully writes the byte; -1 otherwise
 */
int out_bit_file_stream_write_byte(OutputBitFileStream *stream, uint8_t byte);

/*
 * Function: out_bit_file_stream_write_str
 * ----------------------------
 * Writes a string into the OutputBitFileStream stream.
 *
 * stream: stream to write
 * str: string to write
 *
 * returns: 0 if successfully writes the string; -1 otherwise
 */
int out_bit_file_stream_write_str(OutputBitFileStream *stream, const char *str);

/*
 * Function: out_bit_file_stream_flush
 * ----------------------------
 * Flushes the OutputBitFileStream stream.
 *
 * stream: stream to flush
 *
 * returns: 0 if successfully flushes the stream; -1 otherwise
 */
int out_bit_file_stream_flush(OutputBitFileStream *stream);

/*
 * Function: out_bit_file_stream_destroy
 * ----------------------------
 * Destroyes a OutputBitFileStream stream.
 *
 * stream: stream to destroy
 */
void out_bit_file_stream_destroy(OutputBitFileStream *stream);