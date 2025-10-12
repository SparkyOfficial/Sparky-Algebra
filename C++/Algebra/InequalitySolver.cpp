/*
 * Inequality Solver for Systems of Linear Inequalities
 * Author: Андрій Будильников
 * 
 * This program solves systems of linear inequalities using a basic approach.
 */

#include <iostream>
#include <vector>
#include <string>

// Represents a linear inequality in the form ax + by ≤ c, ≥ c, < c, or > c
class LinearInequality {
public:
    double a, b, c;
    std::string op;
    
    LinearInequality(double a, double b, double c, std::string op) 
        : a(a), b(b), c(c), op(op) {}
};

// Solves systems of linear inequalities
class InequalitySolver {
private:
    std::vector<LinearInequality> inequalities;

public:
    // Adds an inequality to the system
    void addInequality(LinearInequality inequality) {
        inequalities.push_back(inequality);
    }
    
    // Checks if a given point satisfies all inequalities
    bool checkSolution(int x, int y) {
        for (const auto& inequality : inequalities) {
            double leftSide = inequality.a * x + inequality.b * y;
            
            if (inequality.op == "<=" && leftSide > inequality.c) return false;
            if (inequality.op == ">=" && leftSide < inequality.c) return false;
            if (inequality.op == "<" && leftSide >= inequality.c) return false;
            if (inequality.op == ">" && leftSide <= inequality.c) return false;
        }
        return true;
    }
    
    // Prints the system of inequalities
    void printSystem() {
        for (const auto& inequality : inequalities) {
            std::cout << inequality.a << "x + " << inequality.b << "y " 
                      << inequality.op << " " << inequality.c << std::endl;
        }
    }
    
    // Solves the system of inequalities using a basic approach
    // For demonstration purposes, we'll check a range of values
    void solve() {
        std::cout << "Solving system of inequalities:" << std::endl;
        printSystem();
        
        // For simplicity, we'll test integer solutions in a limited range
        std::cout << "\nPossible integer solutions in range [-10, 10]:" << std::endl;
        bool foundSolution = false;
        
        for (int x = -10; x <= 10; x++) {
            for (int y = -10; y <= 10; y++) {
                if (checkSolution(x, y)) {
                    std::cout << "(" << x << ", " << y << ")" << std::endl;
                    foundSolution = true;
                }
            }
        }
        
        if (!foundSolution) {
            std::cout << "No integer solutions found in the tested range." << std::endl;
        }
    }
};

// Main method to demonstrate the solver
int main() {
    InequalitySolver solver;
    
    // Example system:
    // x + y <= 5
    // 2x - y >= 0
    // x >= 0
    // y >= 0
    
    solver.addInequality(LinearInequality(1, 1, 5, "<="));
    solver.addInequality(LinearInequality(2, -1, 0, ">="));
    solver.addInequality(LinearInequality(1, 0, 0, ">="));
    solver.addInequality(LinearInequality(0, 1, 0, ">="));
    
    solver.solve();
    
    return 0;
}