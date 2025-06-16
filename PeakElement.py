class Solution:   
    def peakElement(self,arr):
        # Code here
        n=len(arr)
        for i in range(n):
            left=True
            right=True
            #check for left element
            if i>0 and arr[i]<=arr[i-1]:
                left=False
            #check for right element
            if i<n-1 and arr[i]<=arr[i+1]:
                right=False
            if left and right:
                return i