#include "InputBitFileStream.h"

int in_bit_file_stream_open(InputBitFileStream *stream, const char *filename)
{
    stream->file = fopen(filename, "r");
    if (stream->file == NULL)
        return -1;

    stream->buffer = 0;
    stream->count = 0;

    return 0;
}

int in_bit_file_stream_read_bit(InputBitFileStream *stream, uint8_t *bit)
{
    if (stream->count == 0)
    {
        stream->buffer = fgetc(stream->file);

        if (ferror(stream->file))
            return -1;

        stream->count = 8;
    }

    *bit = stream->buffer >> (BITS_IN_BYTE - 1);
    stream->buffer <<= 1;
    stream->count--;

    return 0;
}

int in_bit_file_stream_read_byte(InputBitFileStream *stream, uint8_t *byte)
{
    uint8_t parsed_byte = 0;

    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        uint8_t bit;
        int status = in_bit_file_stream_read_bit(stream, &bit);
        if (status < 0)
            return status;

        parsed_byte |= bit << (BITS_IN_BYTE - 1 - i);
    }

    *byte = parsed_byte;

    return 0;
}

void in_bit_file_stream_rewind(InputBitFileStream *stream)
{
    rewind(stream->file);
    stream->buffer = 0;
    stream->count = 0;
}

void in_bit_file_stream_destroy(InputBitFileStream *stream)
{
    fclose(stream->file);
}
