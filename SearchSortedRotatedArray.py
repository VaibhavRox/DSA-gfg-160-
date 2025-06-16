#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        #just do binary search
        lo=0   #lower limit
        hi=len(arr)-1     #upper limit
        while lo<=hi:
            mid=lo+(hi-lo)//2
            
            if arr[mid]==key:
                return mid
            #if left half sorted
            if arr[mid]>=arr[lo]:
                #if key lies in this half, move upper limit to middle
                if key>=arr[lo] and key<arr[mid]:
                    hi=mid-1
                #otherwise put lo to mid
                else:
                    lo=mid+1
            #if right half sorted
            else:
                if key>arr[mid] and key<=arr[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        return -1 # if key not found