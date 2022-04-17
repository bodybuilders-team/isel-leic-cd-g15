#pragma once

#include <stdio.h>
#include "unary_common.h"

/*
 * Function: unary_parse_model
 * ----------------------------
 * Parses a model
 *
 * src_fp: file containing the model
 * model: parsed model
 *
 * returns: 0 if successfully parses the model; negative number otherwise
 */
int unary_parse_model(FILE *src_fp, unary_model *model);

/*
 * Function: unary_decode
 * ----------------------------
 * Decodes a file.
 *
 * src_filename: file to decode
 * dst_filename: file where the decoded file will be printed
 *
 * returns: 0 if successfully decodes the file; negative number otherwise
 */
int unary_decode(const char *src_filename, const char *dst_filename);
