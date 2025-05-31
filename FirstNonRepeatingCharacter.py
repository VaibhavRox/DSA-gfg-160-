class Solution:
    def nonRepeatingChar(self,s):
        #code here
        charCount={}
        for i in s:
            charCount[i]=charCount.get(i,0)+1
        for val in charCount:
            if charCount[val]==1:
                return val
        return '$'
    
    