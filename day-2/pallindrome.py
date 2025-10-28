#Write a program to print all palindrome numbers between a given lower and upper limit.
# 121 
#ans :121

import java.util.*;

public class Day3Palindrome {          
    // Method to reverse a number
    static int palindrome(int num) {
        int rem = 0;
        int div = num;
        while (div != 0) {
            int r = div % 10;
            rem = (rem * 10) + r;
            div = div / 10;
        }
        return rem;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Lower and Upper Limit:");
        int ll = sc.nextInt(); // lower limit
        int ul = sc.nextInt(); // upper limit

        System.out.println("Palindrome numbers between " + ll + " and " + ul + " are:");
        for (int i = ll; i <= ul; i++) {
            if (i == palindrome(i)) {
                System.out.println(i);
            }
        }

        sc.close();
    }
}

 #
 #Example 1 — i = 11 (a palindrome)

#Call palindrome(11):

#start: rem = 0, div = 11

#iteration 1:

#r = div % 10 = 11 % 10 = 1

#rem = (0 * 10) + 1 = 1

#div = div / 10 = 11 / 10 = 1 (integer division)

#iteration 2:

#r = 1 % 10 = 1

#rem = (1 * 10) + 1 = 11

#div = 1 / 10 = 0

#loop ends, return rem = 11

#Back in main: compare i == palindrome(i) → 11 == 11 → true → print 11.
#------------------------------------------------------------------------------
# Python program to print all palindrome numbers between a given lower and upper limit
# Function to check if a number is palindrome

# Program to print all palindrome numbers between a given lower and upper limit

def palindrome(num):
    rem = 0
    div = num
    while div != 0:
        r = div % 10
        rem = (rem * 10) + r
        div = div // 10   # Integer division
    return rem


def main():
    ll = int(input("Enter Lower Limit: "))
    ul = int(input("Enter Upper Limit: "))

    print(f"Palindrome numbers between {ll} and {ul} are:")
    for i in range(ll, ul + 1):
        if i == palindrome(i):
            print(i)


if __name__ == "__main__":
    main()
