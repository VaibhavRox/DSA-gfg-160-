class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        #Count each occurence
        c0=c1=c2=0
        for i in arr:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        idx=0
        #Just put them in the places
        for i in range(c0):
            arr[idx]=0
            idx+=1
        for i in range(c1):
            arr[idx]=1
            idx+=1
        for i in range(c2):
            arr[idx]=2
            idx+=1
        