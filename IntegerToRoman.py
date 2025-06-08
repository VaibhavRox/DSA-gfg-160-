class Solution:
    def intToRoman(self, num: int) -> str:
        #take two lists, one with roman symbols and another number list with corresponding values of symbol
        n=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        s=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        i=0
        res=""
        while (num>0 and i<len(n)):
            if(num>=n[i]):
                res=res+s[i]
                num=num-n[i]
            else:
                i+=1
        return res