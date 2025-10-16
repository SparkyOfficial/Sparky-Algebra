/*
 * TestCombinatorics.kt
 * Author: Андрій Будильников
 * 
 * Test program for combinatorics functions in Kotlin
 */

fun main() {
    println("Testing combinatorics functions...\n")
    
    // test factorial
    println("Factorial(0) = ${Combinatorics.factorial(0)}")
    println("Factorial(1) = ${Combinatorics.factorial(1)}")
    println("Factorial(5) = ${Combinatorics.factorial(5)}")
    println("Factorial(10) = ${Combinatorics.factorial(10)}")
    
    println()
    
    // test permutation
    println("Permutation(5, 0) = ${Combinatorics.permutation(5, 0)}")
    println("Permutation(5, 1) = ${Combinatorics.permutation(5, 1)}")
    println("Permutation(5, 3) = ${Combinatorics.permutation(5, 3)}")
    println("Permutation(10, 2) = ${Combinatorics.permutation(10, 2)}")
    
    println()
    
    // test combination
    println("Combination(5, 0) = ${Combinatorics.combination(5, 0)}")
    println("Combination(5, 1) = ${Combinatorics.combination(5, 1)}")
    println("Combination(5, 3) = ${Combinatorics.combination(5, 3)}")
    println("Combination(10, 2) = ${Combinatorics.combination(10, 2)}")
    
    println()
    
    // test catalan number
    println("CatalanNumber(0) = ${Combinatorics.catalanNumber(0)}")
    println("CatalanNumber(1) = ${Combinatorics.catalanNumber(1)}")
    println("CatalanNumber(2) = ${Combinatorics.catalanNumber(2)}")
    println("CatalanNumber(3) = ${Combinatorics.catalanNumber(3)}")
    println("CatalanNumber(4) = ${Combinatorics.catalanNumber(4)}")
    println("CatalanNumber(5) = ${Combinatorics.catalanNumber(5)}")
    
    println("\nAll tests completed! 🎉")
}