#pragma once

#include "unary_common.h"

int unary_write_model(OutputBitFileStream *out_stream, unary_model *model);

int unary_encode(const char *src_filename, const char *dst_filename);
