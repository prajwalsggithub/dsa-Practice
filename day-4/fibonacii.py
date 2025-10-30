# python program to print fibonacci series
# Fibonacci series up to n terms

n = 10  # how many Fibonacci numbers to print
first = 0
second = 1

print(first, second, end=" ")  # print first two numbers

for i in range(2, n):
    next = first + second
    print(next, end=" ")
    first = second
    second = next


#output:# 0 1 1 2 3 5 8 13 21 34

-------------------------------------------------------------------------
//java program to print fibonacci series
public class fibonacii { 
    public static void main(String args[]) { 
        int n = 10; // how many Fibonacci numbers to print 
        int first = 0, second = 1; 
        int next; 
 
        System.out.print(first + " " + second + " "); // print first two numbers 
 
        for (int i = 2; i < n; i++) { 
            next = first + second;   // next number = sum of previous two 
            System.out.print(next + " "); 
            first = second;          // move forward 
            second = next; 
        } 
    } 
}
