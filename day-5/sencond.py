#python program to find the second largest number in an array
arr = [1, 2, 5,4]
max_value =max(arr)
sl=0
for i in range(len(arr)):
    if sl < arr[i] < max_value:
        sl=arr[i]
        print(sl)



-----------------------------------------------------------------
# Find the second largest number in an array
class Main {
    public static void main(String[] args) {
      //  int arr[]=new int[10];
      int arr[]={1,2,5,4};
      int max=0;
      for(int i=0;i<arr.length;i++){
          if(max<arr[i]){
              max=arr[i];
      
    
          }
          
      }
        int sl=0;
        for(int i=0;i<arr.length;i++){
            if((sl<arr[i]) && (arr[i]<max)){
                sl=arr[i];
            }
        }
        System.out.print(sl);
     
    }
}