cmake_minimum_required(VERSION 3.16)
project(ex3 C)

set(CMAKE_C_STANDARD 99)

include_directories(include)
add_executable(ex3 src/main.c src/OutputBitFileStream.c include/OutputBitFileStream.h
        include/file_tree_foreach.h src/file_tree_foreach.c include/InputBitFileStream.h src/InputFileStream.c include/unary_common.h include/unary_encode.h src/unary_encode.c include/unary_decode.h src/unary_decode.c include/utils.h src/utils.c src/unary_common.c)
target_link_libraries(ex3 m)