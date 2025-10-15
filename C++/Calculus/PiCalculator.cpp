/*
 * pi calculator
 * author: Андрій Будильников
 * 
 * this program calculates pi using several different methods
 */

#include <iostream>
#include <random>
#include <cmath>

class PiCalculator {
public:
    // leibniz formula for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    static double leibnizFormula(int iterations) {
        double pi = 0;
        for (int i = 0; i < iterations; i++) {
            if (i % 2 == 0) {
                pi += 1.0 / (2 * i + 1);
            } else {
                pi -= 1.0 / (2 * i + 1);
            }
        }
        return pi * 4;
    }
    
    // monte carlo method for pi
    static double monteCarloMethod(int samples) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(-1.0, 1.0);
        
        int insideCircle = 0;
        
        for (int i = 0; i < samples; i++) {
            double x = dis(gen);
            double y = dis(gen);
            
            if (x * x + y * y <= 1) {
                insideCircle++;
            }
        }
        
        return 4.0 * insideCircle / samples;
    }
    
    // nilakantha series: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    static double nilakanthaSeries(int iterations) {
        double pi = 3;
        for (int i = 1; i <= iterations; i++) {
            double denominator = 2 * i * (2 * i + 1) * (2 * i + 2);
            if (i % 2 == 1) {
                pi += 4.0 / denominator;
            } else {
                pi -= 4.0 / denominator;
            }
        }
        return pi;
    }
};

int main() {
    std::cout << "pi calculation methods" << std::endl;
    std::cout << "====================" << std::endl;
    
    int iterations = 1000000;
    std::cout << "leibniz formula (" << iterations << " iterations): " << PiCalculator::leibnizFormula(iterations) << std::endl;
    
    int samples = 1000000;
    std::cout << "monte carlo method (" << samples << " samples): " << PiCalculator::monteCarloMethod(samples) << std::endl;
    
    std::cout << "nilakantha series (" << iterations << " iterations): " << PiCalculator::nilakanthaSeries(iterations) << std::endl;
    
    std::cout << "actual value of pi: " << M_PI << std::endl;
    
    return 0;
}