class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_so_far=arr[0]
        curr=arr[0]
        for i in range(1,len(arr)):
            curr=max(curr+arr[i],arr[i])
            max_so_far=max(curr,max_so_far)
        return max_so_far