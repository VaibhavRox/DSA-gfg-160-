#User function Template for python3
class Solution:
    def trimzeros(self,s):
        firstbit=s.find('1')   #find position of first 1 occurance, to trim leading zeros
        return s[firstbit:] if firstbit!=-1 else 0
    
    def addBinary(self, s1, s2):
            # code here
            s1=self.trimzeros(s1)
            s2=self.trimzeros(s2)
            s1=str(s1)
            s2=str(s2)
            n=len(s1)
            m=len(s2)
            if n<m:
                s1,s2=s2,s1
                n,m=m,n
            j=m-1
            carry=0
            result=[]  #just append the digits of result normally, then return it reversed and joined together
            for i in range(n-1,-1,-1):      #go from the back of both numbers
                bit1=int(s1[i])
                bitsum=bit1+carry
                if j>=0:
                    bit2=int(s2[j])
                    bitsum+=bit2
                    j-=1
                #get the result bit and carry
                bit=bitsum%2
                carry=bitsum//2
                result.append(str(bit))
            #if any carry remaining append it to result
            if carry>0:
                result.append(str('1'))
            return ''.join(result[::-1])
            
            
            