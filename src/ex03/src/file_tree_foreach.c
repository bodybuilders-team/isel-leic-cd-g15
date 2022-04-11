#include "file_tree_foreach.h"
#include <dirent.h>
#include <errno.h>
#include <stdio.h>
#include <sys/stat.h>
#include <string.h>

int file_tree_foreach(const char *dirpath, void (*doit)(const char *, void *), void *context)
{
    DIR *dir;
    dir = opendir(dirpath);
    if (dir == NULL)
    {
        fprintf(stderr, "opendir(%s): %s\n", dirpath, strerror(errno));
        return -1;
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL)
    {
        struct stat statbuf;
        char filepath[strlen(dirpath) + 1 + strlen(entry->d_name) + 1];
        strcpy(filepath, dirpath);
        strcat(filepath, "/");
        strcat(filepath, entry->d_name);

        int result = stat(filepath, &statbuf);
        if (result == -1)
        {
            fprintf(stderr, "stat(%s,...): %s\n", filepath, strerror(errno));
            continue;
        }

        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        if (S_ISDIR(statbuf.st_mode))
        {
            int result = file_tree_foreach(filepath, doit, context);
            if (result == -1)
                return -1;
        }
        else
            doit(filepath, context);
    }
    closedir(dir);

    return 0;
}
