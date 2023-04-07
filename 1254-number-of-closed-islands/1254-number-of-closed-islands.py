class Solution:
    
    def helper(self,grid,i,j):
        if i==-1 or i==len(grid) or j==-1 or j==len(grid[0]) or grid[i][j]==1:return 
        grid[i][j]=1
        self.helper(grid,i+1,j)
        self.helper(grid,i-1,j)
        self.helper(grid,i,j+1)
        self.helper(grid,i,j-1)
        return
    def closedIsland(self, grid: List[List[int]]) -> int:
        # for ele in grid:print(ele)
        # print('fasafaf')
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if (i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1) and grid[i][j]==0:
                    self.helper(grid,i,j)
        # for ele in grid:print(ele)
        # print('fasafaf')
        count=0
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==0:
                    count+=1
                    self.helper(grid,i,j)
        # for ele in grid:print(ele)
        return count
        
        