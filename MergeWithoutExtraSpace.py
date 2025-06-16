class Solution:
    def mergeArrays(self, a, b):
        # code here
        i=len(a)-1
        j=0
        #swap largest elements of A to B
        while i>=0 and j<len(b):
            if a[i]<b[j]:
                i-=1
            else:
                a[i],b[j]=b[j],a[i]
                i-=1
                j+=1
        #just sort the remaining arrays
        a.sort()
        b.sort()
        