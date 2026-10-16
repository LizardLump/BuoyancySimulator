cmake_minimum_required(VERSION 3.10)

project(BuoyancySimulator)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build/)

add_subdirectory(contrib)
add_subdirectory(BuoyancySimulator)