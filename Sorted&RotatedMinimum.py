#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        min_=arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min_:
                min_=arr[i]
            else:
                continue
        return min_