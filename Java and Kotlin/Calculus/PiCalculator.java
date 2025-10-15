/*
 * pi calculator
 * author: Андрій Будильников
 * 
 * this program calculates pi using several different methods
 */

import java.util.Random;

public class PiCalculator {
    // leibniz formula for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    public static double leibnizFormula(int iterations) {
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
    public static double monteCarloMethod(int samples) {
        Random rand = new Random();
        int insideCircle = 0;
        
        for (int i = 0; i < samples; i++) {
            double x = rand.nextDouble() * 2 - 1;  // -1 to 1
            double y = rand.nextDouble() * 2 - 1;  // -1 to 1
            
            if (x * x + y * y <= 1) {
                insideCircle++;
            }
        }
        
        return 4.0 * insideCircle / samples;
    }
    
    // nilakantha series: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    public static double nilakanthaSeries(int iterations) {
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
    
    public static void main(String[] args) {
        System.out.println("pi calculation methods");
        System.out.println("====================");
        
        int iterations = 1000000;
        System.out.println("leibniz formula (" + iterations + " iterations): " + leibnizFormula(iterations));
        
        int samples = 1000000;
        System.out.println("monte carlo method (" + samples + " samples): " + monteCarloMethod(samples));
        
        System.out.println("nilakantha series (" + iterations + " iterations): " + nilakanthaSeries(iterations));
        
        System.out.println("actual value of pi: " + Math.PI);
    }
}