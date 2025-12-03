// Find the second largest number in an array
class Main {
    public static void main(String[] args) {
        int arr []={3,4,5,9,6,10};
        int max=Integer.MIN_VALUE;
         int secmax=Integer.MIN_VALUE;
        for(int i=0;i<arr.length;i++){
           if (arr[i]>max){
               max=arr[i];
           }
        }
        for(int i=0;i<arr.length;i++){
        if(arr[i]>secmax && arr[i]!=max){
            secmax=arr[i];
        }
        }
     System.out.print(secmax);
    }
}

// python code to find the second largest number in an array
arr = [3, 4, 5, 9, 6, 10]
max_num = float('-inf')
sec_max = float('-inf')
for num in arr:
    if num > max_num:
        max_num = num
for num in arr:
    if num > sec_max and num != max_num:
        sec_max = num
print(sec_max)
