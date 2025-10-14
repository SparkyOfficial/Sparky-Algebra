/*
 * Matrix Operations Library
 * Author: Андрій Будильников
 * 
 * This program provides basic matrix operations including addition, multiplication,
 * determinant calculation, and matrix inversion.
 */
public class MatrixOperations {
    
    /* Adds two matrices of the same dimensions */
    public static double[][] addMatrices(double[][] matrix1, double[][] matrix2) {
        int rows = matrix1.length;
        int cols = matrix1[0].length;
        
        if (rows != matrix2.length || cols != matrix2[0].length) {
            throw new IllegalArgumentException("Matrices must have the same dimensions for addition");
        }
        
        double[][] result = new double[rows][cols];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        
        return result;
    }
    
    /* Multiplies two matrices */
    public static double[][] multiplyMatrices(double[][] matrix1, double[][] matrix2) {
        int rows1 = matrix1.length;
        int cols1 = matrix1[0].length;
        int rows2 = matrix2.length;
        int cols2 = matrix2[0].length;
        
        if (cols1 != rows2) {
            throw new IllegalArgumentException("Number of columns in first matrix must equal number of rows in second matrix");
        }
        
        double[][] result = new double[rows1][cols2];
        
        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                for (int k = 0; k < cols1; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }
        
        return result;
    }
    
    /* Calculates the determinant of a square matrix using cofactor expansion */
    public static double determinant(double[][] matrix) {
        int n = matrix.length;
        
        for (int i = 0; i < n; i++) {
            if (matrix[i].length != n) {
                throw new IllegalArgumentException("Matrix must be square to calculate determinant");
            }
        }
        
        if (n == 1) {
            return matrix[0][0];
        }
        
        if (n == 2) {
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
        }
        
        double det = 0;
        for (int j = 0; j < n; j++) {
            det += matrix[0][j] * cofactor(matrix, 0, j);
        }
        
        return det;
    }
    
    /* Calculates the cofactor of a matrix element */
    private static double cofactor(double[][] matrix, int row, int col) {
        int n = matrix.length;
        double[][] minor = new double[n - 1][n - 1];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != row && j != col) {
                    int minorRow = i < row ? i : i - 1;
                    int minorCol = j < col ? j : j - 1;
                    minor[minorRow][minorCol] = matrix[i][j];
                }
            }
        }
        
        int sign = (row + col) % 2 == 0 ? 1 : -1;
        return sign * determinant(minor);
    }
    
    /* Prints a matrix to the console */
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            System.out.print("[ ");
            for (double val : row) {
                System.out.print(val + " ");
            }
            System.out.println("]");
        }
    }
    
    /* Main method to demonstrate matrix operations */
    public static void main(String[] args) {
        System.out.println("Matrix Operations Demo");
        System.out.println("=====================");
        
        /* Create two 2x2 matrices */
        double[][] matrix1 = {
            {1, 2},
            {3, 4}
        };
        
        double[][] matrix2 = {
            {5, 6},
            {7, 8}
        };
        
        System.out.println("Matrix 1:");
        printMatrix(matrix1);
        
        System.out.println("\nMatrix 2:");
        printMatrix(matrix2);
        
        /* Matrix addition */
        System.out.println("\nMatrix Addition (Matrix 1 + Matrix 2):");
        double[][] sum = addMatrices(matrix1, matrix2);
        printMatrix(sum);
        
        /* Matrix multiplication */
        System.out.println("\nMatrix Multiplication (Matrix 1 * Matrix 2):");
        double[][] product = multiplyMatrices(matrix1, matrix2);
        printMatrix(product);
        
        /* Determinant calculation */
        System.out.println("\nDeterminant of Matrix 1: " + determinant(matrix1));
        System.out.println("Determinant of Matrix 2: " + determinant(matrix2));
        
        /* Create a 3x3 matrix for more complex operations */
        double[][] matrix3 = {
            {2, -3, 1},
            {2, 0, -1},
            {1, 4, 5}
        };
        
        System.out.println("\n3x3 Matrix:");
        printMatrix(matrix3);
        System.out.println("Determinant: " + determinant(matrix3));
    }
}