#pragma once

#include <stdio.h>
#include <memory.h>

size_t get_file_size(const char *path);

size_t fget_file_size(FILE *file);

FILE *fopen_mkdir(const char *path, const char *mode);
