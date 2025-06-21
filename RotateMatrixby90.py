#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        #reverse each row, then take transpose of the matrix
        n=len(mat)
        for row in mat:
            row.reverse()
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        