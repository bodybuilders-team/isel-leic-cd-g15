cmake_minimum_required(VERSION 3.16)
project(ex3 C)

set(CMAKE_C_STANDARD 99)

include_directories(include)
add_executable(ex3 src/main.c src/streams/OutputBitFileStream.c include/streams/OutputBitFileStream.h
        include/file_tree_foreach.h src/file_tree_foreach.c include/streams/InputBitFileStream.h src/streams/InputFileStream.c include/unary/unary_common.h include/unary/unary_encode.h src/unary/unary_encode.c include/unary/unary_decode.h src/unary/unary_decode.c include/utils.h src/utils.c src/unary/unary_common.c)
add_library(unary SHARED  src/streams/OutputBitFileStream.c include/streams/OutputBitFileStream.h
        include/file_tree_foreach.h src/file_tree_foreach.c include/streams/InputBitFileStream.h src/streams/InputFileStream.c include/unary/unary_common.h include/unary/unary_encode.h src/unary/unary_encode.c include/unary/unary_decode.h src/unary/unary_decode.c include/utils.h src/utils.c src/unary/unary_common.c)

target_link_libraries(ex3 m)