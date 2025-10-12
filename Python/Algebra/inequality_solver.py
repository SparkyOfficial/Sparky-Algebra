"""
Inequality Solver for Systems of Linear Inequalities
Author: Андрій Будильников

This program solves systems of linear inequalities using a basic approach.
"""

class LinearInequality:
    """
    Represents a linear inequality in the form ax + by ≤ c, ≥ c, < c, or > c
    """
    def __init__(self, a, b, c, op):
        self.a = a  # Coefficient of x
        self.b = b  # Coefficient of y
        self.c = c  # Constant term
        self.op = op  # <=, >=, <, >

class InequalitySolver:
    """
    Solves systems of linear inequalities
    """
    def __init__(self):
        self.inequalities = []
    
    def add_inequality(self, inequality):
        """
        Adds an inequality to the system
        """
        self.inequalities.append(inequality)
    
    def check_solution(self, x, y):
        """
        Checks if a given point satisfies all inequalities
        """
        for inequality in self.inequalities:
            left_side = inequality.a * x + inequality.b * y
            
            if inequality.op == "<=" and left_side > inequality.c:
                return False
            elif inequality.op == ">=" and left_side < inequality.c:
                return False
            elif inequality.op == "<" and left_side >= inequality.c:
                return False
            elif inequality.op == ">" and left_side <= inequality.c:
                return False
        return True
    
    def print_system(self):
        """
        Prints the system of inequalities
        """
        for inequality in self.inequalities:
            print(f"{inequality.a}x + {inequality.b}y {inequality.op} {inequality.c}")
    
    def solve(self):
        """
        Solves the system of inequalities using a basic approach
        For demonstration purposes, we'll check a range of values
        """
        print("Solving system of inequalities:")
        self.print_system()
        
        # For simplicity, we'll test integer solutions in a limited range
        print("\nPossible integer solutions in range [-10, 10]:")
        found_solution = False
        
        for x in range(-10, 11):
            for y in range(-10, 11):
                if self.check_solution(x, y):
                    print(f"({x}, {y})")
                    found_solution = True
        
        if not found_solution:
            print("No integer solutions found in the tested range.")

def main():
    """
    Main function to demonstrate the solver
    """
    solver = InequalitySolver()
    
    # Example system:
    # x + y <= 5
    # 2x - y >= 0
    # x >= 0
    # y >= 0
    
    solver.add_inequality(LinearInequality(1, 1, 5, "<="))
    solver.add_inequality(LinearInequality(2, -1, 0, ">="))
    solver.add_inequality(LinearInequality(1, 0, 0, ">="))
    solver.add_inequality(LinearInequality(0, 1, 0, ">="))
    
    solver.solve()

if __name__ == "__main__":
    main()