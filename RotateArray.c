// User function Template for C
void reverse(int arr[],int start,int end)
{
    while(start<end)
    {
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++;end--;
    }
}
// Function to rotate an array by d elements in counter-clockwise direction.
void rotateArr(int arr[], int n, int d) {
    d=d%n;
    reverse(arr,0,d-1);
    reverse(arr,d,n-1);
    reverse(arr,0,n-1);
}