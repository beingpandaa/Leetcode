class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def dfs(i,j):
            if i==n or j==m or i<0 or j<0 or grid[i][j]==0:
                return 0          
            grid[i][j]=0
            return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i+1,j)+dfs(i-1,j)
        
        
        n=len(grid)
        m=len(grid[0])
        count=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count=max(count,dfs(i,j))
        return count
    
        
        
            