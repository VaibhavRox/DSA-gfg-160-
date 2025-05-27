#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        exp=1
        for i in arr:
            if i<exp:
                continue
            elif i==exp:
                exp+=1
            elif i>exp:
                return exp
        return exp