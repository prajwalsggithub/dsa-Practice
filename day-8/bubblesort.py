# python program bubblesort
arr=[6,5,3,2,7,4]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range(i,len(arr)):
    print("Try programiz.pro",arr[i])


----------------------------------------------------------------
# bubblesort prohgram in java
class Main {
    public static void main(String[] args) {
        int arr[]={6,5,3,2,7,4};
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        for(int i=0;i<arr.length;i++){
        
        System.out.println("Try programiz.pro"+ arr[i]);
    }
}}