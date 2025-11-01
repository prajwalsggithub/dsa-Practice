
#python code for bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

--------------------------------------------------------------------
#Write a Java program to sort an array of integers in ascending order using Bubble Sort. 
public class bbblesort { 
public void bulbbleSort(int arr[]){ 
    for(int i=0;i<arr.length;i++){ 
        for(int j=0;j<arr.length-1;j++){ 
            if(arr[j]> arr[j+1]){ 
                int temp=arr[j]; 
                arr[j]=arr[j+1]; 
                arr[j+1]=temp; 
            } 
        }  
    } 
} 
    public static void main(String args[]){ 
        int arr[]={5,4,1,3,2,2,5,3,4,6,6}; 
            bulbbleSort(arr); 
           
        for (int i = 0; i < arr.length; i++) { 
            System.out.print(arr[i] + " "); 
    } 
} 
}