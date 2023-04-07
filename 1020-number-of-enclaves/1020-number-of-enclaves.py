class Solution:
    def helper(self,grid,i,j):
        if i==-1 or i==len(grid) or j==-1 or j==len(grid[0]) or grid[i][j]==0:return 
        grid[i][j]=0
        self.helper(grid,i+1,j)
        self.helper(grid,i-1,j)
        self.helper(grid,i,j+1)
        self.helper(grid,i,j-1)
        return 
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # for ele in grid:
        #     print(ele)
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1:
                    self.helper(grid,i,j)
        count=0
        # for ele in grid:
        #     print(ele)
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==1:
                    count+=1
        return count