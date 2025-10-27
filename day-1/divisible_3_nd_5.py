#using python Write a program to find the sum of all numbers between m and n that are divisible by both 3 and 5
m=1
n=20
sum=0
for i in range(m,n+1):
    if i % 3 == 0 and i % 5 == 0:
        sum=sum+i 

print("sum of divisible of 3 and 5",sum)


#----------------------------------------------
#using java Write a program to find the sum of all numbers between m and n that are divisible by both 3 and 5
#class Main {
 #   public static void main(String[] args) {
     #   //Write a program to find the sum of all numbers between m and n that are divisible by both 3 and 5
     #   int m=1;
     #   int n=20;
       # int sum=0;
       # for(int i=m;i<=n;i++){
       #    if (i % 3 == 0 && i % 5 == 0) {
        #        sum=sum+i;
           # }
       # }
        
     
      #  System.out.println("sum of divisible of 3 and 5"+sum);
   # }
#}