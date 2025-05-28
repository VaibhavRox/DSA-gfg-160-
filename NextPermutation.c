// User function Template for C

// Function to find the next permutation
void nextPermutation(int arr[], int n) {
    // code here
    int i=n-2;
    //step 1 find decreasing element from end
    while (i>=0 && arr[i]>=arr[i+1]){
        i--;
    }
    
    if (i>=0){
        //step 2 find element just greater than arr[i]
        int j=n-1;
        while (arr[j]<=arr[i]){
            j--;
        }
        //swap them 
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }
    //reverse the rest
    int left=i+1,right=n-1;
    while(left<right){
        int temp=arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
        left++;right--;
    }
}