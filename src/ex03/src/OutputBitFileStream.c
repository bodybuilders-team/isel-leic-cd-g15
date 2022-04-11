#include "OutputBitFileStream.h"

int out_bit_file_stream_open(OutputBitFileStream *stream, const char *filename)
{
    stream->file = fopen(filename, "wb");
    if (stream->file == NULL)
        return -1;

    stream->buffer = 0;
    stream->count = 0;

    return 0;
}

int out_bit_file_stream_write_bit(OutputBitFileStream *stream, uint8_t bit)
{
    bit &= 1;
    stream->buffer <<= 1;
    stream->buffer |= bit;
    stream->count++;

    if (stream->count == BITS_IN_BYTE)
        return out_bit_file_stream_flush_buffer(stream);

    return 0;
}

int out_bit_file_stream_write_byte(OutputBitFileStream *stream, uint8_t byte)
{
    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        uint8_t bit = byte >> (BITS_IN_BYTE - i - 1);
        int status = out_bit_file_stream_write_bit(stream, bit);
        if (status < 0)
            return status;
    }

    return 0;
}

int out_bit_file_stream_write_str(OutputBitFileStream *stream, const char *str)
{
    for (const char *ptr = str; *ptr != '\0'; ptr++)
    {
        int status = out_bit_file_stream_write_byte(stream, *ptr);
        if (status < 0)
            return status;
    }
    return 0;
}

int out_bit_file_stream_flush(OutputBitFileStream *stream)
{
    int status = out_bit_file_stream_flush_buffer(stream);
    if (status < 0)
        return status;

    int f_status = fflush(stream->file);
    if (f_status < 0)
        return -1;

    return 0;
}

/*
 * Function: out_bit_file_stream_flush_buffer
 * ----------------------------
 * Flushes the OutputBitFileStream stream buffer.
 *
 * stream: stream to flush
 *
 * returns: 0 if successfully flushes the stream buffer; -1 otherwise
 */
static int out_bit_file_stream_flush_buffer(OutputBitFileStream *stream)
{
    if (stream->count == 0)
        return 0;

    stream->buffer <<= (BITS_IN_BYTE - stream->count);
    int c = fputc(stream->buffer, stream->file);

    stream->count = 0;
    stream->buffer = 0;
    if (c == EOF)
        return -1;
        
    return 0;
}

void out_bit_file_stream_destroy(OutputBitFileStream *stream)
{
    fclose(stream->file);
}