 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0
        unique_sorted=sorted(set(arr))
        max_len=1
        curr_len=1
        for i in range(1,len(unique_sorted)):
            if unique_sorted[i]==unique_sorted[i-1]+1:
                curr_len+=1
                max_len=max(max_len,curr_len)
            else:
                curr_len=1
        return max_len