#pragma once

#include <stdio.h>
#include <memory.h>

/*
 * Function: get_file_size
 * ----------------------------
 * Gets the size of a specific file.
 *
 * path: file path
 *
 * returns: the file size
 */
size_t get_file_size(const char *path);

/*
 * Function: fget_file_size
 * ----------------------------
 * Gets the size of a specific file.
 *
 * file: file
 *
 * returns: the file size
 */
size_t fget_file_size(FILE *file);

/*
 * Function: fopen_mkdir
 * ----------------------------
 * Opens a file with a specific mode.
 *
 * path: file path
 * mode: open mode
 *
 * returns: open file
 */
FILE *fopen_mkdir(const char *path, const char *mode);
