# python  code to convert binary to decimal
input_num = 1010  # binary number
decimal_num = 0
power = 0
while input_num > 0:
    last_digit = input_num % 10
    decimal_num += last_digit * (2 ** power)
    input_num //= 10
    power += 1

print(decimal_num)
    




----------------------------------------------------------------------------
# Write a Java program to convert a binary number (given as an integer) to its decimal equivalent. 
int n = 1010; // binary number 
int sum = 0; 
int i = 0; 
 
while(n != 0) { 
    int digit = n % 10;               // get the last digit 
    sum = sum + digit * (int)Math.pow(2, i); // multiply by 2^position 
    n = n / 10;                       // remove last digit 
    i++;                               
} 
System.out.println(sum);