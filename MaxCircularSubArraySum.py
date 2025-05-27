class Solution:
    def kadane(self, arr):
    # code here
        max_so_far=curr=arr[0]
        for i in range(1,len(arr)):
            curr=max(curr+arr[i],arr[i])
            max_so_far=max(curr,max_so_far)
        return max_so_far
    def min_kadane(self,arr):
        min_so_far=curr=arr[0]
        for i in range(1,len(arr)):
            curr=min(curr+arr[i],arr[i])
            min_so_far=min(curr,min_so_far)
        return min_so_far
    def circularSubarraySum(self,arr):
        max_val=self.kadane(arr)
        min_val=self.min_kadane(arr)
        if max_val<0:
            return max_val
        else:
            return max(max_val,sum(arr)-min_val)
        