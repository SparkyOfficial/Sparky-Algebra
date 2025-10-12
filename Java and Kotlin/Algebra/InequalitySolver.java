/*
 * Inequality Solver for Systems of Linear Inequalities
 * Author: Андрій Будильников
 * 
 * This program solves systems of linear inequalities using a basic approach.
 */

import java.util.ArrayList;
import java.util.List;

// Represents a linear inequality in the form ax + by ≤ c, ≥ c, < c, or > c
class LinearInequality {
    public double a, b, c;
    public String op;
    
    public LinearInequality(double a, double b, double c, String op) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.op = op;
    }
}

// Solves systems of linear inequalities
public class InequalitySolver {
    private List<LinearInequality> inequalities;
    
    public InequalitySolver() {
        inequalities = new ArrayList<>();
    }
    
    // Adds an inequality to the system
    public void addInequality(LinearInequality inequality) {
        inequalities.add(inequality);
    }
    
    // Checks if a given point satisfies all inequalities
    private boolean checkSolution(int x, int y) {
        for (LinearInequality inequality : inequalities) {
            double leftSide = inequality.a * x + inequality.b * y;
            
            switch (inequality.op) {
                case "<=":
                    if (leftSide > inequality.c) return false;
                    break;
                case ">=":
                    if (leftSide < inequality.c) return false;
                    break;
                case "<":
                    if (leftSide >= inequality.c) return false;
                    break;
                case ">":
                    if (leftSide <= inequality.c) return false;
                    break;
            }
        }
        return true;
    }
    
    // Prints the system of inequalities
    private void printSystem() {
        for (LinearInequality inequality : inequalities) {
            System.out.println(inequality.a + "x + " + inequality.b + "y " + 
                              inequality.op + " " + inequality.c);
        }
    }
    
    // Solves the system of inequalities using a basic approach
    // For demonstration purposes, we'll check a range of values
    public void solve() {
        System.out.println("Solving system of inequalities:");
        printSystem();
        
        // For simplicity, we'll test integer solutions in a limited range
        System.out.println("\nPossible integer solutions in range [-10, 10]:");
        boolean foundSolution = false;
        
        for (int x = -10; x <= 10; x++) {
            for (int y = -10; y <= 10; y++) {
                if (checkSolution(x, y)) {
                    System.out.println("(" + x + ", " + y + ")");
                    foundSolution = true;
                }
            }
        }
        
        if (!foundSolution) {
            System.out.println("No integer solutions found in the tested range.");
        }
    }
    
    // Main method to demonstrate the solver
    public static void main(String[] args) {
        InequalitySolver solver = new InequalitySolver();
        
        // Example system:
        // x + y <= 5
        // 2x - y >= 0
        // x >= 0
        // y >= 0
        
        solver.addInequality(new LinearInequality(1, 1, 5, "<="));
        solver.addInequality(new LinearInequality(2, -1, 0, ">="));
        solver.addInequality(new LinearInequality(1, 0, 0, ">="));
        solver.addInequality(new LinearInequality(0, 1, 0, ">="));
        
        solver.solve();
    }
}