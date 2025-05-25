void reverseArray(int arr[], int n) {
    // Code here
    int x=n-1;
    int i=0;
    while (i<x)
    {
        int temp=arr[i];
        arr[i]=arr[x];
        arr[x]=temp;
        i++;x--;
    }
    return arr;
}