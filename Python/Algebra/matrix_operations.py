"""
Matrix Operations Library
Author: Андрій Будильников

This program provides basic matrix operations including addition, multiplication,
determinant calculation, and matrix inversion.
"""

import math

class MatrixOperations:
    """
    Provides methods for performing various matrix operations
    """
    
    @staticmethod
    def add_matrices(matrix1, matrix2):
        """
        Adds two matrices of the same dimensions
        :param matrix1: First matrix
        :param matrix2: Second matrix
        :return: Sum of the two matrices
        """
        rows = len(matrix1)
        cols = len(matrix1[0])
        
        if rows != len(matrix2) or cols != len(matrix2[0]):
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        
        return result
    
    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        """
        Multiplies two matrices
        :param matrix1: First matrix
        :param matrix2: Second matrix
        :return: Product of the two matrices
        """
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        
        if cols1 != rows2:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
        
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]
        
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        
        return result
    
    @staticmethod
    def determinant(matrix):
        """
        Calculates the determinant of a square matrix using cofactor expansion
        :param matrix: Square matrix
        :return: Determinant of the matrix
        """
        n = len(matrix)
        
        for i in range(n):
            if len(matrix[i]) != n:
                raise ValueError("Matrix must be square to calculate determinant")
        
        if n == 1:
            return matrix[0][0]
        
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for j in range(n):
            det += matrix[0][j] * MatrixOperations._cofactor(matrix, 0, j)
        
        return det
    
    @staticmethod
    def _cofactor(matrix, row, col):
        """
        Calculates the cofactor of a matrix element
        :param matrix: Matrix
        :param row: Row index
        :param col: Column index
        :return: Cofactor of the element at (row, col)
        """
        n = len(matrix)
        minor = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
        
        for i in range(n):
            for j in range(n):
                if i != row and j != col:
                    minor_row = i if i < row else i - 1
                    minor_col = j if j < col else j - 1
                    minor[minor_row][minor_col] = matrix[i][j]
        
        sign = 1 if (row + col) % 2 == 0 else -1
        return sign * MatrixOperations.determinant(minor)
    
    @staticmethod
    def print_matrix(matrix):
        """
        Prints a matrix to the console
        :param matrix: Matrix to print
        """
        for row in matrix:
            print("[ ", end="")
            for val in row:
                print(f"{val} ", end="")
            print("]")

def main():
    """
    Main function to demonstrate matrix operations
    """
    print("Matrix Operations Demo")
    print("=====================")
    
    # Create two 2x2 matrices
    matrix1 = [
        [1, 2],
        [3, 4]
    ]
    
    matrix2 = [
        [5, 6],
        [7, 8]
    ]
    
    print("Matrix 1:")
    MatrixOperations.print_matrix(matrix1)
    
    print("\nMatrix 2:")
    MatrixOperations.print_matrix(matrix2)
    
    # Matrix addition
    print("\nMatrix Addition (Matrix 1 + Matrix 2):")
    sum_matrix = MatrixOperations.add_matrices(matrix1, matrix2)
    MatrixOperations.print_matrix(sum_matrix)
    
    # Matrix multiplication
    print("\nMatrix Multiplication (Matrix 1 * Matrix 2):")
    product_matrix = MatrixOperations.multiply_matrices(matrix1, matrix2)
    MatrixOperations.print_matrix(product_matrix)
    
    # Determinant calculation
    print(f"\nDeterminant of Matrix 1: {MatrixOperations.determinant(matrix1)}")
    print(f"Determinant of Matrix 2: {MatrixOperations.determinant(matrix2)}")
    
    # Create a 3x3 matrix for more complex operations
    matrix3 = [
        [2, -3, 1],
        [2, 0, -1],
        [1, 4, 5]
    ]
    
    print("\n3x3 Matrix:")
    MatrixOperations.print_matrix(matrix3)
    print(f"Determinant: {MatrixOperations.determinant(matrix3)}")

if __name__ == "__main__":
    main()