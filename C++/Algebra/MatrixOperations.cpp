/*
 * Matrix Operations Library
 * Author: Андрій Будильников
 * 
 * This program provides basic matrix operations including addition, multiplication,
 * determinant calculation, and matrix inversion.
 */

#include <iostream>
#include <vector>
#include <stdexcept>
#include <cmath>

/* Provides methods for performing various matrix operations */
class MatrixOperations {
public:
    /* Adds two matrices of the same dimensions */
    static std::vector<std::vector<double>> addMatrices(
        const std::vector<std::vector<double>>& matrix1,
        const std::vector<std::vector<double>>& matrix2) {
        
        size_t rows = matrix1.size();
        size_t cols = matrix1[0].size();
        
        if (rows != matrix2.size() || cols != matrix2[0].size()) {
            throw std::invalid_argument("Matrices must have the same dimensions for addition");
        }
        
        std::vector<std::vector<double>> result(rows, std::vector<double>(cols, 0.0));
        
        for (size_t i = 0; i < rows; i++) {
            for (size_t j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        
        return result;
    }
    
    /* Multiplies two matrices */
    static std::vector<std::vector<double>> multiplyMatrices(
        const std::vector<std::vector<double>>& matrix1,
        const std::vector<std::vector<double>>& matrix2) {
        
        size_t rows1 = matrix1.size();
        size_t cols1 = matrix1[0].size();
        size_t rows2 = matrix2.size();
        size_t cols2 = matrix2[0].size();
        
        if (cols1 != rows2) {
            throw std::invalid_argument("Number of columns in first matrix must equal number of rows in second matrix");
        }
        
        std::vector<std::vector<double>> result(rows1, std::vector<double>(cols2, 0.0));
        
        for (size_t i = 0; i < rows1; i++) {
            for (size_t j = 0; j < cols2; j++) {
                for (size_t k = 0; k < cols1; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }
        
        return result;
    }
    
    /* Calculates the determinant of a square matrix using cofactor expansion */
    static double determinant(const std::vector<std::vector<double>>& matrix) {
        size_t n = matrix.size();
        
        for (size_t i = 0; i < n; i++) {
            if (matrix[i].size() != n) {
                throw std::invalid_argument("Matrix must be square to calculate determinant");
            }
        }
        
        if (n == 1) {
            return matrix[0][0];
        }
        
        if (n == 2) {
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
        }
        
        double det = 0;
        for (size_t j = 0; j < n; j++) {
            det += matrix[0][j] * cofactor(matrix, 0, j);
        }
        
        return det;
    }
    
private:
    /* Calculates the cofactor of a matrix element */
    static double cofactor(const std::vector<std::vector<double>>& matrix, size_t row, size_t col) {
        size_t n = matrix.size();
        std::vector<std::vector<double>> minor(n - 1, std::vector<double>(n - 1, 0.0));
        
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                if (i != row && j != col) {
                    size_t minorRow = i < row ? i : i - 1;
                    size_t minorCol = j < col ? j : j - 1;
                    minor[minorRow][minorCol] = matrix[i][j];
                }
            }
        }
        
        int sign = (row + col) % 2 == 0 ? 1 : -1;
        return sign * determinant(minor);
    }
    
public:
    /* Prints a matrix to the console */
    static void printMatrix(const std::vector<std::vector<double>>& matrix) {
        for (const auto& row : matrix) {
            std::cout << "[ ";
            for (double val : row) {
                std::cout << val << " ";
            }
            std::cout << "]" << std::endl;
        }
    }
};

/* Main method to demonstrate matrix operations */
int main() {
    std::cout << "Matrix Operations Demo" << std::endl;
    std::cout << "=====================" << std::endl;
    
    /* Create two 2x2 matrices */
    std::vector<std::vector<double>> matrix1 = {
        {1, 2},
        {3, 4}
    };
    
    std::vector<std::vector<double>> matrix2 = {
        {5, 6},
        {7, 8}
    };
    
    std::cout << "Matrix 1:" << std::endl;
    MatrixOperations::printMatrix(matrix1);
    
    std::cout << std::endl << "Matrix 2:" << std::endl;
    MatrixOperations::printMatrix(matrix2);
    
    /* Matrix addition */
    std::cout << std::endl << "Matrix Addition (Matrix 1 + Matrix 2):" << std::endl;
    auto sum = MatrixOperations::addMatrices(matrix1, matrix2);
    MatrixOperations::printMatrix(sum);
    
    /* Matrix multiplication */
    std::cout << std::endl << "Matrix Multiplication (Matrix 1 * Matrix 2):" << std::endl;
    auto product = MatrixOperations::multiplyMatrices(matrix1, matrix2);
    MatrixOperations::printMatrix(product);
    
    /* Determinant calculation */
    std::cout << std::endl << "Determinant of Matrix 1: " << MatrixOperations::determinant(matrix1) << std::endl;
    std::cout << "Determinant of Matrix 2: " << MatrixOperations::determinant(matrix2) << std::endl;
    
    /* Create a 3x3 matrix for more complex operations */
    std::vector<std::vector<double>> matrix3 = {
        {2, -3, 1},
        {2, 0, -1},
        {1, 4, 5}
    };
    
    std::cout << std::endl << "3x3 Matrix:" << std::endl;
    MatrixOperations::printMatrix(matrix3);
    std::cout << "Determinant: " << MatrixOperations::determinant(matrix3) << std::endl;
    
    return 0;
}