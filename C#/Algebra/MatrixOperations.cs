/*
 * Matrix Operations Library
 * Author: Андрій Будильников
 * 
 * This program provides basic matrix operations including addition, multiplication,
 * determinant calculation, and matrix inversion.
 */

using System;

namespace Algebra
{
    /// <summary>
    /// Provides methods for performing various matrix operations
    /// </summary>
    public class MatrixOperations
    {
        /// <summary>
        /// Adds two matrices of the same dimensions
        /// </summary>
        /// <param name="matrix1">First matrix</param>
        /// <param name="matrix2">Second matrix</param>
        /// <returns>Sum of the two matrices</returns>
        public static double[,] AddMatrices(double[,] matrix1, double[,] matrix2)
        {
            int rows = matrix1.GetLength(0);
            int cols = matrix1.GetLength(1);
            
            if (rows != matrix2.GetLength(0) || cols != matrix2.GetLength(1))
            {
                throw new ArgumentException("Matrices must have the same dimensions for addition");
            }
            
            double[,] result = new double[rows, cols];
            
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < cols; j++)
                {
                    result[i, j] = matrix1[i, j] + matrix2[i, j];
                }
            }
            
            return result;
        }
        
        /// <summary>
        /// Multiplies two matrices
        /// </summary>
        /// <param name="matrix1">First matrix</param>
        /// <param name="matrix2">Second matrix</param>
        /// <returns>Product of the two matrices</returns>
        public static double[,] MultiplyMatrices(double[,] matrix1, double[,] matrix2)
        {
            int rows1 = matrix1.GetLength(0);
            int cols1 = matrix1.GetLength(1);
            int rows2 = matrix2.GetLength(0);
            int cols2 = matrix2.GetLength(1);
            
            if (cols1 != rows2)
            {
                throw new ArgumentException("Number of columns in first matrix must equal number of rows in second matrix");
            }
            
            double[,] result = new double[rows1, cols2];
            
            for (int i = 0; i < rows1; i++)
            {
                for (int j = 0; j < cols2; j++)
                {
                    for (int k = 0; k < cols1; k++)
                    {
                        result[i, j] += matrix1[i, k] * matrix2[k, j];
                    }
                }
            }
            
            return result;
        }
        
        /// <summary>
        /// Calculates the determinant of a square matrix using cofactor expansion
        /// </summary>
        /// <param name="matrix">Square matrix</param>
        /// <returns>Determinant of the matrix</returns>
        public static double Determinant(double[,] matrix)
        {
            int n = matrix.GetLength(0);
            
            if (n != matrix.GetLength(1))
            {
                throw new ArgumentException("Matrix must be square to calculate determinant");
            }
            
            if (n == 1)
            {
                return matrix[0, 0];
            }
            
            if (n == 2)
            {
                return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0];
            }
            
            double det = 0;
            for (int j = 0; j < n; j++)
            {
                det += matrix[0, j] * Cofactor(matrix, 0, j);
            }
            
            return det;
        }
        
        /// <summary>
        /// Calculates the cofactor of a matrix element
        /// </summary>
        /// <param name="matrix">Matrix</param>
        /// <param name="row">Row index</param>
        /// <param name="col">Column index</param>
        /// <returns>Cofactor of the element at (row, col)</returns>
        private static double Cofactor(double[,] matrix, int row, int col)
        {
            int n = matrix.GetLength(0);
            double[,] minor = new double[n - 1, n - 1];
            
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i != row && j != col)
                    {
                        int minorRow = i < row ? i : i - 1;
                        int minorCol = j < col ? j : j - 1;
                        minor[minorRow, minorCol] = matrix[i, j];
                    }
                }
            }
            
            int sign = (row + col) % 2 == 0 ? 1 : -1;
            return sign * Determinant(minor);
        }
        
        /// <summary>
        /// Prints a matrix to the console
        /// </summary>
        /// <param name="matrix">Matrix to print</param>
        public static void PrintMatrix(double[,] matrix)
        {
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            
            for (int i = 0; i < rows; i++)
            {
                Console.Write("[ ");
                for (int j = 0; j < cols; j++)
                {
                    Console.Write(matrix[i, j].ToString("F2") + " ");
                }
                Console.WriteLine("]");
            }
        }
        
        /// <summary>
        /// Main method to demonstrate matrix operations
        /// </summary>
        public static void Main(string[] args)
        {
            Console.WriteLine("Matrix Operations Demo");
            Console.WriteLine("=====================");
            
            // Create two 2x2 matrices
            double[,] matrix1 = {
                { 1, 2 },
                { 3, 4 }
            };
            
            double[,] matrix2 = {
                { 5, 6 },
                { 7, 8 }
            };
            
            Console.WriteLine("Matrix 1:");
            PrintMatrix(matrix1);
            
            Console.WriteLine("\nMatrix 2:");
            PrintMatrix(matrix2);
            
            // Matrix addition
            Console.WriteLine("\nMatrix Addition (Matrix 1 + Matrix 2):");
            double[,] sum = AddMatrices(matrix1, matrix2);
            PrintMatrix(sum);
            
            // Matrix multiplication
            Console.WriteLine("\nMatrix Multiplication (Matrix 1 * Matrix 2):");
            double[,] product = MultiplyMatrices(matrix1, matrix2);
            PrintMatrix(product);
            
            // Determinant calculation
            Console.WriteLine($"\nDeterminant of Matrix 1: {Determinant(matrix1):F2}");
            Console.WriteLine($"Determinant of Matrix 2: {Determinant(matrix2):F2}");
            
            // Create a 3x3 matrix for more complex operations
            double[,] matrix3 = {
                { 2, -3, 1 },
                { 2, 0, -1 },
                { 1, 4, 5 }
            };
            
            Console.WriteLine("\n3x3 Matrix:");
            PrintMatrix(matrix3);
            Console.WriteLine($"Determinant: {Determinant(matrix3):F2}");
        }
    }
}