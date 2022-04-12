#pragma once

#include <stdio.h>
#include "unary_common.h"

int unary_parse_model(FILE *src_fp, unary_model *model);

int unary_decode(const char *src_filename, const char *dst_filename);
