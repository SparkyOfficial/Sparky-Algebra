#!/bin/bash
# Build and run script for C++ combinatorics

echo "Building combinatorics program..."

# Compile the combinatorics implementation and test
g++ -std=c++11 -o combinatorics_test test_combinatorics.cpp Combinatorics.cpp

if [ $? -eq 0 ]; then
    echo "Build successful!"
    echo "Running tests..."
    ./combinatorics_test
else
    echo "Build failed!"
fi