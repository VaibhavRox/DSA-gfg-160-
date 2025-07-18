class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        from collections import defaultdict
        count=0
        prefix_sum=0
        prefix_counts=defaultdict(int)
        prefix_counts[0]=1  #Empty prefix has sum 0
        for i in arr:
            prefix_sum+=i
            if (prefix_sum-k) in prefix_counts:
                count+=prefix_counts[prefix_sum-k]
            prefix_counts[prefix_sum]+=1
        return count