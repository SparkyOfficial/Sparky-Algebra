/*
 * pi calculator
 * author: Андрій Будильников
 * 
 * this program calculates pi using several different methods
 */

using System;

namespace Calculus
{
    public class PiCalculator
    {
        // leibniz formula for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
        public static double LeibnizFormula(int iterations)
        {
            double pi = 0;
            for (int i = 0; i < iterations; i++)
            {
                if (i % 2 == 0)
                {
                    pi += 1.0 / (2 * i + 1);
                }
                else
                {
                    pi -= 1.0 / (2 * i + 1);
                }
            }
            return pi * 4;
        }
        
        // monte carlo method for pi
        public static double MonteCarloMethod(int samples)
        {
            Random rand = new Random();
            int insideCircle = 0;
            
            for (int i = 0; i < samples; i++)
            {
                double x = rand.NextDouble() * 2 - 1;  // -1 to 1
                double y = rand.NextDouble() * 2 - 1;  // -1 to 1
                
                if (x * x + y * y <= 1)
                {
                    insideCircle++;
                }
            }
            
            return 4.0 * insideCircle / samples;
        }
        
        // nilakantha series: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
        public static double NilakanthaSeries(int iterations)
        {
            double pi = 3;
            for (int i = 1; i <= iterations; i++)
            {
                double denominator = 2 * i * (2 * i + 1) * (2 * i + 2);
                if (i % 2 == 1)
                {
                    pi += 4.0 / denominator;
                }
                else
                {
                    pi -= 4.0 / denominator;
                }
            }
            return pi;
        }
        
        public static void Main(string[] args)
        {
            Console.WriteLine("pi calculation methods");
            Console.WriteLine("====================");
            
            int iterations = 1000000;
            Console.WriteLine($"leibniz formula ({iterations} iterations): {LeibnizFormula(iterations)}");
            
            int samples = 1000000;
            Console.WriteLine($"monte carlo method ({samples} samples): {MonteCarloMethod(samples)}");
            
            Console.WriteLine($"nilakantha series ({iterations} iterations): {NilakanthaSeries(iterations)}");
            
            Console.WriteLine($"actual value of pi: {Math.PI}");
        }
    }
}