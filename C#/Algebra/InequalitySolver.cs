/*
 * Inequality Solver for Systems of Linear Inequalities
 * Author: Андрій Будильников
 * 
 * This program solves systems of linear inequalities using a basic approach.
 */

using System;
using System.Collections.Generic;

namespace Algebra
{
    /// <summary>
    /// Represents a linear inequality in the form ax + by ≤ c, ≥ c, < c, or > c
    /// </summary>
    public class LinearInequality
    {
        public double A { get; set; }  // Coefficient of x
        public double B { get; set; }  // Coefficient of y
        public double C { get; set; }  // Constant term
        public string Operator { get; set; }  // <=, >=, <, >
        
        public LinearInequality(double a, double b, double c, string op)
        {
            A = a;
            B = b;
            C = c;
            Operator = op;
        }
    }
    
    /// <summary>
    /// Solves systems of linear inequalities
    /// </summary>
    public class InequalitySolver
    {
        private List<LinearInequality> inequalities;
        
        public InequalitySolver()
        {
            inequalities = new List<LinearInequality>();
        }
        
        /// <summary>
        /// Adds an inequality to the system
        /// </summary>
        public void AddInequality(LinearInequality inequality)
        {
            inequalities.Add(inequality);
        }
        
        /// <summary>
        /// Solves the system of inequalities using a basic approach
        /// For demonstration purposes, we'll check a range of values
        /// </summary>
        public void Solve()
        {
            Console.WriteLine("Solving system of inequalities:");
            PrintSystem();
            
            // For simplicity, we'll test integer solutions in a limited range
            Console.WriteLine("\nPossible integer solutions in range [-10, 10]:");
            bool foundSolution = false;
            
            for (int x = -10; x <= 10; x++)
            {
                for (int y = -10; y <= 10; y++)
                {
                    if (CheckSolution(x, y))
                    {
                        Console.WriteLine($"({x}, {y})");
                        foundSolution = true;
                    }
                }
            }
            
            if (!foundSolution)
            {
                Console.WriteLine("No integer solutions found in the tested range.");
            }
        }
        
        /// <summary>
        /// Checks if a given point satisfies all inequalities
        /// </summary>
        private bool CheckSolution(int x, int y)
        {
            foreach (var inequality in inequalities)
            {
                double leftSide = inequality.A * x + inequality.B * y;
                
                switch (inequality.Operator)
                {
                    case "<=":
                        if (leftSide > inequality.C) return false;
                        break;
                    case ">=":
                        if (leftSide < inequality.C) return false;
                        break;
                    case "<":
                        if (leftSide >= inequality.C) return false;
                        break;
                    case ">":
                        if (leftSide <= inequality.C) return false;
                        break;
                }
            }
            return true;
        }
        
        /// <summary>
        /// Prints the system of inequalities
        /// </summary>
        private void PrintSystem()
        {
            foreach (var inequality in inequalities)
            {
                Console.WriteLine($"{inequality.A}x + {inequality.B}y {inequality.Operator} {inequality.C}");
            }
        }
        
        /// <summary>
        /// Main method to demonstrate the solver
        /// </summary>
        public static void Main(string[] args)
        {
            InequalitySolver solver = new InequalitySolver();
            
            // Example system:
            // x + y <= 5
            // 2x - y >= 0
            // x >= 0
            // y >= 0
            
            solver.AddInequality(new LinearInequality(1, 1, 5, "<="));
            solver.AddInequality(new LinearInequality(2, -1, 0, ">="));
            solver.AddInequality(new LinearInequality(1, 0, 0, ">="));
            solver.AddInequality(new LinearInequality(0, 1, 0, ">="));
            
            solver.Solve();
        }
    }
}