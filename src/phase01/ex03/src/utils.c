#include "utils.h"
#include <malloc.h>
#include <unistd.h>
#include <sys/stat.h>

size_t get_file_size(const char *path) {
    FILE *fp = fopen_mkdir(path, "rb");
    return fget_file_size(fp);
}

size_t fget_file_size(FILE *fp) {
    fseek(fp, 0, SEEK_END);     // seek to end of file
    size_t size = ftell(fp);    // get current file pointer
    fseek(fp, 0, SEEK_SET);     // seek back to beginning of file

    return size;
}

static void mkdir_helper(const char *dir) {
    char tmp[256];
    char *p = NULL;
    size_t len;

    snprintf(tmp, sizeof(tmp), "%s", dir);
    len = strlen(tmp);
    if (tmp[len - 1] == '/')
        tmp[len - 1] = 0;
    for (p = tmp + 1; *p; p++)
        if (*p == '/') {
            *p = 0;
            mkdir(tmp, S_IRWXU);
            *p = '/';
        }
    mkdir(tmp, S_IRWXU);
}


FILE *fopen_mkdir(const char *path, const char *mode) {
    char *dir = strdup(path);
    char *sep = strrchr(dir, '/');
    if (sep) {
        *sep = '\0';
        mkdir_helper(dir);
    }
    free(dir);
    return fopen(path, mode);
}

