#pragma once

#include "unary_common.h"

/*
 * Function: unary_write_model
 * ----------------------------
 * Writes a model to an OutputBitFileStream.
 *
 * out_stream: stream
 * model: model to write
 *
 * returns: 0 if successfully writes the model; negative number otherwise
 */
int unary_write_model(OutputBitFileStream *out_stream, unary_model *model);

/*
 * Function: unary_encode
 * ----------------------------
 * Encodes a file.
 *
 * src_filename: file to encode
 * dst_filename: file where the encoded file will be printed
 *
 * returns: 0 if successfully encodes the file; negative number otherwise
 */
int unary_encode(const char *src_filename, const char *dst_filename);
