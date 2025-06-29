class Solution:
    def serachRowMatrix(self,mat,x):
        for row in mat:
            low,high=0,len(row)-1
            while low<=high:
                mid=(low+high)//2
                if row[mid]==x:
                    return True
                elif row[mid]>x:
                    high=mid-1
                else:
                    low=mid+1
        return False