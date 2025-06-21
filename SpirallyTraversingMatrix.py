class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        m,n=len(mat),len(mat[0])
        res=[]
        top,bottom,left,right=0,m-1,0,n-1
        while top<=bottom and left<=right:
            #Print top row from left to right
            for i in range(left,right+1):
                res.append(mat[top][i])
            top+=1
            
            #Print last column from top to bottom
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right-=1
            
            #Print last row from right to left
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(mat[bottom][i])
                bottom-=1
            
            #print first column, upto second row
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left+=1
                
        return res