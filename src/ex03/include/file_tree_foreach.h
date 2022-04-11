#pragma once

/*
 * Function: file_tree_foreach
 * ----------------------------
 * Goes through the directory tree below the path and to all files found,
 * invokes a function pointed to by doit, passing the name of the current
 * file and parameter context.
 *
 * dirpath: path the the directory tree
 * doit: function to be invoked
 * context: context passed to the function
 *
 * returns: 0 if successfully goes through all files
 */
int file_tree_foreach(const char *dirpath, void (*doit)(const char *, void *), void *context);
