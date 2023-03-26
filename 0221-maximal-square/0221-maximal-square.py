class Solution:
    def helper(self,matrix,row,col,dp):
        if row==len(matrix) or col==len(matrix[0]) or matrix[row][col]=='0':return 0
        
        if dp[row+1][col]==-1:dp[row+1][col]=self.helper(matrix,row+1,col,dp)
        if dp[row+1][col+1]==-1:dp[row+1][col+1]=self.helper(matrix,row+1,col+1,dp)
        if dp[row][col+1]==-1:dp[row][col+1]=self.helper(matrix,row,col+1,dp)
        
        if dp[row+1][col]==0 or dp[row][col+1]==0 or dp[row+1][col+1]==0:return 1
        return (min(dp[row+1][col] ,dp[row][col+1] ,dp[row+1][col+1]))+1
    
        
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[-1 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        ar=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ar=max(ar,self.helper(matrix,i,j,dp))
        return ar**2
                