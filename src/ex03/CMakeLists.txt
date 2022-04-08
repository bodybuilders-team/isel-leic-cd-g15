cmake_minimum_required(VERSION 3.16)
project(ex3 C)

set(CMAKE_C_STANDARD 17)

include_directories(include)
add_executable(ex3 src/main.c src/OutputBitFileStream.c src/utils.c include/OutputBitFileStream.h
        include/file_tree_foreach.h src/file_tree_foreach.c include/utils.h include/InputBitFileStream.h src/InputFileStream.c)
