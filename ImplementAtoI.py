#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        res=0
        sign=1
        idx=0
        while idx<len(s) and (s[idx]==' '):  #ignore whitespaces
            idx+=1
        if idx<len(s) and (s[idx]=='+' or s[idx]=='-'): #Account for the sign
            if s[idx]=='-':
                sign=-1
            idx+=1
        while idx<len(s) and ('0'<=s[idx]<='9'):
            res=10*res+int(s[idx]) #append current digit to result
            #Handle overflow and underflow conditions
            if res>(2**31-1):
                return sign*(2**31-1) if sign==1 else -2**31
            idx+=1
        return sign*res
        