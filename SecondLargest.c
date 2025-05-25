int getSecondLargest(int *arr, int n) {
    // code here
    int largest=arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>largest)
        {
            largest=arr[i];
        }
    }
    int sec=-1;
    for(int i=0;i<n;i++)
    {
        if((arr[i]>sec) && (arr[i]<largest))
        {
            sec=arr[i];
        }
    }
    
    return sec;
}
