# Program to print numbers not present in the list

a = [0, 2, 3, 7]
a.sort()

start = 0
max_val = max(a)

for i in range(max_val):
    if i != a[start]:
        print(i)
    else:
        start += 1















-----------------------------------------------------------------

import java.util.Arrays;

public class NumbernotPresent {
	public static void main(String[] args) {
		
	
	int a[]= {0,2,3,7};
	Arrays.sort(a);
	int start=0;
	int max=0;
	for(int i=0;i<=a.length-1;i++) {
		if(a[i]>max) {
			max=a[i];
		}
		
	}
	for(int i=0;i<=max-1;i++) {
		
		if(i!=a[start]) {
			System.out.println(i);
		}
		else {
			start++;
		}
		
	}


	
	
	
	
	
	
	
	
	
//   for(int i=0;i<max;i++) {
//	   
//	   for(int j=0;j<a.length-1;j++) {
//		   
//		   if(i!=a[j]) {
//			   System.out.println(i);
//		   }
//		   
//	   }
//   }
	
	

}
}