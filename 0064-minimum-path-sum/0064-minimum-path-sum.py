class Solution:
    def helper(self,grid,i,j,dp):
        if i==len(grid)-1 and j==len(grid[0])-1:return grid[i][j]
        if i==len(grid) or j==len(grid[0]):return sys.maxsize
        
        if dp[i+1][j]==sys.maxsize:dp[i+1][j]=self.helper(grid,i+1,j,dp)
        if dp[i][j+1]==sys.maxsize:dp[i][j+1]=self.helper(grid,i,j+1,dp)
        # if dp[i+1][j+1]==sys.maxsize:dp[i+1][j+1]=self.helper(grid,i+1,j+1,dp)
        return grid[i][j]+min(dp[i][j+1],dp[i+1][j])
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[sys.maxsize for i in range(len(grid[0])+1)]for i in range (len(grid)+1)]
        return self.helper(grid,0,0,dp)
        