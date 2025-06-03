#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        #sort in reverse
        citations.sort(reverse=True)
        n=len(citations)
        idx=0
        while idx<n and citations[idx]>idx:
            idx+=1
        return idx