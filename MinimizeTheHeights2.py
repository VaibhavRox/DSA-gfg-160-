#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        ans=arr[n-1]-arr[0]
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            maxi=max(arr[i-1]+k,arr[n-1]-k)
            mini=min(arr[0]+k,arr[i]-k)
            ans=min(ans,maxi-mini)
        return ans