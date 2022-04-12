#include <stdio.h>
#include <string.h>
#include "file_tree_foreach.h"
#include "unary_common.h"

#include "unary_encode.h"
#include "unary_decode.h"

void test_callback(const char *file_path) {
    char *file_name = strrchr(file_path, '/') + 1;

    char encoded_file_path[512];
    sprintf(encoded_file_path, "../encoded_test_files/%s.unary", file_name);

    int encode_status = unary_encode(file_path, encoded_file_path);
    if (encode_status < 0) {
        printf("Error encoding file %s status: %d\n", file_path, encode_status);
        return;
    }

    char decoded_file_path[512];
    sprintf(decoded_file_path, "../decoded_test_files/%s", file_name);

    int decode_status = unary_decode(encoded_file_path, decoded_file_path);
    if (decode_status < 0) {
        printf("Error decoding file %s, status: %d\n", decoded_file_path, decode_status);
        return;
    }

    unary_print_test(file_path, encoded_file_path, decoded_file_path);
}

int main() {
    fopen("../test.txt", "w");
    freopen("../test.txt", "a+", stdout);
    file_tree_foreach("../test_files", (void (*)(const char *, void *)) test_callback, NULL);
}