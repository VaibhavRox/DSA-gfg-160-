#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		                  # code here
                max_so_far=min_so_far=arr[0]
                curr=arr[0]
                for i in range(1,len(arr)):
                        if arr[i]<0:
                            max_so_far,min_so_far=min_so_far,max_so_far
                            max_so_far=max(max_so_far*arr[i],arr[i])
                            min_so_far=min(min_so_far*arr[i],arr[i])
                            curr=max(curr,max_so_far)
                                
                return curr