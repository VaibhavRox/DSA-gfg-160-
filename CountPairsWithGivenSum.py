#User function Template for python3

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        count=0
        freq={}
        for i in range(len(arr)):
            if (target-arr[i]) in freq: #Check if complement exists in freq:
                count+=freq[target-arr[i]]
            freq[arr[i]]=freq.get(arr[i],0)+1
        return count